# SRTM Digital Elevation Model on Hadoop Cloud Sandbox \[GEN\]

```{image} assets/tuto_srtm_icon.png
```

**SRTM Digital Elevation Model**

This application generates the STRM DEM in ROI_PAC or GAMMA ready format

**EO sources supported**:

> - SRTM

**Output specifications**

> - DEM in ROI_PAC or GAMMA ready format

## Select the processing

- Login to the platform (see {doc}`User Profile <../community-guide/user>` section).
- Select the processing service “SRTM Digital Elevation Model”:

:::{figure} assets/tuto_srtm_1.png
:align: center
:figclass: align-center
:width: 750px
:::

The "SRTM Digital Elevation Model" panel is displayed with parameters values to be filled-in.

:::{NOTE}
SRTM valid in the \[-56 deg,+60 deg\] range of latitudes.
:::

:::{NOTE}
Parameters comes with default pre-filled values which are the same as the ones used in this tutorial, so you may skip the following section and directly use the pre-filled parameters.
:::

## Fill the parameters

### SAR product catalogue entry

- Select **EO Data / Envisat** as data collection.
- Type **ASA_IM\_\_0P** in the Search Terms field (1):

:::{figure} assets/tuto_srtm_2.png
:align: center
:figclass: align-center
:width: 750px
:::

- Click on Show Other Parameters and apply the date value **2010-05-02** in both:

* time:start field
* time:end field

then click on the button **Search**:

:::{figure} assets/tuto_srtm_3.png
:align: center
:figclass: align-center
:width: 750px
:::

- Drag and Drop the first result in the *SAR product catalogue entry(ies) in RDF format* field:

:::{figure} assets/tuto_srtm_4.png
:align: center
:figclass: align-center
:width: 750px
:::

### Format of the generated DEM

- Fill the *Format of the generated DEM (roi_pac or gamma)* filed with **gamma** or **roi_pac**

:::{figure} assets/tuto_srtm_5.png
:align: center
:figclass: align-center
:width: 750px
:::

## Run the job

- Click on the button Run Job and see the Running Job

:::{figure} assets/tuto_srtm_6.png
:align: center
:figclass: align-center
:width: 750px
:::

- After few minutes, see the Successful Job:

:::{figure} assets/tuto_srtm_7.png
:align: center
:figclass: align-center
:width: 750px
:::

- Click on the button *Show results on map*, then on the tgz result on the *Results Table* in the bottom left side
- You can also download the .tgz file:

:::{figure} assets/tuto_srtm_8.png
:align: center
:figclass: align-center
:width: 750px
:::
