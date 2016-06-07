Developer Cloud Sandbox
=======================

The Developer Cloud Sandbox is a Virtual Machine (VM) that provides scientific developers with an Exploitation Platform-as-a-Service (PaaS). It consists of a development environment for processor integration and testing, and a framework for Cloud provisioning.
The Developer Cloud Sandbox PaaS allows you to plug scientific applications written in a variety of languages (e.g. Java, C++, IDL, Python, R), then deploy, automate, manage and scale them in a very modular way. The algorithm integration is performed from within a dedicated Virtual Machine, running initially as a simulation environment (sandbox mode) that can readily scale to production (cluster mode). Accessed from an harmonized Shell environment, support tools also facilitate the data access and workflow management tasks.

The `Getting Started Guide <http://docs.terradue.com/developer-sandbox/start/index.html>`_ will drive you step by step through the use of your Sandbox from access to a Laboratory to the Sandbox remote use.

Create a Developer Cloud Sandbox
--------------------------------

To create your own Developer Cloud Toolbox:

- Access the Cloud Dashboard (see :ref:`dashboard`)
- Click on |plus.png| to create a new Developer Cloud Sandbox
- Type the Developer Cloud Sandbox name
- Select the **Developer Cloud Sandbox** template

.. figure:: assets/sandbox_create.png
	:figclass: align-center
        :width: 600px
        :align: center
        :alt: alternate text

- Click on **Create**
- Wait for the Developer Cloud Sandbox to be deployed

.. figure:: assets/sandbox_deploy.png
	:figclass: align-center
        :width: 600px
        :align: center
        :alt: alternate text

- Annotate the *<sandbox ip>* value:

.. figure:: assets/sandbox_ip.png
	:figclass: align-center
        :align: center
        :alt: alternate text


Access a Developer Cloud Sandbox
--------------------------------

To connect your Developer Cloud Sandbox you need a secure connection with the Terradue's infrastructure. Following this guide you will be able to access your Sandbox through the Secure Shell (SSH) network protocol.

.. WARNING::
  The VNC access for the Developer Cloud Sandbox templates is intended only for administrator usage. The regular users shall use the Secure Shell (SSH) access, as described in this section.

Prerequisites
^^^^^^^^^^^^^

- You have the <sandbox ip> value,
- You are connected to the GEP Laboratory (see :ref:`laboratory`),
- You installed your SSH key pair (see `Generate and install the SSH key pair <http://docs.terradue.com/developer-sandbox/start/laboratory/index.html#generate-and-install-the-ssh-key-pair>`) 

.. _connecting_from_unix_linux_mac:

Connecting from Unix / Linux / Mac
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Open a Terminal,

- Type:

.. code-block:: bash

  ssh <cloud_username>@<sandbox host>

That's all :-)

.. _connecting_from_windows:

Connecting from Windows
^^^^^^^^^^^^^^^^^^^^^^^

- Open a Command Prompt,
- Change directory to the putty unzipped folder:

.. code-block:: bash

  cd \path\to\your\putty\folder
  
- Type:

.. code-block:: bash

  PUTTY.EXE -i id_rsa.ppk <cloud_username>@<sandbox_host>

That's all :-)

.. |plus.png| image:: assets/plus.png
