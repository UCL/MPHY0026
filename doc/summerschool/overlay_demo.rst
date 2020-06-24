.. _SummerSchoolOverlay:

Overlay
=======

Sub-Heading
^^^^^^^^^^^

Overlays can be used in IGT for a number of applications:

* Augmented Reality (AR) - 3D model overlay, showing important anatomical information.
* Provide additional information e.g. text/diagrams.

Overlay can be displayed over a clincal video feed, or through a head mounted display e.g. Microsoft Hololens.

Challenges
^^^^^^^^^^
Where to place the overlay data? Data should be conveniently located, but don't want to obscure the clincian's view.
If doing AR, how is the AR model aligned to the real life view? Manual aligment is simple to implement, but can be difficult to orient properly for complex shapes (See exercise). Techniques for automatic registration are covered later in the course.


Exercise
^^^^^^^^

    python mphy0026_overlay.py

Two cases are presented, a 2D alignment of a circle, and a more realistic example where a liver model needs to be alinged to a background shape.

* Does adjusting the opacity of the model make it easier/harder?
* How does 3D alignment compare to 2D aligment?
