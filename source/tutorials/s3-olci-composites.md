# Sentinel-3 OLCI composites

```{image} assets/Sentinel-3-OLCI-composites-icon.png
:width: 200px
```

**Sentinel-3 OLCI composites**

This service takes as input a Sentinel-3 OLCI Level 1 (OL_1_EFR\_\_\_) product and uses the bands Oa08, Oa06, Oa_04 to do a true colour RGB composite.

______________________________________________________________________

**EO sources supported**

This service supports as input the **Sentinel-3 OLCI Level 1 (OL_1_EFR\_\_\_)** product.

**Output specifications**

The service provides the following output product.

```{eval-rst}
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output – Sentinel-3 OLCI composites                                                                                                           |
+===============================+===============================================================================================================+
| **Correspondent file**        | Sentinel-3 OLCI composites                                                                                    |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Raster format**             | GeoTIFF                                                                                                       |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **resolution**                | Native                                                                                                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Projection types**          | EPSG:3857 - WGS84 – Pseudo Mercator                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Output Filename example**   | S3 OLCI Natural Colors - Quicklook (2020-08-26T09:08:53/2020-08-26T10:08:53)                                  |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
```

## Select the processing

- Login to the platform (see {doc}`user <../community-guide/user>` section)
- Go to the Geobrowser, expand the panel “Processing services” on the right hand side and select the processing service “S3 OLCI Composites”:

:::{figure} assets/Sentinel-3-OLCI-composites.png
:align: center
:figclass: align-center
:width: 750px
:::

This will display the "S3 OLCI Composites" service panel including several pre-defined parameters values to be filled-in.

:::{figure} assets/Sentinel-3-OLCI-composites-1.png
:align: center
:figclass: align-center
:width: 750px
:::

## Fill the parameters

### Reference input

- Select the Sentinel-3 data collection in the EO Data button.

:::{figure} assets/Sentinel-3-OLCI-composites-2.png
:align: center
:figclass: align-center
:width: 750px
:::

- Select the area for which you want to do an anlysis, e.g over Munich.

:::{figure} assets/Sentinel-3-OLCI-composites-3.png
:align: center
:figclass: align-center
:width: 750px
:::

- Click on the lens icon to open the Search Panel
- Select **OL_1_EFR\_\_\_** as Product Type.
- Apply the date value, for example **2020-08-26** in both **time:start** and **time:end** fields.

:::{figure} assets/Sentinel-3-OLCI-composites-4.png
:align: center
:figclass: align-center
:width: 250px
:::

- Drag and Drop the selected item in the *Input references* field:

:::{figure} assets/Sentinel-3-OLCI-composites-5.png
:align: center
:figclass: align-center
:width: 750px
:::

- Select **Yes** or **No** in **Natural colors (Oa08, Oa06, Oa_04)** field.

:::{figure} assets/Sentinel-3-OLCI-composites-6.png
:align: center
:figclass: align-center
:width: 750px
:::

## Run the job

- Click on the button Run Job and see the Running Job

:::{figure} assets/Sentinel-3-OLCI-composites-7.png
:align: center
:figclass: align-center
:width: 350px
:::

:::{figure} assets/Sentinel-3-OLCI-composites-8.png
:align: center
:figclass: align-center
:width: 350px
:::

- After about 45 minutes, see the Successful Job:

:::{figure} assets/Sentinel-3-OLCI-composites-9.png
:align: center
:figclass: align-center
:width: 350px
:::

## Results: download and visualization

- Click on the button *Show results*
- See the result on map:

:::{figure} assets/Sentinel-3-OLCI-composites-10.png
:align: center
:figclass: align-center
:width: 750px
:::

- The following output files are produced:

  > - **S3 OLCI Natural Colors - Quicklook (2020-08-26T09:08:53/2020-08-26T10:08:53) - product GeoTIFF RGB**
