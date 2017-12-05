Surface Temperature Map (STEMP)
===============================

The Surface Temperature Map Process (STEMP) tool aims to produce surface temperature maps using  optical satellite data having thermal bands (Landsat 8, Sentinel 3). STEMP is also able to produce an hot spot detection map only during eruption using Sentinel 2 data.

STEMP produces a GeoTIFF file as output. It contains the surface temperature maps (or the hot spot pixel  for Sentinel 2). The output name of this product is the same of the input file with the "_TEMP.tif" final code. The processing, running in automatic,  can be executed also in manual mode.

Three different tools are installed on Geohazards TEP platform: 

	- STEMP-L8 for Landsat 8
	- STEMP-S2 for Sentinel 2
	- STEMP-S3 for Sentinel 3

Select the processing
---------------------

1. Login to the platform
2. Select the processing service (STEMP-L8 or STEMP-S2 or STEMP-S3)

.. figure:: assets/tuto_stemp_1.png
	:figclass: align-center
        :width: 750px
        :align: center
 
Fill the parameters 
-------------------

1. Select from "EO data" the file to process: 

	- Landsat 8 for STEMP-L8 
	- Sentinel-2 for STEMP-S2
	- Sentinel-3 for STEMP-S3

.. figure:: assets/tuto_stemp_2.png
	:figclass: align-center
        :width: 750px
        :align: center 
 
2. Select volcano area to verify if EO input data are available by using the draw a rectangle , polygon or custom WKT filter.

.. figure:: assets/tuto_stemp_3.png
	:figclass: align-center
        :width: 750px
        :align: center 

All EO input data are visualized, select “hide all” to hide all the data 

.. figure:: assets/tuto_stemp_4.png
	:figclass: align-center
        :width: 750px
        :align: center  

3. Visualize single EO data by clicking on “show/hide layer”. The selected input data is displayed. An example is the L8 data of 22th Novembere 2017. Remind: search data without clouds. 

.. figure:: assets/tuto_stemp_5.png
	:figclass: align-center
        :width: 750px
        :align: center 

4. Fill the start date of the file
5. Fill the end date of the file (start and end date must be the same)
6. Select the volcano name

.. figure:: assets/tuto_stemp_6.png
	:figclass: align-center
        :width: 750px
        :align: center 

7. Follow the same procedure above mentioned for STEMP-S2 or STEMP-S3

Run the job
-----------

1. Click on the button "Run job" and see the running job

.. figure:: assets/tuto_stemp_7.png
	:figclass: align-center
        :width: 750px
        :align: center 

2. See the Running job:

.. figure:: assets/tuto_stemp_8.png
	:figclass: align-center
        :width: 750px
        :align: center 

3. At the end of the process click on the button "Show results" and the see the result on map: 

.. figure:: assets/tuto_stemp_9.png
	:figclass: align-center
        :width: 750px
        :align: center 
 
4. Result for STEMP-S2 is showed

.. figure:: assets/tuto_stemp_10.png
	:figclass: align-center
        :width: 750px
        :align: center 

5. Result for STEMP-S3 is showed

.. figure:: assets/tuto_stemp_11.png
	:figclass: align-center
        :width: 750px
        :align: center 

6. Metadata are showed when click on the result map.
 
.. figure:: assets/tuto_stemp_12.png
	:figclass: align-center
        :width: 750px
        :align: center 

