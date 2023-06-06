---
substitutions:
  plus.png: |-
    ```{image} assets/plus.png
    ```
---

# Developer Cloud Sandbox

The Developer Cloud Sandbox is a Virtual Machine (VM) that provides scientific developers with an Exploitation Platform-as-a-Service (PaaS). It consists of a development environment for processor integration and testing, and a framework for Cloud provisioning.
The Developer Cloud Sandbox PaaS allows you to plug scientific applications written in a variety of languages (e.g. Java, C++, IDL, Python, R), then deploy, automate, manage and scale them in a very modular way. The algorithm integration is performed from within a dedicated Virtual Machine, running initially as a simulation environment (sandbox mode) that can readily scale to production (cluster mode). Accessed from an harmonized Shell environment, support tools also facilitate the data access and workflow management tasks.

The [Getting Started Guide](http://docs.terradue.com/developer-sandbox/start/index.html) will drive you step by step through the use of your Sandbox from access to a Laboratory to the Sandbox remote use.

## Create a Developer Cloud Sandbox

To create your own Developer Cloud Toolbox:

- Access the Cloud Dashboard (see {ref}`dashboard`)
- Click on {{ plus.png }} to create a new Developer Cloud Sandbox
- Type the Developer Cloud Sandbox name
- Select the **Developer Cloud Sandbox** template

:::{figure} assets/sandbox_create.png
:align: center
:alt: alternate text
:figclass: align-center
:width: 600px
:::

- Click on **Create**
- Wait for the Developer Cloud Sandbox to be deployed

:::{figure} assets/sandbox_deploy.png
:align: center
:alt: alternate text
:figclass: align-center
:width: 600px
:::

- Annotate the *\<sandbox ip>* value:

:::{figure} assets/sandbox_ip.png
:align: center
:alt: alternate text
:figclass: align-center
:::

## Access a Developer Cloud Sandbox

To connect your Developer Cloud Sandbox you need a secure connection with the Terradue's infrastructure. Following this guide you will be able to access your Sandbox through the Secure Shell (SSH) network protocol.

:::{WARNING}
The VNC access to a "Developer Cloud Sandbox" virtual machine is intended only for the administrator usage. Regular users can access via the Secure Shell (SSH) only, as described in this section.
:::

### Prerequisites

- You have the \<sandbox ip> value,
- You are connected to the GEP Laboratory (see {ref}`laboratory`),
- You installed your SSH key pair (see `Generate and install the SSH key pair <http://docs.terradue.com/developer-sandbox/start/laboratory/index.html#generate-and-install-the-ssh-key-pair>`)

(connecting-from-unix-linux-mac)=

### Connecting from Unix / Linux / Mac

- Open a Terminal,
- Type:

```bash
ssh <cloud_username>@<sandbox host>
```

That's all :-)

(connecting-from-windows)=

### Connecting from Windows

- Open a Command Prompt,
- Change directory to the putty unzipped folder:

```bash
cd \path\to\your\putty\folder
```

- Type:

```bash
PUTTY.EXE -i id_rsa.ppk <cloud_username>@<sandbox_host>
```

That's all :-)
