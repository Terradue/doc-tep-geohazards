ROI_PAC on Hadoop Cloud Sandbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the processing
=====================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Select the processing service “Repeat Orbit Interferometry Package (ROI_PAC)”:

.. figure:: assets/tuto_roi_pac_1.png
	:figclass: align-center
        :width: 750px
        :align: center

The "Repeat Orbit Interferometry Package (ROI_PAC)" panel is displayed with parameters values to be filled-in.

Fill the parameters
===================

Master product reference
-----------------------

* Type **ASA_IM__0P** in the Search Terms field (1) and then click on the lens icon (2):

.. figure:: assets/tuto_roi_pac_2.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on Show Other Parameters apply the date value **2010-05-02** in both:
- time:start field
- time:end field 
then click on the button **Search**:

.. figure:: assets/tuto_roi_pac_3.png
	:figclass: align-center
        :width: 750px
        :align: center

* Drag and Drop the first result in the *ASAR Master product catalogue entry* field:

.. figure:: assets/tuto_roi_pac_4.png
	:figclass: align-center
        :width: 750px
        :align: center

Slave product reference
------------------------

* Perform the same procedure described previously (`Master product reference`_), using the value **2010-03-28**. Apply this date value in both:
- time:start field
- time:end field 
Pick one of the results having the same track, then drag and drop one of the results in the *ASAR Slave product catalogue entry* field:

.. figure:: assets/tuto_roi_pac_5.png
	:figclass: align-center
        :width: 750px
        :align: center

Run the job
===========

* Click on the button Run Job and see the Running Job

.. figure:: assets/tuto_roi_pac_6.png
	:figclass: align-center
        :width: 750px
        :align: center

* After about 20 minutes, see the Successful Job:

.. figure:: assets/tuto_roi_pac_7.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on the button *Show results on map*, then on the *geo_100328-100502.unw.phase.tif* result on the *Results Table* in the bottom left side

* See the result on map: 

.. figure:: assets/tuto_roi_pac_8.png
	:figclass: align-center
        :width: 750px
        :align: center
