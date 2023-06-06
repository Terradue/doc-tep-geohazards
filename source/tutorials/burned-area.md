---
substitutions:
  br: |-
    ```{raw} html
    <br />
    ```
---

# Sentinel-2 Burned Area Analysis

```{image} assets/tuto_burned-area_icon.png
```

**Sentinel-2 Burned Area Analysis**

This service takes as input a pair (pre-event and post-event) of Sentinel-2 MSI L2A products and generates a Burned Area Analysis map and NIR/SVWI RGB composites for the two input Sentinel-2 acquisitions. {{ br }}
This service gives the best results when the post fire image is very close to the fire date. {{ br }}
The masks for the water masks are applied by the service.

**EO sources supported**

> - Sentinel-2 MSI L2A

**Output specifications**

The service provides the following output product.

```{eval-rst}
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output – Burned Area Analysis map                                                                                                             |
+===============================+===============================================================================================================+
| **Correspondent file**        | Burned Area Analysis map                                                                                      |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Raster format**             | GeoTIFF                                                                                                       |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **resolution**                | Native                                                                                                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Projection types**          | EPSG:3857 - WGS84 – Pseudo Mercator                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Output Filename example**   | Burned area analysis (2020-10-05T07:37:49.0240000Z/2020-10-15T07:39:09.0240000Z)                              |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
```

```{eval-rst}
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output – NIR/SVWI RGB composite of the pre-event input                                                                                        |
+===============================+===============================================================================================================+
| **Correspondent file**        | NIR/SVWI RGB composite of the pre-event input                                                                 |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Raster format**             | GeoTIFF                                                                                                       |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **resolution**                | Native                                                                                                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Projection types**          | EPSG:3857 - WGS84 – Pseudo Mercator                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Output Filename example**   | NIR/SVWI RGB composite (2019-08-15T14:01:01.0240000Z/2019-08-15T14:01:01.0240000Z)                            |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
```

```{eval-rst}
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output – NIR/SVWI RGB composite of the post-event input                                                                                       |
+===============================+===============================================================================================================+
| **Correspondent file**        | NIR/SVWI RGB composite of the post-event input                                                                |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Raster format**             | GeoTIFF                                                                                                       |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **resolution**                | Native                                                                                                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Projection types**          | EPSG:3857 - WGS84 – Pseudo Mercator                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Output Filename example**   | NIR/SVWI RGB composite (2019-08-30T14:00:59.0240000Z/2019-08-30T14:00:59.0240000Z)                            |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
```

```{eval-rst}
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output – notebook used for generating dNBR and RBR                                                                                            |
+===============================+===============================================================================================================+
| **Correspondent file**        | notebook used for generating dNBR and RBR                                                                     |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **File format**               | python file (ipynb)                                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Output Filename example**   | Reproducibility notebook used for generating dNBR and RBR                                                     |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
```

```{eval-rst}
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output – stage-in notebook for Sentinel-2 data for generating dNBR and RBR                                                                    |
+===============================+===============================================================================================================+
| **Correspondent file**        | notebook for Sentinel-2 data for generating dNBR and RBR                                                      |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **File format**               | python file (ipynb)                                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Output Filename example**   | Reproducibility stage-in notebook for Sentinel-2 data for generating dNBR and RBR                             |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
```

______________________________________________________________________

This tutorial will describe the processing of a pair of Sentinel-2 MSI images to generate a Burned Area Analysis map and NIR/SVWI RGB composites for the two input Sentinel-2 acquisitions on the GEP. {{ br }}
The Burned Area map is obtained through the interesection between AOI and the pre-fire, post-fire Sentinel-2 choosen as input products. {{ br }}
The formula used to estimate burn severity is the Normalized Band Ratio (NBR):

:::{figure} assets/tuto_burned-area_0.png
:align: center
:figclass: align-center
:width: 250px
:::

A high NBR value indicates healthy vegetation while a low value indicates bare ground and recently burnt areas. Non-burnt areas are normally attributed to values close to zero.
The Burned Area Analysis product output of the service provides the delta Normalized Burn Ratio (dNBR) and the Relativized Burn Ratio (RBR).
The dNBR (the difference between pre-fire and post-fire) is useful to identify recently burned areas and differentiate them from bare soil and other non-vegetated areas. The RBR is advantageous when the absolute change between pre-fire and post-fire NBR is small.

