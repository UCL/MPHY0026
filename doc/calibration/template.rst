.. _Template:

Template-based tool calibration
===============================

Template-based tool calibration finds the transformation between a tracked marker/sensor and the tip of a tool (e.g., pointer). 
This method can be seen as an equivalent to pivot calibration.
This process consists in placing the surgical instrument in a tracked template with known geometry, in one or more positions. 
Then the spatial relationship can be found by acquiring one or more sets of tracking data, tracking both objects at the same time.

.. figure:: cascination_template_1.jpg
  :alt: Template-based calibration on the CAScination system.
  :width: 300

  Template-based calibration on the `CAScination <https://www.cascination.com/>`_ system.


.. figure:: medtronic_template_1.jpg
  :alt: Template-based calibration on the Medtronic Bucholz Freehand system.
  :width: 300

  Template-based calibration on the `Medtronic Bucholz Freehand <https://www.medtronic.com/uk-en/index.html>`_ system, position 1.


The following video shows how the calibration in the CAScination system is performed:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/i8akai5SCZk?start=222" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


The following video shows a similar approach for the Claron system:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/2Mj7mgkvEbY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


In all cases, if the divot where the pointer tip is located is known in the coordinate
system of the calibration template, the same pointer tip position can be identified
in the coordinate system of the pointer, just by multiplying the point by the 2 tracking transformation.

Exercise: Write out the maths!

Errors
------
The accuracy of this method mainly depends on how accurately the template is tracked.
Bear in mind that optical tracking accuracy is depth dependent, so further away from the
tracker is worse! Also, particularly for optical trackers, tracking rigid bodies is also
very orientation dependent. If the tracked markers for a tool, lie in a plane, this
should be perpendicular to the tracker. If multiple tracking frames are acquired,
they can also be averaged which may improve the accuracy.
