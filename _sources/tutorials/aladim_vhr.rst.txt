ALADIM-VHR: Automatic LAndslide Detection and Inventory Mapping from multispectral Very-High Resolution data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: assets/tuto_aladim_vhr_icon.png 


**ALADIM**

This service is developed by CNRS-EOST (Strasbourg, France). It allows to detect and map new landslides triggered by large forcing events (earthquake, heavy rains) from the analysis of pre- and post-event imagery, and is based on change detection methods. It allows the processing of Very-High Resolution (VHR) multispectral data (typically Pléiades and Spot 6/7). The set of pre- and post-image should be accurately co-registered in order to use the service. A training dataset of manually mapped landslides (by digitalization), the extent of the training areas, and the extent of the region of interest (ROI) should be provided as inputs (shape file-format) by the user. The outputs consist in a database of landslide polygons than can be assimilated to an Earth-Observation derived landslide inventory. ALADIM builds on the change detection methodology partially described in [1]_ and [2]_ . 

**EO sources supported**:

    - Mandatory: A couple of ortho-rectified multispectral (MS) images (typically Pléiades and Spot 6/7), including 4 bands (B, G, R and NIR) 
    - Optional: A couple of ortho-rectified panchromatic (P) images


**Output specifications**

    - A shapefile (*.shp files) containing the landslides detected at an F2 optimal threshold.
    - An image (geotiff file format) containing all landslides detected at an F2 optimal threshold.
    - Two documents (*.pdf files) presenting the cross-validation quality control (precision-recall curves and accuracies of the parameters).

-----

This tutorial introduces to the use of the service for the detection and the mapping of landslides from VHR multispectral images. To this end, we will process a couple of Spot-6/Spot-7 images acquired before and after `Hurricane Matthew`_ which hit Haiti in October 2016. The images are available through the CEOS Recovery Observatory.

.. _`Matthew Hurricane`: https://en.wikipedia.org/wiki/Hurricane_Matthew
.. _`CEOS Recovery Observatory`: http://ceos.org/ourwork/workinggroups/disasters/recovery-observatory/


Select the processing service
=============================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Go to the Geobrowser, expand the panel “Processing services” on the right hand side and select the processing service “ALADIM-VHR”:

.. figure:: assets/tuto_aladim_vhr_1.png
	:figclass: align-center
        :width: 750px
        :align: center

This will display the service panel including several pre-defined parameters which can be adapted.

.. figure:: assets/tuto_aladim_vhr_2.png
	:figclass: align-center
        :width: 750px
        :align: center

Use case: Landslide detection and mapping from SPOT6-SPOT7 multispectral data
=============================================================================

Upload input data
-----------------
 
The input images must be uploaded by the user. The image file names must include the acquisition dates and the following terms: bgrn_before and bgrn_after (for the multispectral images pre- and post-event) and, optional, pan_before and pan_after (for the panchromatic pre- and post-images)   
For this tutorial we present the example of a couple of multispectral images and a couple of panchromatic images acquired by SPOT6 and SPOT7 satellites. 
The first image was acquired before Hurricane Matthew on 14-04-2016 and the second after the event on 04-04-2017. Ideally, images acquired at the same session should be used to obtain similar radiometric signatures.   

Upload your data:

.. figure:: assets/tuto_aladim_vhr_3.png
	:figclass: align-center
        :width: 750px
        :align: center

.. figure:: assets/tuto_aladim_vhr_4.png
	:figclass: align-center
        :width: 750px
        :align: center

Drag and drop your images in the fields of the service panel:

.. figure:: assets/tuto_aladim_vhr_5.png
	:figclass: align-center
        :width: 750px
        :align: center
      

Create an archive for the ensemble of your input shapefiles (training_areas.shp, training_samples.shp and aoi.shp). The framework requires a flat .tar.gz format (i.e. the contents of the archive file must not include folders). 
A tutorial about the input dataset creation is available here: :doc:`tutorial <aladim_input_dataset_preparation>`

Upload the archive:

.. figure:: assets/tuto_aladim_vhr_6.png
	:figclass: align-center
        :width: 750px
        :align: center

.. figure:: assets/tuto_aladim_vhr_7.png
	:figclass: align-center
        :width: 750px
        :align: center


Drop the archive in the field of the service panel "shape files uri":

.. figure:: assets/tuto_aladim_vhr_8.png
	:figclass: align-center
        :width: 750px
        :align: center

Set the processing parameters 
-----------------------------