## Select the processing

- Login to the platform (see {doc}`user <../community-guide/user>` section)
- Select the processing service “Sentinel-2 Burned Area Analysis”:

:::{figure} assets/tuto_burned-area_1.png
:align: center
:figclass: align-center
:width: 750px
:::

The "Sentinel-2 Burned Area Analysis" panel is displayed with parameters values to be filled-in.

## Fill the parameters

### Pre-event product reference

- Select the Sentinel-2 data collection in the EO Data button.
- Select the area for which you want to do an anlysis, e.g Corumba in Brasil.

:::{figure} assets/burned_area-2.png
:align: center
:figclass: align-center
:width: 750px
:::

- Click on the lens icon and select **S2MSI2A** as Product Type in the Search Panel
- Apply the date value **2019-08-15** in both **time:start** and **time:end** fields

:::{figure} assets/burned_area-3.png
:align: center
:figclass: align-center
:width: 750px
:::

- Drag and Drop the selected item in the first *Input reference* field:

:::{figure} assets/burned_area-4.png
:align: center
:figclass: align-center
:width: 750px
:::

:::{NOTE}
pre-event input can be picked up directly by using the following text filter: S2A_MSIL2A_20190815T140101_N0213_R067_T21KUU_20190815T214633
:::

### Post-event product reference

- Perform the same procedure described previously ([Pre-event product reference]), using the value **2019-08-30**.

Pick one of the results having the same track, then drag and drop one of the results in the *Input reference* field:

:::{figure} assets/burned_area-5.png
:align: center
:figclass: align-center
:width: 750px
:::

:::{NOTE}
post-event input can be picked up directly by using the following text filter: S2B_MSIL2A_20190830T140059_N0213_R067_T21KUU_20190830T180923
:::

### Area Of Interest in WKT

- Click on the *Magic tool wizard* and select **AOI**. The input parameter is automatically filled with the WKT representing the area selected.

:::{figure} assets/burned_area-6.png
:align: center
:figclass: align-center
:width: 350px
:::

:::{NOTE}
you can also specify manually a different AOI in WKT format, or draw a new area on the map using the search tool and get its value from the *Magic tool wizard*.
:::

## Run the job

- Click on the button Run Job and see the Running Job

:::{figure} assets/burned_area-7.png
:align: center
:figclass: align-center
:width: 350px
:::

- After about 20 minutes, see the Successful Job

## Results: download and visualization

- Click on the button *Show results*
- See the result on map:

:::{figure} assets/burned_area-8.png
:figclass: |-
:  align-center
:  :width: 750px
:  :align: center
:::

- The following files are produced:

  > - **Burned area analysis (2019-08-15T14:01:01.0240000Z/2019-08-30T14:00:59.0240000Z)**: Burned area analysis map
  > - **NIR/SVWI RGB composite (2019-08-15T14:01:01.0240000Z/2019-08-15T14:01:01.0240000Z)**: NIR/SVWI RGB composite of the pre-event input
  > - **NIR/SVWI RGB composite (2019-08-30T14:00:59.0240000Z/2019-08-30T14:00:59.0240000Z)**: NIR/SVWI RGB composite of the post-event input
  > - **Reproducibility notebook used for generating dNBR and RBR**: notebook used for generating dNBR and RBR
  > - **Reproducibility stage-in notebook for Sentinel-2 data for generating dNBR and RBR**: notebook for Sentinel-2 data for generating dNBR and RBR

## Reference

- Parks, S. A., Dillon, G. K. & Miller, C. A New Metric for Quantifying Burn Severity: The Relativized Burn Ratio. Remote Sens. 6, 1827–1844 (2014)
- Keeley, J. E. Fire intensity, fire severity and burn severity: a brief review and suggested usage. Int. J. Wildland Fire 18, 116–126 (2009)

## Further reading

- Normalized Burn Ratio by Humbold State University - [link](http://gsp.humboldt.edu/OLM/Courses/GSP_216_Online/lesson5-1/NBR.html).
- UN-SPYDER Knowledge Portal – Normalized Burn Ratio - [link](http://un-spider.org/node/10959).
