GeoBrowser area for data and Cloud processing services
======================================================

GeoBrowser
----------

.. figure:: ../../includes/geobrowser.png
	:figclass: img-border img-max-width


The GeoBrowser is composed of:

	- a `Map`_, where the user can make search query and see results
	- `Contexts`_ links
	- `Results`_ tab (initialy hidden)
	- `Processing services tab`_ (initialy hidden)

Map
~~~

The map is just a simple map, on which you can zoom in, zoom out and navigate.

Some buttons maybe used to interact with the map:

-  |geobrowser_button_search.png| search area
-  |geobrowser_button_plus.png| Zoom in
-  |geobrowser_button_minus.png| Zoom out
-  |geobrowser_button_query.png| Open query search tab
-  |geobrowser_button_polygon.png| Edit the search bbox by drawing a polygon on the map
-  |geobrowser_button_recbox.png| Edit the search bbox by drawing a rectangle on the map
-  |geobrowser_button_dynamicsearch.png| Enable/Disable dynamic search (the search bbox is the current view on the map)
-  |geobrowser_button_fullscreen.png| Put the map in full screen
-  |geobrowser_button_layers.png| Change the background of the map | Select layers to be displayed.

It is also possible to directly select on the map the temporal parameter of the search by moving the temporal bar.

.. figure:: ../../includes/geobrowser_timebar.png
	:figclass: img-border img-max-width

.. tip:: in the *Search Term* field supported wildcards are '*', which matches any character sequence (including the empty one), and '?', which matches any single character.

It is also possible to add layers on the map:

Data Results layer
******************

Display the results (orange polygons) of the current search or context.

Disaster charter layer
**********************

Add disaster events on the map (list of events comes from https://www.disasterscharter.org).
For a better visibility, events are grouped by location, accordingly to the zoom level. If you zoom in, grouped events will split into smaller groups or unique events:

-  |geobrowser_disaster_big_group.png| group of more than 10 events
-  |geobrowser_disaster_small_group.png| group of less than 10 events
-  |geobrowser_disaster_event.png| unique event

You can click on a unique event and get related data or access the webpage related to this event.


Density map layer
*****************

Currently disactivated.


Contexts
~~~~~~~~

.. figure:: ../../includes/geobrowser_contexts.png
	:figclass: img-border

Some pre-defined context are accessible on the top of the map.
One context is the result of a query on a specific catalog with pre-defined search parameters.
The existing pre-defined contexts are:

- EO data
- EO processing
- Publications
- Community

Results
~~~~~~~

.. figure:: ../../includes/geobrowser_resulttab.png
	:figclass: img-border img-max-width

The result tab is divided in two parts:

- On the left, the **Results Table** showing the list of current results displayed on the map. Results are paginatd, only 20 items are displayed, select another page to discover more products.
- On the right, the **Features Basket** showing all data in the current basket.

Results can be dragged fron the left table to the basket. Then the basket can be saved as a new data package and shared with other users.
Saved Data packages can then be loaded into the basket. (see :doc:`data <../data>` for more details)


Cloud Processing
----------------

Processing services tab can be expanded by clicking on *Processing Services* on the right of the map.
It is composed of two sub tabs.

Processing services tab
~~~~~~~~~~~~~~~~~~~~~~~

This tab contains the list of available Processing Services. Usually, only 20 Processing services are displayed. If you are looking for a specific one, you can filter the results using the **Filter services** input.

Jobs tab
~~~~~~~~

This tab contains the list of available jobs associated to your user.
Details on jobs can be accessed by clicking on the title of the job.

.. figure:: ../../includes/geobrowser_jobs.png
	:figclass: img-border


.. |geobrowser_button_query.png| image:: ../../includes/geobrowser_button_query.png
.. |geobrowser_button_plus.png| image:: ../../includes/geobrowser_button_plus.png
.. |geobrowser_button_minus.png| image:: ../../includes/geobrowser_button_minus.png
.. |geobrowser_button_search.png| image:: ../../includes/geobrowser_button_search.png
.. |geobrowser_button_polygon.png| image:: ../../includes/geobrowser_button_polygon.png
.. |geobrowser_button_recbox.png| image:: ../../includes/geobrowser_button_recbox.png
.. |geobrowser_button_dynamicsearch.png| image:: ../../includes/geobrowser_button_dynamicsearch.png
.. |geobrowser_button_fullscreen.png| image:: ../../includes/geobrowser_button_fullscreen.png
.. |geobrowser_button_layers.png| image:: ../../includes/geobrowser_button_layers.png
.. |geobrowser_disaster_big_group.png| image:: ../../includes/geobrowser_disaster_big_group.png
.. |geobrowser_disaster_small_group.png| image:: ../../includes/geobrowser_disaster_small_group.png
.. |geobrowser_disaster_event.png| image:: ../../includes/geobrowser_disaster_event.png
