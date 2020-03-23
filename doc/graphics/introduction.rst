.. _Graphics:

Graphics
========

Introduction
------------

In this section, we give a brief overview of some graphics concepts that
are required for image-guided surgery.

Computer Graphics is a big field, worthy of several modules on a computer science course,
and the subject of many a classic text book such as: :ref:`bookFoleyVanDam`.

For this course, once you have identified your imaging modalities,
worked out tracking, calibration, registration and segmentation,
we come to the part of "and now put something on the screen".
In order to do that, we will cover basic concepts, as in reality,
most people in this field are still at that level.

We will cover:

* Surface Rendering
* Mesh Decimation
* Mesh Smoothing
* Volume Rendering
* Texture Mapping


Surface Versus Volume Rendering
-------------------------------

First, to continue the introduction, lets look at the two main types of visualisation:


Surface Rendering
^^^^^^^^^^^^^^^^^

In this video, we see:

* Contouring, drawing round objects of interest, labelling pixels, resulting in a segmented region.
* Converting segmented regions into triangle meshes.
* Reducing the numbers of triangles, to ensure rendering is fast enough.
* Rendering such a surface

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Ai8oLmPrm10" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Volume Rendering
^^^^^^^^^^^^^^^^

In this video, we see how volume visualisation is different.

* Volume visualisation works on voxel data directly
* There is no explicit segmentation step
* The value of a pixel in the image is determined by what a ray of light travels through, and functions that map 3D image (e.g. MR/CT) intensity or gradient to opacity and colour.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/7DzXGSoCcpU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Mixed Surface and Volume Rendering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also mix surface rendering and volume rendering:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/m_HJWgqj0yE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Graphics APIs
-------------

You should be aware that there are many `graphics APIs <https://en.wikipedia.org/wiki/List_of_3D_graphics_libraries>`_.

For someone working in CAS, you need to know there are different levels:

* Low Level: OpenGL, WebGL, Vulkan, Metal
* High Level: VTK, Java3D
* Games Engines: Unity, Unreal


Low Level - OpenGL
^^^^^^^^^^^^^^^^^^

The low level ones, let you explicitly control the graphics card. You
have complete control over every single triangle drawn, or ray cast, but
at the cost of massively increased complexity. Look at `this <https://github.com/MattClarkson/CMakeCatchTemplate/blob/master/Code/GuiApps/QOpenGLDemo/mpOpenGLWidget.cpp>`_ code to draw one triangle!!!


High Level - VTK
^^^^^^^^^^^^^^^^

High level APIs encapsulate the low level detail, and provide a
more easily accessible interface. In addition, they are often wrapped
in a much nicer scripting language (e.g. Python for VTK).

In CAS, lots of systems use VTK, and so do we in these notes.
Recently, `Kitware <https://www.kitware.com/>`_ have provided VTK.js, a Javascript re-write of VTK.
Here we show some `VTK.js examples <https://kitware.github.io/vtk-js/examples/>`_, as they can be demonstrated in the browser!!

(Thank you Kitware!)

The code is fairly similar to the `VTK Python or C++ Examples <https://lorensen.github.io/VTKExamples/site/>`_, and the same principles apply throughout.


VTK Examples
------------

Cone Example
^^^^^^^^^^^^

Demonstrates:

* Fast rendering, browser uses WebGL, and hence hardware acceleration
* In surface rendering, everything is typically composed of triangles, points or lines. More complex shapes made up of lots of triangles.
* OpenGL will render arbitrary polygons, but all polygons can be converted to triangles, and hence the hardware is optimised for triangles, so most people only use triangles.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://kitware.github.io/vtk-js/examples/Cone/index.html" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>


Marching Cubes Example
^^^^^^^^^^^^^^^^^^^^^^

Here is another example. I believe it was originally generated from a CT scan. So, skin has a low value, and bone has a high value.
As the iso-surface value is changed, the Marching Cubes algorithm is re-run, and a new surface is generated.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://kitware.github.io/vtk-js/examples/VolumeContour/index.html" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>


If we look at some `code, <https://kitware.github.io/vtk-js/examples/VolumeContour.html#Source>`_
we see that you don't have to worry about points, and triangles, and array buffers. The VTK provided classes hide the detail.

VTK has a pipeline architecture, you connect things together in a pipeline, then connect your pipeline to a window,
and the system renders the result.


The Marching Cubes Algorithm
----------------------------

The Marching Cubes algorithm is used to create a surface from voxel data.
We have already seen this above in the Surface Rendering example.

Let's take another look.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://kitware.github.io/vtk-js/examples/ImageMarchingCubes/index.html" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

What's going on?

* Set radius to zero.
* Imagine a cube of data in front of the camera. (e.g. 50 x 50 x 50)
* Imagine the values go from zero in the middle to a maximum value (e.g. 100) at the end of the cube
* At some intermediary value (e.g. 50), we want to extract the surface,
* The marching cubes algorithm will determine where to place the triangles to represent the surface.
* More voxels gives higher resolution

Marching cubes [Lorensen1987]_ was published in 1987. The core of the algorithm is explained by the following diagram.

.. figure:: MarchingCubesIllustration.png
  :alt: 3 Cases from The Marching Cubes Algorithm
  :width: 600

  Three cases from the Marching Cubes Algorithm. Originally 15 cases proposed.


and this video provides more explanation.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/NLsdLUbOvCY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Mesh Post-Processing
--------------------

Once a triangle mesh has been created, some post-processing is normally done to
reduce size (decimation), and reduce noise (smoothing). These are briefly
described below and in the accompanying video.


Mesh Decimation
^^^^^^^^^^^^^^^

The aim in mesh-decimation is to remove points without destroying the topology and
general shape of the mesh too much.

In VTK, the `decimation <https://vtk.org/doc/nightly/html/classvtkDecimatePro.html>`_, is based on [Schroeder1992]_.

.. figure:: MeshDecimationIllustration.jpg
  :alt: Illustration of Mesh Decimation in VTK
  :width: 600

  Mesh decimation seeks to remove certain points. See video.


Mesh Smoothing
^^^^^^^^^^^^^^

In VTK, the `smoothing <https://vtk.org/doc/nightly/html/classvtkSmoothPolyDataFilter.html>`_, is based on a
Laplacian smoothing Operator. I (Matt) found `these <http://graphics.stanford.edu/courses/cs468-12-spring/LectureSlides/06_smoothing.pdf>`_ notes helpful.

.. figure:: MeshSmoothingIllustration.jpg
  :alt: Illustration of Mesh Smoothing in VTK
  :width: 600

  Mesh smoothing is implemented using the Laplacian Operator which can be thought of adding a displacement vector, computed as a weighted offset towards the mean of the neighborhood. See video.


Mesh Decimation and Smoothing Video
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

More details describing the above decimation and smoothing diagram can be found in this video:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/NLsdLUbOvCY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
