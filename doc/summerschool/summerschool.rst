.. _SummerSchoolIntro:

Summer School
=============

Introduction
------------

Welcome to a series of tutorials, developed for the
Medical Image Computing Summer School 2020 (`MedICSS`_).


The Idea
--------

Augmented Reality (AR) is where additional information is used
to augment the visual display of a scene. In medical terms, this normally
occurs in two guises:

* Video see through: The "reality" is represented by a video image from a medical device such as a laparoscope or endoscope, which naturally displays on a monitor.

.. figure:: https://media.springernature.com/full/springer-static/image/art%3A10.1007%2Fs11548-018-1761-3/MediaObjects/11548_2018_1761_Fig1_HTML.jpg?as=webp
  :alt: SmartLiver overlay.
  :width: 600

  Laparoscopic overlay, overlaying CT data onto laparoscopic video. This example taken from [Thompson2018]_, available `here <https://link.springer.com/article/10.1007/s11548-018-1761-3>`_, licensed under `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0)>`_.

The overlaid information may not be pre-operative MR/CT data. It could also be another live image modality.
Take a look at `this example <https://link.springer.com/article/10.1007/s00464-014-3433-x/figures/4>`_
from Xin Kang ... Raj Shekhar and colleagues, in `this article <https://link.springer.com/article/10.1007%2Fs00464-014-3433-x>`_.

In the above article, the laparoscope and laparoscopic ultrasound is Electro-Magnetically (EM) tracked.
Pratt et al. provide a pure vision based system:

.. figure:: https://media.springernature.com/full/springer-static/image/art%3A10.1007%2Fs11548-015-1279-x/MediaObjects/11548_2015_1279_Fig5_HTML.jpg?as=webp
  :alt: Vision based overlay.
  :width: 600

  Pratt et al. provide a vision based overlay, where the video camera itself tracks the position of the ultrasound probe. See `Pratt et al, 2015 <https://link.springer.com/article/10.1007/s11548-015-1279-x>`_.

* Optical see through: The "reality" is directly observed via a visor, or semi silvered mirror, onto which is projected additional information.

The most obvious example right now, is the Microsoft Hololens. See this example from ApoQlar, on the `ApoQlar YouTube channel <https://www.youtube.com/watch?v=JeqxBQERp7Q&feature=youtu.be>`_.

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/JeqxBQERp7Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


While we can't develop such technology in a week, we can explore the general idea!


The Basic Augmented Reality Demo
--------------------------------

Ordinarily, `MedICSS`_ is located at UCL and is based around the
Basic Augmented Reality Demo (`BARD`_). The `BARD`_ project demonstrates
augmenting a live video feed, with an overlay from a pre-operative scan.
This is a fairly typical scenario in medical augmented reality (AR).
However, `BARD`_ requires a physical phantom such as the
`pelvis phantom`_ in our lab at UCL.

.. figure:: https://scikit-surgerybard.readthedocs.io/en/latest/_images/phantom_01.png
  :alt: The pelvis phantom at UCL.
  :width: 600

  Pelvis phantom at UCL.

We also have a CT scan of the phantom. Then we take a webcam and
register the CT coordinates to a reference marker, track the
marker with a webcam and overlay the CT scan on the live video.


.. figure:: https://scikit-surgerybard.readthedocs.io/en/latest/_images/overlay_01.png
  :alt: The overlay of a CT scan ontop of the webcam video.
  :width: 600

  The overlay of the CT scan of the phantom on the live webcam feed.

This demonstrates Augmented (adding the CT data), Reality (represented by webcam video)
as an example of video see through AR.

The BARD demo uses:

 * Video Camera Calibration
 * Pointer Calibration (Pivot calibration)
 * Point based registration
 * Overlay


The New Home-Based Tutorials
----------------------------


So, in 2020, we developed a new series of tutorials
with the aim of exploring each component of an image-guided
surgery system in turn.

These tutorials are:

  - :ref:`SummerSchoolCameraCalibration`
  - :ref:`SummerSchoolPivotCalibration`
  - :ref:`FidRegistrationTutorial`
  - :ref:`SummerSchoolOverlay`

As we can't actually do an overlay onto a physical object, the overlay
tutorial focuses on implementing something similar to
`Pratt et al, 2015 <https://link.springer.com/article/10.1007/s11548-015-1279-x>`_
where the video camera itself is doing the tracking.

Each tutorial should be fairly stand-alone, and suitable for completing at
home, or for distance learning.

Have fun!

.. _`MedICSS`: https://medicss.cs.ucl.ac.uk/
.. _`BARD`: https://scikit-surgerybard.readthedocs.io/en/latest/?badge=latest
.. _`pelvis phantom`: https://scikit-surgerybard.readthedocs.io/en/latest/_images/phantom_01.png