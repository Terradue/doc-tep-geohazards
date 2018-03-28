G-POD GAMMA DInSAR Service
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: assets/tuto_gamma_dinsar_icon.png
        
**GAMMA DInSAR**

The GAMMA SAR and Interferometry Software is a collection of programs, developed by GAMMA Remote Sensing, which allows processing of SAR, interferometric SAR (InSAR) and differential interferometric SAR (DInSAR) data. The GAMMA DInSAR service integrated on the ESA's Grid Processing On Demand (G-POD) performs the generation of differential interferograms starting from ENVISAT L1 SLC.

**EO sources supported**:

    - Envisat ASAR L1 SLC

**Output specifications**

  - differential interferograms
  
Select the processing
=====================

* Sign-in on the Portal https://geohazards-tep.eo.esa.int/ (see guidance :doc:`user <../community-guide/user>` section)

* Access the Geobrowser: https://geohazards-tep.eo.esa.int/geobrowser/

* Open the tab "Processing services" from the right of the map, and then select the processing service “GAMMA DInSAR”:


Select the files to process
===========================

* Load the data package called “GAMMA DInSAR Tutorial” containing the following products:

.. code-block:: gamma-dinsar-parameter

  ENVISAT ASAR ASA_IMS_1P, 2009-04-12T09:24:26.652Z, , Track: 79
  ENVISAT ASAR ASA_IMS_1P, 2009-02-01T09:24:28.014Z, , Track: 79
  
.. figure:: assets/tuto_gamma_dinsar_1.png
	:figclass: align-center
        :width: 750px
        :align: center  
  
Fill the parameter values
=========================

Mandatory paramters
--------------------

* As *Job title*, type:

.. code-block:: gamma-dinsar-parameter

  GAMMA DInSAR

* As input *Files*, drag and drop the selected product:

.. code-block:: gamma-dinsar-parameter

  ENVISAT ASAR ASA_IMS_1P, 2009-04-12T09:24:26.652Z, , Track: 79
  ENVISAT ASAR ASA_IMS_1P, 2009-02-01T09:24:28.014Z, , Track: 79

.. figure:: assets/tuto_gamma_dinsar_2.png
	:figclass: align-center
        :width: 750px
        :align: center	
        
* As *Bounding Box*, type:

.. code-block:: gamma-dinsar-parameter

  12.86,42.11,13.64,42.6

* As *Master File* drag and drop in the box the following product:

.. code-block:: gamma-dinsar-parameter

  ENVISAT ASAR ASA_IMS_1P, 2009-02-01T09:24:28.014Z, , Track: 79

.. figure:: assets/tuto_gamma_dinsar_3.png
	:figclass: align-center
        :width: 750px
        :align: center	

Run the job
===========

* Click on the button "Run Job" at the bottom of the GAMMA DInSAR processor tab, and monitor the progress of the running Job:

.. figure:: assets/tuto_gamma_dinsar_4.png
	:figclass: align-center
        :width: 750px
        :align: center	
        
* Wait for the Job completion, then check the status is set as "Successful Job” and and download the GAMMA DInSAR processing results once the Job is completed:

.. figure:: assets/tuto_gamma_dinsar_5.png
	:figclass: align-center
        :width: 750px
        :align: center	
