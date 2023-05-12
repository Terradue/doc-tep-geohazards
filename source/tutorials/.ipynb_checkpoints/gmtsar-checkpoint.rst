GMT5SAR InSAR - Stripmap
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: assets/tuto_gmtsar_icon.png
        
**GMT5SAR InSAR - Stripmap**

GMT5SAR is an open source (GNU General Public License) InSAR processing system. This service provides standard 2-pass processing of a master product against one or more slave products.

**EO sources supported**:

    - ERS-1/2 SAR
    - Envisat ASAR Image Mode Level 1 (ASA_IMS_1P)

**Output specifications**

    - amplitude of interferogram (display_amp.ps  )
    - phase of interferogram (phase.ps)
    - correlation of interferogram (corr.ps)

-----

This tutorial covers the typical InSAR processing to form an interferogram using two SAR images and a digital elevation model.

The GMT5SAR processing service can also process several pairs master/slave (same master).

Select the processing
=====================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Select the processing service "GMT5SAR InSAR - Stripmap":

.. figure:: assets/tuto_gmtsar_v2_1.png
	:figclass: align-center
        :width: 750px
        :align: center

The "GMT5SAR InSAR - Stripmap" panel is displayed with parameters values to be filled-in.

.. NOTE:: Parameters comes with default pre-filled values which are the same as the ones used in this tutorial, so you may skip the following section and directly use the pre-filled parameters.

Fill the parameters
===================

.. NOTE:: slave and master can be picked up by using the following data package (alternatively to the search steps described): **BajaCaliforniaEQ**

Slave product reference
-----------------------

* Select **EO Data / Envisat** as data collection.

* Type **ASA_IM__0P** in the Search Terms field (1):

.. figure:: assets/tuto_gmtsar_v2_2_1.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on Show Other Parameters and apply the date value **2010-05-02** in both:
- time:start field
- time:end field
then click on the button **Search**:

.. figure:: assets/tuto_gmtsar_v2_2_1.png
	:figclass: align-center
        :width: 750px
        :align: center

* Drag and Drop the first result in the *Slave product reference* field:

.. figure:: assets/tuto_gmtsar_v2_2_1.png
	:figclass: align-center
        :width: 750px
        :align: center

Master product reference
------------------------

* Perform the same procedure described previously (`Slave product reference`_), using the value **2010-03-28** in both the **time:start** field and the **time:end** field:

.. figure:: assets/tuto_gmtsar_v2_2_1.png
	:figclass: align-center
        :width: 750px
        :align: center

* Drag and drop the first result in the *Master product reference* field:

.. figure:: assets/tuto_gmtsar_v2_2_1.png
	:figclass: align-center
        :width: 750px
        :align: center

* Select the Snaphu threshold

.. figure:: assets/tuto_gmtsar_v2_2_1.png
	:figclass: align-center
        :width: 750px
        :align: center
		
Run the job
===========

* Click on the button Run Job and see the Running Job

.. figure:: assets/tuto_gmtsar_v2_3.png
	:figclass: align-center
        :width: 750px
        :align: center

* After about 25 minutes, see the Successful Job:

.. figure:: assets/tuto_gmtsar_v2_4.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on the button *Show results on map*, then on the *phase_mask_ll.tiff* result on the *Results Table* in the bottom left side

* See the result on map:

.. figure:: assets/tuto_gmtsar_v2_4.png
	:figclass: align-center
        :width: 750px
        :align: center


More info
=========

http://topex.ucsd.edu/gmtsar/
