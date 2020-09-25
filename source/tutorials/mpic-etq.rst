MPIC-ETQ: Multiple pairwise optical image correlation for Earthquake
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: assets/tuto_mpicopt_icon.png
        
**MPIC-ETQ**

**MPIC-EarThQuake** is derived from the **MPIC-OPTical** service developed by CNRS EOST, Strasbourg, France [1]_.

"The MPIC-OPT (Mutiple Pairwise Image Correlation of OPtical image Time-series) service enables the processing of optical image time-series for the monitoring of persistent surface deformation (continuously moving landslides and glaciers). It enables the on-demand processing of time series of Sentinel-2 (Pleaides and Spot6/7 in its VHRO version) if time series (of at least 2 dates, but the more the better) are available over an area. It comprises three components for a) the measurement of sub-pixel displacement among one or multiple optical image pairs (sub-pixel image correlation), b) the correction outlier and geometric residuals and c) a component for spatio-temporal analysis of the stack of image pairs with the possibility to i) compute multi-temporal fusion parameters and/or ii) invert time-series using the Time-series for Image Optic (TIO) algorithm developed by Isterre, Grenoble, France [2]_,[3]_. This service targets the detection and measurement of horizontal ground deformation (e.g. co-seismic slip, landsliding) based on sub-pixel image correlation or optical flow. It combines methods for sub-pixel image matching of multiple-pair combinations as presented in [1]_ and the correction of systematic co-registration residuals as presented in [4]_.
MPIC-OPT is proposed on the GEP in two versions: MPIC-ETQ and MPIC-MM."


**MPIC-ETQ** is tailored for co-seismic monitoring allowing a limited number of input images. It uses the MicMac image matching correlator developed by IGN/ENS, Paris, France [5]_ and proposes a limited number of parameters which makes it relatively easy to launch by non-expert users. 

**EO sources supported**:

    - Sentinel-2 MSI L1C

**Output specifications**

* **Mean displacement:** A floating point GeoTiff representing the average displacement over all time steps in *meters*. The naming convention is *MM_Mean_displ__magnitude_tile_date1_to_dateN.tif*
* **Mean velocity:** Two floating point GeoTiffs representing the mean absolute velocities in E−W direction and N−S direction in *meters/day* respectively. The naming conventions are *MM_Mean_velocity_EW_tile_date1_to_dateN.tif* and  *MM_Mean_velocity_NS_tile_date1_to_dateN.tif*.
* **Quality map:** A floating point GeoTiff representing per pixel the percentage of the pairs with *NCC > minimum correlation threshold*. 
* **Coherence Vector:** A floating point GeoTiff in the range [0,1] representing per pixel the coherence of the displacement. A coherence vector value of 0 indicates a highly variable direction of the displacement while a coherence vector value close to 1 indicates a consistent and persistent displacement in the same direction.  
* **Corrected displacement fields and correlation maps for each time step:** Floating point GeoTiffs representing the measured displacements among the two respective input images in pixels in E-W direction (east is postive) and N-S direction (South is positive) after the corrections selected by the user: The naming conventions are *MM_EW_displ_tile_date1_vs_date2_corrected.tif* and *MM_NS_displ_tile_date1_vs_date2_corrected.tif* respectively.
* **Filtered displacement fields and correlation maps for each time step:** Floating point GeoTiffs representing the measured displacements among the two respective input images in pixels in E-W direction (east is postive) and N-S direction (South is positive) after filtering: The naming conventions are *MM_EW_displ_tile_date1_vs_date2_FILTER_Displmax.tif* and *MM_NS_displ_tile_date1_vs_date2_FILTER_Displmax.tif* respectively.

* **Cloud masks:** 8-bit GeoTiffs representing the mask for each time step. Six flags are indicated : 0 = clear; 1 = null; 2 = cloud; 3 = shadow; 4 = snow; 5 = water. The naming convention is: *Tile_date_spectral_mask.tif*
* **DEM products:** 

* **Correllation coefficient:**  8-bit GeoTiffs representing the correlation coefficient for each time step with the correlation coefficient [0,1] quantized to a range of 128 to 255. The naming convention is *MM_Corr_tile_date1_date2.tif*.
* **Decorrellation masks:**  8-bit GeoTiffs representing the decorellation mask. Pixel . The naming convention is *tile_date1_date2_decorrel_mask.tif*

.. Convention:: The displacement and the mean velocity products are displayed with this convention: positive values are toward the **South** and toward the **East** in the *Forward* time direction. If *Forward+Backward* option is activated the products in the *Backward* direction will have opposite signs as compared to the ones in the *Forward* direction of the time.


