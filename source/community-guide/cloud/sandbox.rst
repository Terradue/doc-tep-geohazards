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

Prerequisites
^^^^^^^^^^^^^

- You have the <sandbox ip> value,
- You are connected to the GEP Laboratory (see :ref:`laboratory`).

Download the Certificate in PEM format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Go to https://ca.terradue.com/gpodcs/cgi/certdown.cgi?U=name@organization.com (use your registration e-mail instead of name@organization.com),

- Choose as **Certificate Format** the PEM,

  - *(Alternative)* If you are using Windows (see below) or if you don't want type the passphrase each time you want to access the Sandbox, choose as **Certificate Format** the PEM (Unencrypted key), 
  
- Type the certificate passphrase that you chose during the registration, when prompted,

- Store securely the PEM Certificate in your filesystem, especially if you chose the PEM (Unencrypted key) format.

.. _connecting_from_unix_linux_mac:

Connecting from Unix / Linux / Mac
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Open a Terminal,

- Type:

.. code-block:: bash

  chmod 600 <yourcertificate.pem>
  ssh -i <yourcertificate.pem> <umsso name>@<sandbox_host>

- If you chose PEM format when you downloaded the Certificate, provide the passphrase when prompted.

That's all :-)

.. _connecting_from_windows:

Connecting from Windows
^^^^^^^^^^^^^^^^^^^^^^^

Download and install PuTTY
**************************

PuTTY is a well-known freely available SSH client http://www.putty.org/. To download and install it:

- Go to http://the.earth.li/~sgtatham/putty/latest/x86/putty.zip,

- Unzip the downloaded file in a location of your filesystem that you prefer.
  
Generate a Private Key from the PEM Certificate
***********************************************

PuTTY needs a private key file (.ppk). Here the procedure to generate it from a PEM Certificate:

- Open the PEM Certificate **Unencrypted key format** with a text editor (e.g. Notepad), 

- Copy in your clipboard the part:

.. code-block:: bash

  -----BEGIN RSA PRIVATE KEY-----
  MII....
  -----END RSA PRIVATE KEY-----

- Create a new empty file named <yourcertificate>.private, open it with a text editor (e.g. Notepad) and paste the part that you copied in the previous point, 

.. NOTE::
  You should paste also -----BEGIN RSA PRIVATE KEY----- and -----END RSA PRIVATE KEY----- in the file <yourcertificate>.private

- Open a Command Prompt and type:

.. code-block:: bash

  puttygen <yourcertificate>.private
  
- Store securely in your filesystem the private key generated, naming it in <yourcertificate>.ppk .

*(Alternative)*

Use the import function in the puttygen GUI:

- Double-click on the puttygen executable,
  
- Click on the **Import** command from the **Conversions** menu,

- Click on the **Save private key** button,

- Store securely in your filesystem the private key generated, naming it in <yourcertificate>.ppk .

Connect with PuTTY
******************

- Open a Command Prompt and type:

.. code-block:: bash

  putty -i <yourcertificate>.ppk <umsso name>@<sandbox ip>

That's all :-)

.. NOTE::
  The PEM certificate is not used to access the system with PuTTY. Only the generated <yourcertificate>.ppk file is needed.

.. |plus.png| image:: assets/plus.png
