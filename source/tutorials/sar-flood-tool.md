# SAR Flood Tool Service

```{image} assets/SAR_flood_icon.png
```

**SAR based Flood processing chain**

Service using the SNAP Sentinel-1 IW SLC Amplitude Coherence Composites and a Flood Classifier developed and integrated in GEP by eGEOS to extract flooded areas from Sentinel-1 interferometric multi-temporal stack to support flood mapping.

**EO sources supported**:

> - Sentinel-1 TOPSAR IW SLC

**Output specifications**

> - water mask GeoTiff file

## Select the processing

- Sign-in on the Portal <https://geohazards-tep.eu/> (see guidance {doc}`user <../community-guide/user>` section)
- Access the Geobrowser: <https://geohazards-tep.eu/geobrowser/>
- Open the tab "Processing services" from the right of the map, then select the processing service “SAR flood extraction”.

## Select the files to process

- Click on the *Data Packages* button in the bottom right of the screen, within the Features Basket panel.

Then select from the list the "SAR-flood-trial-case" data package and click on *load*.
The input data are standard interferometric Sentinel-1 SLC images, e.g. the images have the same relative orbit number. In order to select suitable images for the service you can use the following string in the search box (top left of the web page):

```parameter
track:81 && pt:slc
```

The selected data package contains the reference to the following input file:

```parameter
S1A_IW_SLC__1SDV_20150328T061348_20150328T061415_005228_0069A4_2B88
S1A_IW_SLC__1SDV_20151205T061403_20151205T061430_008903_00CBC9_FD2D
S1A_IW_SLC__1SDV_20151217T061404_20151217T061434_009078_00D09B_065C
```

:::{figure} assets/SAR_flood_2.png
:align: center
:figclass: align-center
:width: 750px
:::

## Fill the parameter values

Define values for the "Job title", the "SAR images" and the "Sub-swath" fields.

- As *Job title*, type:

```parameter
SAR flood extraction
```

- As input *SAR images*, drag and drop the selected input file:

:::{figure} assets/SAR_flood_3.png
:align: center
:figclass: align-center
:width: 750px
:::

- As *Sub-swath*, select:

```parameter
IW-3
```

## Run the job

- Click on the button "Run Job" at the bottom of the sar flood extraction processor tab, and monitor the progress of the running Job:

:::{figure} assets/SAR_flood_4.png
:align: center
:figclass: align-center
:width: 750px
:::

- Wait for the Job completion, then check the status is set as "Successful Job”.

:::{figure} assets/SAR_flood_5.png
:align: center
:figclass: align-center
:width: 750px
:::

- Download the sar flood extraction processing results once the Job is completed:

:::{figure} assets/SAR_flood_6.png
:align: center
:figclass: align-center
:width: 750px
:::

The output of the service (flood mask) is a GeoTiff file, represented in byte format, with "1" value where the flood is present, "0" otherwise.
