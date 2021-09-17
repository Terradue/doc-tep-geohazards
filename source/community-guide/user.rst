.. _user-profile:

User Profile
============

This sections provides a detailed description on how to sign-in on GEP and access your user profile.

.. _community-guide-user-sign-in-label:

Sign-in
-------

To sign-in on GEP, you need to have an account created on Terradue Cloud Platform.

	- `I have already an account at Terradue`_
	- `I don't have yet an account at Terradue`_
    
	    - `Create a new account from scratch`_
	    - `Create your account from a trusted Identity Provider`_

I already have an account at Terradue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Access the GEP Community Portal through the following URL: https://geohazards-tep.eu/#!. 

.. figure:: ../includes/user-signin-1.png
	:align: center
	:width: 80%
	:figclass: img-container-border

	Figure 1: The Geohazards TEP portal

2. Click on **Sign-in**, you are automatically redirected to the Terradue signin page.

.. figure:: ../includes/user-signin-2.png
	:align: center
	:width: 80%
	:figclass: img-container-border

	Figure 1: The Terradue signin page

3. Log in using your Terradue credentials or, use your credentials from a trusted Identity Provider (EO-IAM, EPOS, EOSC, google, linkedin, yahoo).

4. You are logged on GEP

5. If not done, you can configure your account.

I don't have yet an account at Terradue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new account from scratch
`````````````````````````````````

1. Access the GEP Community Portal through the following URL: https://geohazards-tep.eu/#!. 

.. figure:: ../includes/user-signin-1.png
	:align: center
	:width: 80%
	:figclass: img-container-border

	Figure 1: The Geohazards TEP portal

2. Click on **Register**, you are automatically redirected to the Terradue platform registration page. 

.. figure:: ../includes/user-signin-3.png
	:align: center
	:width: 80%
	:figclass: img-container-border

	Figure 1: The Geohazards TEP portal

3. Fill-in all required information and click on **Create my account**. An email is sent, asking to confirm your email address.

.. NOTE::
	Password must contain at least 8 characters, with at least one upper case lettre, one lower case letter, one integer and a special character (!, @, ?, ...).

4. Click on the link on the email to validate your account.

5. In a new tab, access again https://geohazards-tep.eu/#!

6. Click on **Sign-in**, you are automatically redirected to the Terradue sign-in page.

.. figure:: ../includes/user-signin-2.png
	:align: center
	:width: 80%
	:figclass: img-container-border

	Figure 1: The Terradue platform signin page

7. Log in using your Terradue credentials.

8. You are logged in on GEP

9. If not done, you can configure your account.

Create your account from a trusted Identity Provider
`````````````````````````````````````````````````````
1. Access the GEP Community Portal through the following URL: https://geohazards-tep.eu/#!. 

.. figure:: ../includes/user-signin-1.png
	:align: center
	:width: 80%
	:figclass: img-container-border

	Figure 1: The Geohazards TEP portal

2. Click on **Sign-in**, you are automatically redirected to the Terradue platform signin page.

.. figure:: ../includes/user-signin-2.png
	:align: center
	:width: 80%
	:figclass: img-container-border

	Figure 1: The Terradue platform signin page

3. Click on the button corresponding to your external Identity Provider (EO-IAM, EPOS, EOSC, google, linkedin, yahoo).
4. Your account is automatically created on Terradue Cloud Platform.
5. You are logged in on GEP
6. If not done, you can configure your account.

Profile pages
-------------

Once logged in, your username will be displayed on the login menu (top right of the screen).

By clicking on your username, you will access your profile page.
The other icons give the following functionalities:

..
   - |user_signin_balance.png| Your current accounting balance (if greater than 0)

- |user_signin_settings.png| Access to administration settings (for users with special privileges)
- |user_signin_contactus.png| Link to contact the Geohazards Tep support team
- |user_signin_documentation.png| Link to the Geohazards Tep documentation
- |user_signin_logout.png| Log out from the portal

.. |user_signin_settings.png| image:: ../includes/user_signin_settings.png
.. |user_signin_documentation.png| image:: ../includes/user_signin_documentation.png
.. |user_signin_balance.png| image:: ../includes/user_signin_balance.png
.. |user_signin_contactus.png| image:: ../includes/user_signin_contactus.png
.. |user_signin_logout.png| image:: ../includes/user_signin_logout.png

Edit your profile
~~~~~~~~~~~~~~~~~

.. figure:: ../includes/user_profile.png
	:figclass: img-border
	:scale: 80%
	
Fill in your profile:

1. Edit information such as firstname and lastname, organization (username and email can not be modified).
2. Once you are done, just click on **Submit** to save your changes.

Data package API key
~~~~~~~~~~~~~~~~~~~~

You can get a private API key associated to your account.
Currently this key can be used only to get access to your data packages without being logged in on the portal:
e.g: https://geohazards-tep.eu/t2api/data/package/search?key=MY_API_KEY

.. figure:: ../includes/user_profile_apikey.png
	:figclass: img-border
	:scale: 80%

Application Scenario
~~~~~~~~~~~~~~~~~~~~

You can submit from here a new candidate application and follow it's status progress (saved draft, submitted for review, ...).
A dedicated Application Scenario form will guide you in the process of defining your application.
Once submitted, the Platform Operations team will follow-up directly on the Portal about your request, in particular, to provide you with a quotation and a guidance for sponsorship when applicable (scientific research purposes).

.. figure:: ../includes/user_profile_appscenario.png
	:figclass: img-border img-max-width
	:scale: 80%

Github account
~~~~~~~~~~~~~~

.. figure:: ../includes/user_github.png
	:figclass: img-border
	:scale: 70%

Linking your Github account to your profile will support you with use of GitHub as your Git repository for software development activities on Terradue Cloud Platform, such as integrating new Processing Services for GEP.

..note:: Link your GitHub account is not mandatory but highly recommended for application developers.

To link your GitHub account:

1. Fill in your GitHub name and validate by clicking on |user_github_edit.png|.
2. You should add a SSH public key to your GitHub account, click on **Add your public key** and finally accept the request on your GitHub account.

.. |user_github_edit.png| image:: ../includes/user_github_edit.png

My granted roles
~~~~~~~~~~~~~~~~

To find out which roles have been assigned to you in your communities, just go to the **My granted roles** tab on your profile page.
The communities for which you are a member are listed here, along with your role in it.

.. figure:: ../includes/user_community.png
	:figclass: img-border
	:scale: 70%

My notebooks
~~~~~~~~~~~~

Direct access to your Jupyter notebooks are provided from the **My notebooks** tab, according to your subscription plan.

Usage
~~~~~

To find out how you are using the platform, just go to the **Usage** tab on your profile page.
You will see what is your level for each type of usage of the platform.


.. figure:: ../includes/user_profile_usage.png
	:figclass: img-border
	:scale: 80%

To find out more precisely the number of data packages you loaded, the number of jobs you created, how many failed or were successful, ... Just go the **Analytics** page from the portal homepage.
You will see:

- how many data collection you loaded
- how many data packages and items you loaded
- how many wps jobs you created and how many failed or succeeded

.. req:: GEP-TS-ICD-010
    :show:

    This section shows that the platform has an analytics web widget.
