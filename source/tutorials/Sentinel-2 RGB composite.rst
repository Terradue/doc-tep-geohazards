Sentinel-2 L1C and L2A RGB composite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: assets/Sentinel-2-RGB-composite-icon.png
        :width: 200px

**Sentinel-2 L1C and L2A RGB composite**

This service performs RGB band combination from user defined bands of the Sentinel-2 MSI L1C or L2A products (up to 4 - full tiles) provided as input.

-----

**EO sources supported**

This service supports as input the **Sentinel-2 L1A** and **Sentinel-2 L2A** products.

**Output specifications**

The service provides the following output product.

+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output – Sentinel-2 L1C and L2A RGB composite 												|
+===============================+===============================================================================================================+
| **Correspondent file**        | Sentinel-2 RGB composite                                                                                      |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Raster format**             | GeoTIFF                                                                                                       |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **resolution**                | Native		                                                                                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Projection types**          | EPSG:3857 - WGS84 – Pseudo Mercator                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Output Filename example**   | Natural Colors - Quicklook (2020-08-13T10:08:31/2020-08-13T10:08:31)                                          |    
+-------------------------------+---------------------------------------------------------------------------------------------------------------+


Select the processing
=====================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Go to the Geobrowser, expand the panel “Processing services” on the right hand side and select the processing service “Sentinel-2 RGB Composites”:

.. figure:: assets/Sentinel-2-RGB-composite.png
	:figclass: align-center
        :width: 750px
        :align: center

This will display the "Sentinel-2 RGB Composites" service panel including several pre-defined parameters values to be filled-in.

.. figure:: assets/Sentinel-2-RGB-composite-1.png
	:figclass: align-center
        :width: 750px
        :align: center
        
Fill the parameters
===================

Reference input
---------------

* Select the Sentinel-2 data collection in the EO Data button.

.. figure:: assets/Sentinel-2-RGB-composite-2.png
	:figclass: align-center
        :width: 750px
        :align: center
        
* Select the area for which you want to do an anlysis, e.g over Roma (Italy).

.. figure:: assets/Sentinel-2-RGB-composite-3.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on the lens icon to open the Search Panel
* Select **S2MSI1C** or **S2MSI2A** as Product Type. The three products must have the same Product Type and Level.
* Apply the date value, for example **2020-08-01** in **time:start** field and **2020-08-15** in **time:end** field

.. figure:: assets/Sentinel-2-RGB-composite-4.png
	:figclass: align-center
        :width: 250px
        :align: center
        

* Drag and Drop the selected item in the *Input references* field:

.. figure:: assets/Sentinel-2-RGB-composite-5.png
	:figclass: align-center
        :width: 750px
        :align: center


Run the job
===========

* Click on the button Run Job and see the Running Job

.. figure:: assets/Sentinel-2-RGB-composite-6.png
	:figclass: align-center
        :width: 350px
        :align: center

.. figure:: assets/Sentinel-2-RGB-composite-7.png
      	:figclass: align-center
        :width: 350px
        :align: center

* After about 45 minutes, see the Successful Job:

.. figure:: assets/Sentinel-2-RGB-composite-8.png
	:figclass: align-center
        :width: 350px
        :align: center

Results: download and visualization
===================================

* Click on the button *Show results*

* See the result on map:

.. figure:: assets/Sentinel-2-RGB-composite-9.png
      	:figclass: align-center
        :width: 750px
        :align: center

* The following output files are produced:

    - **Natural Colors - Quicklook (2020-08-13T10:08:31/2020-08-13T10:08:31) - product GeoTIFF RGB**
    
