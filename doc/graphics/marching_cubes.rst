.. _GraphicsMarchingCubes:

The Marching Cubes Algorithm
============================

The Marching Cubes algorithm is used to create a surface from voxel data.
We have already seen this above in the Surface Rendering example.

The Marching cubes [Lorensen1987]_ was published in 1987. The core of the algorithm is explained by the following diagram and video.

.. figure:: MarchingCubesIllustration.png
  :alt: 3 Cases from The Marching Cubes Algorithm
  :width: 600

  Three cases from the Marching Cubes Algorithm. Originally 15 cases proposed.


and this video provides more explanation.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/NLsdLUbOvCY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Here's a simple example, just picking an iso-surface out from a volume:

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://kitware.github.io/vtk-js/examples/ImageMarchingCubes/index.html" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

What's going on?

* Set radius to zero.
* Imagine a cube of data in front of the camera. (e.g. 50 x 50 x 50)
* Imagine the values go from zero in the middle to a maximum value (e.g. 100) at the end of the cube.
* At some intermediary value (e.g. 50), we want to extract the surface.
* The marching cubes algorithm will determine where to place the triangles to represent the surface.
* More voxels gives higher resolution.


Marching Cubes Example
----------------------

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


Marching Cubes Video
--------------------

This video by Sebastian Lague is very helpful:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/M3iI2l0ltbE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
