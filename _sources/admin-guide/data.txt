Data collections management
===========================

Manage Data Collections
-----------------------

| The Data Collections management page contains a list of all existing Data Collections in DB, with the possibility for an Administrator to *Create* a new Data Collection, *Update* or *Delete* an existing one.
| The Administrator can also *Manage* groups that can see each Data Collection (by clicking on |manage|). This will allow him to define if the Data Collection is public (visible for all), private (visible only by the owner and administrators) or restricted only to a list of groups.

| To add a group, click on |plus| in front of the group's name in the *All Groups* panel.
| To remove a group, click on |minus| in front of the group's name in the *Allowed Groups* panel.

.. |manage| image:: ../includes/groups_manage.png
.. |plus| image:: ../includes/plus.png
.. |minus| image:: ../includes/minus.png

Publish or update an OWS context document
-----------------------------------------

A OWS context document contains one or more entries describing documents. Full specification for OWS documents is available at http://www.opengeospatial.org/standards/owc

Each document is identified with a unique identifier within the collection in which it is published.
The following example describes step by step how to publish a user result in the "EO processing" collection.

1. Generate the OWS document based on the following template:

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<feed xmlns="http://www.w3.org/2005/Atom">
	  <id>urn:uuid:607ba1aa-7f43-4b85-9d75-adab715dc9c5</id>
	  <entry>
	  	<id>ALOS.20070211_20100219.Nepal_S.2cmyr.tif</id>
	    <title type="text">Himalaya / Nepal - Landslide - ALOS.20070211_20100219</title>
	    <published>2015-05-04</published>
	    <updated>2015-05-04</updated>
	    <summary type="text/html"><![CDATA[
							<table>
								<tbody>
									<tr valign="top">
										<td>
											<b>Source</b></td>
										<td>
											EO-WORLD
										</td>
									</tr>
									<tr valign="top">
										<td>
											<b>Site</b></td>
										<td>Himalaya - Nepal</td>
									</tr>
									<tr>
										<td>
											<strong>Platform</strong></td>
										<td>
											ALOS</td>
									</tr>
									<tr valign="top">
										<td>
											<b>Observations</b></td>
										<td>
											20070211_20100219</td>
									</tr>
								</tbody>
							</table>
	<p></p>
		]]>
	    </summary>
	    <identifier xmlns="http://purl.org/dc/elements/1.1/">ALOS.20070211_20100219.Nepal_S.2cmyr.tif</identifier>
	    <box xmlns="http://www.georss.org/georss">27.328 86.35 28.15 87.1</box>	
	    <offering xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://www.opengis.net/owc/1.0" code="http://www.opengis.net/spec/owc-atom/1.0/req/wms"> 
		  <operation code="GetMap" method="GET" href="https://maps.eo.esa.int/erdas-apollo/coverage_public/NEPAL?service=WMS&amp;version=1.1.1&amp;request=GetMap&amp;layers=ALOS.20070211_20100219.Nepal_S.2cmyr&amp;styles=&amp;bbox=86.35,27.328,87.1,28.15&amp;width=1024&amp;height=1024&amp;srs=EPSG:4326&amp;format=image/png&amp;transparent=TRUE" type="image/png"/>
	    </offering>
	    <date xmlns="http://purl.org/dc/elements/1.1/">2007-02-11/2010-02-19</date>
	  </entry>
	</feed>

PLease note the important fields:

- identifier (mandatory) : contains the unique identifier within the collection. If an entry with the same name exists, it will be overriden.

- title (mandatory) : main label to be displayed in the result table of the geobrowser

- published and updated (mandatory) : date for the ordering in the collection, documents are disployed in the descending order of publication.

- box (mandatory) : must contain the area of interest of the entry. (minY minX maxY maxX)

- date (mandatory) : on date or interval of dates serparated by a '/' (format http://en.wikipedia.org/wiki/ISO_8601)

- summary (optional) : short description in text or html to be display in the popup when result is selected

- offering (optional) : defines the properties of a specific service binding or inline content for an offering. In the current example, the offering is a WMS layer for quicklook visualization on the map. Whenever possible, the geobrowser shall display the offering on the map.

2. via a curl command or with any other REST client, POST the document to the right collection:

.. code-block:: curl

	curl 'http://data.terradue.int/gs/catalogue/tepqwsr/gtfeature' -H 'Pragma: no-cache' -H 'Content-Type: application/atom+xml' -H 'Accept: application/xml' -H 'Cache-Control: no-cache' -d @file.atom

The collections to post to are:

- http://data.terradue.int/gs/catalogue/tepqw/gtfeature : EO data
- http://data.terradue.int/gs/catalogue/tepqwsr/gtfeature : EO-based products
- http://data.terradue.int/gs/catalogue/tepqwpub/gtfeature : Publications
- http://data.terradue.int/gs/catalogue/users/gtfeature : Community


