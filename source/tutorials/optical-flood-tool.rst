Optical Flood Tool Service
~~~~~~~~~~~~~~~~~~~~~~

Select the processing
=====================

* Sign-in on the Portal https://geohazards-tep.eo.esa.int/ (see guidance :doc:`user <../community-guide/user>` section)

* Access the Geobrowser: https://geohazards-tep.eo.esa.int/geobrowser/

* Open the tab "Processing services" from the right of the map, then select the processing service “Optical flood extraction”.


Select the files to process
===========================

* Click on the *Data Packages* button in the bottom right of the screen, within the Features Basket panel. 
Then select from the list the "Optical-flood-trial-case" data package and click on *load*. 
The selected data package contains the reference to the following input file:

.. code-block:: parameter

    LC82020232016054LGN00
    S2 to be defined

.. figure:: assets/Optical_flood_1.png
	:figclass: align-center
        :width: 750px
        :align: center

Fill the parameter values
=========================
Define values for the "Job title" and the "optical images" fields.

* As *Job title*, type:

.. code-block:: parameter

  Optical flood extraction

* As input *optical images*, drag and drop the selected input file:

.. figure:: assets/tuto_pfasar_2.png
    :figclass: align-center
    :width: 750px
    :align: center


Run the job
===========

* Click on the button "Run Job" at the bottom of the optical flood extraction processor tab, and monitor the progress of the running Job:

.. figure:: assets/tuto_pfasar_4.png
	:figclass: align-center
        :width: 750px
        :align: center

* Wait for the Job completion, then check the status is set as "Successful Job”.

.. figure:: assets/tuto_pfasar_5.png
	:figclass: align-center
        :width: 750px
        :align: center

* Download the optical flood extraction processing results once the Job is completed:

.. figure:: assets/tuto_pfasar_6.png
	:figclass: align-center
        :width: 750px
        :align: center