-----

This tutorial will introduce you to the use of the service for the quantification of co-seismic displacement. To this end we will process Sentinel-2 images acquired before and after the Ridgecrest earthquakes (California, USA, 2019).

.. The service is one of three services implemented by CNRS-EOST on the Geohazards Exploitation platform which are mainly dedicated the detection and monitoring of landslides and measurements of surface deformation. This includes the generation of surface models and orthoimages from very-high resolution (VHR) Pléiades images (DSM-OPT), the detection and measurement of surface motion (e.g. landslides and co-seismic slip) from time-series of Sentinel-2 images (MPIC-OPT), and the rapid mapping of newly triggered landslides using Sentinel-2 or VHR orthoimages from before and after major triggering events such as earthquakes or heavy rainstorms.

Select the processing service
=============================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Go to the Geobrowser, expand the panel “Processing services” on the right hand side and select the processing service “MPIC-ETQ”:

.. figure:: assets/tuto_mpicetq_1.png
	:figclass: align-center
        :width: 750px
        :align: center

This will display the service panel including several pre-defined parameters which can be adapted .

.. figure:: assets/tuto_mpicetq_2.png
	:figclass: align-center
        :width: 750px
        :align: center

Use case: July 2019 Ridgecrest Earthquakes
==========================================

Select input data
-----------------

The Geobrowser offers multiple ways to search and discover a large variety of EO-based dataset and the interested reader should refer to the :doc:`Geobrowser <../community-guide/platform/geobrowser>` section for a general introduction. 
For this tutorial we will rely on readily prepared data package which is accessible through the "Data Packages" tab on the upper left of the screen. If you type "Ridgecrest" into the search box you should be able to find a data package named "Ridgecrest_2019_S2_2im". Alternatively you can access the `Ridgecrest data package`_ directly by clicking on the provided link.

.. _`Ridgecrest data package`: https://geohazards-tep.eu/t2api/share?url=https%3A%2F%2Fgeohazards-tep.eu%2Ft2api%2Fdata%2Fpackage%2Fsearch%3Fid%3DRidgecrest_2019_S2_2im


.. figure:: assets/tuto_mpicetq_3.png
	:figclass: align-center
        :width: 750px
        :align: center

Click on the data package, hold shift and Drag and Drop all four results in the *Sentinel-2 products* field in the service panel on the right:

.. figure:: assets/tuto_mpicetq_4.png
	:figclass: align-center
        :width: 750px
        :align: center

.. caution:: Sentinel-2 datasets distributed before 27 September 2016 contain multiple tiles. For such datasets the *Geobrowser* currently returns several results including both the original multi-tile dataset and a preview of the footprints of the contained tiles. For processing you must select **only** the original multi-tile datasets. For datasets after 27 September 2016 there is no such ambiguity.

Set the processing parameters 
-----------------------------

There is a total of 16 processing parameters that can be adjusted and when hovering over the parameter fields you will see a short explanation for each of the parameters.

