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

-  |geobrowser_button_search.png| search text
-  |geobrowser_button_search_area.png| search area
-  |geobrowser_button_plus.png| Zoom in
-  |geobrowser_button_minus.png| Zoom out
-  |geobrowser_button_query.png| Open query search tab
-  |geobrowser_button_polygon.png| Edit the search bbox by drawing a polygon on the map
-  |geobrowser_button_recbox.png| Edit the search bbox by drawing a rectangle on the map
-  |geobrowser_button_placemark.png| Edit the search bbox by selecting a point as AOI
-  |geobrowser_button_wkt.png| Allow to enter a WKT or upload a shapefile, a kml or a geojson to be displayed on the map as bounding box
-  |geobrowser_button_meter.png| Measure an area
-  |geobrowser_button_fullscreen.png| Put the map in full screen
-  |geobrowser_button_layers.png| Change the background of the map | Select layers to be displayed.

Search area
***********
From the geobrowser, a search area can be accessed by clicking on the |geobrowser_button_search_area.png| button. This expands a view containing all search parameters associated to the current catalogue on which the search will be performed.
Some parameters are just free text, others can be chosen from a list, and some parameters can be filled from the geobrowser. This is the case of:

- the temporal parameter which can be filled by moving the temporal bar present on the geobrowser.

.. figure:: ../../includes/geobrowser_timebar.png
	:figclass: img-border img-max-width

- the geographical area which can be filled either from the bbox drawn on the map using |geobrowser_button_polygon.png|, |geobrowser_button_recbox.png|, |geobrowser_button_placemark.png| or by uploading a shapefile, a kml or geojson file, using the import button |geobrowser_button_wkt.png|.

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

Area of interest
*****************

.. figure:: ../../includes/aoi.png
	:align: center
	:figclass: img-container-border
	:scale: 80%


Area of interest may be defined by the user using the tools to draw a polygon or a rectangle on the map (see `Map`_). Once set, the search will be automatically updated with data corresponding to this AOI.

Area of interest external definition
````````````````````````````````````

Complex Area of interest can be defined by uploading or referencing a vector based file:

- shapefile (limited to 1MB)
- kml (limited to 1MB)

Area of Interest according to processing service
````````````````````````````````````````````````

Area of Interest may be directly used to fill bounding box parameters exposed by Processing services.
For that, you can use the |get_param_from_map_button.png| button, displayed along the parameter input field. Clicking on it will allow directly to fill the input with the value of the current search bounding box.

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

.. figure:: ../../includes/geobrowser_jobs.png
	:figclass: img-border


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
.. |geobrowser_button_search_area.png| image:: ../../includes/geobrowser_button_search_area.png
.. |geobrowser_button_search.png| image:: ../../includes/geobrowser_button_search.png
.. |geobrowser_button_polygon.png| image:: ../../includes/geobrowser_button_polygon.png
.. |geobrowser_button_recbox.png| image:: ../../includes/geobrowser_button_recbox.png
.. |geobrowser_button_placemark.png| image:: ../../includes/geobrowser_button_placemark.png
.. |geobrowser_button_meter.png| image:: ../../includes/geobrowser_button_meter.png
.. |geobrowser_button_wkt.png| image:: ../../includes/geobrowser_button_wkt.png
.. |geobrowser_button_fullscreen.png| image:: ../../includes/geobrowser_button_fullscreen.png
.. |geobrowser_button_layers.png| image:: ../../includes/geobrowser_button_layers.png
.. |geobrowser_disaster_big_group.png| image:: ../../includes/geobrowser_disaster_big_group.png
.. |geobrowser_disaster_small_group.png| image:: ../../includes/geobrowser_disaster_small_group.png
.. |geobrowser_disaster_event.png| image:: ../../includes/geobrowser_disaster_event.png
.. |get_param_from_map_button.png| image:: ../../includes/get_param_from_map_button.png
