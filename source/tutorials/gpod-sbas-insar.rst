G-POD SBAS InSAR Service
~~~~~~~~~~~~~~~~~~~~~~~~

This tutorial describes how to submit a job for the SBAS-InSAR service to obtain a ground displacement time series from ERS and/or ENVISAT ASAR data. The tutorial is addressed to users already familiar with InSAR processing, analysis and products, and gives some hints and recommendation for the best service usage experience.

The provided service performs the full SBAS-InSAR chain from RAW data (Level 0) focusing to displacement time series generation.

The main user actions are the following:
*	select the Input SAR Raw data to be processed;
*	optionally define the area of SAR data to be processed;
*	set input parameters/threshold (e.g. baseline, temporal coherence, …) for SBAS-InSAR processing;
*	obtain SBAS-InSAR geocoded (Lat/Lon and/or UTM WGS84) results, such as mean deformation velocity map and deformation time series.

As additional feature, the possibility to generate single or stack of interferograms co-registered to a single master geometry is also available.

Users are encouraged to use the SBAS-InSAR service here described for scientific purposes. Please, note that commercial use (including service provisioning) of any part of this service is not allowed without express permission from the CNR-IREA Institute and ESA. 
Being this service available for free for scientific use, please recognize the effort made by the authors by citing:

=====  =====  ======
F. Casu, S. Elefante, P. Imperatore, I. Zinno, M. Manunta, C. De Luca and R. Lanari, "SBAS-DInSAR Parallel Processing for Deformation Time-Series Computation," IEEE JSTARS, vol. 7, no. 8, pp. 3285-3296, 2014, doi: 10.1109/JSTARS.2014.2322671
=====  =====  ======

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

.. code-block:: sbas-parameter

  false

* As *Processing Mode*, select:

.. code-block:: sbas-parameter
  
  MTA

.. figure:: assets/tuto_sbas_6.png
	:figclass: align-center
        :width: 750px
        :align: center
        
.. note::

  You can leave all the other fields unchanged.

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
