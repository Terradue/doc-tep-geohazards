# Sentinel-3 SLSTR composites \[[adb-i](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1/Using_satellite_information_to_help_rebuild_after_a_disaster), wb, [idct](https://disasterscharter.org/web/guest/disaster-types/-/asset_publisher/TC3LharmzylW/content/trial-of-the-charter-platform-prototypes;jsessionid=8F4DB8226069BBED7716EE4ED4CA2879.jvm1?redirect=https%3A%2F%2Fdisasterscharter.org%2Fweb%2Fguest%2Fdisaster-types%3Bjsessionid%3D8F4DB8226069BBED7716EE4ED4CA2879.jvm1%3Fp_p_id%3D101_INSTANCE_TC3LharmzylW%26p_p_lifecycle%3D0%26p_p_state%3Dnormal%26p_p_mode%3Dview%26p_p_col_id%3Dcolumn-1%26p_p_col_count%3D1)\]

```{image} assets/s3-slstr-composite-icon.png
:width: 200px
```

**Sentinel-3 SLSTR composites**

This service takes as input a Sentinel-3 SLSTR Level 1 (SL_1_RBT\_\_\_) product on DESCENDING orbit and uses the bands S3, S2, S1 to do a False Colour Infrared RGB composite.
The output of the service is a EO data product in GeoTIFF format. The product is a RGBA GeoTiff file obtained through the composition of S3, S2, S1 bands [^id3]. The output GeoTiff is displayed in geobrowser with the possibility to access product metadata.

**EO sources supported**

> - Sentinel-3 SLSTR Level 1 (SL_1_RBT\_\_\_) product until 15-Jan-2020 with DESCENDING orbit only [^id4]

```{eval-rst}
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| OUTPUT PRODUCT SPECIFICATION                                                                                                                  |
+===============================+===============================================================================================================+
| **Information type**          | False Colour Infrared RGBA composite for Sentinel-3 SLSTR Level 1 (SL_1_RBT___)                               |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Raster format**             | GeoTIFF                                                                                                       |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Resolution**                | Native (500 metres)                                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **RED**                       | S3 band (VNIR band)                                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **GREEN**                     | S2 band (Red band)                                                                                            |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **BLUE**                      | S1 band (Green band)                                                                                          |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **ALPHA**                     | set transparency for nodata pixels                                                                            |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Browse product available**  | YES (GeoTIFF)                                                                                                 |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Output Filename example**   | S3 SLSTR False color Infrared - Quicklook (2020-01-11T23:01:47/2020-01-11T23:01:47)                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
```

______________________________________________________________________

This tutorial will describe the processing of Sentinel-3 SLSTR Level 1 (SL_1_RBT\_\_\_) product on DESCENDING orbit and uses the bands S3, S2, S1 to generate a False Colour Infrared RGB composite for the one input Sentinel-3 acquisitions on the GEP.

## Select the processing

- Login to the platform (see {doc}`user <../community-guide/user>` section)
- Go to the Geobrowser, expand the panel “Processing services” on the right hand side and select the processing service “Sentinel-3 SLSTR composites”:

:::{figure} assets/s3-slstr-composite-1.png
:align: center
:figclass: align-center
:width: 750px
:::

This will display the "Sentinel-3 SLSTR composites" service panel including several pre-defined parameters values to be filled-in.

:::{figure} assets/s3-slstr-composite-2.png
:align: center
:figclass: align-center
:width: 750px
:::

## Fill the parameters

### Reference input

- Select the Sentinel-3 data collection in the EO Data button.

:::{figure} assets/s3-slstr-composite-3.png
:align: center
:figclass: align-center
:width: 750px
:::

- Select the area for which you want to do an anlysis, e.g over Australia.

:::{figure} assets/s3-slstr-composite-4.png
:align: center
:figclass: align-center
:width: 750px
:::

- Click on the lens icon to open the Search Panel
- Select **SL_1_RBT\_\_\_** as Product Type
- Apply the date value, for example **2020-01-02**, in both **time:start** and **time:end** fields

:::{figure} assets/s3-slstr-composite-5.png
:align: center
:figclass: align-center
:width: 250px
:::

- Verify that the product has DESCENDING Orbit
- Drag and Drop the selected item in the *Sentinel-3 SLSTR Level 1 (SL_1_RBT\_\_\_) input reference* field:

:::{figure} assets/s3-slstr-composite-6.png
:align: center
:figclass: align-center
:width: 750px
:::

:::{NOTE}
input can be picked up directly by using the following text filter: S3A_SL_1_RBT\_\_\_\_20200102T233200_20200102T233500_20200104T044209_0179_053_201_3420_LN2_O_NT_003
:::

## Run the job

- Click on the button Run Job and see the Running Job

:::{figure} assets/s3-slstr-composite-7.png
:align: center
:figclass: align-center
:width: 350px
:::

:::{figure} assets/s3-slstr-composite-8.png
:align: center
:figclass: align-center
:width: 350px
:::

- After about 20 minutes, see the Successful Job:

:::{figure} assets/s3-slstr-composite-9.png
:align: center
:figclass: align-center
:width: 350px
:::

## Results: download and visualization

- Click on the button *Show results*
- See the result on map:

:::{figure} assets/s3-slstr-composite-10.png
:align: center
:figclass: align-center
:width: 750px
:::

- The following files are produced:

  > - **S3 SLSTR False color Infrared - Quicklook (2020-01-11T23:01:47/2020-01-11T23:01:47) - product GeoTIFF RGBA**

## Reference

[^id3]: <https://crisp.nus.edu.sg/~research/tutorial/opt_int.htm>

## Note

[^id4]: SNAP6 is used in this service and supports only products with Baseline collection equal to 003 or less
