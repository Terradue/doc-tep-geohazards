SETAP Service
~~~~~~~~~~~~~

.. image:: assets/tuto_setap_icon.png

**Sentinel-1 Extended Timing Annotation Processor (SETAP)**

The Extended Timing Annotation Dataset for Copernicus Sentinel-1 (S1-ETAD)
is a new auxiliary product developed by ESA (with DLR as contractor),
providing users with corrections to improve geometric accuracy of
Sentinel-1 (SM and IW) SLC images to centimetric levels.

The product contains analysis-ready layers for removing the atmospheric path
delays, the solid Earth tidal deformation, and the Sentinel-1 system specific
effects related to the IPF SAR processor (Doppler shift, accurate bi-static
correction and height dependent FM-rate mismatch).

To generate such corrections, the service uses precise information from
different ancillary data sources such as IGS and ECMWF.


.. _data-sources-label:
**EO sources supported**:

* **Sentinel-1 SLC**: standard Sentinel-1 L1A products
* **Sentinel-1 Annotations**: Sentinel-1 L1A products containing only the
  XML annotations.
  The information contained in XML annotation is the only one used by
  the S1-ETAD processor.
  The advantage of using S1-Annotation products is that they have a size
  (in MB) by far smaller than standard ones so they can be downloaded in
  a faster.

  .. TODO: check the note below with @hervé
  .. .. note:: if the requested product is not online you could get an error.
  .. .. seealso:: FAQ below

**Output specifications**

* `Format specification document`_ of the output auxiliary product containing
  corrections layers.

.. _Format specification document: https://sentinels.copernicus.eu/documents/247904/4629150/Sentinel-1-ETAD-Product-Format-Specification.pdf

-----

This tutorial describes how to submit a job for the SATAP service to obtain
one or more S1-ETAD products.

The tutorial is addressed to users already familiar with Geo-hazards thematic
Exploitation Platform (GEP) processing, and gives some hints and recommendation
for the best service usage experience.

The main user actions are the following:

* select the desired data source ("Sentinel-1 SLC" or "Sentinel-1 Annotations")
* select the input SAR SLC data to be processed
* optionally set input parameters for processing (default values shall be
  fine for all use cases)
* obtain S1-ETAD products.


Select the processing
=====================

* Sign-in on the Portal https://geohazards-tep.eu/ (see guidance
  :doc:`user <../community-guide/user>` section)

* Access the Geobrowser: https://geohazards-tep.eu/geobrowser/?id=esa-setap

.. figure:: assets/tuto_setap_0.png
   :figclass: align-center
   :width: 750px
   :align: center

* Open the tab "Processing services" from the right of the map, and then
  select the processing service “SETAP”.

.. figure:: assets/tuto_setap_1.png
   :figclass: align-center
   :width: 750px
   :align: center


Select the files to process
===========================

* Select the data source (see :ref:`data-sources-label`).

.. figure:: assets/tuto_setap_2.png
   :figclass: align-center
   :width: 750px
   :align: center


* Filter and select data for your job as described in the
  :doc:`../community-guide/platform/geobrowser` documentation and in the
  :doc:`Data discovery<../community-guide/data>` section.

* Insert the selected data into the *Product (url) list* field in the
  application panel on the right of the Web UI.
  A single "drag and drop" can be used to insert all data.
  Of course *Product (url) list* can also be edited manually.

.. figure:: assets/tuto_setap_3.png
   :figclass: align-center
   :width: 750px
   :align: center


During the selection the input data for your processing, it have to be taken
into account that the processing itself is data-take based.
Input products (S1 slices) are grouped by the SETAP service according to their
data-take ID.
Each group corresponds to a complete or partial acquisition data-take.
Groups are precessed independently (and concurrently) to generate a single
S1-ETAD product per group.

Please also consider that, currently, the maximum number of products per
job is 35.
To process a larger number of input product it is possible to run multiple
jobs but it is strongly recommended to feed al products belonging to the
same data-take to the same job.

.. rubric:: Example 1

A job is started with 35 S1-SLC input products belonging to the same data-take
(possibly incomplete).

In this case only one S1-ETAD product is generated.


.. rubric:: Example 2

The job is started with 35 S1-SLC inout products belonging to an
interferometric stack (single slice).

