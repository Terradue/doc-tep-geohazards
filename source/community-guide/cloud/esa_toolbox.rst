ESA Cloud Toolbox
=================

Create an ESA Cloud Toolbox
---------------------------

To create your own ESA Cloud Toolbox:

- Access the cloud dashboard (see :ref:`dashboard`)
- Click on |cloud_dahsboard_plus.png| to create a new Virtual Machine
- Set the Virtual Machine name (e.g 'my esa toolbox')
- Select the **ESA Cloud Toolbox** template
- Click on **Create**
- Wait for the VM to be deployed
- Get the <ESA Cloud Toolbox IP>.

.. figure:: ../../includes/cloud_esatoolbox_create.png
        :figclass: align-center


Access an ESA Cloud Toolbox
---------------------------

Prerequisites
^^^^^^^^^^^^^

- You are connected to the GEP Laboratory (see :ref:`laboratory`).

Procedure
^^^^^^^^^

VNC Connection
++++++++++++++

*(Option 1 - using a browser)*

- Access the Cloud Dashboard (see :ref:`dashboard`)
- Click on *details* button of the Virtual Machine corresponding to your Esa Cloud Toolbox 

.. figure:: assets/esa_toolbox_1.png
        :figclass: align-center
        :align: center
        :alt: alternate text

- Click on the *VNC* button, as shown in the following picture:

.. figure:: assets/esa_toolbox_2.png
        :figclass: align-center
        :width: 600px
        :align: center
        :alt: alternate text

.. NOTE::
        You may have to allow your browser to open new pop-ups and allow unsafe script load.

*(Option 2 - using a VNC client)*

- Download and install a VNC client (`UltraVNC <http://www.uvnc.com/downloads/ultravnc.html>` or `RealVNC <https://www.realvnc.com/>` or `TightVNC <http://www.tightvnc.com/>`)

- Open the VNC client and connect to:

.. code-block:: info

  <ESA Cloud Toolbox IP>:5902

Further references: http://wiki.services.eoportal.org/tiki-index.php?page=CloudToolbox+FAQ

User Login
++++++++++

- See the VNC screen: 

.. figure:: assets/esa_toolbox_3.png
        :figclass: align-center
        :width: 600px
        :align: center
        :alt: alternate text

- Enter your username: **pi**
- Enter your password: **piuser2014**
- *(Only for the first connection)* Now to set a new password, re-enter the password: **piuser2014**

.. figure:: assets/password2.png
        :figclass: align-center

|bulb| *Before to perform this step, be sure to see a screen similar to the image below, that is without any other text (e.g. "You are required to change your password immediately (root enforced)")*

- *(Only for the first connection)* And finally enter (twice) your new password:

.. |cloud_dahsboard_plus.png| image:: ../../includes/cloud_dahsboard_plus.png
