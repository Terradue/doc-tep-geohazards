Sentinel-2 Multitemporal RGB composite with Gefolki coregistration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: assets/s2-multitemporal-RGB-Gefolki-icon.png
        :width: 200px

**Sentinel-2 Multitemporal RGB composite with Gefolki coregistration**

This service takes three Sentinel-2 acquisitions to generate a multitemporal RGB composite with Gefolki coregistration including a coregistration step with GEFOLKI.
The output of the service is a EO data product in GeoTIFF format. The product is a a multitemporal RGB composite GeoTiff file obtained through the composition of B04, B03, B02 or B08, B04, B03
bands. The output GeoTiff is displayed in geobrowser with the possibility to access product metadata.

-----

This tutorial will describe the processing of three Sentinel-2 acquisitions to generate a multitemporal RGB composite with Gefolki coregistration including a coregistration step with GEFOLKI.

Select the processing
=====================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Go to the Geobrowser, expand the panel “Processing services” on the right hand side and select the processing service “Sentinel-2 Multitemporal RGB composite with Gefolki coregistration”:

.. figure:: assets/s2-multitemporal-RGB-Gefolki.png
	:figclass: align-center
        :width: 750px
        :align: center

This will display the "Sentinel-2 Multitemporal RGB composite with Gefolki coregistration" service panel including several pre-defined parameters values to be filled-in.

.. figure:: assets/s2-multitemporal-RGB-Gefolki-1.png
	:figclass: align-center
        :width: 750px
        :align: center
        
Fill the parameters
===================

Reference input
---------------

* Select the Sentinel-2 data collection in the EO Data button.

.. figure:: assets/s2-multitemporal-RGB-Gefolki-2.png
	:figclass: align-center
        :width: 750px
        :align: center
        
* Select the area for which you want to do an anlysis, e.g over Napoli (Italy).

.. figure:: assets/s2-multitemporal-RGB-Gefolki-3.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on the lens icon to open the Search Panel
* Select **S2MSI1C** or **S2MSI2A** as Product Type. The three products must have the same Product Type.
* Apply the date value, for example **2020-06-12** in **time:start** field and **2020-08-11** in **time:end** field

.. figure:: assets/s2-multitemporal-RGB-Gefolki-4.png
	:figclass: align-center
        :width: 250px
        :align: center
        

* Drag and Drop three items, one for each of the fields: *Product for RGB composite red band* , *Product for RGB composite green band* , *Product for RGB composite blu band*:

.. figure:: assets/s2-multitemporal-RGB-Gefolki-5.png
	:figclass: align-center
        :width: 750px
        :align: center

* Select one of the two possible choices for the RGB composite: **B04, B03, B02** or **B08, B04, B03**

.. figure:: assets/s2-multitemporal-RGB-Gefolki-6.png
	:figclass: align-center
        :width: 750px
        :align: center
        
Area Of Interest in WKT
-----------------------

* Click on the *Magic tool wizard* and select **AOI**. The input parameter is automatically filled with the WKT representing the area selected.

.. figure:: assets/s2-multitemporal-RGB-Gefolki-7.png
	:figclass: align-center
        :width: 350px
        :align: center

.. NOTE:: you can also specify manually a different AOI in WKT format, or draw a new area on the map using the search tool and get its value from the *Magic tool wizard*.

Run the job
===========

* Click on the button Run Job and see the Running Job

.. figure:: assets/s2-multitemporal-RGB-Gefolki-8.png
	:figclass: align-center
        :width: 350px
        :align: center

.. figure:: assets/s2-multitemporal-RGB-Gefolki-9.png
      	:figclass: align-center
        :width: 350px
        :align: center

* After about 45 minutes, see the Successful Job:

.. figure:: assets/s2-multitemporal-RGB-Gefolki-10.png
	:figclass: align-center
        :width: 350px
        :align: center

Results: download and visualization
===================================

* Click on the button *Show results*

* See the result on map:

.. figure:: assets/s2-multitemporal-RGB-Gefolki-11.png
      	:figclass: align-center
        :width: 750px
        :align: center

* The following files are produced:

    - **Sentinel-2 Multitemporal RGB composite - product GeoTIFF RGB**
    - **Input Product + selected bands - product GeoTIFF**
