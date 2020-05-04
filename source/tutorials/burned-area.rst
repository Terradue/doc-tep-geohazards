Sentinel-2 Burned Area Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: assets/tuto_burned-area_icon.png

**Sentinel-2 Burned Area Analysis**

.. |br| raw:: html

   <br />

This service takes as input a pair (pre-event and post-event) of Sentinel-2 MSI L2A products and generates a Burned Area Analysis map and NIR/SVWI RGB composites for the two input Sentinel-2 acquisitions. |br|
This service work better when post fire image is very close to the fire data and masks are applied for the water pixels.

**EO sources supported**

    - Sentinel-2 MSI L2A

**Output specifications**

    - Burned Area Analysis map
    - NIR/SVWI RGB composites
    - Reproducibility notebooks

-----

This tutorial will describe the processing of a pair of Sentinel-2 MSI images to generate a Burned Area Analysis map and NIR/SVWI RGB composites for the two input Sentinel-2 acquisitions on the GEP. |br|
The Burned Area map is obtained through the interesection between AOI and the pre-fire, post-fire Sentinel-2 choosen as input products. |br|
The formula used to estimate burn severity is the Normalized Band Ratio (NBR):

.. figure:: assets/tuto_burned-area_0.png
	:figclass: align-center
        :width: 250px
        :align: center
|	

A high NBR value indicates healthy vegetation while a low value indicates bare ground and recently burnt areas. Non-burnt areas are normally attributed to values close to zero.
The difference between the pre-fire and post-fire NBR obtained from the images is used to calculate the delta NBR (dNBR or ∆NBR). [1]_ [2]_

Select the processing
=====================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Select the processing service “Sentinel-2 Burned Area Analysis”:

.. figure:: assets/tuto_burned-area_1.png
	:figclass: align-center
        :width: 750px
        :align: center

The "Sentinel-2 Burned Area Analysis" panel is displayed with parameters values to be filled-in.

Fill the parameters
===================

Pre-event product reference
---------------------------

* Select the Sentinel-2 data collection in the EO Data button.
* Select the area for which you want to do an anlysis, e.g Corumba in Brasil.

.. figure:: assets/tuto_burned_area_1.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on the lens icon and select **S2MSI2A** as Product Type in the Search Panel
* Apply the date value **2019-08-15** in both **time:start** and **time:end** fields

.. figure:: assets/tuto_burned_area_2.png
	:figclass: align-center
        :width: 750px
        :align: center

* Drag and Drop the selected item in the first *Input reference* field:

.. figure:: assets/tuto_burned_area_3.png
	:figclass: align-center
        :width: 750px
        :align: center

.. NOTE:: pre-event input can be picked up directly by using the following text filter: S2A_MSIL2A_20190815T140101_N0213_R067_T21KUU_20190815T214633

Post-event product reference
----------------------------

* Perform the same procedure described previously (`Pre-event product reference`_), using the value **2019-08-30**.
Pick one of the results having the same track, then drag and drop one of the results in the *Input reference* field:

.. figure:: assets/tuto_burned_area_4.png
	:figclass: align-center
        :width: 750px
        :align: center

.. NOTE:: post-event input can be picked up directly by using the following text filter: S2B_MSIL2A_20190830T140059_N0213_R067_T21KUU_20190830T180923

Area Of Interest in WKT
-----------------------

* Click on the *Magic tool wizard* and select **AOI**. The input parameter is automatically filled with the WKT representing the area selected.

.. figure:: assets/tuto_burned_area_5.png
	:figclass: align-center
        :width: 350px
        :align: center

.. NOTE:: you can also specify manually a different AOI in WKT format, or draw a new area on the map using the search tool and get its value from the *Magic tool wizard*.
Run the job
===========

* Click on the button Run Job and see the Running Job

.. figure:: assets/tuto_burned_area_6.png
	:figclass: align-center
        :width: 350px
        :align: center

* After about 20 minutes, see the Successful Job

Results: download and visualization
===================================

* Click on the button *Show results*

* See the result on map:

.. figure:: assets/tuto_burned_area_7.png
    :figclass: align-center
        :width: 750px
        :align: center
	

* The following files are produced:

    - **Burned area analysis (2019-08-15T14:01:01.0240000Z/2019-08-30T14:00:59.0240000Z)**: Burned area analysis map
    - **NIR/SVWI RGB composite (2019-08-15T14:01:01.0240000Z/2019-08-15T14:01:01.0240000Z)**: NIR/SVWI RGB composite of the pre-event input
    - **NIR/SVWI RGB composite (2019-08-30T14:00:59.0240000Z/2019-08-30T14:00:59.0240000Z)**: NIR/SVWI RGB composite of the post-event input



Reference
==================================
- Parks, S. A., Dillon, G. K. & Miller, C. A New Metric for Quantifying Burn Severity: The Relativized Burn Ratio. Remote Sens. 6, 1827–1844 (2014)
- Keeley, J. E. Fire intensity, fire severity and burn severity: a brief review and suggested usage. Int. J. Wildland Fire 18, 116–126 (2009)

Further reading
==================================
.. [1] Normalized Burn Ratio by Humbold State University - `link <http://gsp.humboldt.edu/OLM/Courses/GSP_216_Online/lesson5-1/NBR.html>`_.
.. [2] UN-SPYDER Knowledge Portal – Normalized Burn Ratio - `link <http://un-spider.org/node/10959>`_.
