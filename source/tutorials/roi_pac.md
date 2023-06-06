# Interferogram generation with ROI_PAC

```{image} assets/tuto_roi_pac_icon.png
```

**Repeat Orbit Interferometry Package (ROI_PAC)**

Data processing software allowing researchers in the area of topography and surface displacements studies to apply Interferometric Synthetic Aperture Radar (InSAR) methods.

**EO sources supported**:

> - Envisat ASAR Image Mode Level 0 (ASA_IM\_\_0P)

**Output specifications**

To be defined

______________________________________________________________________

This tutorial processes a pair of Envisat ASAR data with ROI_PAC (Repeat Orbit Interferometry PACkage) [^f1], a software package jointly created by the Jet Propulsion Laboratory division of NASA and CalTech for processing SAR data to create InSAR (Interferometric synthetic aperture radar) images, or 'interferograms'. This geodetic method uses two or more synthetic aperture radar (SAR) scenes to generate maps of surface deformation or digital elevation models, using differences in the phase of the waves returning to the radar sensor. The technique can potentially measure centimetre-scale changes in deformation over spans of days to years. It has applications for geophysical monitoring of natural hazards, for example earthquakes, volcanoes and landslides, and in structural engineering, in particular monitoring of subsidence and structural stability.

The tutorial uses a coseismic pair of Envisat ASAR Image Mode Level 0 for the 2010 Baja California earthquake.

The 2010 Baja California earthquake (also known as 2010 Easter earthquake, 2010 Sierra El Mayor earthquake, or 2010 El Mayor – Cucapah earthquake) was an earthquake of 7.2 magnitude on the moment magnitude scale. It started 26 kilometers (16 mi) south of Guadalupe Victoria, Baja California, Mexico, at a depth of 10 km (6.2 mi).
Learn more about the event in the [2010 Baja California earthquake Wikipedia](http://en.wikipedia.org/wiki/2010_Baja_California_earthquake) entry.

The processing service code is available in the GitHub repository [geohazards-tep/InSAR-ROI_PAC](https://github.com/geohazards-tep/InSAR-ROI_PAC).

## Select the processing

- Login to the platform (see {doc}`user <../community-guide/user>` section)
- Select the processing service “Repeat Orbit Interferometry Package (ROI_PAC)”:

:::{figure} assets/tuto_roi_pac_1.png
:align: center
:figclass: align-center
:width: 750px
:::

The "Repeat Orbit Interferometry Package (ROI_PAC)" panel is displayed with parameters values to be filled-in.

## Fill the parameters

:::{NOTE}
slave and master can be picked up by using the following data package (alternatively to the search steps described): **BajaCaliforniaEQ**
:::

### Master product reference

- Type **ASA_IM\_\_0P** in the Search Terms field (1) and then click on the lens icon (2):

:::{figure} assets/tuto_roi_pac_2.png
:align: center
:figclass: align-center
:width: 750px
:::

- Click on Show Other Parameters apply the date value **2010-05-02** in both:

* time:start field
* time:end field

then click on the button **Search**:

:::{figure} assets/tuto_roi_pac_3.png
:align: center
:figclass: align-center
:width: 750px
:::

- Drag and Drop the first result in the *ASAR Master product catalogue entry* field:

:::{figure} assets/tuto_roi_pac_4.png
:align: center
:figclass: align-center
:width: 750px
:::

### Slave product reference

- Perform the same procedure described previously ([Master product reference]), using the value **2010-03-28**. Apply this date value in both:

* time:start field
* time:end field

Pick one of the results having the same track, then drag and drop one of the results in the *ASAR Slave product catalogue entry* field:

:::{figure} assets/tuto_roi_pac_5.png
:align: center
:figclass: align-center
:width: 750px
:::

## Run the job

- Click on the button Run Job and see the Running Job

:::{figure} assets/tuto_roi_pac_6.png
:align: center
:figclass: align-center
:width: 750px
:::

- After about 20 minutes, see the Successful Job:

:::{figure} assets/tuto_roi_pac_7.png
:align: center
:figclass: align-center
:width: 750px
:::

- Click on the button *Show results on map*, then on the *geo_100328-100502.unw.phase.tif* result on the *Results Table* in the bottom left side
- See the result on map:

:::{figure} assets/tuto_roi_pac_8.png
:align: center
:figclass: align-center
:width: 750px
:::

```{rubric} References
```

[^f1]: [ROI_PAC Website](http://aws.roipac.org/cgi-bin/moin.cgi)
