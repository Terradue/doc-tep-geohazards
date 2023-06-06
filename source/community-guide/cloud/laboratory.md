(laboratory)=

# Join the GEP Laboratory

A GEP Laboratory is a virtual network on Terradue Cloud Platform, dedicated to the hosting of your Cloud resources.
A GEP laboratory and its services are secured by authenticated VPN access. The following sections will guide you through the procedures related to the VPN Setup.

(laboratory-prerequisites)=

## Prerequisites

- You are registered on the Geohazards Exploitation Platform <https://geohazards-tep.eu/umsso>
- You are registered on Terradue's Portal <https://www.terradue.com/portal/signup>
- You received an e-mail with subject "VPN Setup procedure | Join your Laboratory !".

## Install your OpenVPN Client

Download and install your OpenVPN Client, in order to establish a connection with Terradue's VPN server.

:::{important}
if you have a previously installed VPN client (e.g. Tunnelblick) on your system, such **previously installed client must be disconnected and then be disabled** (we recommend uninstalling it).
:::

- Go to <https://access.terradue.com>
- Type as Username the email used during your registration to the Terradue's Portal,
- Type as Password the passphrase that you chose during the registration,
- Once logged, all the connection setup is automatic, you must only approve the access by the new client.

(run-your-vpn-connection)=

## Run your VPN Connection

- In your desktop tray, click on the "OpenVPN Connect" icon.
- From the dropdown menu, select the entry "Connect to access.terradue.com".
- Provide your username and password to approve the access, if required.
- Check that the "OpenVPN Connect" icon in your desktop tray is now featuring a green symbol.
- That's all :-)

:::{admonition} Congrats
You have now completed your setup for accessing your GEP laboratory.
You shall be able to access your user dashboard here: <http:/>/\<sandbox_ip>/dashboard.
**So, let's try a first** {doc}`Connect to your Sandbox <../sandbox>` **now !**
:::

## Known caveats

### DNS issues

When the OpenVPN client is installed on a Linux/Unix OS, the OpenVPN Server is unable to alter the DNS settings on the client in question.
A typical behaviour in such cases is that you are able to ping your Sandbox through its IPv4 address, but not through the hostname.
To solve this kind of issue, add manually Terradue's DNS server as a new line in your */etc/resolv.conf* file:

```bash
nameserver 10.16.20.14
```

If you are using the NetworkManager tool (e.g. in the GNOME desktop environment), you should instead statically add the nameserver address 10.16.20.14 through the GUI.

### HTTP proxy server

When the *OpenVPN Connect* client is installed behind a corporate HTTP proxy server, the connection fails because the proxy server doesn't allow the VPN traffic. Thus the *OpenVPN Connect* client is not able to automatically download the *.ovpn* configuration file.

Hereafter a procedure to configure your VPN connection in that situation:

- Remove any previous version of the *OpenVPN Connect* client,
- Download and install the latest OpenVPN client from <https://openvpn.net/index.php/open-source/downloads.html>,
- Go to <https://access.terradue.com/?src=login>,
- Type as Username the email used during the registration,
- Type as Password the passphrase that you chose during the registration,
- Download the *client.ovpn* configuration file from the link *"Yourself (user-locked profile)"*,
- Modify the *client.ovpn* as described below:
- Substitute:

```bash
remote access.terradue.com 443 udp
remote access.terradue.com 443 udp
remote access.terradue.com 443 tcp
remote access.terradue.com 443 udp
remote access.terradue.com 443 udp
remote access.terradue.com 443 udp
remote access.terradue.com 443 udp
remote access.terradue.com 443 udp
```

With:

```bash
remote access.terradue.com 443 tcp
http-proxy <proxy_address> <proxy_port>
http-proxy-retry
```

Check with your Network Administrator the values of *\<proxy_address>* *\<proxy_port>*.

- Put the *client.ovpn* configuration file under *\<installation-dir>/config*,
- Start the OpenVPN connection.

## Going further

### How to use the OpenVPN Command Line Interface

If the system you are using has not a Graphical User Interface for OpenVPN, you have to use the OpenVPN's command line.
Also, in some scenarios you need to use the OpenVPN's command line interface, for example in a script to automatically start the VPN connection.
It can also be useful when you want to automatically start the VPN from a startup script.

So you can execute the OpenVPN client through the "openvpn" command by using the prompt (Unix Shell or Windows Prompt).

The CLI parameters are listed and described in the manual page of OpenVPN.
You can check them by typing the command:

```bash
man openvpn
```

from a Unix shell, the OpenVPN's manual page will be displayed.
A great number of parameters are available to directly use in the command line prefixed by two consecutive hyphens (--).
The same parameters (not prefixed by --) can also be specified in the configuration file.

:::{NOTE}
Except for a few cases, it is better to specify the parameters in a configuration file rather than having them in a too long and heavy to read command line.
:::

### How to manually setup OpenVPN on other Platforms

To download the "OpenVPN Connect" client for installation on another computer, you can access installation material and configuration templates from here:

<https://access.terradue.com/?src=connect>

You can establish a VPN connexion with Terradue's OpenVPN server by using the command line.

- Go to <https://access.terradue.com/?src=login>,
- Type as Username the email used during the registration,
- Type as Password the passphrase that you chose during the registration,
- Download the client.ovpn configuration file from the link "Yourself (user-locked profile)",
- Download the cacert.pem from <https://ca.terradue.com/gpodcs/certs/cacert.pem>
- Put the files client.ovpn and cacert.pem in a same directory (suppose /etc/openvpn/).
- Change the current directory to /etc/openvpn/ and exec (with root privileges) the command:

```bash
openvpn --config client.ovpn
```

- You are requested for the Username and the Password,
- If the client is authenticated against the server, the VPN connection is established.

### How to build and install OpenVPN

For the most operating system in which OpenVPN works, binary packages already compiled exist.
Anyway, sometimes, above all for some Linux Distributions, you could need to build OpenVPN by starting with the source code.

- Download the OpenVPN's source code from the site <http://openvpn.net>. Pick the latest stable release that is available (*suppose the release 2.0.9 in the rest of this document*);
- Extract the files which are stored in the zipped archive that you have downloaded by using the tar command in the following manner:

```bash
tar xvfz openvpn-2.0.9.tar.gz
```

- Change the current directory to openvpn-2.0.9 with the command:

```bash
cd openvpn-2.0.9
```

- Check the system and produce the Makefiles by using the following command:

```bash
./configure --prefix=/usr
make
make install
```

If the ./configure procedure claims that the lzo libraries and headers are not found in the system, install the lzo compression software as follows below:

- Download the source package of LZO from the site <http://www.oberhumer.com/> and extract its content with the command:

```bash
tar xvfz lzo-2.02.tar.gz
```

- Change the current directory to lzo-2.02 and install the LZO software with the commands:

```bash
./configure --prefix=/usr
make
make install
```

:::{WARNING}
Because the files will be written below the system directory /usr, the *make install* command must be executed with root privileges.
:::
