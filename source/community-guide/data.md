---
substitutions:
  search: |-
    ```{image} ../includes/geobrowser_button_query.png
    ```
---

# Data

:::{figure} ../includes/data.png
:align: center
:figclass: img-container-border
:scale: 30%
:::

Discovery of data is made through the {doc}`geobrowser <platform/geobrowser>`.

You can search for data from a specific collection of a catalogue or from a public or private data package, look for data related to specific events, simply see amongst the proposed contextualized results, or even search within results of a processed wps job.

Put data in your basket and save it for later, or simply drag and drop data as a parameter of a process.

When the OWS Context describing the data contains the adequate information, the data can be visualized on the geobrowser (e.g as an image, as a time series, ...) and a popup containing metadata about the data will be displayed.

## Discover data

Data discovery is made through the map. To get specific data:

1. Focus on an area of the geobrowser.
2. Select a time period on the time slider.
3. Click on {{ search }} to open the query tab.
4. Fill in specific parameters.
5. Click on **Search**.
6. Results appear on the map and the **Results Table**.
7. Click on a result (directly on the map or in the Results table) to get more info about this result.

:::{tip}
in the *Search Term* field supported wildcards are '\*', which matches any character sequence (including the empty one), and '?', which matches any single character.
:::

:::{figure} ../includes/geobrowser_map_data.png
:align: center
:figclass: img-border
:scale: 75%

Example of Sentinel 1 popup information
:::

:::{figure} ../includes/geobrowser_map_data_result.png
:align: center
:figclass: img-border
:scale: 75%

Example of process result popup information
:::

## Manage the search filters

Once you have performed a search, all filters used for this search are displayed on the window, grouped by type of filter (e.g time, spatial, earth observation, ...).
You can then remove one filter, remove the whole filter group or check the selected value (go over with the mouse during few seconds).

:::{figure} ../includes/geobrowser_filters.png
:align: center
:figclass: img-border
:scale: 50%
:::

## Discover contextualized data

Data related to a specific context can be accessed by clicking on one of the available context on the top-right of the browser.

Currently existing contexts are:

- EO data
- EO processing
- Publications
- Community

Once clicked on a context, data automatically appear on the map.

## Discover data related to a specific event

To access data related to a specific event:

1. Access the geobrowser, by default, data related to specific geohazards events (provided by the disaster charter) are displayed on the map.
2. Focus on one event.
3. Click on **Time filter**, **Spatial filter** or **Both filters** to use the event metadata to make a query.
4. Data related to this event is automatically added to the result tab and displayed on the map.

:::{figure} ../includes/geobrowser_data_event.png
:figclass: img-border
:::

## Discover data results from a processing job

To visualize results on the map:

1. Access the job (see [Access public jobs] or {doc}`Share a job <sharing>`).
2. If a layer is detected, you can display it on the map from the **Results** part of the job description.
3. Click on **Show results on map**.
4. The layer is displayed on the map.
5. A popup containing results metadata is displayed by clicking on the product.

::::{warning}
> You may need to be connected to the GEP Virtual Private Network (see {ref}`laboratory`), in order to download the results.

:::{figure} ../includes/geobrowser_job_result_visualisation.png
:align: center
:figclass: img-border
:scale: 75%
:::
::::

## Select data in your basket

Data can be selected on the map as well as on the result tab.

1. Click on data on the map to make it appear on the **Results Table**.
2. Drag data from the **Results Table** to the **Features Basket**.
3. Data appears on the **Features Basket**.

:::{figure} ../includes/geobrowser_basket.png
:figclass: img-border
:::

## Save basket as data package

To create a new data package:

1. Add all data you want in the **Features Basket**.
2. Click on **Save**.
3. Choose a name for the data package.
4. Click on **Save**.
5. The data package is saved on the platform, you can re-access it later.

:::{figure} ../includes/geobrowser_dp_save.png
:figclass: img-border
:scale: 75%
:::

## Load an existing data package

To access a previously saved data package:

1. Click on the **Data Packages** tab.
2. Select a data package on the list.
3. To add all the items from the data package into the current basket, click on *load*.
4. To use the data package as the current search, click on *set as current search*.

:::{figure} ../includes/geobrowser_dp_load.png
:figclass: img-border
:scale: 75%
:::

## Clear the basket

To clear your current basket:

1. Click on **Remove all** on the basket tab.
2. Your basket is now empty.

## Use data in a process

1. Select one of the processing services and open it.
2. The list of parameters is visible.
3. Select one or more entries either from the **Results Table** or from the **Features Basket**.
4. Drag the data and drop it over the selected parameter.
5. In case of several items, it creates one occurence of the parameter per item.
6. Data are ready to be used in the process. Click on **Run process** to actually run the process.

## Download data

To download a data listed on the *Results Table*:

1. Click on the data on the list or directly on the geobrowser.
2. A popup is displayed, containing a **Download** button.
3. Click on the button, if it exists several links to the data, a dropdown list is displayed.
4. Click on one of the links. The download may start directly or you may be redirected to the server hosting the data for authorization.

### Data Gateway

If the resource location points to a data gateway url (usually the name contains **via Data Gateway**), ex: **https://store.terradue.com/download/sentinel1/files/v1/S1A_IW_SLC\_\_1SDH_20160915T090555_20160915T090624_013061_014B4B_4793**

then the download is performed via the Data Gateway that enables many function such as caching to allow the best download performance of the data requested.

:::{warning}
Please be aware that the Data Gateway Proxy Download may take some time to start depending of the configuration of the repository from which you perform the download. Indeed, the data gateway may be required to perform Implicit caching before delivering the data.
:::

## Upload dataset on Terradue storage

Most of thematic applications provide to the user a **Store Upload** button allowing him to upload local data to his private storage or to the storages shared with the community (e.g gep-community).
For more details on how to use this functionality, see {ref}`dataupload`.

## Publish datasets on Terradue catalogue

Most of thematic applications provide to the user a **Data Publication** WPS service allowing him to publish data from his private storage or from storages shared with the community (e.g gep-community) to the Terradue catalogue, under his private index or under an index shared with the community (e.g gep-community). For more details on how to use this functionality, see {ref}`datapublish`.

For more details on how to use this functionality, see {ref}`dataupload`.
