G-POD SBAS InSAR Service
~~~~~~~~~~~~~~~~~~~~~~~~

Select the processing
=====================

* Sign-in on the Portal https://geohazards-tep.eo.esa.int/ (see guidance :doc:`user <../community-guide/user>` section)

* Access the Geobrowser: https://geohazards-tep.eo.esa.int/geobrowser/

.. figure:: assets/tuto_sbas_0.png
	:figclass: align-center
        :width: 750px
        :align: center

* Open the tab "Processing services" from the right of the map, and then select the processing service “InSAR SBAS”.

.. figure:: assets/tuto_sbas_1.png
	:figclass: align-center
        :width: 750px
        :align: center

The "InSAR SBAS" panel is displayed with parameter values to be filled-in.

Select the files to process
===================

* Browse the Data Packages looking for *London Desc ASAR* package and click on the load button to upload it.

.. figure:: assets/tuto_sbas_2.png
	:figclass: align-center
        :width: 750px
        :align: center

* Surf the map to the London (UK) Area of Interest: the browser page should appear as depicted in the next figure.

.. figure:: assets/tuto_sbas_3.png
	:figclass: align-center
        :width: 750px
        :align: center
        
* Set the *Job Title* with a meaningful name (e.g. London ASAR) and push the *sel. all* button in the Feature Basket. 
      
.. figure:: assets/tuto_sbas_4.png
	:figclass: align-center
        :width: 750px
        :align: center
                
* Drag all the selected data and drop them within the Files field on the right panel.                
                
.. figure:: assets/tuto_sbas_5.png
	:figclass: align-center
        :width: 750px
        :align: center                
                
                
Fill the parameter values
===================

* As *Lat*, type:

.. code-block:: sbas-parameter
  
  51.5

* As *Lon*, type:

.. code-block:: sbas-parameter
  
 -0.13
 
* As *Cut data over selected AoI* type:

  false

* As *Processing Mode*, select:

.. code-block:: sbas-parameter
  
  MTA

.. figure:: assets/tuto_sbas_6.png
	:figclass: align-center
        :width: 750px
        :align: center
        
.. note::

  You can leave all the other fields as blank.

Run the job
===========

* Click on the button "Run Job" at the bottom of the SBAS InSAR processor tab, and monitor the progress of the running Job:

.. figure:: assets/tuto_sbas_7.png
	:figclass: align-center
        :width: 750px
        :align: center

* After about 21 hours of processing time, check the status is set as "Successful Job"

* Download the SBAS InSAR processing results once the Job is completed:

.. figure:: assets/tuto_sbas_8.png
	:figclass: align-center
        :width: 750px
        :align: center
