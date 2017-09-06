Using GitHub
============

GitHub is a web-based hosting service for software development projects that use the Git revision control system. 

GitHub offers both paid plans for private repositories, and free accounts for open source projects.

GEP Laboratory and the GitHub organization
++++++++++++++++++++++++++++++++++++++++++

The GEP laboratory has a one-to-one relationship with the corresponding GEP GitHub organization https://github.com/geohazards-tep/.

Organizing the GitHub teams
+++++++++++++++++++++++++++

Within a GEP GitHub organization, you can organize as many teams including any number of members (typically developers).

Owners have full access to all repositories and have admin rights to the organization. 

Created teams can have several levels of priviliedges:

* Read Access: This team will be able to view and clone its repositories. 
* Write Access: This team will be able to read its repositories, as well as push to them.
* Admin Access: This team will be able to push/pull to its repositories, as well as add other collaborators to them.

.. tip:: We recommend managing teams with a reduced number of member within a team with write access. The remaining team members with Read only access are invited to fork the repository and submit pull requests. The owners can then moderate these requests. 

Organizing the repository
+++++++++++++++++++++++++

The repository should follow the structure below:

.. code-block:: bash

  README.md # the markdown file used to generate the html summary seen at the bottom of projects. 
  .gitignore # Git uses it to determine which files and directories to ignore, before making a commit.
  pom.xml # the Project Object Model file containing information about the project and configuration details used by Maven to build the project
  /src # root folder of the application
    /main
      /app-resources
        application.xml
        /job_template1
          run.sh
          /etc
          /bin
        /job_template2
          ...
      /java # if your application has Java code
      /resources # resources used to build the application
      /R # if you application has R code
      /python # if you application uses python code
      /...
      /doc # use this folder to document the application 
      
.. seealso::
  
Have a look at the application tutorials which implements the recommended structure: 
    
    * MERIS Algal bloom detection https://github.com/Terradue/dcs-beam-algalbloom
    * BEAM Toolbox Java FLH processor https://github.com/Terradue/dcs-beam-flh-java
    * Landsat NDVI python module https://github.com/Terradue/dcs-python-ndvi
    * SST timeseries R package https://github.com/Terradue/dcs-r-gbifsst

The typical application development workflow
++++++++++++++++++++++++++++++++++++++++++++

Cloning an existing repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You'll need the SSH clone URL in the form: git@github.com:Terradue/dcs-beam-flh-java.git

Log on the sandbox using your key:

.. code-block:: bash

  ssh -A -i ~/.ssh/<name>.pem <sandbox ip> 
  
Example:

.. code-block:: bash

  ssh -A -i ~/.ssh/mrossi.pem 10.14.10.20

Run the commands on the shell:

.. code-block:: bash

  cd 
  git clone git@github.com:Terradue/dcs-beam-flh-java.git

Creating a new repository on github.com
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The procedure is describe here: https://help.github.com/articles/creating-a-new-repository

.. tip:: 

  Make sure to create a README.md file to enable cloning as described above

Building the application
^^^^^^^^^^^^^^^^^^^^^^^^

Once the repository contains the structure described above, use *maven* to build and install the application for you:

.. code-block:: bash

  cd ~/dcs-beam-flh-java
  mvn install
  
This will use the information available in the *pom.xml* file to:

* Compile the BEAM Java code and copy the JARs in the right spot 
* Copy the app-resources files to the */application* file system.

At this point you can use *ciop-simjob* and *ciop-simwf* to test the application

.. tip::

  Do not edit files in /application, do it in the cloned directory and then run mvn install again. This will help you maintain the application repository aligned

Updating files
^^^^^^^^^^^^^^

Whilst editing the files in */application* may seem the most obvious way to change your application it also the way to loose changes.

In fact, you should edit the files in the **source** which has been cloned in your */home* folder and use mvn install to update the build which is in */application* with mvn install

Releasing the application
^^^^^^^^^^^^^^^^^^^^^^^^^

The pom.xml also contains information to create releases in GitHub.

To create releases of the application on GitHub use *mvn deploy*:

.. code-block:: bash

  cd ~/dcs-beam-flh-java
  mvn deploy

.. tip:: You can create pre-releases of the application by setting the version in the pom.xml with <version>x.y**-SNAPSHOT**</version>

Documenting the application
^^^^^^^^^^^^^^^^^^^^^^^^^^^

We suggest using the GitHub Pages.

The GitHub pages are public webpages freely hosted and easily published through the GitHub site. 

GitHub pages can be managed manually or using frameworks. We suggest using R Gitbook or Sphinx as documentation generator tool that converts marked-up plaintext files into properly formatted HTML, PDF, EPub or other documents. 

.. warning:: the GitHub pages of a private repository will be public and thus visible to anybody!

To create the GitHub Pages for the project, a new branch and do some one-time setup have to be performed. 

The pom.xml file contains the information on how to build the documentation and update the gh-pages repository branch.

Going further
+++++++++++++

There are several high quality free ebooks on the Web (e.g. http://gitbookio.github.io/git/en/) and GitHub provides a comprehensive web-site to get started here: https://help.github.com/
