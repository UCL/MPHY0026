.. _FidRegistrationTutorial

Fiducial Registration Tutorial
==============================

Introduction
------------

This is the `SciKit-Surgery`_ tutorial on fiducial marker based registration. 
It was developed as a two hour tutorial for online delivery during the 2020 
`Medical Imaging Summer School`_ hosted by UCL, but should be more broadly useable.
The concepts taught are directly applicable to fiducial marker based registration
as applied to image guided interventions, and are more broadly applicable to 
other registration and calibrations where a good understanding of residual errors 
is required. 

The tutorial makes used the Python application `SciKit-SurgeryFRED`_.
The tutorial is divided into four sections:

* Familiarisation with the software and the relevant statistics (45 minutes)
* Analysis of data generated in the first section (45 minutes)
* Playing a game using the software (10 minutes)
* Discussion and writing up results (20 minutes)

Learning Objectives
^^^^^^^^^^^^^^^^^^^

After completing the tutorial students should be able to:

* Explain what is meant by the terms Fiducial Localisation Error (FLE), Target Registration Error (TRE) and Fiducial Registration Error (FRE)
* Be familiar derivation of statistics for the expected value of the TRE and FRE.
* Produce data showing how different statistics may be used to estimate the likely TRE for a single registration.
* Explain why FRE may be used to assess registration accuracy.
* Explain why FRE may not be a useful predictor of TRE.


Assumed Knowledge
^^^^^^^^^^^^^^^^^

`SciKit-SurgeryFRED`_ is Python software, it is assumed that pupils have a working Python installation and are able to install packages. If this tutorial has been installed as part of the `MPHY0026`_ module, then `SciKit-SurgeryFRED`_ should have already been installed. If not you should be able to install `SciKit-SurgeryFRED`_ using:

:: 

    pip install scikit-surgeryfred

and the source code installed with

:: 

    git clone https://github.com/UCL/scikit-surgeryfred


Related Tutorials
^^^^^^^^^^^^^^^^^

This tutorial was designed to replace the point based registration session of the `SciKit-SurgeryBARD`_ tutorial, to enable remote delivery when the students do not have access to a suitable phantom or printer.


Part 1 Introduction to Registration with SciKit-SurgeryFRED
-----------------------------------------------------------

Start scikit-surgeryfred, if you've installed it via pip you should be able to run 

:: 

    sksurgeryfred https://github.com/UCL/scikit-surgeryfred/raw/master/data/brain512.png

or 

:: 

    python -m sksurgeryfred https://github.com/UCL/scikit-surgeryfred/raw/master/data/brain512.png

If you've cloned the repository you should be able to run.

::

    tox
    source .tox/py37/bin/activate
    python sksurgeryfred.py data/brain512.png

The first argument should point to a png image. We've supplied a MRI of a brain, but it other images are possible.

.. figure:: scikit-surgeryfred_0.png
  :width: 100%

  Figure 1: SciKit-SurgeryFRED opens a window with two scenes, at left is the preoperative image (MRI) with a target point marked in red. At right is the intra-operative scene where only the patient outline is visible. We will use fiducial based registration to locate the target point on the intraoperative scene.

You can watch the SciKit-SurgeryFRED video:

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/t_6CH5uroYo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

On staring SciKit-SurgeryFRED you should see two images side by side as in Figure 1. The pre-operative image at
left has a target identified in red. The idea is to locate the target on the intraoperative image at right, where we can only see the patient's outline. Locating the target in the intraoperative image is done here using fiducial marker based registration. Mouse clicking on either image will place a fiducial marker on each image, defining a point correspondence between the two images.

.. figure:: scikit-surgeryfred_1.png
  :width: 100%

  Figure 2: Clicking on either image places a fiducial marker (in green) defining a point correspondence between the images

.. figure:: scikit-surgeryfred_1_zoom.png
  :width: 100%

  Figure 3: SciKit-SurgeryFRED adds a Fiducial Localisation Error to the marker in the intraoperative image. The zoomed in region shows the cross hair where the marker is in the pre-operative image, and the green circle where we have located it. The difference between the circle and cross hair centre is the FLE for this marker.


Point based registration requires at least three points to work. So keep adding marker points. At this point you may want to revisit the literature on point based registration, [Fitzpatrick1998]_, [Fitzpatrick2001]_, and  [Maurer1998]_ and consider where to place the fiducial markers to best effect. 

.. figure:: scikit-surgeryfred_3.png
  :width: 100%

  Figure 4: With 3 or more fiducial markers place, SciKit-SurgeryFRED is able to peform a point-based "Procrustes" registration between the two images. Note that the target is now present in the intraoperative together with a cross hair. Similarly to figure 3, the cross hair represents the actual position of the target, whereas the red circle is the estimated position using point based registration. The difference between the two centres if the Target Registration Error (TRE), in this case 2.18 mm ("Actual TRE").


You can add as many marker points as you like (SciKit-Surgery-FRED currently crashes after around 65 markers are placed) and see how the six measures (defined below) in the text boxes change. Placed markers cannot be deleted, but you can restart the registration with a new target by pressing 'r'. 

What the text boxes mean
^^^^^^^^^^^^^^^^^^^^^^^^

SciKitSurgery-FRED has four text boxes list six metrics, this is what they mean and how they should behave.

The first text box contains:

* "Number of Fids" is the number of fiducial markers placed, which should increase by one each time you click on the image.
* "Expected FLE" is the expected absolute value of the Fiducial Localisation Error. SciKit-SurgeryFRED models the FLE as a two dimensional isotropic normally distributed random variable. Each time a new registration is started (by starting the application or by pressing 'r') the standard deviation of the FLE is randomly selected from a uniform distribution between 0.5 and 5.0. Each time a fiducial is placed, its position is perturbed in two dimensions by this standard deviation. The expected absolute value of an FLE with a given standard deviation is calculated and is shown here.  

The second text box contains the expected values TRE and FRE as derived by [Fitzpatrick1998]_.

* "Expected FRE" is the expected value of the fiducial localisation error. This the expected absolute value of he fiducial registration error as defined in equation 10 of [Fitzpatrick1998]_. FRE is a function of the expected FLE and the number of fiducial markers. FLE should increase slightly as the number of fiducial markers increases.

.. figure:: fre_equation_10.png
  :width: 50%

* "Expected TRE" is the expected value of the target registration error. This the expected absolute value of he target registration error as defined in equation 46 of [Fitzpatrick1998]_. TRE is a function of the FLE and the number and geometry of the fiducial markers. Although it should reduce gradually as more fiducial markers are placed, it can be greatly altered by where you place the markers. Try this many times and see what happens to expected TRE for different marker configurations.

.. figure:: tre_equation_46.png
  :width: 50%



.. _`SciKit-Surgery`: https://github.com/UCL/scikit-surgery/wikis/home
.. _`Medical Imaging Summer School`: https://medicss.cs.ucl.ac.uk/
.. _`SciKit-SurgeryFRED`: https://github.com/UCL/scikit-surgeryfred
.. _`MPHY0026`: https://mphy0026.readthedocs.io/en/latest/
.. _`SciKit-SurgeryBARD`: https://scikit-surgerybard.readthedocs.io/en/latest/02_4_Register_And_Ovelay.html
