.. _PointBasedRegistration:

Point-Based Registration
========================

Papers
^^^^^^

Within the research literature, most people reference:

* [Arun1987]_, using SVD
* [Horn1987]_, using quaternions

and [Eggert1998]_ suggests there is not much difference between them.


Examples
^^^^^^^^

.. figure:: Matt_CT_Points.png
  :width: 100%
.. figure:: Matt-World-Points.png
  :width: 50%

  Figure 1: (top) At least 3 points are selected in pre-operative data such as MR/CT. (bottom) The same 3 points are measured in physical space, using a coordinate measuring device, such as a tracker.

* :ref:`additional_resources:Examples - Image-Guided Surgery for Brain Tumours`
* [Prevost2019]_: CASCination system uses long pointer, 4 points on liver - see `supplementary material <https://www.journalacs.org/cms/10.1016/j.jamcollsurg.2016.06.392/attachment/a000fb26-217c-481e-a7e6-4b0a2e826b5c/mmc1.mp4>`_ in [Conrad2016]_, namely left/middle hepatic vein drainage, main portcal vein drainage, insertion of fulsiform ligament, insertion of gallbladder dome.


Fiducial marker types
^^^^^^^^^^^^^^^^^^^^^

Accuracy is determined by the fiducial marker type, and the ability to accurately measure it in the OR.

* Bone implanted screws, detachable heads
* Stick on markers
* Bite-blocks


Typical Performance
^^^^^^^^^^^^^^^^^^^

* Neurosurgery:
* Liver surgery: Time was median 8:50 min. Accuracy (FRE), 14.0mm to 9.2mm, mean 12.8mm [Prevost2019].

