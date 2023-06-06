# ADORE DORIS

Interferogram generation with ADORE DORIS

This service (\[ADORE DORIS GitHub\](<https://github.com/Terradue/doc-tep-geohazards/blob/develop/source/tutorials/adore.rst>)) was made available in the GEP processing services list as part of the GEP Early Adopters Programme (2016-2020).

```{image} assets/tuto_adore_icon.png
```

**ADORE DORIS interferometric processor**

ADORE DORIS is an Interferometric Synthetic Aperture Radar (InSAR) processor developed by the University of Miami Geodesy Group, to help researchers generate interferograms with ease.
ADORE stands for Automated DORIS Environment. DORIS is a standalone program that can perform most common steps of the interferometric radar processing in a modular set up.
DORIS handles SLC (Single Look Complex) data to generate interferometric products, and can be used to georeference unwrapped products.
This service supports processing of ENVISAT ASAR Image Mode Level 1 (ASA_IMS_1P) data.

**EO sources supported**:

> - Envisat ASAR Image Mode Level 1 (ASA_IMS_1P)

**Output specifications**

> - coseismic interferogram

## Select the processing

- Login to the platform (see {doc}`user <../community-guide/user>` section)
- Select the processing service “ADORE DORIS interferometric processor”:

:::{figure} assets/tuto_adore_1.png
:align: center
:figclass: align-center
:width: 750px
:::

The "ADORE DORIS Interferometric Processor" panel is displayed with parameters values to be filled-in.

:::{NOTE}
Parameters comes with default pre-filled values which are the same as the ones used in this tutorial, so you may skip the following section and directly use the pre-filled parameters.
:::

## Fill the parameters

:::{NOTE}
slave and master can be picked up by using the following data package (alternatively to the search steps described): **ADORE_LAquila**
:::

### Slave product reference

- Select **EO Data / Envisat** as data collection.
- Type **ASA_IMS_1P** in the Search Terms field (1):

:::{figure} assets/tuto_adore_2.png
:align: center
:figclass: align-center
:width: 750px
:::

- Click on Show Other Parameters:

:::{figure} assets/tuto_adore_3.png
:align: center
:figclass: align-center
:width: 750px
:::

- apply the date value **2008-03-26** in both:

* time:start field
* time:end field

then click on the button **Search**:

:::{figure} assets/tuto_adore_4.png
:align: center
:figclass: align-center
:width: 750px
:::

- Drag and Drop the first result (the one with **Track 129**) in the *Slave product reference* field:

:::{figure} assets/tuto_adore_5.png
:align: center
:figclass: align-center
:width: 750px
:::

:::{figure} assets/tuto_adore_6.png
:align: center
:figclass: align-center
:width: 750px
:::

### Master product reference

- Perform the same procedure described previously ([Slave product reference]), using as values **2009-03-11** . Apply this date value in both:

* time:start field
* time:end field :

:::{figure} assets/tuto_adore_7.png
:align: center
:figclass: align-center
:width: 750px
:::

- Drag and drop the result in the *Master product reference* field:

:::{figure} assets/tuto_adore_8.png
:align: center
:figclass: align-center
:width: 750px
:::

### Point of Interest

- Type

```adore-parameter
POINT(13.4 42.35)
```

in the *Point of Interest* field:

### Extent

- Type

```adore-parameter
2000,2000
```

in the *Extend*:

### Settings for ADORE Doris separated by comma

- Type

```adore-parameter
cc_winsize="128 128",fc_acc="8 8",int_multilook="4 4",coh_multilook="4 4",dumpbaseline="15 10"
```

in the *Settings for ADORE Doris separated by comma* field:

:::{figure} assets/tuto_adore_9.png
:align: center
:figclass: align-center
:width: 750px
:::

## Run the job

- Click on the button Run Job:

:::{figure} assets/tuto_adore_10.png
:align: center
:figclass: align-center
:width: 750px
:::

- See the Running Job:

:::{figure} assets/tuto_adore_11.png
:align: center
:figclass: align-center
:width: 750px
:::

- After about 20 minutes, see the Successful Job:

:::{figure} assets/tuto_adore_12.png
:align: center
:figclass: align-center
:width: 750px
:::

- Click on the button *Show results on map*, then on the *20090311_20080326_cint.tiff* result on the *Results Table* in the bottom left side
- See the result on map:

:::{figure} assets/tuto_adore_13.png
:align: center
:figclass: align-center
:width: 750px
:::
