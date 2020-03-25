.. _SurfaceVersusVolume:

Surface Versus Volume Rendering
===============================

In computing at least, "rendering" means "drawing", and "visualisation" is the process of
drawing a picture of data, so the terms "rendering" and "visualisation" are fairly interchangeable.

First, lets look at the two main types of rendering:


Surface Rendering
-----------------

In this video, we see:

* Contouring, drawing round objects of interest, labelling pixels, resulting in a segmented region.
* Converting segmented regions into triangle meshes.
* Reducing the numbers of triangles, to ensure rendering is fast enough.
* Rendering such a surface, as a solid surface or as wireframe.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Ai8oLmPrm10" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Volume Rendering
----------------

In this video, we see how volume rendering is different to surface rendering:

* Volume rendering works on voxel data directly.
* There is no explicit segmentation step.
* The value of a pixel in the image is determined by what a ray of light travels through, and functions that map 3D image (e.g. MR/CT) intensity or gradient to opacity and colour.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/7DzXGSoCcpU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Mixed Surface and Volume Rendering
----------------------------------

You can also mix surface rendering and volume rendering:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/m_HJWgqj0yE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
