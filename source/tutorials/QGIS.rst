QGIS USER MANUAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS has a powerful Application Programming Interface to extend the core functionality of the software as well as write scripts to automate your tasks. The QGIS Export post-processing service takes one or more references to results obtained on <platform> to generate a compressed archive with:

  - A QGIS project
  - The data associated to the reference(s) provided as input as a geopackage
  - Two QGIS layouts rendered as PDF and PNG (including a PNG world file)


Select the processing
=====================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Select the processing service “QGIS export”:

.. figure:: assets/QGIS.png
	:figclass: align-center
        :width: 750px
        :align: center

The "QGIS export" panel is displayed with parameters values to be filled-in.

.. figure:: assets/QGIS_1.png
	:figclass: align-center
        :width: 750px
        :align: center

Fill the parameters
===================

  - The input parameters to provide are:
  - Area of interest (not mandatory): specify the AOI of the service.
  - World zone name (not mandatory): name of the AOI that, if specified, appears in the legend of the final results. If not specified, the field will be filled in by the string: “Area of interest”.
  - Title ( mandatory): field where the title of the final result is specified. The length of the string must be  less than or equal to 45 characters.
  - Description (mandatory): description of the service that is used as input for the QGIS service. The length of the string must be  less than or equal to 550 characters.
  - Logo URL (mandatory): url of the GEP logo
  - Disclaimer (mandatory): 
  - Data source description (mandatory): description of the products used as input (Sentinel-1, Sentinel-2, etc.). Example: https://emergency.copernicus.eu/mapping/system/files/components/EMSN074_01ZAGREB_P09RCMON_00OVERVIEW_v2.pdf
  - Main map (mandatory): represents the main result of the service that is used as input, such as for example: Sentinel-2 Burned Area, where the main map is the pixels that represent the fire. It must be put as Main map otherwise the result would be overlaid with the others and would no longer be seen in the final .pdf file.
  - Other map (not mandatory): secondary results of the service that are used as input
  
.. figure:: assets/QGIS_2.png
	:figclass: align-center
        :width: 750px
        :align: center
        
Once downloaded and extracted, the QGIS project can be opened with QGIS.

Discovering the contents of the project
===================

  - In this project we integrated the QGIS software among our services. The results of this project are:
  - PDF file for each layout
  - PNG file for each layout
  - QGIS file that must be opened directly with QGIS
  
.. figure:: assets/QGIS_3.png
	:figclass: align-center
        :width: 750px
        :align: center
        
Adding a background layer
===================

There is an input parameters: Other map, whose purpose is to add a background layer. If this parameter is empty, google maps will be the background layer.

Accessing the layouts
===================

To access the layouts, you need to download the QGIS project and open it with QGIS. 
Once opened QGIS, click on Project, open.

.. figure:: assets/QGIS_4.png
	:figclass: align-center
        :width: 750px
        :align: center

Select the .qgs file located in the previously downloaded folder.

.. figure:: assets/QGIS_5.png
	:figclass: align-center
        :width: 750px
        :align: center
        
Therefore, to visualize the layouts click on Project, Layout and choose one of the two layouts available.

.. figure:: assets/QGIS_6.png
	:figclass: align-center
        :width: 750px
        :align: center
        
Modifying the layouts
===================

To change the layout, open, for example, the GEP landscape layout window.

.. figure:: assets/QGIS_7.png
	:figclass: align-center
        :width: 750px
        :align: center

Then, to modify the layout click on one of the contents of the layout and at the bottom right a window will open with all the features.

.. figure:: assets/QGIS_8.png
	:figclass: align-center
        :width: 750px
        :align: center
        
Therefore, you can now make all the changes and then save them.      
