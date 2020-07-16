.. _VolumeRendering:

Volume Rendering
================

The following diagrams and video illustrate the basic concept of volume rendering.

.. figure:: VolumeRenderingRayCasting.png
  :alt: Illustration of Ray Casting
  :width: 600

  Volume Rendering in medical imaging, is implemented via Ray Casting. Imagine the reverse of a pinhole camera model. For each image pixel, project a ray into space, and evaluate the voxel intensity values along each step through the volume. See video.


.. figure:: VolumeRenderingCompositing.png
  :alt: Illustration of Compositing
  :width: 600

  At each step along the ray, you evaluate a function to compute the value of the resultant pixel. Functions depend on the volume data value, the opacity transfer function and colour transfer functions. See video.


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/QdNW_IUIrow" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

You should now have a fair idea of what the following VTK.js example is doing:

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://kitware.github.io/vtk-js/examples/PiecewiseGaussianWidget/index.html" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

For the above example, the instructions for use are `here <https://kitware.github.io/vtk-js/examples/PiecewiseGaussianWidget.html>`_.


Other types of volume rendering include:

* MIP = Maximum Intensity Projection. For each ray, just extract the maximum value along the ray path.
* Average Intensity Projection. Like MIP, but extract average intensity. Not widely used.
* Minimum Intensity Projection. Like MIP, but extract minimum intensity. Not widely used.
