Interferogram generation with ADORE DORIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: assets/tuto_adore_icon.png 
    :width: 50px
    :align: left

**ADORE DORIS interferometric processor**

**EO sources supported**:

    - Envisat ASAR Image Mode Level 1 (ASA_IMS_1P)
    - TerraSAR-X SAR

**Output specifications**

To be defined

Select the processing
=====================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Select the processing service “ADORE DORIS interferometric processor”:

.. figure:: assets/tuto_adore_1.png
	:figclass: align-center 
        :width: 750px
        :align: center
        
The "ADORE DORIS Interferometric Processor" panel is displayed with parameters values to be filled-in.

Fill the parameters
===================

Slave product reference
-----------------------

* Type **ASA_IMS_1P** in the Search Terms field (1) and then click on the lens icon (2):

.. figure:: assets/tuto_adore_2.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on Show Other Parameters:

.. figure:: assets/tuto_adore_3.png
	:figclass: align-center
        :width: 750px
        :align: center

* apply the date value **2008-03-26** in both:

- time:start field
- time:end field 

then click on the button **Search**:

.. figure:: assets/tuto_adore_4.png
	:figclass: align-center
        :width: 750px
        :align: center

* Drag and Drop the first result (the one with **Track 129**) in the *Slave product reference* field:

.. figure:: assets/tuto_adore_5.png
	:figclass: align-center
        :width: 750px
        :align: center

.. figure:: assets/tuto_adore_6.png
	:figclass: align-center
        :width: 750px
        :align: center

Master product reference
------------------------

* Perform the same procedure described previously (`Slave product reference`_), using as values **2009-03-11** . Apply this date value in both:

- time:start field
- time:end field :

.. figure:: assets/tuto_adore_7.png
	:figclass: align-center
        :width: 750px
        :align: center

* Drag and drop the result in the *Master product reference* field:

.. figure:: assets/tuto_adore_8.png
	:figclass: align-center
        :width: 750px
        :align: center

Point of Interest
-----------------

* Type
  
.. code-block:: adore-parameter
  
  POINT(13.4 42.35)
  
in the *Point of Interest* field:

Extent
------

* Type
  
.. code-block:: adore-parameter
 
  2000,2000

in the *Extend*:

Settings for ADORE Doris separated by comma
-------------------------------------------

* Type
  
.. code-block:: adore-parameter

  cc_winsize="128 128",fc_acc="8 8",int_multilook="4 4",coh_multilook="4 4",dumpbaseline="15 10"

in the *Settings for ADORE Doris separated by comma* field:

.. figure:: assets/tuto_adore_9.png
	:figclass: align-center
        :width: 750px
        :align: center

Run the job
===========

* Click on the button Run Job:

.. figure:: assets/tuto_adore_10.png
	:figclass: align-center
        :width: 750px
        :align: center

* See the Running Job:

.. figure:: assets/tuto_adore_11.png
	:figclass: align-center
        :width: 750px
        :align: center

* After about 20 minutes, see the Successful Job:

.. figure:: assets/tuto_adore_12.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on the button *Show results on map*, then on the *20090311_20080326_cint.tiff* result on the *Results Table* in the bottom left side

* See the result on map: 

.. figure:: assets/tuto_adore_13.png
	:figclass: align-center
        :width: 750px
        :align: center
