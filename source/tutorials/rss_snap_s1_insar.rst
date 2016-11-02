SNAP S1 TOPS-IW Interferometric processor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This tutorial processes a pair of Sentinel-1 TOPSAR IW data with the SNAP S1 TOPS-IW Interferometric processor. 
SNAP (SeNtinel’s Application Platform) [#f1]_ is the common architecture for all Sentinel Toolboxes jointly developed by Brockmann Consult, Array Systems Computing and C-S. The interferometric processing chain for Sentinel 1 TOPSAR IW images is implemented through the tools contained in the Sentinel-1 Toolbox.

The interferometric SAR technique
---------------------------------

Interferometric synthetic aperture radar (InSAR) exploits the phase difference between two complex radar SAR observations taken from slightly different sensor positions and extracts information about the earth’s surface. A SAR signal contains amplitude and phase information. The amplitude is the strength of the radar response and the phase is the fraction of one complete sine wave cycle (a single SAR wavelength). The phase of the SAR image is determined primarily by the distance between the satellite antenna and the ground targets. By combining the phase of these two images after coregistration, an interferogram can be generated whose phase is highly correlated to the terrain topography. The InSAR technique can potentially measure millimetre-scale changes in deformation over spans of days to years. It has applications for geophysical monitoring of natural hazards, for example earthquakes, volcanoes and landslides, and in structural engineering, in particular monitoring of subsidence and structural stability.

Sentinel-1 Interferometric Wide Swath Products
----------------------------------------------

The Interferometric Wide (IW) swath mode is the main acquisition mode over land for Sentinel-1. It acquires data with a 250 km swath at 5 m by 20 m spatial resolution (single look). IW mode captures three sub-swaths using Terrain Observation with Progressive Scans SAR (TOPSAR). With the TOPSAR technique, in addition to steering the beam in range as in ScanSAR, the beam is also electronically steered from backward to forward in the azimuth direction for each burst, avoiding scalloping and resulting in homogeneous image quality throughout the swath. TOPSAR mode replaces the conventional ScanSAR mode, achieving the same coverage and resolution as ScanSAR, but with a nearly uniform SNR (Signal-to-Noise Ratio) and DTAR (Distributed Target Ambiguity Ratio). IW SLC products contain one image per sub-swath and one per polarisation channel, for a total of three (single polarisation) or six (dual polarisation) images in an IW product. Each sub-swath image consists of a series of bursts, where each burst has been processed as a separate SLC image. The individually focused complex burst images are included, in azimuth time order, into a single sub-swath image with black-fill demarcation in between, similar to ENVISAT ASAR Wide ScanSAR SLC products.

The tutorial uses a coseismic pair of Sentinel-1 TOPSAR IW data related to the August 2016 center Italy's earthquake.

The 2016 center Italy's earthquake (also known as 2016 Amatrice earthquake) was an earthquake, measuring 6.2 on the moment magnitude scale, hit Central Italy on 24 August 2016 at 03:36:32 CEST (01:36 UTC). Its epicentre was close to Accumoli, with its hypocentre at a depth of 4 km, approximately 75 km (47 mi) southeast of Perugia and 45 km (28 mi) north of L'Aquila, in an area near the borders of the Umbria, Lazio, Abruzzo and Marche regions.
Learn more about the event in the `2016 center Italy's earthquake Wikipedia <https://en.wikipedia.org/wiki/2016_Central_Italy_earthquake>`_ entry.

The processing service code is available in the GitHub repository `geohazards-tep/rss-snap-s1-insar <https://github.com/geohazards-tep/dcs-rss-snap-s1-insar>`_.

Select the processing
=====================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Select the processing service “SNAP S1 TOPS-IW Interferometric processor”:

.. figure:: assets/tuto_rss_snap_s1_insar_1.png
	:figclass: align-center
        :width: 750px
        :align: center

The "SNAP S1 TOPS-IW Interferometric processor" panel is displayed with parameters values to be filled-in.

Fill the parameters
===================

Master product reference
------------------------

* Click on the **EO data** icon (1) and select **Sentinel-1** (2), then click on the lens icon (3):

.. figure:: assets/tuto_rss_snap_s1_insar_2.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on **Show Other Parameters** and apply the following values:
 
            * Product type **SLC** in **eop:productType** field
			
			* Platform **S1A** in **eop:platform** field
            		
			* Track number **22** in **eop:track** field
			
			* Spatial search box **13.1,42.65,13.35,42.9** in **geo:box** field
			
			* Date value **2016-08-21** in both **time:start** and **time:end** fields			
			
then click on the button **Search**:

.. figure:: assets/tuto_rss_snap_s1_insar_3.png
	:figclass: align-center
        :width: 750px
        :align: center

* Drag and Drop the result in the *Master product reference* field:

.. figure:: assets/tuto_rss_snap_s1_insar_4.png
	:figclass: align-center
        :width: 750px
        :align: center

Slave product reference
-----------------------

* Perform the same procedure described previously (`Master product reference`_), using the value **2016-09-02**. Apply this date value in both:

- time:start field
- time:end field

Pick the result, then drag and drop one of the results in the *Slave product reference* field:

.. figure:: assets/tuto_rss_snap_s1_insar_5.png
	:figclass: align-center
        :width: 750px
        :align: center
		
Perform phase unwrapping and Subset Bounding Box for Unwrapping 
---------------------------------------------------------------

If also the displacement of the earthquake's epicentre is desired: 

* Click on the **Perform phase unwrapping** setting (1) and select **true**

* Click on the **Get from current search** button (2) near the **Subset Bounding Box for Unwrapping** parameter box. It should be automatically filled with **13.1,42.65,13.35,42.9**, as already set during the previous `Master product reference`_ selection procedure.

**NOTE**: The *Subset Bounding Box for Unwrapping* parameter is mandatory even if the phase unwrapping is not requested (i.e. when "Perform phase unwrapping"=false). Please put "-180.0,-56.0,180.0,60.0" as bounding box value in case of wrapped interferogram generation only.


.. figure:: assets/tuto_rss_snap_s1_insar_6.png
	:figclass: align-center
        :width: 750px
        :align: center 

Other parameters
----------------

* **Product polarisation**: **VV** as the default value;
* **Orbit type**: **Sentinel Restituted (Auto Download)** as the default value;
* **Azimuth coherence window size**: **6** as the default value;
* **Range coherence window size**: **20** as the default value;
* **DEM type**: **SRTM 3 Sec** ;
* **Azimuth Multilook factor**: **1** as the default value;
* **Range Multilook factor**: **4** as the default value;
* **Pixel spacing in meters**: **15.0** as the default value.

		
Run the job
===========

* Click on the button **Run Job** and see the Running Job

.. figure:: assets/tuto_rss_snap_s1_insar_7.png
	:figclass: align-center
        :width: 750px
        :align: center

* After the processing end (it can take some hours), see the Successful Job:

.. figure:: assets/tuto_rss_snap_s1_insar_8.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on the button *Show results*, then on the results on the *Results Table* in the bottom left side:

    * **coh_VV_21Aug2016_02Sep2016.png**:  coeherence quick-look product; 
    * **displacement_ifg_srd_VV_21Aug2016_02Sep2016.png**:  displacement quick-look product;
    * **phase_ifg_srd_VV_21Aug2016_02Sep2016.png**: interferometric phase quick-look product.  

* See the result on map:

.. figure:: assets/tuto_rss_snap_s1_insar_9.png
	:figclass: align-center
        :width: 750px
        :align: center
		
.. figure:: assets/tuto_rss_snap_s1_insar_10.png
	:figclass: align-center
        :width: 750px
        :align: center
		
.. figure:: assets/tuto_rss_snap_s1_insar_11.png
	:figclass: align-center
        :width: 750px
        :align: center
		
It is possible to download the tif products and/or the png quick-look products by clicking on the product name and then on the "Download" button (1).

.. figure:: assets/tuto_rss_snap_s1_insar_12.png
	:figclass: align-center
        :width: 750px
        :align: center

Warning on output products deletion
===================================

Please note that the generated output (in particular the .tiff products) are not stored in a persistent manner on the platform. 
The Tiff products will be automatically deleted after two weeks.
  	

.. rubric:: References

.. [#f1] `SNAP Website <http://step.esa.int/main/toolboxes/snap>`_