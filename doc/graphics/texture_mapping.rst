.. _TextureMapping:

Texture Mapping
===============

The final technique we will look at is texture mapping.

Texture mapping is a way of assigning an :math:`(t_x, t_y)` value to a vertex,
where the values of :math:`(t_x, t_y)`, which normally range :math:`[0-1]` refer to locations in an image. i.e. a pixel array.
When it comes time to render a polygon, then instead of just painting the polygon a single colour, the texture image is painted on top of the polygon.

This was developed initially to add repeating textures that could be rendered very quickly. Graphics hardware soon had dedicated processors to
do this in real-time, giving much improved visual effects.

See `this page <https://learnopengl.com/Getting-started/Textures>`_ for examples. So rather than have to produce
polygon models and work out how to mathematically define a colour function that looked like wood/metal/grass for example,
you can just take a photo, store the picture as a texture map, and map the coordinates of your triangles into the texture map.
This gave very much enhanced realism, at fast rendering speeds.

By why mention this for medical imaging?

Take a look at this example:

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://kitware.github.io/vtk-js/examples/MultiSliceImageMapper/index.html" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

In this example, there are 3 image planes, axial, sagittal and coronal. How are they drawn on screen?

Each slice is extracted and mapped to a bit of texture memory. Then for each slice, you define 4 points that represent
the location in space of the corners. The graphics subsystem then simply maps the value of the image onto the correct
location in space. In other words, you are rendering 3 squares, where each square is rendered as a texture map.

i.e. you don't paint these pixels 1 by 1.

So, in this way, the location in space can be changed very quickly as the graphics hardware can rotate/translate
the objects using hardware acceleration. If you change the slice then the image data can be remapped onto texture memory very quickly,
and the picture redrawn.


