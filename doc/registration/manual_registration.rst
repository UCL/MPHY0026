.. _ManualRegistration:

Manual Registration
====================

Examples
^^^^^^^^

Use a mouse or gesture device to manually rotate/translate/scale a pre-operative CT dataset
so that it aligns with the intra-operative scene, e.g. live video.

* To get a feel for this `try manipulating this model, provided on-line by Kitware <https://kitware.github.io/vtk-js/examples/VolumeContour.html>`_.
* To overlay a 3D liver CT model over a 2D video image, giving an augmented reality feel, follow the :ref:`PythonSetup`, then try:

.. code-block:: language

    python mphy0026_manual_registration.py \
    -b doc/registration/liver_background.png \
    -m doc/registration/liver.vtp \
    -c doc/registration/liver_camera.txt

in the root of the MPHY0026 (i.e. this course) git repo.

Or, see Manual Alignment done with SmartLiver:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/-12OjjU2i9E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Discussion
    - how usable is it?
    - Which is better or worse: Manual alignment, but reliable or Automatic alignment, but only semi-reliable?


Papers
^^^^^^

No algorithm to speak of, so these are examples
of how it's used:

* [Pratt2012]_ : Manually align on iPad, using gestures, for image-guided partial nephrectomy
* [Thompson2013a]_ : Manually align, keyboard controls, for radical prostatectomy


Typical Performance
^^^^^^^^^^^^^^^^^^^

Pros:

* Robust (no algorithm to fail)
* Easy to implement for rigid/scaling
* Easy to validate, on a phantom, and get approved

Cons:

* Not suitable for non-rigid alignment
* Normally inaccurate
* Time consuming for the user
* Highly user dependent
* How to interact with the device? who? is the user sterile?
* Hard to re-register, due to the above mentioned time and user variability for instance

Accuracy:

* Depends on anatomy and user interface, and user
* e.g. 10-20mm is not uncommon with deformable anatomy, maybe < 1-3mm with neuro?
