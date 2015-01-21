User Profile
============

.. figure:: ../includes/user.png
	:align: center
	:width: 30%
	:figclass: img-container-border


Find out how to sign-in using **EO-SSO**, access your **Cloud** account by providing a valid **certificate** and prove your identity, or even link your profile with your **Github** account.

Sign in
-------

Once registered on ESA EO Single Sign On (EOSSO), you can simply sign-in using the username and password provided by ESA and you will be automatically redirected to the platform homepage.

Edit your profile
-----------------

.. figure:: ../includes/user_profile.png
	:figclass: img-border
	:scale: 80%
	
Fill in your profile:

1. Edit information such as first and last names, email, ... (username can not be modified though).
2. Once you are done, just click on **Submit** to save your changes.

*Note*: Direct access to your EO-SSO account is provided by clicking on **EO-SSO account**.

Change your password
--------------------

To change your EO-SSO password:

1. On your profile page, click on **EO-SSO account**.
2. On the EO-SSO account page, click on **Change user password**.
3. Write your old password, and your new password (twice).
4. Click on **Submit**.
5. Your password is updated.

Upload your certificate
-----------------------

.. figure:: ../includes/user_certificate.png
	:figclass: img-border img-max-width
	:scale: 80%

Certificate is the key to access the cloud environment, it is thus very important that you set it correctly in your profile.

No certificate
~~~~~~~~~~~~~~

If you don't have yet any valid certificate:

1. Request a new one to Terradue (clicking *Request certificate* button). 
2. The new certificate, once created, will automatically be added to your profile.

Existing certificate
~~~~~~~~~~~~~~~~~~~~

If you already have a valid certificate and you want to use it:

1. Select a valid **PEM** certificate from your computer by clicking **Select file**.
2. Once the correct file is chosen, click on **Upload file**.
3. Your certificate is automatically added to your profile.

Access the Cloud Dashboard
--------------------------

If you can see the cloud logo |sunstone_logo.png|, congratulations, all is correctly set up.
Just click on it to be redirected to the Cloud Dashboard (powered by OpenNebula).

If you cannot see the cloud logo, something is missing in your profile. Please check:

1. You have a valid certificate stored in your user profile. If not, see `Upload your certificate`_.
2. You have an account created on the Cloud Controller. If not, create one by clicking on **Create**.

From this page, users can check everything is alright to access the Cloud Dashboard.
If not done, the user will be asked to upload a valid certificate, and to create an account on the Cloud Controller.
Once all is good, the Sunstone logo will be displayed and clickable to redirect the user to the Cloud dashboard (powered by OpenNebula).

.. |sunstone_logo.png| image:: ../includes/sunstone_logo-small.png

Link your Github account
------------------------

.. figure:: ../includes/user_github.png
	:figclass: img-border
	:scale: 70%

Link your Github account to your profile will allow you to use Github as Software repository for the developments on your Sandboxes. You can also release and share your code there.

|bulb| *Link your github account is not mandatory but highly recommanded.*

.. |bulb| image:: ../includes/bulb.png

To link your Github account:

1. Fill in your github name and validate by clicking on |user_github_edit.png|.
2. You should add your ssh public key to your github account. If you don't have a Terradue certificate, you will need to add it manually. Finally click on **Add your public key** and accept the request on your Github account.

.. |user_github_edit.png| image:: ../includes/user_github_edit.png
