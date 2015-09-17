.. _user-profile:

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
At the first access, you may be asked to check your inbox in order to confirm your address

.. figure:: ../includes/email_confirmation1.png
	:figclass: img-border
	:scale: 80%

If you never received the confirmation email, you can ask the system to send it again by clicking on the link **send again the confirmation email**:

.. figure:: ../includes/email_confirmation2.png
	:figclass: img-border
	:scale: 80%

After clicked the link received by email, you'll be able to see your profile page of the portal:

.. figure:: ../includes/email_confirmation3.png
	:figclass: img-border
	:scale: 80%


Edit your profile
-----------------

.. figure:: ../includes/user_profile.png
	:figclass: img-border
	:scale: 80%
	
Fill in your profile:

1. Edit information such as first and last names, email, ... (username can not be modified though).
2. Once you are done, just click on **Submit** to save your changes.

.. NOTE::
		Direct access to your EO-SSO account is provided by clicking on *EO-SSO account*.

Change your password
--------------------

To change your EO-SSO password:

1. On your profile page, click on **EO-SSO account**.
2. On the EO-SSO account page, click on **Change user password**.
3. Write your old password, and your new password (twice).
4. Click on **Submit**.
5. Your password is updated.

.. NOTE::
		If your UMSSO password is different from the one recorded in your profile, a message will appear in your profile (see image below).
		*Terradue Support Team* needs to perform manual operations as the email is associated to the certificate and the cloud account.

.. figure:: ../includes/user_profile_email_change.png
	:figclass: img-border
	:scale: 80%

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
2. You will receive an email with a link to download the certificate.
3. The new certificate, once created, will automatically be added to your profile.


Existing certificate
~~~~~~~~~~~~~~~~~~~~

If you already have a valid certificate and you want to use it:

1. Select a valid **PEM** certificate from your computer by clicking **Select file**.
2. Once the correct file is chosen, click on **Upload file**.
3. Your certificate is automatically added to your profile.

Remove your certificate
-----------------------

.. figure:: ../includes/certificate_removal.png
	:figclass: img-border img-max-width
	:scale: 80%

If you need to change your certificate, you need first to remove it.
As it is link to your cloud account, *Terradue Support Team* needs to perform manual operations to remove it correctly.

1. Click on *Remove Certificate*
2. A message appear on the certificate view, confirming the request is under process.
3. Wait until you receive an email from *Terradue Support Team* telling you the certificate has been succesfully removed.
4. You can now upload a new certificate (see `Upload your certificate`_).

Access the Cloud Dashboard
--------------------------

To access the Cloud dashboard, you will need to have a valid certificate stored on the platform, as well as an account on the Cloud Controller.


1. You don't have a valid certificate stored on the platform ? See `Upload your certificate`_.

.. figure:: ../includes/cloud_certificate_missing.png
	:figclass: img-border img-max-width
	:scale: 80%

2. You don't have an account on the Cloud Controller ? Create one by clicking on **Create**.

.. figure:: ../includes/cloud_account_missing.png
	:figclass: img-border img-max-width
	:scale: 80%

3. You can see the cloud logo |sunstone_logo.png| ? Congratulations, all is correctly set up.

.. figure:: ../includes/cloud_dashboard_ok.png
	:figclass: img-border img-max-width
	:scale: 80%

Just click on it to be redirected to the Cloud Dashboard (powered by OpenNebula, see :doc:`Cloud Dashboard <cloud/dashboard>`).

.. |sunstone_logo.png| image:: ../includes/sunstone_logo-small.png

Link your Github account
------------------------

.. figure:: ../includes/user_github.png
	:figclass: img-border
	:scale: 70%

Link your Github account to your profile will allow you to use Github as Software repository for the developments on your Sandboxes. You can also release and share your code there.

..note:: Link your github account is not mandatory but highly recommanded.

To link your Github account:

1. Fill in your github name and validate by clicking on |user_github_edit.png|.
2. You should add your ssh public key to your github account. If you don't have a Terradue certificate, you will need to add it manually. Finally click on **Add your public key** and accept the request on your Github account.

.. |user_github_edit.png| image:: ../includes/user_github_edit.png

See your groups
---------------

To find out to which groups you belong, just go to the **Groups** tab on your profile page.
The groups in which you are a member are listed here.

See your usage
--------------

To find out how you are using the platform, just go to the **Usage** tab on your profile page.
You will see what is your level for each type of usage of the platform.
