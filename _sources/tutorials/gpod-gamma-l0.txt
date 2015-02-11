G-POD GAMMA Level0 Service
~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the processing
=====================

* Login to the platform (see :doc:`user <../community-guide/user>` section)

* Select the processing service “GAMMA Level-0 WPS”:

.. figure:: assets/tuto_gamma_1.png
	:figclass: align-center
        :width: 750px
        :align: center
        
The "GAMMA Level-0 WPS" panel is displayed with parameters values to be filled-in.

Fill the parameters
===================

.. NOTE::
        Compress parameters is currently fixed to **NOCMP** value and is thus not visible on the processing service.
        Input data files are not yet available for the process.


Computing Element
-----------------

* Select 

.. code-block:: adore-parameter
  
  CE 01 SL6 UK 

in the *Computing Element* field.

.. figure:: assets/tuto_gamma_2.png
	:figclass: align-center
        :width: 750px
        :align: center

Task Caption
------------

* Type any caption you want, e.g **my_gamma_test** * in the *Task Caption* field.

Bounding Box
------------

* Type
  
.. code-block:: adore-parameter
  
  12.7,41.7,13.3,42
  
in the *Bounding Box* field:


Start Date
----------

* Type
  
.. code-block:: adore-parameter
  
  2008-11-23
  
in the *Start Date* field:

End Date
--------

* Type
  
.. code-block:: adore-parameter
  
  2008-11-24
  
in the *End Date* field:

Priority
--------

* Select 

.. code-block:: adore-parameter
  
  0.25 

in the *Priority* field.

.. figure:: assets/tuto_gamma_3.png
    :figclass: align-center
        :width: 750px
        :align: center

Run the job
===========

* Click on the button Run Job:

.. figure:: assets/tuto_gamma_4.png
	:figclass: align-center
        :width: 750px
        :align: center

* See the Running Job:

.. figure:: assets/tuto_gamma_5.png
	:figclass: align-center
        :width: 750px
        :align: center

* After about 8 minutes, see the Successful Job:

.. figure:: assets/tuto_gamma_6.png
	:figclass: align-center
        :width: 750px
        :align: center

