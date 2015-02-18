G-POD SBAS InSAR Service
~~~~~~~~~~~~~~~~~~~~~~~~

Select the processing
=====================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Select the processing service “InSAR SBAS WPS”:

.. figure:: assets/tuto_sbas_1.png
	:figclass: align-center
        :width: 750px
        :align: center

The "InSAR SBAS WPS" panel is displayed with parameters values to be filled-in.

Fill the parameters
===================

* As *Task Caption*, type:

.. code-block:: sbas-parameter

  SBAS Tutorial Task

* As *Bounding Box*, type:

.. code-block:: sbas-parameter
 
  14.36,40.78,14.5,40.88

* As *Start Date*, type:

.. code-block:: sbas-parameter
  
  2008-01-01T00:00:00

* As *End Date*, type:

.. code-block:: sbas-parameter
  
  2008-06-30T23:59:59

* As *Track Number*, type:

.. code-block:: sbas-parameter
  
  129

* As *Lat*, type:

.. code-block:: sbas-parameter
  
  40.858049

* As *Lon*, type:

.. code-block:: sbas-parameter
  
  14.310228

* As *Processing Mode*, select *IFG*:

* As *Zone UTM*, type:

.. code-block:: sbas-parameter
  
  13  

* As *CM_UTM*, type:

.. code-block:: sbas-parameter
  
  15

* As *Y0*, type:

.. code-block:: sbas-parameter
  
  0

.. note::

  You can left all the other field as blank.

.. figure:: assets/tuto_sbas_2.png
        :figclass: align-center
        :width: 750px
        :align: center

Run the job
===========

* Click on the button Run Job and see the Running Job:

.. figure:: assets/tuto_sbas_3.png
	:figclass: align-center
        :width: 750px
        :align: center

* After about 2 hours, see the Successful Job:

.. figure:: assets/tuto_sbas_4.png
	:figclass: align-center
        :width: 750px
        :align: center
