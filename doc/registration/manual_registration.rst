.. _ManualRegistration:

Manual Registration
====================

Examples
^^^^^^^^

Use a mouse or gesture device to manually rotate/translate/scale a pre-operative CT dataset
so that it aligns with the intra-operative scene, e.g. live video.

* To get a feel for this `try manipulating this model, provided on-line by Kitware <https://kitware.github.io/vtk-js/examples/VolumeContour.html>`_.
* To overlay a 3D liver CT model over a 2D video image, giving an augmented reality feel, try:

.. code-block:: language

    python mphy0026_manual_registration.py \
    -b doc/registration/liver_background.png \
    -m doc/registration/liver.vtp \
    -c doc/registration/liver_camera.txt

in the root of the MPHY0026 (i.e. this course) git repo.

* Or see: :ref:`additional_resources:Examples: Manual Alignment, CT to Tracker`


Examples from the literature:

* [Pratt2012]_ : Manually align on iPad, using gestures, for image-guided partial nephrectomy
* [Thompson2013a]_ : Manually align, keyboard controls, for radical prostatectomy


Typical Performance
^^^^^^^^^^^^^^^^^^^

Pros:

* Easy to implement for rigid/scaling
* Robust (no algorithm to fail)
* Easy to validate, and get approved

Cons:

* Hard to implement for non-rigid cases
* Normally inaccurate
* Time consuming
* Highly user dependent
* How to interact with the device? who? is the user sterile?
* Hard to re-register, due to time and user variability for instance

Accuracy:

* Depends on anatomy and user interface, and user
* e.g. 10-20mm is not uncommon
