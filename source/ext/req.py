def setup(app):
    app.add_config_value('req_include_reqs', False, 'html')

    app.add_node(reqtrace)
    app.add_node(req,
                 html=(visit_req_node, depart_req_node),
                 latex=(visit_req_node, depart_req_node),
                 text=(visit_req_node, depart_req_node))

    app.add_directive('req', ReqDirective)
    app.add_directive('reqtrace', ReqtraceDirective)
    app.connect('doctree-resolved', process_req_nodes)
    app.connect('env-purge-doc', purge_reqs)

    return {'version': '0.1'}   # identifies the version of our extension



from docutils import nodes
from docutils.nodes import section
from docutils.nodes import title

class req(nodes.Admonition, nodes.Element):
    pass

class reqtrace(nodes.General, nodes.Element):
    pass

def visit_req_node(self, node):
    self.visit_admonition(node)

def depart_req_node(self, node):
    self.depart_admonition(node)



from docutils.parsers.rst import Directive

class ReqtraceDirective(Directive):

    def run(self):
        return [reqtrace('')]



from sphinx.util.compat import make_admonition
from docutils.parsers.rst import directives
from sphinx.locale import _
from sphinx.application import Sphinx
from pprint import pprint

def find_parent_section_name(node):
    if isinstance(node, section):
        #pprint(node[node.first_child_matching_class(title)][0].astext())
        return node
    if node.parent:
        return find_parent_section_name(node.parent)
    else:
        return

  


class ReqDirective(Directive):

    """Directive to insert Requirement trace markup

    Example::

        .. req:: HEP-TS-FUN-049 
            :show:
            
            This section describe how the WOIS GUI interface is used as the main user interface which allow to run the workflows and or create new ones
    """

    # this enables content in the directive
    has_content = True
    option_spec = {'show': directives.unchanged,
                   }

    def run(self):
        env = self.state.document.settings.env

        targetid = "req-%d" % env.new_serialno('req')
        targetnode = nodes.target('', '', ids=[targetid])

        ad = make_admonition(req, self.name, [_('Requirement coverage')], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)

        if not hasattr(env, 'req_all_reqs'):
            env.req_all_reqs = []

        

        env.req_all_reqs.append({
            'docname': env.docname,
            'evidence': '\n'.join(self.content[-1:]),
            'section' : find_parent_section_name(self.state),
            'reqid' : self.content[0],
            'req': ad[0].deepcopy(),
            'target': targetnode,
        })

        if not self.options.has_key('show'):
            return [targetnode]

        return [targetnode] + ad


def purge_reqs(app, env, docname):
    if not hasattr(env, 'req_all_reqs'):
        return
    env.req_all_reqs = [req for req in env.req_all_reqs
                          if req['docname'] != docname]


def append_row(tbody, cells):
    row = nodes.row()
    tbody += row
  
    for cell in cells:
        entry = nodes.entry()
        row += entry
  
        if isinstance(cell, basestring):
            node = nodes.paragraph(text=cell)
        else:
            node = cell
  
        entry += node



def process_req_nodes(app, doctree, fromdocname):
    for node in doctree.traverse(req):
        if not app.config.req_include_reqs:
            node.parent.remove(node)

    # Replace all reqtrace nodes with a list of the collected reqs.
    # Augment each req with a backlink to the original location.
    env = app.builder.env

    for node in doctree.traverse(reqtrace):
        if not app.config.req_include_reqs:
            node.replace_self([])
            continue

        content = []

        reqtable = nodes.table(classes=['reqtable'])
  
        tgroup = nodes.tgroup(cols=3)
        reqtable += tgroup
  
        tgroup += nodes.colspec(colwidth=15, classes=['reqid'])
        tgroup += nodes.colspec(colwidth=15, classes=['section'])
        tgroup += nodes.colspec(colwidth=70, classes=['evidence'])
  
        thead = nodes.thead()
        tgroup += thead
        append_row(thead, ['Req', 'Section', 'Evidence'])
  
        tbody = nodes.tbody()
        tgroup += tbody

        sorted_req = sorted(env.req_all_reqs, key=lambda req: req['reqid'])

        for req_info in sorted_req:

            refpara = nodes.paragraph()
            refpara += nodes.Text("","")

            # Create a reference
            try:
                newnode = nodes.reference('', '')
                #pprint(req_info['reqid'])
                section = req_info['section']
                section_name = ''
                if section.get('secnumber'):
                    section_name += (('%s' + self.secnumber_suffix) %
                             '.'.join(map(str, node['secnumber'])))
                section_name += section[section.first_child_matching_class(title)][0].astext()
                pprint(section_name)
                innernode = nodes.emphasis(section_name,section_name)
                newnode['refdocname'] = req_info['docname']
                newnode['refuri'] = app.builder.get_relative_uri(
                    fromdocname, req_info['docname'])
                newnode['refuri'] += '#' + req_info['target']['refid']
                newnode.append(innernode)
                refpara += newnode
                refpara += nodes.Text('', '')
            except:
                continue

            append_row(tbody,
               [req_info['reqid'],
                refpara,
                req_info['evidence']])

            
        content.append(reqtable)

        node.replace_self(content)