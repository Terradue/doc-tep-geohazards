# GMT5SAR InSAR - Sentinel-1 TOPSAR

```{image} assets/tuto_gmtsar_icon_S1.png
:width: 120px
```

**GMT5SAR InSAR - Sentinel-1 TOPSAR**

GMT5SAR is an open source (GNU General Public License) InSAR processing system. This service provides standard 2-pass processing of a master product against one or more slave products.

**EO sources supported**:

> - Sentinel-1 SLC

**Output specifications**

For each generated interferogram (one per sub-swath) the following output files are provided:

> - Amplitude, phase, correlation, unwrapped phase, filtered phase, LOS displacement — image files in NetCDF format “.grd”
> - Corresponding files after geocoding with suffix “\_ll.grd”
> - Postscript plots: “.ps”
> - Preview images “.tiff” and “.png”

______________________________________________________________________

This tutorial covers the typical InSAR processing to form an interferogram using two SAR images and a digital elevation model.

The GMT5SAR processing service can also process several pairs master/slave (same master).

## Select the processing

- Login to the platform (see {doc}`user <../community-guide/user>` section)
- Select the processing service "GMT5SAR InSAR - Sentinel-1 TOPSAR":

:::{figure} assets/s1_0.png
:align: center
:figclass: align-center
:width: 750px
:::

The "GMT5SAR InSAR - Sentinel-1 TOPSAR" panel is displayed with parameters values to be filled-in.

:::{NOTE}
Parameters comes with default pre-filled values which are the same as the ones used in this tutorial, so you may skip the following section and directly use the pre-filled parameters.
:::

## Fill the parameters

### Slave product reference

- Select **EO Data / Sentinel-1 / SLC** as data collection.
- Type **S1B_IW_SLC\_\_1SDV_20170718T041442_20170718T041509_006537_00B7E8_BD0D** in the Search Terms field:

:::{figure} assets/s1_1_1.png
:align: center
:figclass: align-center
:width: 750px
:::

- To access advanced filter functionalities, you can open the **Search form** on the top left of the map and use filters such as start/end time or specficis ones (associated to the current selected data collection)
- Drag and Drop the first result in the *Slave product reference* field:

:::{figure} assets/s1_1_1.png
:align: center
:figclass: align-center
:width: 750px
:::

### Master product reference

- Type **S1A_IW_SLC\_\_1SDV_20170724T041510_20170724T041538_017608_01D766_AB23** in the Search Terms field (1):
- Drag and drop the first result in the *Master product reference* field:

:::{figure} assets/s1_1_2.png
:align: center
:figclass: align-center
:width: 750px
:::

### Polarization

- Select the Polarization

:::{figure} assets/s1_1_2.png
:align: center
:figclass: align-center
:width: 750px
:::

### Snaphu threshold

- Select the Snaphu threshold

:::{figure} assets/s1_1_2.png
:align: center
:figclass: align-center
:width: 750px
:::

## Run the job

- Click on the button Run Job and see the Running Job

:::{figure} assets/s1_2.png
:align: center
:figclass: align-center
:width: 750px
:::

- After about 25 minutes, see the Successful Job:

:::{figure} assets/s1_3.png
:align: center
:figclass: align-center
:width: 750px
:::

- Click on the button *Show results on map*
- See the result on map:

:::{figure} assets/s1_3.png
:align: center
:figclass: align-center
:width: 750px
:::

## More info

<http://topex.ucsd.edu/gmtsar/>
