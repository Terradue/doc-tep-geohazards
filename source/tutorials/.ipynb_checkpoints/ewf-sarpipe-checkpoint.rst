S-1 SAR PIPE - Sentinel-1 Interferometric Processing Engine [EXP]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: assets/ewf_sarpipe_icon.png

**S-1 SAR PIPE - Sentinel-1 Interferometric Processing Engine**

S-1 SAR PIPE is a Sentinel-1 SAR data processing chain developed by ARESYS.

This service allows to produce interferograms and coherence maps starting from Sentinel-1 RAW data, supporting both STRIPMAP and TOPSAR (IW and EW) acquisition modes.

Its main advantages are:

- the data stack consistency, ensured starting the processing directly from RAW data, and

- the processing efficiency, ensured limiting the analysis only to the desired area of interest.

**EO sources supported**:

- Sentinel-1 STRIPMAP and TOPSAR (IW and EW) RAW data

**Output specifications**

The service provides 2 output products:

+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Interferogram                                                                                                                                 |
+===============================+===============================================================================================================+
| Correspondent file            | Interferogram                                                                                                 |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Information types             | Interferogram (abs and phase) computed from input RAW couple, focused and coregistered                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Raster format                 | GeoTIFF                                                                                                       |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Resolution                    | Native (same as `Level-1 SLC products`_)                                                                      |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Projection types              | SAR coordinates (slant range vs azimuth)                                                                      |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Bit depth                     | Float 32 complex                                                                                              |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Processing Level              | L2                                                                                                            |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Physical product available    | YES                                                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Browse product available      | YES (both GeoTIFF and PNG)                                                                                    |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output Filename example       | <product name>_interferogram.tif                                                                              |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+

|

+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Coherence map                                                                                                                                 |
+===============================+===============================================================================================================+
| Correspondent file            | Coherence map                                                                                                 |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Information types             | Coherence map computed from input RAW couple, focused and coregistered                                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Raster format                 | GeoTIFF                                                                                                       |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Resolution                    | Native (same as `Level-1 SLC products`_)                                                                      |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Projection types              | SAR coordinates (slant range vs azimuth)                                                                      |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Bit depth                     | Float 32                                                                                                      |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Processing Level              | L2                                                                                                            |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Physical product available    | YES                                                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Browse product available      | YES (both GeoTIFF and PNG)                                                                                    |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Output Filename example       | <product name>_coherence.tif                                                                                  |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+


.. _Level-1 SLC products: https://sentinel.esa.int/web/sentinel/user-guides/sentinel-1-sar/resolutions/level-1-single-look-complex


-----


Select the processing Service
=============================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Select the processing service **S-1 SAR PIPE**:

.. figure:: assets/ewf_sarpipe_tutorial_01.png
	:figclass: align-center
        :width: 750px
        :align: center

Select the files to process
===========================

This service takes as input a list of Sentinel-1 RAW products.

The oldest image is selected to be the **Master** one, i.e. the reference product on which the others (the Slaves) are re-projected and resampled to compute the interferometric phase and interferometric coherence.

Input SAR data selection must be carried out with particular care, since a wrong data selection can result to an unfeasible processing:

    •   The processing service accepts as inputs **only Sentinel-1 RAW (i.e. Level-0) data**.
    •   The Sentinel-1 RAW data must pertain to the **same acquisition mode**.
    •   The user must select **images related to the same track only**.
    •   The user must select **images related to the same polarization only**.
    •   **Spatial overlap** is strictly needed between the images pair.

.. figure:: assets/ewf_sarpipe_tutorial_11.png
    :figclass: align-center
        :width: 750px
        :align: center

For this tutorial, a pre-defined data set has been prepared to speed up data selection step:

* Browse the Data Packages looking for **S-1 SAR PIPE -- August 2016 Central Italy earthquake** package and click on the **load** button to upload it.

.. figure:: assets/ewf_sarpipe_tutorial_02.png
	:figclass: align-center
        :width: 750px
        :align: center

* Select all the products, then drag and drop the selected data in the **L0 level data input** field.

.. figure:: assets/ewf_sarpipe_tutorial_03.png
    :figclass: align-center
        :width: 750px
        :align: center

Fill parameters
===============

* Scroll down the S-1 SAR PIPE configuration menu to show all the parameters.

.. figure:: assets/ewf_sarpipe_tutorial_04.png
    :figclass: align-center
        :width: 750px
        :align: center

Product polarisation
++++++++++++++++++++

S-1 SAR PIPE processes only one polarisation channel that can be selected between:

    •   **VV**: Vertical in both transmission and receiving phases, contained in DV and SV products (default value).
    •   **VH**: Vertical in transmission phase and Horizontal in receiving phase, contained only in DV products.
    •   **HH**: Horizontal in both transmission and receiving phases, contained in DH and SH products.
    •   **HV**: Horizontal in transmission phase and Vertical in receiving phase, contained only in DH products.

**For this run leave the VV default value.**

Bounding Box
++++++++++++

With this parameter is possible to set the AOI (Area Of Interest) where the interferometric processing is performed.
The AOI format is:

    lon_min,lat_min,lon_max,lat_max

**For this run set this AOI: 13.0,42.5,13.4,42.9**


Run the job and results browsing
================================

* Click on the button **Run Job** and see the **Running Job**.

.. figure:: assets/ewf_sarpipe_tutorial_05.png
    :figclass: align-center
        :width: 750px
        :align: center

.. figure:: assets/ewf_sarpipe_tutorial_06.png
    :figclass: align-center
        :width: 750px
        :align: center

* After the processing end (it can take some time, depending on the AOI dimensions), see the **Successful Job**:

.. figure:: assets/ewf_sarpipe_tutorial_07.png
    :figclass: align-center
        :width: 750px
        :align: center

* Scroll down the **Job status** screen, click on the button **Show results**, then check the results list on the **Results Table** in the bottom left side:

The following outputs are listed:

    - **<product name>_interferogram.tif**: this is the product that contains the interferogram computed between Master and Slave images. The Browse product is shown on the map and both Physical and Browse products are available for download.
    - **<product name>_coherence.tif**: this is the product that contains the coherence map computed between Master and Slave images. The Browse product is shown on the map and both Physical and Browse products are available for download.


* Click on each result name. The result will be shown on the map together with metadata information tab and colour-table legend.

.. figure:: assets/ewf_sarpipe_tutorial_08.png
    :figclass: align-center
        :width: 750px
        :align: center

.. figure:: assets/ewf_sarpipe_tutorial_09.png
    :figclass: align-center
        :width: 750px
        :align: center

* Click on the product name and then on the **Download** button that appears in the info tab. Depending on the output the following products can be downloaded:

    •   **Product File (tif)**: this is the physical quantity.
    •   **Browse GeoTiff**: this is the GeoTiff browse product as shown on the map.
    •   **Browse Legend (png)**: this is the PNG browse product.
    •   **Metadata (properties)**: a txt file containing all the metadata info displayed in the info tab.

.. figure:: assets/ewf_sarpipe_tutorial_10.png
    :figclass: align-center
        :width: 750px
        :align: center
