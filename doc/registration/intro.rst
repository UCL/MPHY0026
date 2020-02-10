.. _RegistrationIntro:

Registration Intro
==================

Learning Objectives
-------------------

It is essential to understand the key registration methods for CAS,
and also have an understanding of some of the large body of work done
in quantifying the likely error of registration.

* ToDo


Introduction
------------

Registration is the process of aligning two Coordinate systems. See :ref:`Notebooks`.


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

These are covered in the next sections. Coordinate transformations are covered more in the workshops
and their accompanying :ref:`Notebooks`.


A Note on Coordinate Systems and Rotations
------------------------------------------

In 3D space, we typically consider 6 degrees-of-freedom (DOF):

* Translations along x, y, z cartesian axis = 3 DOF
* Rotations about x, y, z cartesian axis = 3 DOF

So, registration and converting coordinates from one
coordinate system to another require understanding of how these work.

However:

* There are `several rotation formulations`_.
* Euler angles get confusing when you consider `extrinsic or intrinsic`_ rotation.
* Euler angles, Quaternions, Rodrigues (axis-angle) representation (see above links), can be converted between each other, and to a 3x3 rotation matrix.
* Rotation matrices are not commutative
* The preferences around ordering of rotation matrices and especially Euler Angles, is software/community/culture/application specific.
* Note that the underlying graphics system may use a different convention to a higher level software API.
* Assume NOTHING. Everytime you implement these things, start with a very clear definition of what you are meant to be implementing.


A Note on VTK Coordinate Systems
--------------------------------

* Several pieces of software, including `Slicer`_, `MITK`_, `PLUS`_, `NifTK`_, `SNAPPY`_ all use VTK.
* Look in `vtkProp3D <https://gitlab.kitware.com/vtk/vtk/blob/master/Rendering/Core/vtkProp3D.cxx#L163>`_, and at ``SetOrientation()`` which says *"Orientation is specified as X,Y and Z rotations in that order, but they are performed as RotateZ, RotateX, and finally RotateY"*.
* vtkProp3D therefore suggests that VTK uses *"Tait–Bryan angles"*, specifically the z-x-y option, which are therefore **intrinsic** rotations meaning, they move with the object being moved.
* In `vtkTransform <https://gitlab.kitware.com/vtk/vtk/blob/master/Common/Transforms/vtkTransform.h#L92>, there is a method ``RotateWXYZ()`` which sets the rotation as an angle about a world axis. Internally, this uses quaternions and converts the world axis to a homogeneous matrix. This is an **extrinsic** rotation.

This has been implemented in the `SNAPPY`_ platform, specifically:

* This matrix construction has been implemented in `scikit-surgerycore <https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgerycore/blob/master/sksurgerycore/transforms/matrix.py>`_
* The *standard* VTK ordering has been implemented in `scikit-surgeryvtk <https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgeryvtk/blob/master/sksurgeryvtk/utils/matrix_utils.py#L47>`_.


A Note on Homogeneous Coordinate Conventions
--------------------------------------------

As is common (e.g. `euclideanspace.com`_, `brainvoyager`_, `opengl`_) we represent

* rotations as the upper-left 3x3 matrix in a 4x4 homogeneous transformation matrix.
* translation as the right-most 3x1 vector in a 4x4 homogeneous transformation matrix.

Note the comment on the `opengl`_ website: *"This is the single most important
tutorial in the whole set. Be sure to read it at least 8 times"*.

This is not being facetious. It is good advice.

.. _`several rotation formulations`: https://en.wikipedia.org/wiki/Rotation_formalisms_in_three_dimensions
.. _`extrinsic or intrinsic`: https://en.wikipedia.org/wiki/Euler_angles#Extrinsic_rotations
.. _`Tait–Bryan angles`: https://en.wikipedia.org/wiki/Euler_angles#Extrinsic_rotations
.. _`euclideanspace.com`: https://www.euclideanspace.com/maths/geometry/affine/matrix4x4/index.htm
.. _`brainvoyager`: https://www.brainvoyager.com/bv/doc/UsersGuide/CoordsAndTransforms/SpatialTransformationMatrices.html
.. _`opengl`: http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/
.. _`Slicer`: https://www.slicer.org/
.. _`MITK`: http://www.mitk.org
.. _`PLUS`: https://plustoolkit.github.io/
.. _`NifTK`: http://www.niftk.org
.. _`SNAPPY`: https://weisslab.cs.ucl.ac.uk/WEISS/PlatformManagement/SNAPPY