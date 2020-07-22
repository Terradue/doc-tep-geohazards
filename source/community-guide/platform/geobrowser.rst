GeoBrowser
======================================================

.. figure:: ../../includes/geobrowser-geobrowser.png
	:figclass: img-border img-max-width

Intro
----------

The geobrowser is a map-based web application, allowing users to perform data exploration, data visualization, data analysis and data processing.

The application spreads on the common OGC standards:

- Opensearch, to have a standard and dynamic way to search data;
- OWS context, to manage a search results;
- WPS, to perform data processing.

The geobrowser is based on a "current search" concept. The "current search" is an entity representing the data of the catalog we are currently navigating. It is defined on the couple **{current opensearch description, current search parameters}**:

- The opensearch description is a document (retrieved by an opensearch description url) describing the data we are exploring in a given moment including how we can search the data, what are the search parameters and how each parameter works. From the opensearch description the geobrowser creates a search engine and populates a dynamic search form.
- The current search parameters is a set of parameters values and filters, from which we can have a search results to show on the geobrowser.

On the geobrowser, users can change and manipulate the current search in 2 ways:

- **By changing the current opensearch description**: a thematic app offers a list of defined Opensearch Descriptor in a tree menu called Contexts Menu. Morehover, you can also change the current search by showing a result of a processing job, or by switching on a correlated search.

- **By applying some filters changing parameters values**: all parameters are included in the Search Panel form, but for some predefinite parameters there is also an utility widget on the map, to make more intuitive the interaction to change the values. For example the search terms, the spatial query buttons and the date are represented as widget inside the map.

A current search always involves a current search result, which is the search result on the catalog with a specific opensearch description and a specific parameters values set. That result is on OWS context standard, encoded in geoJSON format, and contains a list of results entries called Features. Each feature is shown on the Results Panel, and a details view for a selected feature is offered to show all the features info. Morehover, the features containing geographic information (like bounding box, map image, WMS service) are also visible and represented on the Navigation Map.

Let's see in the details each component of the geobrowser.

Geobrowser Layout
-----------------

.. figure:: ../../includes/geobrowser-geobrowser-layout.png
	:figclass: img-border img-max-width

The Geobrowser is composed of:

- **Navigation map**, the map area;
- **Contexts menu**, a menu used to switch among predefinite search;
- **Catalog panel**, a panel showing all info about the current search and the saved results. This panel is splitted in more sub panels, shown only one at a time to improve focus and usability:

   - **Search Panel**
   - **Results Panel**
   - **Features Basket panel (or saved results)**
   - **Data packages panel**
   - **Details panel**

- **Processing panel**


Navigation map
--------------

.. figure:: ../../includes/geobrowser-navigation-map.png

The navigation map is a simple geographic map, on which you can zoom in, zoom out, pan and see all the geographic features of the current results. The Navigation Map can show on the map features as:

- Geometries (or footprints), like polygons or rectangles or points;
- Spatial image, like a jpg or png inside a defined bounding box;
- WMS layers.

Contexts menu
-------------
The Contexts menu is a menu placed on the top, representing a result of a query on a specific catalog with pre-defined search parameters. By choosing a context the Current search will switch with the relative Opensearch Description and optionally with the relative search parameters.

.. figure:: ../../includes/geobrowser-contexts-menu.png


The default pre-defined contexts are:

- EO Data
- EO-based products
- Community
- Private

This can be changed, depending on the Thematic application.

Catalog Panel
-------------
The Catalog Panel is a panel showing all infrmation about the current search and the saved results. This panel implements three of the "Information Seeking Mantra" interactions (search, list results, details on demand). These three interation are represented in three different views and panels: the search panel, the results panel and the details panel, plus two extra panels: the Saved Results panel and the Data Packages panel. To improve focus and usability, one subpanel is visible at a time, by a tab switcher.
Users can open or close the Catalog Panel by the Tools button.

.. figure:: ../../includes/geobrowser-catalog-panel-tabs.png

Search panel
^^^^^^^^^^^^
The search panel is a view containing all search parameters associated to the current catalogue on which the search will be performed. The search panel is showed as a form, and, depending on the opensearch descriptor document, some parameters are just free text, some of them have type restrictions, others can be chosen from a list.
Some predefinite parameters, if present on the opensearch descriptor, are also visible as an external widget on the map, like the Time slider, the Search terms and the Geo Filters. The startIndex standard parameters is also shown as a pagination widget inside the results panel.

.. figure:: ../../includes/geobrowser-catalog-panel-search-panel.png

Results panel
^^^^^^^^^^^^^
This panel shows the result of the current search as a list of features. Some search results information are also visible on the panel header.
When a search is done this panel automatically is activated showing the results.

.. figure:: ../../includes/geobrowser-catalog-panel-results-panel.png

From the results panel users can do different interactions and operations:

- see all results in a scrollable list
- check the type of feature
- select one or more features
- open the details panel for a feature (double click)
- highlight a feature on the map (if the feature has geospatial information)


