FASTVEL for displacement velocity map generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FASTVEL is a PSI based processing software developed by TRE-Altamira.

This tutorial will describe the processing of a set of ASAR or Sentinel-1 IW images to generate a set of differential interferograms 
or a mean displacement velocity map on the GEP.

Processor configuration
=======================

The user shall login on the GEP to the EO services provided by TRE ALTAMIRA and in the Processing Services section, select the FASTVEL service from 
the services tab.


* Select an area on the map. In the "Search Form" temporal selection can be done and specification about other search parameters can be done. 
The images must have the same "Orbit Direction" and the same track.

* Choose the set of images to be processed. A minimum number of 25 images are required.

.. figure:: assets/tuto_fastvel_1.png
	:figclass: align-center
        :width: 750px
        :align: center

Complete the following list of processing parameters:

** SAR data set **: set of SLC images to be processed. A minimum number of 25 images are required. ** Drag 
and drop the selected images on the search result to this field **. Note that depending on: the Maximum Temporal Baseline [days], the 
Maximum Perpendicular Baseline [m], the Maximum Doppler Difference [Hz] and the Maximum Doppler Centroid [Hz], this number could be reduced 
causing the stop of the processing. To that matter it is recommended to put a larger number than 25.

.. figure:: assets/tuto_fastvel_2.png
	:figclass: align-center
        :width: 750px
        :align: center

.. figure:: assets/tuto_fastvel_3.png
	:figclass: align-center
        :width: 750px
        :align: center

** Processing Mode **:

* ** IFG **: generation of a set of differential interferograms. If this mode is selected, the parameters to be considered are: Area Of Interest, 
Maximum Temporal Baseline [days] , Maximum Perpendicular Baseline [m], Maximum Doppler Difference [Hz],   
Maximum Doppler Centroid [Hz], Goldstein phase filter exponential 
factor, Phase Unwrapping

* ** MTA **: generation of the displacement velocity and DEM error maps. If this mode is selected, the parameters to be considered are: 
Area Of Interest, Reference Point Lattitude [deg], Reference Point   Longitude [deg], Maximum Temporal Baseline [days] , Maximum Perpendicular 
Baseline [m], Maximum Doppler Difference [Hz], Maximum Doppler Centroid [Hz], Coherence Threshold, APS  Correlation Distance [m]

* ** Area Of Interest **: restrict process to the selected area. The polygon on the map can be imported as the bounding box in the map. 
It can be also specified by [minlon, minlat, maxlon, maxlat]. Example: 1.717,41.778,1.916,41.878

.. figure:: assets/tuto_fastvel_4.png
	:figclass: align-center
        :width: 750px
        :align: center

* ** Reference Point Latitude [deg] **: Latitude of the point (zero motion) to whom reference the velocity map points values. 
It has to be inside the AOI. An automatic check is done. Example: 

* ** Reference Point Longitude [deg] **: Longitude of the point (zero motion) to whom reference the velocity map points values. 
It has to be inside the AOI. An automatic check is done. Example: 

* ** Maximum Temporal Baseline [days] **: Maximum Temporal Baseline in days between images to allow the corresponding interferogram generation. Default value: 365.

* ** Maximum Perpendicular Baseline [m] **: Maximum Spatial Baseline in meters between images to allow the corresponding interferogram generation. Default value: 400.

* ** Maximum Doppler Difference [Hz] **: Maximum Doppler Centroid differences in Herzts between images to allow the corresponding interferogram generation. 
Default value: 1000.

* ** Maximum Doppler Centroid [Hz] **: Maximum Image Doppler Centroid in Herzts for considering that image to be part of the dataset to process. Default value: 2000.

* ** Goldstein phase filter exponential factor **: (on the IFG mode) filter power factor [0,1]. Default value: 0.5

* ** Phase Unwrapping **: selection (on the IFG mode) of the phase unwrapping of the differential interferograms. Default mode: false.

* ** Coherence Threshold **: (on the MTA mode) mean interferometric coherence threshold for considering a pixel to be processed in the 
generation of the velocity and DEM error maps. Default value: 0.5.

* ** APS Correlation Distance [m] **: (on the MTA mode) Atmospheric Phase Screen Correlation distance, i.e., 
maximum distance in meters allowed for connecting neighboring pixels in the process to generate the velocity and DEM error maps. Default value: 3000.


Running the job
===============

Click on "Run Job" button from the processor configuration panel and wait for the job to complete.

.. figure:: assets/tuto_fastvel_5.png
	:figclass: align-center
        :width: 750px
        :align: center

.. figure:: assets/tuto_fastvel_6.png
	:figclass: align-center
        :width: 750px
        :align: center


View results on the map
=======================

Click on the Show results on map button after the job is completed.

After successful completion of the job, the following elements shall appear on the * Results Table *:

** On IFG mode **:

* The interferometric amplitude in geotiff format. This is the modulus of the complex product of the master SLC image and the coregistered slave SLC image.
* The interferometric coherence in geotiff format. This is a floating point geotiff image with values within [0.0 255.0]. 
Pixel values of 255.0 are equivalent to a coherence value of 1.
* The interferometric phase in geotiff format. This is an integer geotiff image with phase values within [0 255].
* The interferometric phase in in geotiff format RGBA format.
* The unwrapped interferometric phase (if unwrapping selected) in geotiff format. This is the raw unwrapped phase in radians.
* The unwrapped interferometric phase (if unwrapping selected) in geotiff format RGBA format.
* A zip file products.zip containing all geocoded results in geotiff format.

.. figure:: assets/tuto_fastvel_7.png
	:figclass: align-center
        :width: 750px
        :align: center

It is possible to download the result files, first by selecting them on the Results Table, a descriptive window about the file shall appear on the map. 
Clicking on the "download" button retrieves the file.

.. figure:: assets/tuto_fastvel_8.png
	:figclass: align-center
        :width: 750px
        :align: center

** On MTA mode **:

* Mean displacement velocity (cm/y) map in geotiff format. 
* RGB Mean displacement velocity map.
* Corrected topography (DEM error + reference DEM (meters)) map in geotiff format.
* RGB Corrected topography map.
* CSV files with the main information of PSI products, in the LOS (Line Of Sight), in which each line of the database will represent one measurement point. 
  The list of fields in the csv (corresponding to the columns of the database) is the following:

- ID: Unique identifier label for each measurement point.
- Lon: Geographical Longitude position [decimal degrees over WGS84].
- Lat: Geographical Latitude position [decimal degrees over WGS84].
- Topo: Corrected Height error (reference DEM + error height) [meters].
- Coer: Mean Interferometric  Coherence [0,1]
- cosN, cosE, cosU: North, East and Up LOS unitary vector components.
- Vel: LOS ground displacement mean velocity value measured for the observation period [cm/year].
- Erh: Height error [meters].

.. figure:: assets/tuto_fastvel_9.png
	:figclass: align-center
        :width: 750px
        :align: center

It is possible to download the result files, first by selecting them on the Results Table, a descriptive window about the file shall appear on the map. 
Clicking on the "download" button retrieves the file.

.. figure:: assets/tuto_fastvel_10.png
	:figclass: align-center
        :width: 750px
        :align: center


