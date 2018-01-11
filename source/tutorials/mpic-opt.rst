MPIC-OPT: Multiple pairwise optical image correlation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This service targets the detection and measurement of horizontal ground deformation (e.g. co-seismic slip, landsliding) based on sub-pixel image correlation. The service allows to jointly analyse a single pairs or time-series of Sentinel-2 images. It combines methods for sub-pixel image matching of multiple-pair combinations as presented in [1]_ and the correction of systematic co-registration residuals as presented in [2]_.

This tutorial will introduce you to the use of the service for the detection of landslide surface displacement for two use cases beeing the quantification of landslide surface displacement and co-seismic displacement. To this end we will process a series of Sentinel-2 images acquired over the Harmalière landslide (France 2016) in and Sentinel-2 images acquired before and after the Kaikoura earthquake (New Zealand 2016).

Select the processing service
=============================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Go to the Geobrowser, expand the panel “Processing services” on the right hand side and select the processing service “MPIC-OPT”:

.. figure:: assets/tuto_mpicopt_1.png
	:figclass: align-center
        :width: 750px
        :align: center

This will display the service panel including several pre-defined parameters which can be adapted .

.. figure:: assets/tuto_mpicopt_2.png
	:figclass: align-center
        :width: 750px
        :align: center

Use case 1: Landslide surface displacement
==========================================

Select input data
-----------------

The Geobrowser offers multiple ways to search and discover a large variety of EO-based dataset and the interested reader should refer to the :doc:`Geobrowser <../community-guide/platform/geobrowser>` section for a general introduction. 
For this tutorial we will rely on readily prepared data packages which are accessible through the "Data Packages" tab on the lower right of the screen. If you type "Harmaliere" into the search box you should be able to find a data package named "Harmaliere landslide". Similarily you can search for "Kaikoura" to find the data package that we will use in the second part of this tutorial.

.. figure:: assets/tuto_mpicopt_3.png
	:figclass: align-center
        :width: 750px
        :align: center

Click on the data package, hold shift and Drag and Drop all four results in the *Sentinel-2 products* field in the service panel on the right:

.. figure:: assets/tuto_mpicopt_4.png
	:figclass: align-center
        :width: 750px
        :align: center

.. caution:: Sentinel-2 datasets distributed before September 2016 contain multiple tiles. For such datasets the *Geobrowser* currently returns several results including both the original multi-tile dataset and a preview of the footprints of the contained tiles. For processing you must select **only** the original multi-tile datasets. For datasets after October 2016 there is no such ambiguity.

Set the processing parameters 
-----------------------------

There is a total of 9 processing parameters that can be adjusted and when hovering over the parameter fields you will see a short explanation for each of the parameters.

* **Sentinel-2 band:** Specify the Sentinel-2 band used for matching. The option *B04* is recommended since the red band is also used for band to band co-registration by ESA
* **Sentinel-2 tile:** This parameter is mainly for backwards compatibility with older SAFE datasets(before September 2016) where multiple tiles where distributed in one SAFE folder. For such datasets it is necessary to specify Sentinel-2 tile in the format T{UTM zone number}{MGRS code} (e.g. T31TGK). However, here we are dealing with single tile datasets so that the parameter can be set to *NONE*.
* **Temporal matching range:** Defines how many pairs will be created considering the temporal order of the selected images. The default is *2* so that each image is matched with at most the previous 2 images within the selection.
* **Split date:** An optional parameter of the form "YYYY-MM-DD" which will split the time series into two subsets and pairs will only be formed among members of different subsets. We will see the utility of this parameter in the second example and will leave it at *NONE* for the moment.
* **Window size:** The parameter controls the size of the template used for matching among the input images. More specifically it controls the neighborhood around the central pixel so that the default value of *3* results in a 7x7 window size. The minimum value is 1 (3x3 pixel) and the recommended maximum is 7 (15x15 pixel). A smaller window will allow to better reconstruct small scale variations while at the same time can lead to more noise. Vice versa larger window sizes will lead to greater robustness against noise while smoothing small scale details. For small scale movements such as landslides we recommend a smaller window size (e.g. 2) while for large scale movements such as coseismic slip larger window sizes are often better.
* **Decorrelation threshold:** Matches with a correlation coefficient [0,1] will be discarded. The default value is *0.2*.
* **Spatial matching range:** Defines the search range in pixel for finding matches. The actual search range is computed from this parameter as round(Spatial matching range/0.8)+2. This parameter should be adjusted according to the maximum expected displacement taking into account also the possible coregistration bias of the input images. This the considered landslide underwent a period of strong acceleration we will increase this value to *7*.
* **Regularization parameter:** Similar to the window size the regularization parameter controls the smootheness of the expected motion field. Increasing the regularization parameter is putting greater emphasize on a smooth motion field where neighboring pixels will have similar displacment values. For small scale features with strong gradients in the motion fields (e.g. landlsides) we recommend values between 0.05 and 0.3. For large scale features such as coseismic displacement further increasing the value can lead to smoother and less noisy results. Here we will use the default value of *0.3*.
* **Activate backward matching:** If set to True backward matching will be performed for each pair. Here we will leave it at the default beeing *False*.