Features Basket panel (or saved results)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users can save the features from the results panel into a personal user space called Features Basket (or saved results). This panel is similar to the results panel, since it has a list of the features saved by user and those features are visible in the map and on the details panel, but it could contain features from different catalogs.
To put features into the features basket users can simply drag one or more features on the features basket icon.

.. figure:: ../../includes/geobrowser-catalog-panel-features-basket-panel.png

Users can navigate among the features (like on the results panel), remove one or more feature or clean all the features basket.
Moreover users can save and export the features basket in a Data Package, allowing users to share results.

Data packages panel
^^^^^^^^^^^^^^^^^^^

A data package is a saved collection of features. The Data Packages panel shows all data packages visible to users. A data package can be opened by replacing it to the Current Search.

.. figure:: ../../includes/geobrowser-catalog-panel-data-packages-panel.png


Details panel
^^^^^^^^^^^^^

The details panel is a "floating panel", that is, is a panel not visible as a tab. Users can also see this panel from a specific feature, by double click on it, or by opening the details from the popup. This action shows in a vertical scrollable layout page all description information of the feature, including summary, images, key-value information, Also, from the details panel user can perform some actions, like filter the current search by the feature spatial information, or check out some feature correlated results.

.. figure:: ../../includes/geobrowser-catalog-panel-details-panel.png

Processing Panel
----------------

While the Catalog Panel allow users to navigate and retrieve information on the data, the Processing Panel allow users to perform operation on the data. The Geobrowser uses WPS standard to provide rules for standardizing inputs and outputs for invoking processing services. From the processing panel users can:

- navigate among available processing services;
- see a processing service in the details;
- execute a processing service (job);
- search for executed jobs;
- show details for a selected job;
- show results on the navigation map and catalog panel.

To do this there are 4 views: Services tab, Service Details, Jobs tab, Job Details. For no logged users is only possible to view the jobs information and results.

Services Tab
^^^^^^^^^^^^
This tab contains the list of available Processing Services. Users can apply some filters to looking for a specific service. Choosing a service the relative details are shown.

.. figure:: ../../includes/geobrowser-processing-panel-services.png

Service Details
^^^^^^^^^^^^^^^
This view includes a description of the selected service (title, version, description, and so on), followed by a form of all service inputs. Users can fill the form manually, by features dragging (if available for the input) or by the geobrowser clipboard. Is also possible to import and export parameters set in a json format.

.. figure:: ../../includes/geobrowser-processing-panel-service-details.png

Jobs tab
^^^^^^^^
This tab contains the list of available jobs associated to the user or thematic app. Users can filter the job for job title or job type (mine, thematic, all). Details on jobs can be accessed by clicking on the title of the job.
For running jobs it's possible to view the running percentage status.

.. figure:: ../../includes/geobrowser-processing-panel-jobs.png

Job Details
^^^^^^^^^^^
The job details view contains all job information, like some service info, job time, job author, job status (running, succeded, failed) and job results. A job result can be represented as a Opensearch Description element, so users can see the results of a job on the Navigation Map and on the Catalogue control by changing the Geobrowser Current Search with the job result. It's also possible to resubmit the job with the same parameters.

.. figure:: ../../includes/geobrowser-processing-panel-job-details.png


Geobrowser Tools and Utils
--------------------------

Intelligent Map tools
^^^^^^^^^^^^^^^^^^^^^
To simplify the user view on the map, all the map tools buttons are hidden. To show them it's simply necessary go move on the left side of the map.

.. figure:: ../../includes/geobrowser-tools-1.gif

Spatial Filters
^^^^^^^^^^^^^^^
Some Opensearch Descriptions have special standard parameters, for some of them the Geobrowser has a set of widget to allow users to easely and visually change the parameter values. For example, the geo:box parameter (filter by rectangle) and the geo:geometry parameter (filter by a custom shape in wkt) have some spatial buttons inside the map tools. From these controls, users can directly draw on the map the shape to perform the spatial query.

- |geobrowser_button_polygon| Edit the search bbox by drawing a polygon on the map
- |geobrowser_button_recbox| Edit the search bbox by drawing a rectangle on the map
- |geobrowser_button_placemark| Edit the search bbox by selecting a point as AOI
- |geobrowser_button_wkt| Allow to enter a WKT or upload a shapefile, a kml or a geojson to be displayed on the map as bounding box


Geocoding
^^^^^^^^^
The Geocoding control allow users to:
- find some places on the map (giving a place text);
- perform a spatial query on the data by a place found.
A place text could be a country, a city name, a street, a mountain, a river, and so on.

.. figure:: ../../includes/geobrowser-geocoding.png

WMS Layers
^^^^^^^^^^
The geobrowser can show multiple WMS (Web Map Service) layers if there are features exposing WMS layer information on the current search result.
In order to improve the performance and the User experience, when an EO Collection exposes WMS layers, some of them can be active whereas others can be hidden. This behaviour happens after a certain level of zoom, moreover the actual number of the active layers is dynamic and depends on the number of WMS requests necessary to show the layers on the current view on the map.
A User can interactively choose to see a hidden layer, by clicking on it on the Results Panel or directly on its footprint on the map. Footprints are indeed always visible on the map. Furthermore, a User can decide to "lock" one or more layers to study, for instance, correlations between them.
Here below, a legend shows the possible statuses for a product in the result table:

