Sentinel-2 Watermask [`cppp <https://eo4society.esa.int/2022/05/24/advanced-cloud-based-environment-to-support-immediate-disaster-response/>`_, wb, `esa <https://geohazards-tep.eu/#!pages/partners>`_]
~~~~~~~~~~~~~~~~~~~~

.. image:: assets/Sentinel-2-Water-Mask-icon.png
        :width: 200px

**Sentinel-2 Watermask**

This service takes as input a Sentinel-2 MSI Level 1C or Level 2A product to generate a water mask using the NDWI and the SWM.
The output of the service is a EO data product in GeoTIFF format. The output GeoTiff is displayed in the geobrowser with the possibility to access product metadata.

**Relevance to the Charter Processing Environment**:
  - Wildfire: to mask out the water content of vegetation as it may impact the burned area delineation product 
  - Flood: to mask out the water “normally” found in the flooded areas.
  
=====================

The NDWI is most appropriate for water body mapping. The water body has strong absorbability and low radiation in the range from visible to infrared wavelengths. 
The index uses the green and Near Infra-red bands of remote sensing images based on this phenomenon. The NDWI can enhance the water information effectively in most cases. It is sensitive to built-up land and often results in over-estimated water bodies.

**Values description**: NDWI values of water bodies are larger than 0.5. Vegetation has much smaller values, which result in distinguishing vegetation from water bodies easier. Built-up features have positive values between zero and 0.2.

-----

**Output specifications**

The service provides 2 output products.

+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output-1 – Water mask                                                                              			                        |
+===============================+===============================================================================================================+
| Correspondent file            | Water mask using the NDWI the SWM                                                                             |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Information types             | Water mask : BLACK=Earth, WHITE=Water                        						        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Raster format                 | GeoTIFF                                                                                                       |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| resolution                    | Native                                                                    		                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Projection types              | EPSG:3857 - WGS84 – Pseudo Mercator                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Browse product available      | YES as 8 bit PNG file                                                                                         |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output Filename example       | Water mask for S2B_MSIL2A_20200709T100029_N0214_R122_T33TUF_20200709T133643	                                |    
+-------------------------------+---------------------------------------------------------------------------------------------------------------+

|

+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output-2 – WATER_MASK_VECTOR                                                                              			                |
+===============================+===============================================================================================================+
| Correspondent file            | Water mask vector                                                                      		        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Raster format                 | geojson                                                                                                       |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output Filename example       | S2B_MSIL2A_20200709T100029_N0214_R122_T33TUF_20200709T133643_WATER_MASK_VECTOR.geojson	                |    
+-------------------------------+---------------------------------------------------------------------------------------------------------------+


Select the processing
=====================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Go to the Geobrowser, expand the panel “Processing services” on the right hand side and select the processing service “Sentinel-2 Water Mask”:

.. figure:: assets/Sentinel-2-Water-Mask.png
	:figclass: align-center
        :width: 750px
        :align: center

This will display the "Sentinel-2 Water Mask" service panel including several pre-defined parameters values to be filled-in.

.. figure:: assets/Sentinel-2-Water-Mask-1.png
	:figclass: align-center
        :width: 750px
        :align: center
        
Fill the parameters
===================

Reference input
---------------

* Select the Sentinel-2 data collection in the EO Data button.

.. figure:: assets/Sentinel-2-Water-Mask-2.png
	:figclass: align-center
        :width: 750px
        :align: center
        
* Select the area for which you want to do an analysis, e.g over Terracina (Italy).

.. figure:: assets/Sentinel-2-Water-Mask-3.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on the lens icon to open the Search Panel
* Select **S2MSI1C** or **S2MSI2A** as Product Type
* Apply the date value, for example **2020-07-09**, in both **time:start** and **time:end** fields.

.. figure:: assets/Sentinel-2-Water-Mask-4.png
	:figclass: align-center
        :width: 250px
        :align: center
        
* Drag and Drop the selected item in the *Sentinel-2 product for water masking* field:

.. figure:: assets/Sentinel-2-Water-Mask-5.png
	:figclass: align-center
        :width: 750px
        :align: center

Area Of Interest in WKT
-----------------------

* Click on the *Magic tool wizard* and select **AOI**. The input parameter is automatically filled with the WKT representing the area selected.

.. figure:: assets/Sentinel-2-Water-Mask-6.png
	:figclass: align-center
        :width: 350px
        :align: center

.. NOTE:: you can also specify manually a different AOI in WKT format, or draw a new area on the map using the search tool and get its value from the *Magic tool wizard*.

Run the job
===========

* Click on the button Run Job and see the Running Job

.. figure:: assets/Sentinel-2-Water-Mask-7.png
	:figclass: align-center
        :width: 350px
        :align: center

.. figure:: assets/Sentinel-2-Water-Mask-8.png
	:figclass: align-center
        :width: 350px
        :align: center

* After about 20 minutes, see the Successful Job:

.. figure:: assets/Sentinel-2-Water-Mask-9.png
	:figclass: align-center
        :width: 350px
        :align: center

Results: download and visualization
===================================

* Click on the button *Show results*

* See the result on map:

.. figure:: assets/Sentinel-2-Water-Mask-10.png
	:figclass: align-center
        :width: 750px
        :align: center

* The following files are produced:

    - **Water mask for S2B_MSIL2A_20200709T100029_N0214_R122_T33TUF_20200709T133643 - GeoTIFF**
    - **S2B_MSIL2A_20200709T100029_N0214_R122_T33TUF_20200709T133643_WATER_MASK_VECTOR.geojson - geojson**
    
Further reading
==================================
- NDWI Normalized Difference Water Index - `link <https://custom-scripts.sentinel-hub.com/sentinel-2/ndwi/>`_. `link <http://eoscience.esa.int/landtraining2017/files/posters/MILCZAREK.pdf>`_. `link <https://www.sciencedirect.com/science/article/abs/pii/S0034425796000673?via%3Dihub>`_. `link <https://en.wikipedia.org/wiki/Normalized_difference_water_index>`_.

