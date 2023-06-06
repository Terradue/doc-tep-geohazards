# Visualisation

:::{figure} ../includes/visualisation.png
:align: center
:figclass: img-container-border
:scale: 50%
:::

## Access job result

:::{figure} ../includes/job_results.png
:figclass: img-border
:scale: 50 %
:::

To visualize job's result:

1. Select a job in the **Jobs** tab from the Processing services.
2. Click on the job title, the following infos will appear:

- **Job info**: main info about the job + access to the Status/Result location
- **Parameters**: list of used parameters
- **Results**: if specific actions on the result are available
- **XML Result**: XML result returned by the WPS

## Visualize result on the map

:::{NOTE}
The visualization capabilities depends on the offerings presented in the OWS Context document representing the results.
The Geobrowser will be able to display:

- Footprint of a dataset on the map
- WMS/WMS-T raster display in the extent defined
- Projected Image raster overlay (png, jpeg, gif) with a defined extent
- Popup with information given in the abstract of the dataset or a de-fault popup with default information (title, id, dates)
:::

### Jobs results

To visualize results on the map:

1. Access the job once it is finished (see [Access my jobs]).
2. If a layer is detected, you can display it on the map from the **Results** part of the job description.
3. Click on **Show results on map**.
4. The layer is displayed on the map, according to the offerings presented in the OWS Context of the result.

:::{WARNING}
You may need to be connected to the GEP Virtual Private Network (see {ref}`laboratory`), in order to download the results.
:::

### Community results

To visualize community results on the map:

1. Access the Community context on the geobrowser (see {ref}`geobrowser`).
2. Select a data published in the Community context using the search function.
3. The layer is displayed on the map, according to the offerings presented in the OWS Context of the result.

:::{WARNING}
You may need to be connected to the GEP Virtual Private Network (see {ref}`laboratory`), in order to download the results.
:::