In this case each input product belongs to a different data-take and the
service generates 35 S1-ETAD products.


.. rubric:: Example 3

The job is started with 30 S1-SLC inout products belonging to an
interferometric stack covering a wide area.
3 SLC slices are necessary to cover the requested area.

In this case the input products are grouped in 10 different groups and the
service generates 10 S1-ETAD products.


Fill the parameter values
=========================

Once the *Product (url) list* field is filled with the selected data, it is
possible to set remaining parameters.

.. figure:: assets/tuto_setap_4.png
   :figclass: align-center
   :width: 350px
   :align: center

Please note that all the remaining parameters have a default value that
should be perfectly fine for practically all cases.
Nevertheless it is possible to tweak them for very specific purposes.

* **Global TRO data**:
    If set to *true* this parameter specifies that the global ECMWF dataset
    have to be used for troposphere computation.
    By default the value of this parameter is set to *false* to indicate
    that only the relevant region of the global ECMWF dataset covering the
    requested area shall be used for the processing.
    In this case the data download is typically by far faster.
    The computation of the data region covering the requested input products
    is performed automatically by the application.
* **DEM Margin**:
    Tis parameter can be used to tweak the amount of margin to be applied to
    the S1 data footprint when the Copernicus DEM is ingested for the
    processing.
* **Orbit Type**:
    By default the *Orbit type* parameter is set to *AUX_POEORB* meaning that
    orbit with the maximum available accuracy are used for the computation.
    *Precise Orbits* are typically available 20 days after the S1 data
    acquisition.

    It is strongly recommended to not change this setting.

    *Orbit type* parameter can also be set to *AUX_RESORB* that have a
    lower nominal accuracy w.r.t. to *AUX_POEORB*, but are typically available
    1-2 days after the acquisition.

    .. important::

        Support for *Restituted Orbits* (`AUX_RESORB`) is considered
        experimental.


Run the job
===========

* Click on the button "Run Job" at the bottom of the SETAP processor tab,
  and monitor the progress of the running Job:

.. figure:: assets/tuto_setap_5.png
   :figclass: align-center
   :width: 750px
   :align: center

* The Job can take long time to execute depending on the request ad on the
  platform load (typically form 2 to 20 hours).
  When the processing is complete the status is set as "Successful Job"

* Download the S1-ETAD products once the Job is completed.
  Please note that the browsing layer of the S1-ETAD product, consisting in
  a KMZ file, is also published separately, to allow a quicker download.

.. figure:: assets/tuto_setap_6.png
   :figclass: align-center
   :width: 750px
   :align: center


**FAQ**

:Q1:
    Are there limitations in terms of geographic areas, product type,
    acquisition date, maximum number of jobs per user?
:A1:
    Main service limitations are listed below:

    * Geographic limitation: none
    * Temporal limitation:

      - it is not possible to generate S1-ETAD products for dates prior to
        27th of June 2016
      - the generation of S1-ETAD products can happen only 3 weeks after
        the acquisition date of the corresponding SLC product (POE orbits)

    * Product type: the S1-ETAD Service only supports S1-SLC products
      acquired in Stripmap (SM) or Interferometric Wide swath (IW) mode;
      EW is not officially supported at the moment, if you need it please
      contact s1-etad@esa.int
    * (For users of the S1-ETAD Pilot Study) Maximum number of input SLC
      slices per user: 100
      (users needing a larger quota can send their request to s1-etad@esa.int)

      .. TODO: limitations of the DSR end-point (see also above)?


:Q2:
    Do you need KML files for the study regions we are using or is the
    service global?
:A2:
    The service is global. The area of interest for data selection can be
    specified by the user by means of the Web UI (see
    :doc:`Discover data<../community-guide/data>`).
    If the user already have a KML file for its Area Of Interest (AOI),
    it can be uploaded in the Web UI to select the AOI (see the
    "Spatial Filters" section in :doc:`../community-guide/platform/geobrowser`).
:Q3:
    Which periods are you planning to provide ETAD, or will it be done for
    new S1 acquisitions in NRT?
:A3:
    NRT product generation is not supported, also, there is no systematic
    processing on GEP.
    The product generation have to be triggered by the user for any date
    compatible tithe the limitations described in **A1**.
