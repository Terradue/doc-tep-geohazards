.. _user-profile:

User Profile
============

.. figure:: ../includes/user.png
	:align: center
	:width: 30%
	:figclass: img-container-border


Find out how to sign-in using **EO-SSO**, access your **Cloud** resources or even link your profile with your **Github** account.

Register on ESA EO Users’ Single Sign On
----------------------------------------

1. Please access the GEP Community Portal through the URL provided: https://geohazards-tep.eo.esa.int/#!. 

.. figure:: ../includes/qsm1-f1.png
	:align: center
	:width: 80%
	:figclass: img-container-border

	Figure 1: The Geohazards TEP portal

2. On the top right a register button is displayed, encircled in red. Click on this button to go to the ESA EO Users’ Single Sign On registration page. 

3. Figure 2 shows the ESA EO Users’ Single Sign On registration. Fill in all required information. Click on the question mark behind the field for extra info. Afterwards click on Register to continue. A confirmation as shown in Figure 3 is displayed and an email is sent.

.. figure:: ../includes/qsm1-f2.png
	:align: center
	:width: 80%
	:figclass: img-container-border

	Figure 2: The ESA EO Users' Single Sign On Registration Page

.. NOTE::
	Password must contain at least 8 characters, with at least one upper case lettre, one lower case letter, one integer and a special character (!, @, ?, ...).

.. figure:: ../includes/qsm1-f3.png
	:align: center
	:width: 80%
	:figclass: img-container-border

	Figure 3: Confirmation of Registration at ESA EO Users Single Sign On

4. Open your email and click on the link provided by the EO-SSO administrator team. You will be
directed to a page confirming the activation of your account, as indicated by Figure 5.

.. figure:: ../includes/qsm1-f4.png
	:align: center
	:width: 80%
	:figclass: img-container-border
	
	Figure 4: Email sent by the EO-SSO administrator team

.. figure:: ../includes/qsm1-f5.png
	:align: center
	:width: 80%
	:figclass: img-container-border	
	
	Figure 5: Confirmation of Account Activation


Sign-in
-------

Once registered on ESA EO Single Sign On (EO-SSO), you can simply sign-in using your EO-SSO credentials (username and password), and you will be automatically signed-in and redirected to the Geohazards TEP portal.
At the first access, you may be asked to check your inbox in order to confirm your email address (cf. message banner "Pending activation!").

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

.. figure:: ../includes/user_signin.png
	:figclass: img-border
	:scale: 80%

By clicking on your username, you will access your profile page.
The other icons give the following functionalities:

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
-----------------

.. figure:: ../includes/user_profile.png
	:figclass: img-border
	:scale: 80%
	
Fill in your profile:

1. Edit information such as firstname and lastname, email address, organization (username can not be modified though).
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
    If your EO-SSO email is different from the one recorded in your profile, a message will appear in your profile (see image below).

.. figure:: ../includes/user_profile_email_change.png
	:figclass: img-border

Get your Api key
----------------

You can get a private API key associated to your account.
Currently this key can be used only to get access to your data packages without being logged in on the portal:
e.g: https://geohazards-tep.eo.esa.int/t2api/data/package/search?key=MY_API_KEY

.. figure:: ../includes/user_profile_apikey.png
	:figclass: img-border img-max-width
	:scale: 80%


Link your Github account
------------------------

.. figure:: ../includes/user_github.png
	:figclass: img-border
	:scale: 70%

Linking your Github account to your profile will allow you to use Github as your Software repository for your developments on a Cloud  resource of the Platform, such as a Developer Cloud Sandbox virtual machine. You can also release and share your code on GitHub.

..note:: Link your github account is not mandatory but highly recommanded.

To link your Github account:

1. Fill in your Github name and validate by clicking on |user_github_edit.png|.
2. You should add a SSH public key to your Github account, click on **Add your public key** and finally accept the request on your Github account.

.. |user_github_edit.png| image:: ../includes/user_github_edit.png

See your communities
--------------------

To find out which communities you belong to, just go to the **Communities** tab on your profile page.
The communities for which you are a member are listed here, along with your role in it.

.. figure:: ../includes/user_community.png
	:figclass: img-border
	:scale: 70%

See your usage
--------------

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

See your accountings
--------------------

The accounting panel on your profile gives your current credit balance, as well as the list of all transactions associated to your account:

- credit transactions
- debit transactions reported by wps providers for the wps jobs you created, associated to a deposit

.. figure:: ../includes/user_profile_accounting.png
	:figclass: img-border
	:scale: 80%

.. _deposit:
Deposit
~~~~~~~

A deposit transaction is stored when the user execute a job process using as balance the quotation returned first by the processing service for the selected parameters (it implies that the wps provider implemented the **quotation mode**). Deposit transactions can be *active* or *closed*. An **active deposit** is accounted when calculating your account balance (covering the possible debit transactions associated to the same process). A **closed deposit** is not accounted when calculating your account balance (but does not cover anymore the possible debit transactions associated to the same process). A deposit is automatically set from *active* to *closed* when the job process is failed or when the job is succeeded with at least one transaction recorded from the wps provider.

Terms
~~~~~

- **Credit:** amount credited to the account
- **Accounted Debit (+real cost):** amount debited from the account corresponding to a transaction ; real cost shown if different from debit, but not debited (this may vary with on accounting governance)
- **Not Accounted Debit:** amount corresponding to the records received from the provider for this transaction, but not debited from the account, as the transaction is not completed
- **Active Deposit:** Deposit temporarily debited from the account (until the transaction is completed)
- **Closed Deposit:** Deposit value, not debited anymore, informational only

Transaction policy
~~~~~~~~~~~~~~~~~~

The current policy for a wps job process accounting is that the total amount debited to the user corresponds to the real usage of the wps process and cannot be greather than the estimated deposit.
