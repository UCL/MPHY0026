.. _History:

History
=======

Learning Objectives
-------------------

Upon completion of this section, the student will be able to:

* describe landmark events that launched the field of CAS


Discussion
----------

A review paper by Terry Peters and Kevin Cleary gives a good
introduction to the field of Image-guided Interventions [PetersCleary2010]_.

In this section here, we just cover a few key events, before delving more deeply into
a selection of :ref:`SystemExamples` for a more detailed study, of what makes up a CAS system.


Pre X-ray Guidance
------------------

* Before the advent of interventional imaging the only physical way to
determine what was inside the human body was to cut it open and
use your eyes / hands. Thus surgery is both the diagnostic and
theraputic tool.

First X-ray Guidance
--------------------

8th November **1895** - `Röntgen`_ documented the first X-ray experiment. The experiment was first published on 28th Dec 1895 (Wikipedia). The first version that we can actually find, in English, was published on 14th Feb 1896 [Roentgen1896]_.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/e/e3/First_medical_X-ray_by_Wilhelm_R%C3%B6ntgen_of_his_wife_Anna_Bertha_Ludwig%27s_hand_-_18951222.gif
  :alt: First medical X-ray by Wilhelm Röntgen of his wife Anna Bertha Ludwig's hand
  :width: 600

  The first medical X-ray by Wilhelm Röntgen of his wife Anna Bertha Ludwig's hand, Wilhelm Röntgen. [Public domain], from Wikimedia.

11th Jan **1896** - the first clinical use of X-rays by `John Hall-Edwards`_, Birmingham, UK, to remove a needle from a hand (Wikipedia).

7th February **1896** - the first surgical use of X-rays by Professor John Cox, Montreal, Canada, where X-rays were used to remove a bullet from a patients leg [Cox1896]_.


Stereotactic Surgery
--------------------

**1908** - Horsley and Clarke described the stereotactic frame [HorsleyClarke1908]_, defining anatomical coordinates, leading to stereotactic surgery.
"Stereo" - meaning *solid*, and "taxis" meaning *ordered*.


.. figure:: https://s3-eu-west-1.amazonaws.com/smgco-images/images/331/large_1981_1688__0001_.jpg
  :alt: Stereotaxic apparatus used by Sir Victor Horsley and Richard Clarke. Made by Swift and Son, London, c1905
  :width: 600

  Stereotactic apparatus used by Sir Victor Horsley and Richard Clarke. Made by Swift and Son, London, c1905, from sciencemuseumgroup.org.uk, licensed under `CC BY-NC 4.0`_.

This led to other frames, using for example spherical coordinates:

.. figure:: https://s3-eu-west-1.amazonaws.com/smgco-images/images/950/large_1999_0981__0001_.jpg
  :alt: Arc for Leksell Stereotactic System, c1997.
  :width: 600

  Figure Arc for Leksell Stereotactic System, c1997. Frame for Leksell Stereotactic System, c1997. from sciencemuseumgroup.org.uk, licensed under `CC BY-NC 4.0`_.

and with the advent of CT imaging in the 1970's, to frames that could be imaged, to more easily map from
image coordinates to physical coordinates. This means, you can understand where your physical tools are
in relation to pre-operative imaging, or vice-versa.


.. figure:: https://upload.wikimedia.org/wikipedia/en/e/ef/Photograph_of_Stereotactic_Frame_With_3_N-localizers.jpg
  :alt: Stereotactic frame with N-localisers.
  :width: 600

  Stereotactic frame with N-localisers, by Kirigiri, on wikimedia, licensed under `CC BY-SA 3.0`_.


This is an example on YouTube:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/HQojtBKiVfk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Frameless Stereotaxy
--------------------

So, the advent of CT scanning in the 1970s and the modern PC in the 1980s led to the concept of frameless stereotaxy [PetersCleary2010]_,
first in the operating microscope [Roberts1986]_ and then with a mechanical arm for a tracker, with the display using the a 4-quadrant view [Galloway1993]_.

In this course, we will build a tracked pointer, 4 quadrant view for image-guided surgery in :ref:`Workshop1`.

Surgical Planning
-----------------

Pioneered by Terry Peters et al. [Peters1987]_, [Peters1989]_. The aim here was to integrate
multi-modality imaging (MR/CT/DSA) via fiducials visible in each image, and also to provide
a stereoscopic display for better visualisation of DSA.

.. _`John Hall-Edwards`: https://en.wikipedia.org/wiki/John_Hall-Edwards
.. _`Röntgen`: https://en.wikipedia.org/wiki/Wilhelm_R%C3%B6ntgen
.. _`CC BY-NC 4.0`: https://creativecommons.org/licenses/by-nc/4.0/
.. _`CC BY-SA 3.0`: https://creativecommons.org/licenses/by-sa/3.0/