* **DEM:** Specify the Digital Elevation Model that will be used for filtering the displacement fields. The *Merit* [5]_ and the *Copernicus* [6]_ are available to GEP users. By default, the Merit DEM is used.
* **Sentinel-2 band:** Specify the Sentinel-2 band used for matching. The option *B04* is recommended since the red band is also used for band to band co-registration by ESA.
* **Split date:** An optional parameter of the form "yyyy-MM-dd" which will split the time series into two subsets and pairs will only be formed among members of different subsets. This is particularly interesting in the case of quantifying the co-seismic displacement. By default, this field is left empty.
* **Minimum matching range:** Define the minimum matching range for creating the image pairs. The matching range is express in *acquisitions* so if a minimum range is set to 1, all the images (N) will be paired with at least the next image in time (N+1). By default, this parameter is set to 1.
* **Maximum matching range:** Define the maximum matching range for creating the image pairs. The matching range is express in *acquisitions* so if a maximum range is set to 2, all the images (N) will be paired with at most the next second image in time (N+2). By default, this parameter is set to 5.
* **Matching direction:** If set to *Forward* the pairs are only created in the time direction. If *Forward+Backward* is selected, the pairs wil be created in both directions (i.e. time and reverse time direction). By default, *Forward* is set. 
.. caution:: Choosing the *Forward+Backward* option should be carefully considered by user as it increases the number of pairs created and hence, the computing time and ressources.
* **Window size:** Control the size of the template used for matching among the input images. More specifically it controls the neighborhood around the central pixel so that the default value of *3* results in a 7x7 window size. The minimum value is 1 (3x3 pixel) and the recommended maximum is 7 (15x15 pixel). A smaller window will allow to better reconstruct small scale variations while at the same time can lead to more noise. Vice versa larger window sizes will lead to greater robustness against noise while smoothing small scale details. For small scale movements such as landslides we recommend a smaller window size (e.g. 2) while for large scale movements such as coseismic slip larger window sizes are often better.
* **Decorrelation threshold:** Matches with a correlation coefficient [0,1] will be discarded. The default value is *0.2*.
* **Spatial matching range:** Define the search range in pixel for finding matches. The actual search range is computed from this parameter as round(Spatial matching range/0.8)+2. This parameter should be adjusted according to the maximum expected displacement taking into account also the possible coregistration bias of the input images. Since the considered landslide underwent a period of strong acceleration we will increase this value to *7*.
* **Regularization parameter:** Similar to the window size the regularization parameter controls the smoothness of the expected motion field. Increasing the regularization parameter is putting greater emphasis on a smooth motion field where neighboring pixels will have similar displacment values. For small scale features with strong gradients in the motion fields (e.g. landlsides) we recommend values between 0.05 and 0.3. For large scale features such as coseismic displacement further increasing the value can lead to smoother and less noisy results. Here we will use the default value of *0.3*.
* **Snow mask:** If set to *True*, the areas of the images covered by snow are masked. In certain cases like the monitoring of glaciers ice velocity, this parameter should be desactivated. By default, this parameter is set to *True*.
* **Cloud mask:** If set to *True*, the areas of the images covered by clouds are masked. By default, this parameter is set to *True*.
* **Slope mask range minimum:** The pixels located in slopes with an angle larger than the value set in this parameter are filtered out in the final products. By default, the pixels located on slopes with angle larger than 80 degrees are filtered out.
* **Slope mask range maximum:** The pixels located in slopes with an angle smaller than the value set in this parameter are filtered out in the final products. By default, the pixels located on slopes with angle between *Slope mask range minimum* and 90 degrees are filtered out.
* **Apply correction and filtering:** If set to *True*, the geometric corrections as described in [1]_ and filtering as descibed in [0]_ are applied. They are highly recommended for any study case and  are applied by default.
* **Apply correction and filtering:** If set to *True*, the jitter undulation present in certain pairs of Sentinel-2 images can be significantly filetered out [0]_. This correction is recommended for displacement fields with large spatial wavelength like co-seismic displacemnet fields. By default, the correction is applied.



Run the job
-----------

* You are good to go. Click on the button *Run Job* at the bottom of the right panel. 

.. figure:: assets/tuto_mpicetq_5.png
	:figclass: align-center
        :width: 750px
        :align: center

Depending on the allocated resources the execution will require at least few hours to terminate.

* Once the job has finished click on the *Show results* button to get a list and pre-visualization of all displacement maps and the respective multi-temporal indicators.

.. note:: The pre-visualization in the *Geobrowser* is just a preview and the user is encouraged to download the results for further processing and analysis.

.. figure:: assets/tuto_mpicetq_6.png
	:figclass: align-center
        :width: 750px
        :align: center


References
==========

.. [1] Stumpf, A., Malet, J.P. and Delacourt, C., 2017. Correlation of satellite image time-series for the detection and monitoring of slow-moving landslides. Remote Sensing of Environment, 189, pp.40-55.

.. [2] Cavalié, M.-P. Doin, C. Lasserre, P. Briole, Ground motion measurement in the Lake Mead area (Nevada, USA), by DInSAR time series analysis : probing the lithosphere rheological structure,  J. Geophys. Res., 112, B03403, doi:10.1029/2006JB004344, 2007

.. [3] Bontemps, N., P. Lacroix, Doin, M. P. (2018). Inversion of deformation fields time-series from optical images, and application to the long term kinematics of slow-moving landslides in Peru. Remote Sensing of Environment, 210, 144-158, 10.1016/j.rse.2018.02.023

.. [4] Stumpf, A., Michéa, D. Malet, J.P., in Press. Improved co-registration of Sentinel-2 and Landsat-8 imagery for Earth surface motion measurements. Remote Sensing.

.. [5] Yamazaki D., D. Ikeshima, R. Tawatari, T. Yamaguchi, F. O'Loughlin, J.C. Neal, C.C. Sampson, S. Kanae & P.D. Bates A high accuracy map of global terrain elevations Geophysical Research Letters, vol.44, pp.5844-5853, 2017 doi: 10.1002/2017GL072874

.. [6] 