The figure below summarizes the parameter settings for this test.

.. figure:: assets/tuto_mpicopt_5.png
	:figclass: align-center
        :width: 750px
        :align: center


Run the job
-----------

* You are good to go. Click on the button *Run Job* at the bottom of the right panel. Depending on the allocated resources the execution will require at least few hours to terminate.

.. figure:: assets/tuto_mpicopt_6.png
	:figclass: align-center
        :width: 750px
        :align: center

* Once the job has finished click on the *Show results* button to get a list and pre-visualization of all displacement maps and the respective multi-temporal indicators.

.. note:: The pre-visualization in the *Geobrowser* is just a preview and the user is encouraged to download the results for further processing and analysis.

.. figure:: assets/tuto_mpicopt_7.png
	:figclass: align-center
        :width: 750px
        :align: center


Use case 2: Coseismic slip
==========================

With this second use case we will illustrate the use of MPIC-OPT for measurements of co-seismic slip using the example of the `Kaikoura earthquake`_ which hit the southern island of New Zealand on 14 November 2016.

.. _`Kaikoura earthquake`: https://en.wikipedia.org/wiki/2016_Kaikoura_earthquake

Select input data
-----------------

As in the previous example there is already a data package available which we you can find by typing "Kaikoura" in the search box in the "Data Packages" tab on the lower right of the screen.

.. figure:: assets/tuto_mpicopt_8.png
	:figclass: align-center
        :width: 750px
        :align: center

Click on the data package, hold shift and Drag and Drop all four results in the *Sentinel-2 products* field in the service panel on the right:

.. figure:: assets/tuto_mpicopt_9.png
	:figclass: align-center
        :width: 750px
        :align: center


Set the processing parameters 
-----------------------------

.. note:: For this example we will set the **Split date** in which case the **Temporal matching range** is ignored.


* **Sentinel-2 band:** Specify the Sentinel-2 band used for matching. The option *B04* is recommended since the red band is also used for band to band co-registration by ESA.
* **Sentinel-2 tile:** The tile code for this scene is *59GQP*.
* **Temporal matching range:** For this use case we will use the **Split date** parameter in which case all possible pairs are formed and the **Temporal matching range** will be ignored.
* **Split date:** We will set the parameter to the date of the earthquake which is *2016-11-13* (UTC time). Consequently the service will match all scenes before this date with all scenes after this date.
* **Window size:** The parameter controls the size of the template used for matching among the input images. Leave it at the default value of *3* which results in a 7x7 window size.
* **Decorrelation threshold:** We will slightly increase this threshold to *0.33*.
* **Spatial matching range:** Defines the search range in pixel for finding matches. The horizontal offsets for this event reached 10 m and more and we should provide some additional tolerance for possible co-registration offsets. So set the value to *3*.
* **Regularization parameter:** Here again we will use the default value of *0.3*.
* **Activate backward matching:** Set this option to *True* to also inverse the pairs which provides an aditional measurement that can help to reduce the variance of the offsets measured at each time step.

The figure below summarizes the parameter settings for this test.

.. figure:: assets/tuto_mpicopt_10.png
	:figclass: align-center
        :width: 750px
        :align: center

Run the job
-----------

* You are good to go. Click on the button *Run Job* at the bottom of the right panel. Depending on the allocated resources the execution will require at least few hours to terminate.

.. figure:: assets/tuto_mpicopt_11.png
	:figclass: align-center
        :width: 750px
        :align: center

* Once the job has finished click on the *Show results* button to get a list and pre-visualization of all displacement maps and the respective multi-temporal indicators.

.. note:: The pre-visualization in the *Geobrowser* is just a preview and the user is encouraged to download the results for further processing and analysis.

.. figure:: assets/tuto_mpicopt_12.png
	:figclass: align-center
        :width: 750px
        :align: center


References
==========

.. [1] Stumpf, A., Malet, J.P. and Delacourt, C., 2017. Correlation of satellite image time-series for the detection and monitoring of slow-moving landslides. Remote Sensing of Environment, 189, pp.40-55.

.. [2] Stumpf, A., Michéa, D. Malet, J.P., in Press. Improved co-registration of Sentinel-2 and Landsat-8 imagery for Earth surface motion measurements. Remote Sensing.
