.. _PointBasedRegistration:

Point-Based Registration
========================

Examples
^^^^^^^^

.. figure:: Matt_CT_Points.png
  :width: 100%
.. figure:: Matt-World-Points.png
  :width: 50%

  Figure 1: (top) At least 3 points are selected in pre-operative data such as MR/CT. (bottom) The same 3 points are measured in physical space, using a coordinate measuring device, such as a tracker.

* :ref:`additional_resources:Examples - Image-Guided Surgery for Brain Tumours`
* [Prevost2019]_: CASCination system uses long pointer, 4 points on liver - see `supplementary material <https://www.journalacs.org/cms/10.1016/j.jamcollsurg.2016.06.392/attachment/a000fb26-217c-481e-a7e6-4b0a2e826b5c/mmc1.mp4>`_ in [Conrad2016]_, namely left/middle hepatic vein drainage, main portcal vein drainage, insertion of fulsiform ligament, insertion of gallbladder dome.


Papers
^^^^^^

Within the research literature, most people reference:

* [Arun1987]_, using SVD
* [Horn1987]_, using quaternions

and [Eggert1998]_ suggests there is not much difference between them.


Fiducial marker types
^^^^^^^^^^^^^^^^^^^^^

Accuracy is determined by the fiducial marker type, and the ability to accurately measure it in the OR.

* Bone implanted screws, detachable heads. Need picture.
* Stick on markers - e.g. `IZI Medical <https://izimed.com/products/multi-modality-markers>`_
* Bite-blocks - e.g. [Edwards2000]_


Typical Performance
^^^^^^^^^^^^^^^^^^^

Pros:

* Easy to implement for rigid
* Robust. Need 3+ points. Algorithm won't randomly fail as such.
* Easy to validate, on a phantom, and get approved
* With a clear protocol, less user dependent than manual

Cons:

* Not suitable for non-rigid alignment
* Need rigid landmarks, so most suitable for neurosurgery, orthopedics
* Surgery is often draped, might be difficult to use markers in practice
* Needs case by case analysis of registration errors, as its very shape dependent

Accuracy:

* Neurosurgery: Approx 1mm, e.g. [Edwards2000]_
* Liver surgery: Time was median 8:50 min. Accuracy (FRE), 14.0mm to 9.2mm, mean 12.8mm [Prevost2019].

