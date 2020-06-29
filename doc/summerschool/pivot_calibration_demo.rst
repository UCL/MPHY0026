.. _SummerSchoolPivotCalibration:

Make and Calibrate a Pointer 
============================

Introduction
------------

This is the `SciKit-Surgery`_ tutorial on making a tracked pointer and the 
calibration of the pointer. 
It was developed as a two hour tutorial for online delivery during the 2020
`Medical Imaging Summer School`_ hosted by UCL. Tracked pointers are an essential
tool for image guided interventions, but are useful in a variety of 
applications

The tutorial makes used the Python application `SciKit-SurgeryBARD`_

The tutorial is divided into four sections:

* Introduction to tracked pointers (10 mins)
* Introduction to ArUco markers and assembling your pointer (20 mins)
* Calibration of your pointers (40 mins)
* Estimating calibration and tracking accuracy (30 minutes)
* Discussion and writing up results (20 minutes)

Learning Objectives
^^^^^^^^^^^^^^^^^^^

After completing the tutorial students should be able to:

* Describe how a tracked pointer can be used during image guided surgery.
* Demonstrate the use ArUco marker to track an object using SciKit-SurgeryBARD
* Perform a pivot calibration using SciKit-SurgeryBARD
* Estimate the accuracy of the calibrated tracked pointer.

Assumed Knowledge
^^^^^^^^^^^^^^^^^

`SciKit-SurgeryBARD`_ is Python software, it is assumed that pupils have a working Python installation and are able to install packages. If this tutorial has been installed as part of the `MPHY0026`_ module, then `SciKit-SurgeryBARD`_ should have already been installed. If not you should be able to install `SciKit-SurgeryBARD`_ using:

::

    pip install scikit-surgerybard

and the source code installed with

::

    git clone https://github.com/UCL/scikit-surgerybard


Related Tutorials
^^^^^^^^^^^^^^^^^

This tutorial was designed to replace the make your own pointer session of the `SciKit-SurgeryBARD`_ tutorial, to enable remote delivery when the students do not have access to a suitable phantom or printer. In also incorporates parts of the `Pivot Calibration with RANSAC`_ tutorial from the `MPHY0026`_ module.


Part 1 Introduction to Tracked Pointers
---------------------------------------

Tracked pointers enable the user to locate points and surfaces relative to the tracking system. 
Their main use for image guided surgery is to locate fiducial markers for use in `point based registration`_ or to digitise surfaces for `surface based registration`_. More generally they can be
used to make measurements and localise anatomy. 

Tracked pointers consist of three parts. 

* The tip, this is the bit that makes contact with the patient or fiducial marker. It must enable a unique point to be picked, so is often pointed so the tip is unambiguous. However it may also be spherical, so when inserted into a fiducial marker with a spherical divot the centre of the sphere is uniquely identifiable. For surgical applications the tip should be sterile.
* The tracker marker. This is the part that is tracked by the tracking system, e.g. and electromagnetic coil or the reflective spheres used in optical tracking systems.
* The frame and handle. In general it is not possible to place the tracking markers at the tip, so some sort of frame is needed to rigidly connect them. This frame can be designed also act as a handle for the user.

Have a quick look at some of the videos on the linked (above) registration pages, and observe the types of pointers they use.

Part 2 Introduction to ArUco markers and assembling your pointer
----------------------------------------------------------------

This tutorial is designed to be carried out away from the operating theatre so 
we'll make our own tracked pointer using (hopefully) readily available materials. 

For the tip you'll need something with a point, previously we have used pens, for 
today's demo I found a metal skewer which has the benefit of not leaving pen marks.

For the tracking system we'll use OpenCV's implementation of the `ArUco`_ tracking 
library which requires only a calibrated webcam or mobile phone camera and 
the ability to print markers or show them on a screen. Figure 1 shows the
tags we will use for tracking the pointer. You can print them out an stick them onto
some cardbard, or you can display them on your mobile phone screen using the 
QR tag (Figure 2)

The ArUco tracking library relies on using computer vision to detect the 
corners of uniquely identifiable tags in a single frame of video. 

Sub-Heading
^^^^^^^^^^^

some resources


.. figure:: https://github.com/UCL/scikit-surgerybard/raw/master/data/pointer_withscale.png
  :width: 20%

  Figure 1: The patten of six unique tags we will use for pointer tracking. 

.. figure:: https://github.com/UCL/scikit-surgerybard/raw/master/data/qrtags/pointer_qr.png
  :width: 20%
  
  And heres a qrtag link to, so you can get it easiliy on your phone. 
  https://qrgo.page.link/wGpRi


.. _`SciKit-Surgery`: https://github.com/UCL/scikit-surgery/wikis/home
.. _`Medical Imaging Summer School`: https://medicss.cs.ucl.ac.uk/
.. _`MPHY0026`: https://mphy0026.readthedocs.io/en/latest/
.. _`SciKit-SurgeryBARD`: https://scikit-surgerybard.readthedocs.io/en/latest/02_4_Register_And_Ovelay.html
.. _`Pivot Calibration with RANSAC`: https://mphy0026.readthedocs.io/en/latest/notebooks/RANSAC.html
.. _`point based registration`: https://mphy0026.readthedocs.io/en/latest/registration/point_based_registration.html
.. _`surface based registration`: https://mphy0026.readthedocs.io/en/latest/registration/surface_based_registration.html

.. _`ArUco`: https://docs.opencv.org/trunk/d5/dae/tutorial_aruco_detection.html
