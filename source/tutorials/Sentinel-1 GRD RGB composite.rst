Sentinel-1 GRD RGB composite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: assets/Sentinel-1-GRD-RGB-composite-icon.png
        :width: 200px

**Sentinel-1 GRD RGB composite**

This service takes as input one or up to two consecutive Sentinel-1 GRD acquisitions (in the same day) to create an RGB composite. It provides a single date polarization RGB composite taking as input one or up to two consecutive Sentinel-1 GRD data products along an acquisition segment (same track).

-----


Select the processing
=====================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Go to the Geobrowser, expand the panel “Processing services” on the right hand side and select the processing service “Sentinel-1 GRD RGB composite”:

.. figure:: assets/Sentinel-1-GRD-RGB-composite.png
	:figclass: align-center
        :width: 750px
        :align: center

This will display the "Sentinel-1 GRD RGB composite" service panel including several pre-defined parameters values to be filled-in.

.. figure:: assets/Sentinel-1-GRD-RGB-composite-1.png
	:figclass: align-center
        :width: 750px
        :align: center
        
Fill the parameters
===================

Reference input
---------------

* Select the Sentinel-1 data collection in the EO Data button.

.. figure:: assets/Sentinel-1-GRD-RGB-composite-2.png
	:figclass: align-center
        :width: 750px
        :align: center
        
* Select the area for which you want to do an analysis, e.g over Madrid (Spain).

.. figure:: assets/Sentinel-1-GRD-RGB-composite-3.png
	:figclass: align-center
        :width: 1000px
        :align: center

* Click on the lens icon to open the Search Panel
* Select **GRD** as Product Type
* Apply the date value, for example **2020-09-01** in **time:start** field and **2020-09-08** in **time:end** field.

.. figure:: assets/Sentinel-1-GRD-RGB-composite-4.png
	:figclass: align-center
        :width: 250px
        :align: center
        
* Drag and Drop the selected item in the *Input references* field:

.. figure:: assets/Sentinel-1-GRD-RGB-composite-5.png
	:figclass: align-center
        :width: 750px
        :align: center

Area Of Interest in WKT
-----------------------

* Click on the *Magic tool wizard* and select **AOI**. The input parameter is automatically filled with the WKT representing the area selected.

.. figure:: assets/Sentinel-1-GRD-RGB-composite-6.png
	:figclass: align-center
        :width: 350px
        :align: center

.. NOTE:: you can also specify manually a different AOI in WKT format, or draw a new area on the map using the search tool and get its value from the *Magic tool wizard*.

Run the job
===========

* Click on the button Run Job and see the Running Job

.. figure:: assets/Sentinel-1-GRD-RGB-composite-7.png
	:figclass: align-center
        :width: 350px
        :align: center

.. figure:: assets/Sentinel-1-GRD-RGB-composite-8.png
	:figclass: align-center
        :width: 350px
        :align: center

* After about 20 minutes, see the Successful Job:

.. figure:: assets/Sentinel-1-GRD-RGB-composite-9.png
	:figclass: align-center
        :width: 350px
        :align: center

Results: download and visualization
===================================

* Click on the button *Show results*

* See the result on map:

.. figure:: assets/Sentinel-1-GRD-RGB-composite-10.png
	:figclass: align-center
        :width: 750px
        :align: center

* The following files are produced:

    - **S1A_IW_GRDH_1SDV_20200903T181136_20200903T181141_03F910_6B20 - GeoTIFF**
   
