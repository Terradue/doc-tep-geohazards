SENTINEL-1 Toolbox Installation
===============================

The SENTINEL-1 Toolbox (S1TBX) consists in a collection of processing tools and data product readers & writers, as well as a display & analysis application, providing a support environment for handling the large archive of data from ESA SAR missions, including SENTINEL-1, ERS-1 & 2 and ENVISAT, as well as third party SAR data from ALOS PALSAR, TerraSAR-X, COSMO-SkyMed and RADARSAT-2. The various processing tools can be ran independently from the command-line, and are also integrated within the graphical user interface. The Toolbox includes notably tools for calibration, speckle filtering, coregistration, orthorectification, mosaicking, data conversion, polarimetry and interferometry.

Installation on a GEP CloudToolbox
-------------------------------

Prerequisites
^^^^^^^^^^^^^

- You have created and accessed a CloudToolbox (see :ref:`esatoolbox`).

Procedure
^^^^^^^^^

- Access the CloudToolbox environment
- Open the web browser and visit the website https://sentinel.esa.int/web/sentinel/toolboxes/sentinel-1
- Download the *Linux 64-bit* version

.. figure:: assets/s1toolbox_1.png
        :figclass: align-center
        :align: center
        :width: 600px
        :alt: alternate text

- Once the download is complete, open a Terminal and type:

.. code-block:: bash

  cd Downloads

.. figure:: assets/s1toolbox_2.png
        :figclass: align-center
        :align: center
        :width: 600px
        :alt: alternate text

- To start the S1TBX installation wizard, type:

.. code-block:: bash

  chmod +x s1tbx_1.1.1_Linux64_installer.sh
  sh ./s1tbx_1.1.1_Linux64_installer.sh

.. figure:: assets/s1toolbox_3.png
        :figclass: align-center
        :align: center
        :width: 600px
        :alt: alternate text

- From the Setup Wizard window, click on the button *Next* :

.. figure:: assets/s1toolbox_4.png
        :figclass: align-center
        :align: center
        :alt: alternate text

- Click on the button *Next* : 

.. figure:: assets/s1toolbox_5.png
        :figclass: align-center
        :align: center
        :alt: alternate text

- Click on the button *Next* :

.. figure:: assets/s1toolbox_6.png
        :figclass: align-center
        :align: center
        :alt: alternate text

- Click on the button *Next* :

.. figure:: assets/s1toolbox_7.png
        :figclass: align-center
        :align: center
        :alt: alternate text

- Click on the button *Next* :

.. figure:: assets/s1toolbox_8.png
        :figclass: align-center
        :align: center
        :alt: alternate text

- Click on the button *Finish* :

.. figure:: assets/s1toolbox_9.png
        :figclass: align-center
        :align: center
        :alt: alternate text

- You have now access to the S1TBX tools and to the  SENTINEL-1 TOOLBOX 1.1.1 GUI:

.. figure:: assets/s1toolbox_10.png
        :figclass: align-center
        :align: center
        :width: 600px
        :alt: alternate text

