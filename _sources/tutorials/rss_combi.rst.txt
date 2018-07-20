COMBI - Band Combination
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: assets/tuto_combi_icon.png
        
**Band Combination**

This service provides the possibility to perform RGB band combination from user defined bands of single or multiple EO data products. The “Band Combination” processing service of the Charter Processing Platform Prototype is meant to give the possibility to derive user-defined band combinations from multi-mission Optical and SAR data. The processing chain of the service has been developed with the use of GDAL and SNAP software. The service supports optical and SAR detected products from the following missions: Sentinel-2, Landsat 8, UK-DMC 2, Kompsat-3, Sentinel-1.
The output is comprising all 3 selected bands in a single RGB product at the resolution of the finest source band. All bands are in their native format (no radiometric correction applied) thus can serve only for fast screening of the data, not for further processing. The output RGB composite is displayed in geobrowser with the possibility to access product metadata and download it as a GeoTIFF file.

**Output specifications**

+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output – product specifications                                                                                                               |
+===============================+===============================================================================================================+
| Correspondent file            | RGB band combination                                                                                          |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Information types             | RGB Composite with user defined source bands                                                                  |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Raster format                 | GeoTIFF                                                                                                       |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| resolution                    | The source band's finest one                                                                                  |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Projection types              | EPSG:3857 - WGS84 Web Mercator (Auxiliary Sphere)                                                             |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Bit depth                     | 8-bit unsigned integer                                                                                        |
|                               | (Unsigned 8-bit raster dataset per channel, e.g. 1band for grayscale image, 3band fir RGB image)              |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Processing Level              | RGB composite                                                                                                 |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Physical product available    | NO                                                                                                            |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Browse product available      | YES                                                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+

-----

Select the Processing Service
=============================

Log in on the Charter Processing Platform Prototype portal and from the “Processing Services” tab, select the “Band Combination” service.

.. figure:: assets/tuto_combi_1.png
	:figclass: align-center
        :width: 750px
        :align: center 

The “Band Combination” panel is displayed with several parameters values to be filled-in.

.. figure:: assets/tuto_combi_2.png
	:figclass: align-center
        :width: 750px
        :align: center  
 
Select the files to process
===========================

This service takes as input multi-mission commercial and open SAR and Optical EO data products available through Charter Processing Platform Prototype.

In the Charter Processing Platform Protoype it is possible to retrieve different types of data:

•	Commercial satellite imagery (e.g. UK-DMC) acquired during charter activations,
•	Selected open EO data collections (e.g. Sentinel-1),
•	Product metadata of historical and on-going charter activations.

In order to easily access each type of data some pre-defined contexts, which essentially consist of catalog query with pre-defined search parameters, are available on the top of the Charter Processing Platform Prototype interface:

•	Charter data: the Charter Processing Platform Prototype is connected to COS-2 and Charter Order Desks to harvest metadata and collect data products from the Charter virtual constellation. The Entry “Charter data” is providing access to all data collections as metadata collections i.e. footprints of images used for each activation and presented in the search result pane as a series of EO data products.
•	EO data: in addition to Charter data the platform is also able to fetch free EO data products via their dissemination services, such as Copernicus data via SciHub service. The Entry “EO data” allows the user to access the full archive of selected free collections (Sentinel-1, Sentinel-2, Landsat-8, DLR InSAR Browse)

Input SAR and Optical data selection must be carried out with particular care while filling required fields for the RGB band combination, since a wrong data entry can result to an unfeasible processing of the service. 

See table below for a full list of Optical and SAR mission supported by the current version of the “Band Combination” service.
 
.. figure:: assets/tuto_combi_3.png
	:figclass: align-center
        :width: 750px
        :align: center 
 
Open EO product catalogue entry
===============================

In this tutorial you are going to process a sample of free EO data product, derived from Sentinel-2 data collections, with the Band Combination processing service.

From the top bar click on the “EO data” context link to access the full archive of selected free collections (e.g. Sentinel-2).

.. figure:: assets/tuto_combi_4.png
	:figclass: align-center
        :width: 750px
        :align: center 

Zoom in into a specific area of interest (e.g. Italy). Apply spatial filter by drawing a rectangle on the map around an area of interest (e.g. Vercelli):
 
.. figure:: assets/tuto_combi_5.png
	:figclass: align-center
        :width: 750px
        :align: center 
 
Click on the “Search Form” icon and select as product type the L1C product. Apply temporal filter by selecting start and end date of the temporal interval (e.g. 1 April – 1 May 2017). Then click on the button Search:
 
.. figure:: assets/tuto_combi_6.png
	:figclass: align-center
        :width: 750px
        :align: center 

All acquisitions related to specified queries are listed in the Results tab:

.. figure:: assets/tuto_combi_7.png
	:figclass: align-center
        :width: 750px
        :align: center 
 
For future reference, you can also drag and drop one of the product listed in the Results tab (e.g. S2A_MSIL1C_20170430T103021) in the “Features Basket” tab.
 
Fill the parameters
===================

In this tutorial you are going to obtain a RGB composite from a single S2 product (e.g. (S2A_MSIL1C_20170430T103021) using a false color infrared band combination (8-3-2).

In order to do that you can follow below steps:

1.	Insert job title “Band Combination”
2.	Drag and Drop from the Results tab the S2 product in the “Product reference for RED” field
3.	From “RED channel band ID” field select S2 band 8
4.	Drag and Drop the same S2 product also in the “Product reference for GREEN” field
5.	From “GREEN channel band ID” field select S2 band 3
6.	Drag and Drop again the same S2 product also in the “Product reference for BLUE” field
7.	From “BLUE channel band ID” field select S2 band 2
8.	Set as “Product reference for output resolution” the same S2 product.
9.	In the “Perform data cropping” field set true and define as “Subset Bounding Box for Cropping” the extent of area of interest.
 
.. figure:: assets/tuto_combi_8.png
	:figclass: align-center
        :width: 750px
        :align: center 
 
Running the job
===============

Click on “Run Job” button from the processor configuration panel and wait for the job to complete. After few minutes, see the Successful Job:

.. figure:: assets/tuto_combi_9.png
	:figclass: align-center
        :width: 750px
        :align: center  
 
View results
============

Click on the Show results on map button after the job is completed. The Band combination result will appear in the map. You can download the RGB product as GeoTIFF file by clicking on the download link in the metadata popup window.

.. figure:: assets/tuto_combi_10.png
	:figclass: align-center
        :width: 750px
        :align: center 
 
The resulting product should be like the one shown below.

.. figure:: assets/tuto_combi_11.png
	:figclass: align-center
        :width: 750px
        :align: center 

