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

On staring SciKit-SurgeryFRED you should see two images side by side as in Figure 1. The pre-operative image at
left has a target identified in red. The idea is to locate the target on the intraoperative image at right, where we can only see the patient's outline. Locating the target in the intraoperative image is done here using fiducial marker based registration. Mouse clicking on either image will place a fiducial marker on each image, defining a point correspondence between the two images.

.. figure:: scikit-surgeryfred_1.png
  :width: 100%

  Figure 2: Clicking on either image places a fiducial marker (in green) defining a point correspondence between the images

.. figure:: scikit-surgeryfred_1_zoom.png
  :width: 100%

  Figure 3: SciKit-SurgeryFRED adds a Fiducial Localisation Error to the marker in the intraoperative image. The zoomed in region shows the cross hair where the marker is in the pre-operative image, and the green circle where we have located it. The difference between the circle and cross hair centre is the FLE for this marker.


.. figure:: scikit-surgeryfred_3.png
  :width: 100%

  Figure 4: With 3 or more fiducial markers place, SciKit-SurgeryFRED is able to peform a point-based "Procrustes" registration between the two images. 




.. _`SciKit-Surgery`: https://github.com/UCL/scikit-surgery/wikis/home
.. _`Medical Imaging Summer School`: https://medicss.cs.ucl.ac.uk/
.. _`SciKit-SurgeryFRED`: https://github.com/UCL/scikit-surgeryfred
.. _`MPHY0026`: https://mphy0026.readthedocs.io/en/latest/
.. _`SciKit-SurgeryBARD`: https://scikit-surgerybard.readthedocs.io/en/latest/02_4_Register_And_Ovelay.html
