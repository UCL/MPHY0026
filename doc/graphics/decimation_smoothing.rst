.. _DecimationAndSmoothing:

Mesh Decimation And Smoothing
=============================

Once a triangle mesh has been created, some post-processing is normally done to
reduce size (decimation), and reduce noise (smoothing).


Mesh Decimation and Smoothing Video
-----------------------------------

An overview of decimation and smoothing can be found in this video:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Dps_UGngAX8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Mesh Decimation
---------------

The aim in mesh-decimation is to remove points without destroying the topology and
general shape of the mesh too much.

In VTK, the `decimation <https://vtk.org/doc/nightly/html/classvtkDecimatePro.html>`_, is based on [Schroeder1992]_.

.. figure:: MeshDecimationIllustration.jpg
  :alt: Illustration of Mesh Decimation in VTK
  :width: 600

  Mesh decimation seeks to remove certain points. See video.


Mesh Smoothing
--------------

In VTK, the `smoothing <https://vtk.org/doc/nightly/html/classvtkSmoothPolyDataFilter.html>`_, is based on a
Laplacian smoothing Operator. `These <http://graphics.stanford.edu/courses/cs468-12-spring/LectureSlides/06_smoothing.pdf>`_ notes are helpful.

.. figure:: MeshSmoothingIllustration.jpg
  :alt: Illustration of Mesh Smoothing in VTK
  :width: 600

  Mesh smoothing is implemented using the Laplacian Operator which can be thought of adding a displacement vector, computed as a weighted offset towards the mean of the neighborhood. See video.


