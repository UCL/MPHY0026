.. _RegistrationIntro:

Registration Intro
==================

Learning Objectives
-------------------

Introduction
------------

Registration is the process of aligning two `Coordinate systems <notebooks/coordinate_systems.html>`_.

Medical Image Computing (MIC)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In medical imaging terms, this is often done to match image-volumes, e.g. MR/CT

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/PDgBxvi1GdQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Computer Assisted Interventions (CAI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In CAS/IGI/CAI terms, the problem also exists in intra-device or inter-device terms:

* **intra-device**: registering 2 poses of a camera in time
* **inter-device**: registering a camera coordinate system to a tracker

For example, aligning pre-operative data (CT/MR) scans to patient (tracker/world) space, to:

* display the physical location of the tip of a tracked pointer in the MR/CT scan
* overlay MR/CT scan data on top of a laparoscopic video feed


Methods
-------

Typically, methods in CAS, are sub-divided (e.g. in :ref:`bookPeters`) into:

* Manual
* Point-based
* Surface-based (also called Shape-based)
* Volume-based
* Calibration-based


Course Requirements
-------------------

It is essential to understand the key methods for CAS,
and also have an understanding of some of the large body of work done
in quantifying the likely error of registration.


A Note On Coordinate Systems and Rotations
------------------------------------------

In 3D space, we typically consider 6 degrees-of-freedom (DOF):

* Translations along x, y, z cartesian axis = 3 DOF
* Rotations about x, y, z cartesian axis = 3 DOF

