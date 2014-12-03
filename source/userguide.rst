User Guide
==========

This part describes pages of the portal that are common to all users.

Home page
---------

The home page of the E-CEO portal is as shown in the following figure.
It contains a top bar described in the next section.
On the home page are displayed random contests which may have an interest for the current user.

Menu bar
--------

The top menu bar is always visible and provide shortcuts for the user.

Challenges links
^^^^^^^^^^^^^^^^
The menu bar contains the following links to access challenges:

Join a challenge
	Gives access to description of challenges that are open for participants and thus can be joined (it can be already started challenges).

Upcoming challenges
	Gives access to description of futures challenges that are not yet open for participants and thus cannot be joined.

Past challenges
	Gives access to description and results of past challenges run on the platform.

My challenges
	Gives access to challenges the current user is involved in.

Notifications
^^^^^^^^^^^^^
Notifications can be accessed by clicking |bell.png|
in the top of any page. The following list will appear, with all
notifications associated to the current user, along with the number of
days ago it was created. Notifications are ordered by date, from the
newest to the oldest.

.. image:: includes/sum/notifications.png
	:align: center

Clicking on a notification will redirect the browser to the page
corresponding to the notification. The clicked notification will be
removed from the list and considered as “read”.

Notifications can also be accessed by clicking to the link |rssfeed.png|
. The linked page contains a rss feed with all notifications (and could
be used by any feed reader.

.. image:: includes/sum/notifications_feed.png
	:align: center

Support
^^^^^^^
The support page is accessible from the menu bar, by clicking on
**Support**. It gives the possibility to a user to have access to
the list of existing support tickets or to create a new one (by clicking
on **New issue**). Clicking on the Title of the ticket will
redirect to the redmine support page.

.. image:: includes/sum/html_support.png
	:align: center

During the creation of a new ticket, from the interface you can set the
Subject, the Priority as well as the Description. The Assignee will be
by default the E-CEO support team. The ticket can be updated with more
details directly on the redmine support page.

.. image:: includes/sum/html_support2.png
	:align: center

User information
^^^^^^^^^^^^^^^^

From any page, the user can access some infos related to him by clicking
on its name on the top bar.

.. image:: includes/sum/user_info.png
	:align: center

User profile
~~~~~~~~~~~~

From any page, the user can access its profile by clicking **my profile** from the top bar (user infos).

Here he can update its information such as email, affiliation, country,
redmine API Key (used to access support tickets) or to receive
notifications via emails.

To update the Redmin API key, the user must click on **Modify Account** and then set the new API key (can be found on the redmine
profile of the user).

.. image:: includes/sum/user_profile.png
	:align: center
	
User certificate
~~~~~~~~~~~~~~~~

From any page, the user can access its profile by clicking **my certificate** from the top bar (user infos).

Here he can ask for a new certificate or upload the one he has. The
certificate is the one used to access the Private Environment.

.. image:: includes/sum/certif_upload.png
	:align: center

To update the certificate, the user can browse it by clicking
**Select file** or just drag the .pem file into the upload box.

Challenge view
--------------

The challenge view contains all the different pages associated to a challenge.
The pages are accessible from a vertical menu bar on the left.

The list of pages accessible are (with roles who can access):

-  |contestviewmenuhome.png| Challenge description (all)
-  |contestviewmenudatapackage.png| Data packages (all)
-  |contestviewmenuusers.png| Challenge users (initiator / administrator)
-  |contestviewmenuenvironments.png| Environments (all)
-  |contestviewmenucriteria.png| Criteria importance/weights (participant / evaluator / administrator)
-  |contestviewmenuapplications.png| Participants applications (participant / evaluator / administrator)
-  |contestviewmenumetrics.png| Evaluation metrics (evaluator / administrator)
-  |contestviewmenuevaluationresults.png| Evaluation results (all)
-  |contestviewmenuranking.png| Ranking (all)

The accessible pages are not the same depending on the role of the user in the challenge.
Please refer to :doc:`Administrator Guide <administrator>`, :doc:`Initiator Guide <initiator>`, :doc:`Evaluator Guide <evaluator>` or :doc:`Participant Guide <participant>`.

Error messages
--------------

When an error occurs, a pop-up message will appear explaining what is
the error to the user.

.. |homepage.png| image:: includes/sum/homepage.png
.. |bell.png| image:: includes/sum/bell.png
.. |rssfeed.png| image:: includes/sum/rssfeed.png
.. |contestviewmenuhome.png| image:: includes/sum/contestview_menu_home.png
.. |contestviewmenudatapackage.png| image:: includes/sum/contestview_menu_datapackage.png
.. |contestviewmenuusers.png| image:: includes/sum/contestview_menu_users.png
.. |contestviewmenuenvironments.png| image:: includes/sum/contestview_menu_environments.png
.. |contestviewmenuevaluationresults.png| image:: includes/sum/contestview_menu_evaluationresults.png
.. |contestviewmenuranking.png| image:: includes/sum/contestview_menu_ranking.png
.. |contestviewmenucriteria.png| image:: includes/sum/contestview_menu_criteria.png
.. |contestviewmenuapplications.png| image:: includes/sum/contestview_menu_applications.png
.. |contestviewmenumetrics.png| image:: includes/sum/contestview_menu_metrics.png