There is a total of 11 processing parameters that can be adjusted. When hovering over the parameter fields, you will see a short explanation for each of the parameters.

* **ALADIM_N_STRATA:** Number of spatial strata for cross validation. If set to a value >1, then spatial-coverage sampling [4]_ will be used to partition the **training_area(s)** in homogenous patches. Each patch will be used as test data during cross-validation runs to estimate the accuracy of the classification. The recommended default values is 10. If the value is set to 1 the service will attempt to use the originally provided **training_area(s)** for cross-validation.
* **ALADIM_IMAGE_NODATA:** No data value in the provided images (0 by default). Areas with no data in any of the images will be excluded.
* **ALADIM_SEG_SCALE:**	The segmentation scale factor (See [3]_ for details about segmentation). Larger values will result in fewer larger segments and faster processing. Smaller values will result in more more small segments which will increase the processing time but also typically the accuracy of the classification. The default value is 70 but the value depends a lot on the value range of the input imagery and the landscape characteristics.
* **ALADIM_SEG_COLOR_WEIGHT:** A value between 0 and 1 to define the weight of color during the segmentation. The default value is 0.9.
* **ALADIM_SEG_SHAPE_WEIGHT:** A value between 0 and 1 to define the weight of compact shape during the segmentation. The default value is 0.1.
* **ALADIM_SEG_MIN_SIZE:** Minimum allowed segment size. Segments smaller that this value (in pixels) will be merged to their most similar neighbor after the segmentation or deleted if isolated.
* **ALADIM_SUN_AZIMUTH:** A series of comma seperated angles which will be used for the computation of hillshade layers (based on SRTM 30). Typically one would choose the sun azimuths during the acquisition of the pre- and post-event imagery (e.g. from the image metadata).
* **ALADIM_SUN_ELEVATION:**	A series of comma seperated angles which will be used for the computation of hillshade layers (based on SRTM 30). Typically the sun elevations during the acquisition of the pre- and post-event imagery (e.g. from the image metadata). **Must have the same number of entries as ALADIM_SUN_AZIMUTH**
* **ALADIM_POSITIVE_THRESHOLD:** A value between 0 and 1. If the fraction of positive area (i.e. landslide as mapped in the training samples) within a segment exceeds this value it is considered as a positive example. Vice versa it will be considered as a negative example. The default value is 0.5.

The figure below summarizes the parameter settings for this test.

.. figure:: assets/tuto_aladim_vhr_9.png
	:figclass: align-center
        :width: 750px
        :align: center


Run the job
-----------

* You are good to go. Click on the button *Run Job* at the bottom of the right panel. Depending on the allocated resources the execution will require a few hours to terminate.

.. figure:: assets/tuto_aladim_vhr_10.png
	:figclass: align-center
        :width: 750px
        :align: center

* Once the job has finished, click on the *Show results* button to get a list and a pre-visualization of the results.

.. note:: The pre-visualization in the *Geobrowser* is just a preview and the user is encouraged to download the results for further analysis and post-processing.

.. figure:: assets/tuto_aladim_vhr_11.png
	:figclass: align-center
        :width: 750px
        :align: center

.. figure:: assets/tuto_aladim_vhr_12.png
	:figclass: align-center
        :width: 750px
        :align: center

References
==========

.. [1] Stumppf, A., Kerle, N. 20110. Object-oriented mapping of landslides using Random Forests. Remote Sensing of Environment, 115(10): 2564-2577.
.. [2] Stumpf, A., Lachiche, N., Malet, J.-P., Puissant, A., Kerle, N. 2014. Active learning in the spatial domain for remote sensing image classification. IEEE Transactions on Geoscience and Remote Sensing, 52(5): 2492-2507.
.. [3] Lassalle, P., Inglada, J. Michel, J., Grizonnet, M., Malik, P. 2015. A scalable tile-based framework for region-merging segmentation. IEEE Transactions on Geoscience and Remote Sensing, 53(10): 5473-5485.
.. [4] Walvoort, D.J.J., Brus, D.J., De Gruijter, J.J. 2010. A R package for spatial coverage sampling and random sampling from compact geographical strata by k-means. Computers & Geosciences, 36(10): 1261-1267.
.. [5] Zhu, Z., Wang, S., Woodcock, C.E. 2015. Improvement and expansion of the Fmask algorithm: cloud, cloud shadow, and snow detection for Landsats 4-7, 8, and Sentinel 2 images. Remote Sensing of Environment, 159: 269-277.
