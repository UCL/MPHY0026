.. _GraphicsAPIs:

Graphics APIs
=============

You should be aware that there are many `graphics APIs <https://en.wikipedia.org/wiki/List_of_3D_graphics_libraries>`_.

For someone working in CAS, you need to know there are different levels:

* Low Level: OpenGL, WebGL, Vulkan, Metal
* High Level: VTK, Java3D
* Games Engines: Unity, Unreal


Low Level - OpenGL
------------------

The low level ones, let you explicitly control the graphics card. You
have complete control over every single triangle drawn, or ray cast, but
at the cost of massively increased complexity. Look at `this <https://github.com/MattClarkson/CMakeCatchTemplate/blob/master/Code/GuiApps/QOpenGLDemo/mpOpenGLWidget.cpp>`_ code to draw one triangle!!!


High Level - VTK
----------------

High level APIs encapsulate the low level detail, and provide a
more easily accessible interface. In addition, they are often wrapped
in a much nicer scripting language (e.g. Python for VTK).

In CAS, lots of research systems use VTK, and so do we in these notes.


VTK Examples
------------

Recently, `Kitware <https://www.kitware.com/>`_ have provided VTK.js, a Javascript re-write of VTK.
Here we show some `VTK.js examples <https://kitware.github.io/vtk-js/examples/>`_, as they can be demonstrated in the browser!!

(Thank you Kitware!)

The code is fairly similar to the `VTK Python or C++ Examples <https://lorensen.github.io/VTKExamples/site/>`_, and the same principles apply throughout.
So, here we can play or experiment with a high-level API (VTK), provided in the web browser via javascript, and
ignore the fact that at the lowest level, VTK.js is using WebGL to render using the graphics card GPU.


Cone Example
------------

This VTK.js example gives you the opportunity to interact and experiment with some common
rendering settings, just to see the immediate effects on a drawing of a simple cone.

It demonstrates:

* Fast rendering, browser uses WebGL, and hence hardware acceleration.
* In surface rendering, everything is typically composed of triangles, points or lines. More complex shapes are made up of lots of triangles.
* OpenGL will render arbitrary polygons, but all polygons can be converted to triangles, and hence the hardware is optimised for triangles, so most people convert all polygons to only triangles.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://kitware.github.io/vtk-js/examples/Cone/index.html" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>
