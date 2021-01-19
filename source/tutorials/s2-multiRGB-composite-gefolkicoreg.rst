Sentinel-2 Multitemporal RGB composite with Gefolki coregistration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: assets/s2-multitemporal-RGB-Gefolki-icon.png
        :width: 200px

**Sentinel-2 Multitemporal RGB composite with Gefolki coregistration**

This service takes three Sentinel-2 MSI Level 1C or Level 2A acquisitions to generate a multitemporal RGB composite including a coregistration step with GEFOLKI. The three input products must have the same Level. 
The output of the service is a EO data product in GeoTIFF format. The product is a multitemporal RGB composite obtained through the composition of bands B04, B03, B02 (Natural colours) or bands B08, B04, B03 (false colour Infrared).
The service takes the blue band of one of the products as a basis - reference product for the red channel of the RGB composite. Then it does coregistration with GeFolki of the other products for the green and blue bands of the RGB composite.
The output GeoTiff is displayed in the geobrowser with the possibility to access product metadata and downaload it.

-----

This tutorial will describe the processing of three Sentinel-2 acquisitions to generate a multitemporal RGB composite including a coregistration step with GEFOLKI.

**Output specifications**

The service provides the following output products.

+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output-1 – Sentinel-2 Multitemporal RGB composite (B0X|B0Y|B0Z)                                                                               |
+===============================+===============================================================================================================+
| Correspondent file            | Sentinel-2 Multitemporal RGB composite                                                                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Information types             | RGB Composite   : RED=(Red band product B0X), GREEN=(green band product B0Y), BLUE=(Blu band product B0Z)	|
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Raster format                 | GeoTIFF                                                                                                       |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| resolution                    | Native		                                                                                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Projection types              | EPSG:3857 - WGS84 – Pseudo Mercator                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Processing Level              | RGB composite                                                                                                 |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output Filename example       | Sentinel-2 Multitemporal RGB composite obtained through the composition of bands B0X, B0Y, B0Z                |    
+-------------------------------+---------------------------------------------------------------------------------------------------------------+

|

If the parameter service **provided band results** has been set to **Yes**, then:

+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output-2 – Input Product selected bands			                                                                                |
+===============================+===============================================================================================================+
| Correspondent file            | Input Product selected bands		                                                                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Raster format                 | GeoTIFF                                                                                                       |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| resolution                    | Native		                                                                                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Projection types              | EPSG:3857 - WGS84 – Pseudo Mercator                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output Filename example       | Input Product selected bands.tif								                |    
+-------------------------------+---------------------------------------------------------------------------------------------------------------+

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
* Select **S2MSI1C** or **S2MSI2A** as Product Type. The three products must have the same Product Type and Level.
* Apply the date value, for example **2019-08-01** in **time:start** field and **2019-09-05** in **time:end** field

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

Choose the results
-----------------------

* The user can decide to get as output only the RGB, if choose **No** in the **provided results band** parameters, or all the bands used as input, if choose **Yes**. 

.. figure:: assets/s2-multitemporal-RGB-Gefolki-8.png
	:figclass: align-center
        :width: 350px
        :align: center

Run the job
===========

* Click on the button Run Job and see the Running Job

.. figure:: assets/s2-multitemporal-RGB-Gefolki-9.png
	:figclass: align-center
        :width: 350px
        :align: center

.. figure:: assets/s2-multitemporal-RGB-Gefolki-10.png
      	:figclass: align-center
        :width: 350px
        :align: center

* After about 45 minutes, see the Successful Job:

.. figure:: assets/s2-multitemporal-RGB-Gefolki-11.png
	:figclass: align-center
        :width: 350px
        :align: center

Results: download and visualization
===================================

* Click on the button *Show results*

* See the result on map:

.. figure:: assets/s2-multitemporal-RGB-Gefolki-12.png
      	:figclass: align-center
        :width: 750px
        :align: center

* The following output files are produced:

    - **Sentinel-2 Multitemporal RGB composite obtained through the composition of bands B0X, B0Y, B0Z - product GeoTIFF RGB**
    - **Input Product selected bands - product GeoTIFF** - for each input product
    
Reference
==================================
- Plyer, A., et al. (2015). A New Coregistration Algorithm for Recent Applications on Urban SAR Images. Geoscience and Remote Sensing Letters, IEEE, 12(11), 2198-2202.
- Brigot, G., et al. (2016)  Adaptation and Evaluation of an optical flow method applied to co-registration of forest remote sensing images, accepted with modifications in  IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing,  Volume: 9, Issue7, July 2016

Further reading
==================================
- The Coregistration Swiss Army Knife: GeFolki - `link <https://w3.onera.fr/medusa/gefolki>`_.
