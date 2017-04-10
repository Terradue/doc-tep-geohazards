Optical time serie analysis with TIO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The TIO service process a set of correlation maps between different
acquisition dates and produce a time serie analysis based on the
methods described in [Bontemps & Al, 2017][1].

This tutorial will show how to use this service to produce such result
using the geoportal. As an example, we will process the data 
over the Harmalière (France) landslide during summer 2016.


[1] 
"Inversion of deformation fields time-series from optical images, and 
application to the long term kinematics of slow-moving landslides in Peru",
Noélie Bontemps and Pascal Lacroix and Marie-Pierre Doin,
2017

Select the processing
=====================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Select the processing service “TIO”:

.. figure:: assets/tuto_tio_1.png
	:figclass: align-center
        :width: 750px
        :align: center

The "TIO" panel is displayed with parameters values pre-filled with 
reasonnable defaults, but no inputs.

Fill the parameters
===================

References to catalogue entries
-------------------------------

* Select the EO data button (1), click it to display a list of datasets and select **Sentinel-2** (2):

.. figure:: assets/tuto_tio_2.png
	:figclass: align-center
        :width: 750px
        :align: center

* Type **"S2A S2MSI1C INSNOBS"** (with the quotes) in the Search Terms field (1) and then click on the lens icon (2):

.. figure:: assets/tuto_tio_3.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on Show Other Parameters and set the following fields with the specified parameter:

- time:start -> 2016-07-01
- time:end -> 2016-08-14
- geo:box -> 5.655,44.915,5.697,44.946

then click on the button **Search**:

.. figure:: assets/tuto_tio_4.png
	:figclass: align-center
        :width: 750px
        :align: center

* Drag and Drop all the eight results in the *References to catalogue entries* field:

.. figure:: assets/tuto_tio_5.png
	:figclass: align-center
        :width: 750px
        :align: center

* And finish by setting your region of interest using the button that set it from search (1):

.. figure:: assets/tuto_tio_6.png
	:figclass: align-center
        :width: 750px
        :align: center

The region of interest parameter define what subset of the optical products we will
process. This is important that it is a subset of those products, and it will
reduce the requirement in disk space/memory/cpu to process the timeserie.

Run the job
===========

* Click on the button Run Job at the bottom of the right panel and see the Running Job

.. figure:: assets/tuto_tio_7.png
	:figclass: align-center
        :width: 750px
        :align: center

* After a while, see the Successful Job:

.. figure:: assets/tuto_tio_8.png
	:figclass: align-center
        :width: 750px
        :align: center

* Click on the button *Show results on map*, then on the *quicklook_depl_cumule_NS.png* result on the *Results Table* in the bottom left side

* See the result on map:

.. figure:: assets/tuto_tio_9.png
	:figclass: align-center
        :width: 750px
        :align: center


