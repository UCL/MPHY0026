.. _SummerSchoolIntro:

Basic Augmented Reality Demo (BARD)
===================================

Introduction
------------

This series of tutorials aims to teach some of the concepts
used in medical Augmented Reality (AR) applications.


The Idea
--------

Augmented Reality (AR) is where additional information is used
to augment the visual display of a scene. In medical terms, this normally
occurs in two guises:

* **Video see through**: The "reality" is represented by a video image from a medical
device such as a laparoscope or endoscope, which naturally displays on a monitor.

.. figure:: https://media.springernature.com/full/springer-static/image/art%3A10.1007%2Fs11548-018-1761-3/MediaObjects/11548_2018_1761_Fig1_HTML.jpg?as=webp
  :alt: SmartLiver overlay.
  :width: 600

  Laparoscopic overlay, overlaying CT data onto laparoscopic video. This example taken from [Thompson2018]_, available `here <https://link.springer.com/article/10.1007/s11548-018-1761-3>`_, licensed under `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0)>`_.

The overlaid information could come from pre-operative MR/CT data as shown above, or it could also be another live image modality.
Take a look at `this example <https://link.springer.com/article/10.1007/s00464-014-3433-x/figures/4>`_
from Xin Kang ... Raj Shekhar and colleagues, from `this article <https://link.springer.com/article/10.1007%2Fs00464-014-3433-x>`_,
where an ultrasound image is overlaid on the video.
In this ultrasound example, the laparoscope and laparoscopic ultrasound are optically tracked.

In another example, Pratt et al. provide a pure vision based system:

.. figure:: https://media.springernature.com/full/springer-static/image/art%3A10.1007%2Fs11548-015-1279-x/MediaObjects/11548_2015_1279_Fig5_HTML.jpg?as=webp
  :alt: Vision based overlay.
  :width: 600

  Pratt et al. provide a vision based overlay, where the video camera itself tracks the position of the ultrasound probe. See `Pratt et al, 2015 <https://link.springer.com/article/10.1007/s11548-015-1279-x>`_.

In the vision system, the video camera provides the means for sampling the real scene, working out the pose
of the ultrasound probe relative to the video camera, and the AR overlay itself.

* **Optical see through**: The "reality" is directly observed via a visor, or semi-silvered mirror, onto which is projected additional information.

The most obvious example right now, is the Microsoft Hololens. See this example from ApoQlar, on the `ApoQlar YouTube channel <https://www.youtube.com/watch?v=JeqxBQERp7Q&feature=youtu.be>`_.

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/JeqxBQERp7Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


While we can't develop such technology in a week, we can explore the general idea!


The Original Lab-Based Demo
---------------------------

Ordinarily, `MedICSS`_ is located at UCL. The original `BARD`_ project
requires a physical phantom such as the `pelvis phantom`_ in our lab at UCL.

.. figure:: https://scikit-surgerybard.readthedocs.io/en/latest/_images/phantom_01.png
  :alt: The pelvis phantom at UCL.
  :width: 600

  Pelvis phantom at UCL.

We also have a CT scan of the phantom. The general idea is to take a webcam,
register the CT coordinates to a reference marker, track the
marker with a webcam and overlay the CT scan on the live video.

.. figure:: https://scikit-surgerybard.readthedocs.io/en/latest/_images/overlay_01.png
  :alt: The overlay of a CT scan ontop of the webcam video.
  :width: 600

  The overlay of the CT scan of the phantom on the live webcam feed, achieved using `BARD`_, taken from a previous summer school.

This demonstrates Augmented (adding the CT data), Reality (represented by webcam video)
as an example of video see through AR.


The New Home-Based Tutorials
----------------------------

However, in 2020, due to the pandemic, we developed a new series of tutorials
with the aim of exploring each component of an AR system in turn.

As we can't actually do an overlay onto a physical object, due to everyone
being at home, the overlay tutorial focuses on implementing something similar to
`Pratt et al, 2015 <https://link.springer.com/article/10.1007/s11548-015-1279-x>`_
where the video camera itself is doing the tracking.

Each tutorial should be fairly stand-alone, and suitable for completing at
home, or for distance learning.

These tutorials are:

.. toctree::
  :numbered:
  :maxdepth: 1

  camera_calibration_demo.rst
  pivot_calibration_demo.rst
  registration_demo.rst
  overlay_demo.rst

Have fun!

.. _`MedICSS`: https://medicss.cs.ucl.ac.uk/
.. _`BARD`: https://scikit-surgerybard.readthedocs.io/en/latest/?badge=latest
.. _`pelvis phantom`: https://scikit-surgerybard.readthedocs.io/en/latest/_images/phantom_01.png