.. figure:: ../../includes/geobrowser-tools-2.png

On the map, products containing active/hidden WMS layers differ as shown:

.. figure:: ../../includes/geobrowser-tools-3.png

WMS Comparing
^^^^^^^^^^^^^
If two or more features exposing WMS are selected, a new menu item is added on the features selecting dropdown menu: the "Compare Layers" button. By pressing this button an interactive visual comparing tool is opened, showing only the selected layers with a vertical slidebar. This tool is useful for juxtaposed wms layers to allow easy comparision and detection of changes.

.. figure:: ../../includes/geobrowser-compare-1.png

.. figure:: ../../includes/geobrowser-compare-2.gif

Time Slider
^^^^^^^^^^^
If the Current Opensearch Description exposes the standard temporal query parameters (time:start, time:end), and if the thematic app allows it, a Time Slider is added on the bottom of the map. This widget is useful to visual selecting a time range for a time restriction on the current search. Moreover, the Time Slider contains visual representation of the data distribution over the time.

.. figure:: ../../includes/geobrowser-timeline-1.png
.. figure:: ../../includes/geobrowser-timeline-2.png

Search Terms
^^^^^^^^^^^^
The Search Terms is a default standard Opensearch Parameter. The geobrowser represent this with a simple input text widget, always visible on the top left of the map. It's a "keypress" triggered input, users don't need to press a confirmation after typing, the search is automatically launched as users stop to type the text to search.

.. figure:: ../../includes/geobrowser-search-terms.png

Full Screen
^^^^^^^^^^^
A simple button to switch to full screen.

.. figure:: ../../includes/geobrowser-fullscreen.png

Point Info
^^^^^^^^^^
By right-click on a empty point on the map a context menu will open to show some actions like "Center map here" (pan in the selected zone on the map), zoom in, zoom out, and a useful utils "Show coordinates". This utils will show a popup with information about the coordinates of the point selected on the map, in different formats.

.. figure:: ../../includes/geobrowser-point-info.gif

layers control
^^^^^^^^^^^^^^
On the top-right of the map there's the layers control: collapsed in a button, by going over it a panel will expand, showing the list of all layers and layers groups in a scrollable panel.

There are two types of layers: 

- base layers, that are mutually exclusive (only one can be visible on your map at a time), 
- overlays, which are all the layer put over the base layers. Usually a base layer is a global map like streetview.

From the layers control users can switch between the base layers (defined on the thematic app configuration), and can show/hide the overlay layers.
On the geobrowser there are some predefinite overlay layers:

- Data Results: the layers group bound with the Current Search
- Features Basket: the layers group bound with the Features Basket
- Related Search: the layers group associated to a correlated search (if available)

.. figure:: ../../includes/geobrowser-layers-control.png

Moreover, users can also set the opacity b§y clicking on the opacity button and set the opacity slider.

Geobrowser Clipboard
^^^^^^^^^^^^^^^^^^^^
The geobrowser clipboard is a facility used to pass data between the geobrowser components, in particular from the current search status and results to the wps services fields. The Geobrowser Clipboard consists in a set of adaptable and dynamic information stored in a temporary buffer during the user interaction. For example, if user selects one or more features, some selected feature information (such as start time or identifier) are stored in the clipboard for a reuse of the values.
Another clipboard type can be a search value, like search start date or end date.

Each clipboard element has a identifier, a value, a clipboard type (feature or search) and a data type. A value colud be an array, for example, if user selects 10 fields, the search:startDate geobrowser clipboard item stores 10 start dates.

.. figure:: ../../includes/geobrowser-clipboard.png

The wps service fields has a geobrowser clipboard menu, used to retrieve the clipboard values previosely stored.

Drag'n drop Features
^^^^^^^^^^^^^^^^^^^^
A feature (or a set of features) selected from the Results Panel can be dragged to use it as a wps service parameter value, or to add it it to the features basket. The
For the first operation it's necessary to have the wps service opened with the allowed target wps field parameter visible, simply by dropping the feature(s) on the wps field, this field will be set with the feature identifier. This operation is available for the features basket result too: it's possible to add a feature from the features basket on a wps field parameter.
For the second operation (add to features basket), users can add selected features from the results panel to the features basket panel simply by dragging the features and dropping them into the features basket tab icon.


.. |geobrowser_button_polygon| image:: ../../includes/geobrowser_button_polygon.png
.. |geobrowser_button_recbox| image:: ../../includes/geobrowser_button_recbox.png
.. |geobrowser_button_placemark| image:: ../../includes/geobrowser_button_placemark.png
.. |geobrowser_button_wkt| image:: ../../includes/geobrowser_button_wkt.png
