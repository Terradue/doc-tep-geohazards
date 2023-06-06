# STEMP - Surface Temperature Map

```{image} assets/tuto_stemp-s2_icon.png
```

**STEMP**

In the context of the VOLcanoes Thermal Application for GEP (VOLTAGE) pilot INGV has setup an end-to-end processing chain (named STEMP) for the generation of surface temperature maps over volcanic areas. It generates surface temperature map in file format fitting the Researcher and Users needs from new EO missions (currently: Sentinel-2).

**EO sources supported**:
: - Sentinel-2 MSI L1C

**Output specifications**
: - hot spot map (STEMP-S2)

______________________________________________________________________

The Surface Temperature Map Process (STEMP) tool aims to produce an hot spot detection map during eruption using Sentinel 2 data.

STEMP produces a GeoTIFF file as output. It contains the hot spot pixel map. The output name of this product is the same of the input file with the "\_TEMP.tif" final code. The processing, running in automatic, can be executed also in manual mode.

One tool is installed on Geohazards TEP platform:

> - STEMP-S2 for Sentinel 2

## Select the processing

1. Login to the platform
2. Select the processing service (STEMP-S2)

:::{figure} assets/tuto_stemp_1_s2-min.png
:align: center
:figclass: align-center
:width: 750px
:::

## Fill the parameters

1. Select from "EO data" the file to process:

   > - Sentinel-2 for STEMP-S2

:::{figure} assets/tuto_stemp_2_s2-min.png
:align: center
:figclass: align-center
:width: 300px
:::

2. Select volcano area to verify if EO input data are available by using the draw a rectangle, polygon or custom WKT filter.

:::{figure} assets/tuto_stemp_3_s2-min.png
:align: center
:figclass: align-center
:width: 750px
:::

All EO input data are visualized, select “hide all” to hide all the data

:::{figure} assets/tuto_stemp_4_s2-min.png
:align: center
:figclass: align-center
:width: 750px
:::

3. Visualize single EO data by clicking on “show/hide layer”. The selected input data is displayed. An example is the S-2 data of 11th February 2022. Remind: search data with low/no clouds in the "Advanced search form" on the left panel.

:::{figure} assets/tuto_stemp_5_s2-min.png
:align: center
:figclass: align-center
:width: 750px
:::

4. Define the "Job title"
5. Drag and drop the selected S-2 data input into the "Sentinel-2 Input" field. The link to the catalog (e.g. <https://catalog.terradue.com/sentinel2/search?format=json&uid=S2A_MSIL1C_20220211T095131_N0400_R079_T33SVB_20220211T120935>) will appear.
6. Note: the "Job title" and "Sentinel-2 input" can also be imported from a json file ("Import params"), and exported to a json file ("Export params")

:::{figure} assets/tuto_stemp_6_s2-min.png
:align: center
:figclass: align-center
:width: 750px
:::

## Run the job

1. Click on the button "Run job" and see the running job

:::{figure} assets/tuto_stemp_7_s2-min.png
:align: center
:figclass: align-center
:width: 750px
:::

2. See the Running job:

:::{figure} assets/tuto_stemp_8_s2-min.png
:align: center
:figclass: align-center
:width: 750px
:::

3. At the end of the process click on the button "Show results" in the bottom-right corner to see the result on map:

:::{figure} assets/tuto_stemp_9_s2-min.png
:align: center
:figclass: align-center
:width: 750px
:::

4. Result for STEMP-S2 is showed

:::{figure} assets/tuto_stemp_10_s2-min.png
:align: center
:figclass: align-center
:width: 750px
:::

5. Metadata are showed when click on the result map, and results can be downloaded with the "Download" button on the lower-right corner.

:::{figure} assets/tuto_stemp_11_s2-min.png
:align: center
:figclass: align-center
:width: 750px
:::

## Example to test

Use  the following input for testing service and verify results with the output :

- Select the STEMP-S2 service and use the following information:

  > - Job title: *your_job_title*
  > - Sentinel-2 input: *"https://catalog.terradue.com/sentinel2/search?format=json&uid=S2A_MSIL1C_20220211T095131_N0400_R079_T33SVB_20220211T120935"*

Expected result: `T33SVB_20220211T095131_HOT_SPOT.tif
<https://geohazards-tep.eu/t2api/share?url=https%3A%2F%2Fgeohazards-tep.eu%2Ft2api%2Fjob%2Fwps%2Fsearch%3Fid%3D703c1c0f-26c5-4816-9b86-f582769881a2%26key%3D23628ee2-b50c-4f64-a17f-df6d973fc766>`.
