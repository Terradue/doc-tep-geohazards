Sentinel-1 IW mode Interferogram generation with DIAPASON
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DIAPASON is an InSAR processing software developed by the French space agency (CNES) and 
maintained by ALTAMIRA INFORMATION.

This tutorial will describe the processing of interferograms from pairs of Sentinel-1 IW images on the GEP.

Processor configuration
=======================
* The user shall login on the GEP and in the "Processing Services" section , select the "DIAPASON InSAR Sentinel-1 TOPSAR" service from the "services" tab.

.. figure:: assets/tuto_diapiw_1.png
	:figclass: align-center
        :width: 750px
        :align: center

* Select an area on the map . In the "Search Terms" field , you may type "IW AND SLC" to search for
the correct product type covering the area 

.. figure:: assets/tuto_diapiw_2.png
	:figclass: align-center
        :width: 750px
        :align: center

* Choose the image pair to be processed from the "Current search result" pane. 
Drag and Drop the image to be used as master  into the "Sentinel-1 IW master" field, then select the slave image into the "Sentinel-1 IW slave" field.

The images shall be from the same track.

* Set the polarization to process from the "polarization" drow-down list

The available polarizations for the images appear on the list from the "Current search result" pane.
The selected polarization should be available on each of the two images. 

* Optionally you may choose to process an area of interest.

You may set this option in order to process an area  smaller than the coverage of the two images by clicking on the button on the right of the "Area of interest" field. This will set the current area selected on the map as area of interest for the processing. 
When left blank , the area processed is the intersection between the two input images.


* Set the Goldstein filter factor

The value for the Goldstein filter exponential factor shall be a floating point value between 0 and 1.
Higher values will result in more filtering of the output interferogram  phase.

 
.. figure:: assets/tuto_diapiw_3.png
	:figclass: align-center
        :width: 750px
        :align: center

 

Running the job
===============

* Click on "Run Job" button from the processor configuration panel and wait for the job to complete.


.. figure:: assets/tuto_diapiw_4.png
	:figclass: align-center
        :width: 750px
        :align: center


View results on the map
=======================

* Click on the *Show results on map* button after the job is completed.

After successful completion of the job , the interferometric phase ,amplitude and coherence files should appear on the *Results Table*.
The files that can be displayed on the map are the files with the .png extension.


.. figure:: assets/tuto_diapiw_5.png
	:figclass: align-center
        :width: 750px
        :align: center

It is possible to download the result files , first by selecting them on the *Results Table*  , a descriptive window about the file shall appear on the map . Clicking on the "download" button retrieves the file.



.. figure:: assets/tuto_diapiw_6.png
	:figclass: align-center
        :width: 750px
        :align: center



