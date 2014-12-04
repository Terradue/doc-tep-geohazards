Administrator Guide
===================

Role description
----------------

An **administrator** in E-CEO platform will be in charge of administrating one or several challenges.
Challenge **administrators** will use the platform to:

-  set-up environments (`Environments`_ and `Manage Environments`_),
-  define series (`Manage Data Series`_),
-  define evaluation criteria (`Criteria importance weights`_ and `Manage Criteria`_),
-  manage users (`Users`_ and `Manage Users`_),
-  validate participant applications (`Participants applications`_)

Note that **administrator** can also do all actions that **initiator** or **evaluator** can do.

Challenge view
--------------

The challenge view contains all the different pages associated to a challenge. The pages are accessible from a vertical menu bar on the left.
The accessible pages are not the same depending on the role of the challenge.

The list of pages accessible for an **administrator** are:

-  |contestviewmenuhome.png| Challenge description
-  |contestviewmenudatapackage.png| Data packages
-  |contestviewmenuusers.png| Challenge users
-  |contestviewmenuenvironments.png| Environments
-  |contestviewmenucriteria.png| Criteria importance/weights
-  |contestviewmenuapplications.png| Participants applications
-  |contestviewmenumetrics.png| Evaluation metrics
-  |contestviewmenuevaluationresults.png| Evaluation results
-  |contestviewmenuranking.png| Ranking

Global description
^^^^^^^^^^^^^^^^^^
Please refer to :doc:`Initiator Guide <initiator>`.

Data packages
^^^^^^^^^^^^^
Please refer to :doc:`Initiator Guide <initiator>`.

Data package items management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Please refer to :doc:`Initiator Guide <initiator>`.

Users
^^^^^
Please refer to :doc:`Initiator Guide <initiator>`.

Environments
^^^^^^^^^^^^
Please refer to :doc:`Initiator Guide <initiator>`.

Criteria importance weights
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Please refer to :doc:`Evaluator Guide <evaluator>`.

Participants applications
^^^^^^^^^^^^^^^^^^^^^^^^^

Inside the challenge view, the application part contains the information about the applications the administrator needs to validate.

.. image:: includes/sum/contestview_applications_admin.png
	:align: center

The Administrator can then decide to **Validate the application** or **Discard the application** if he juges its not suitable for being evaluated, by clicking on the corresponding button.

Evaluation metrics
^^^^^^^^^^^^^^^^^^
Please refer to :doc:`Evaluator Guide <evaluator>`.

Evaluation results
^^^^^^^^^^^^^^^^^^
Please refer to 
:doc:`Evaluator Guide <evaluator>`.

Ranking
^^^^^^^
Please refer to :doc:`Evaluator Guide <evaluator>`.


Settings
--------

Manage Users
^^^^^^^^^^^^

From the **Settings** |settings.png| from the menu bar, select **Manage User**.

To manage users for a challenge, if not selected, select the tab **Users by Challenges**.

.. image:: includes/sum/user_management.png
	:align: center

Click on **change** to change either the Initiator or the Evaluator of the challenge, and then select the user you want to choose.

Click on **manage** to accept or reject participants for a challenge. From there, you can Accept |accept.png| or Deny |denied.png| a user.

.. image:: includes/sum/participant_management.png
	:align: center

To manage users in general, if not selected, select the tab **All Users**.

From there it is possible to set a user as global Initiator (this user will have rights to create a new challenge).

.. image:: includes/sum/user_management3.png
	:align: center

Manage Data Series
^^^^^^^^^^^^^^^^^^

From the **Settings** |settings.png| from the menu bar, select **Manage Series**. The list of existing series will appear. To create a new one click on **Add Data Series**.
Once all the fields filled, save by clicking **Insert**.

.. image:: includes/sum/series_creation.png
	:align: center

Manage Environments
^^^^^^^^^^^^^^^^^^^

From the **Settings** |settings.png| from the menu bar, select **Manage** **Environments**.

.. image:: includes/sum/manage_environment.png
	:align: center

The Template Settings part allow to select the provider, virtual network and template for the challenge. These settings will be used when the environments are generated.
To create a new environment, click on **Create**.

It is also possible to stop |stopenv.png|, resume |startenv.png| or delete |deleteenv.png| an existing environment.

Manage Criteria
^^^^^^^^^^^^^^^

From the control panel, select **Manage** **Criteria**.

The Administrator can manage the criteria (independently of challenges) from this page by creating new ones |newcriterion.png| or deleting definitively existing ones |newcriterionDescription.png|.
The “Unit/Dimension” field is a list representing the unit of the value of the criterion.

The “Quantification” and “Normalization” fields are both meant to contain formulas. To write a formula, add “$$” in the beginning and in the end of the latex formula. The formula will be displayed on the right part.

The “Quantificationlogic” is the logic used for normalization of the value obtained after quantification. It can be chosen between “Higher is Better” and “Lower is Better”.

The “Actor” field indicates who is calculating the value of the criterion. It could be the system or the evaluator.
Save the new criterion by clickin on **Save Criterion**.
Clicking on **Show info / Modify Criteria** will open the Criteria view.

.. image:: includes/sum/criterion_page.png
	:align: center

.. |settings.png| image:: includes/sum/settings.png
.. |contestviewmenuhome.png| image:: includes/sum/contestview_menu_home.png
.. |contestviewmenudatapackage.png| image:: includes/sum/contestview_menu_datapackage.png
.. |contestviewmenuusers.png| image:: includes/sum/contestview_menu_users.png
.. |contestviewmenuenvironments.png| image:: includes/sum/contestview_menu_environments.png
.. |contestviewmenucriteria.png| image:: includes/sum/contestview_menu_criteria.png
.. |contestviewmenuapplications.png| image:: includes/sum/contestview_menu_applications.png
.. |contestviewmenumetrics.png| image:: includes/sum/contestview_menu_metrics.png
.. |contestviewmenuevaluationresults.png| image:: includes/sum/contestview_menu_evaluationresults.png
.. |contestviewmenuranking.png| image:: includes/sum/contestview_menu_ranking.png
.. |newcriterionDescription.png| image:: includes/sum/new_criterion_Description.png
.. |newcriterion.png| image:: includes/sum/new_criterion.png
.. |accept.png| image:: includes/sum/accept.png
.. |denied.png| image:: includes/sum/denied.png
.. |stopenv.png| image:: includes/sum/stop_env.png
.. |startenv.png| image:: includes/sum/start_env.png
.. |deleteenv.png| image:: includes/sum/delete_env.png
