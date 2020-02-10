.. _Components:

System Components
=================

Learning Objectives
-------------------

Upon completion of this section, the student will be able to:

* Recall the main components
* Understand that the system performace is the sum of each part


Introduction
------------

As mentioned in papers like [PetersCleary2010]_, CAS system normally comprises

* Imaging
* Segmentation
* Tracking / Calibration
* Registration
* Visualisation
* User interface

Imaging
-------

To Do: fill, once we have written imaging lecture.

Segmentation
------------

.. figure:: segmentation_example.png
  :width: 50%

  Figure 1: Data from CT scans can be converted to triangle meshes and rendered. This example produced by `Visible Patient <https://www.visiblepatient.com/en/>`_.

In this course we will cover

* Segmentation methods, e.g. manual, automatic.
* Conversion to a mesh, smoothing, decimation.


Tracking / Calibration
----------------------

Registration
------------

To Do: Need a decent picture.

Visualisation
-------------

.. figure:: smart_liver_vis_1.png
  :width: 50%
.. figure:: smart_liver_vis_2.png
  :width: 50%

  Figure 2: Examples of Visualisations from the SmartLiver project. (top) Wireframe and too many meshes is confusing. (bottom) We experimented with depth fogging and outlines.


User Interface
--------------

.. figure:: smart_liver_gui_v1.png
  :width: 50%
.. figure:: smart_liver_gui_v2.png
  :width: 50%

  Figure 3: Examples of User Interfaces from the SmartLiver project. (top) Desktop application was not very suitable for the OR. (bottom) Complexity was reduced over time to improve usability.


A System-Wide Approach
----------------------

So, the field of CAS is very diverse and multi-disciplinary.
To deploy a CAS system to the OR requires an understanding of all the components.

While an individual project, or research may choose to focus on one small component,
there must always be an eye on the bigger picture, to make sure the system is workable in practice.