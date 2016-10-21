.. _app_workspace:

My Workspace
============

Items Management
----------------

Each user has a personal management app called **My worskpace** in which he can manage items he owns such as:

- data collections,
- data series,
- data packages,
- processing services,
- processing jobs

For each item, the user can:

- edit the item (name, description, ...),
- share it with other users or groups (see :doc:`../community_guide/sharing`)
- transfer the ownership to another user

.. req:: HEP-TS-ICD-015
	:show:

	This section describes how the user can share series, data package, services and jobs.

.. figure:: ../includes/user_edit_collection.png
	:figclass: img-border
	:scale: 80%

.. figure:: ../includes/user_edit_datapackage.png
	:figclass: img-border
	:scale: 80%

Catalog Editor
--------------

The catalogue editor area is a workspace dedicated to the user in which he will be able to access all his files (results of processings, uploaded files, ...), manage them and specially ingest them in one of its catalogues or ask to publish the result as a contribution to the community results (this would need to be validated by an administrator).

.. figure:: ../includes/cas_editor.png
	:figclass: img-border
	:scale: 70 %

.. req:: HEP-TS-DES-004
	:show:

	This section describes the catalogue as a service functionality.

.. req:: HEP-TS-DES-001
	:show:

	This section shows that TEP platform implement a catalogue editor.

My Thematic Apps
----------------

From its workspace app, the user has also the ability to create its own Thematic App, by selecting widgets amongst:

- Dataset search widget defining series, collection or data packages OpenSearch endpoint
- processing Service widget defining service series OpenSearch endpoint
- Map description (background, layers)
- Data package widget defining the data packages OpenSearch endpoint

The application shall be defined using OGC OWS Context.

.. figure:: ../includes/user_new_app.png
	:figclass: img-border
	:scale: 80%

.. req:: HEP-TS-FUN-015
	:show:

	This section describes how a user can create its own thematic application.

