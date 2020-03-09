.. _ImagingOverview:

Imaging Overview
================


Introduction
^^^^^^^^^^^^

In this course, we are focusing on CAS/CAI. So, while it is true that
we are using images, this is not a course on the physics of image
acquisition.

We assume you have read:

* [Elson2010]_ - Review of imaging in surgery, pre-op, intra-op, post-op.
* [PetersClearey2010]_ - Includes more examples of what type of imaging devices are used, and where.

In this section, we have a free-form discussion, based on the following material.


Common Modalities
^^^^^^^^^^^^^^^^^

* MR/CT/PET/SPECT - 3D, pre-op. Need registering together. Plan.
* Ultrasound, X-ray (low-dose flouroscopy), video - 2D, intra-op. Registration? Real-time updates.
* Cone-beam CT, Robotic (Siemens Zeego) C-arm, 3D, intra-op.
* Hybrid OR - typicall MR or CT.
* Advantages/Disadvantages of Hybrid OR?


Examples - Intra-operative Ultrasound to improve Liver Ablation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`CASCination's system  <https://www.cascination.com/>`_ enables enhanced tumour location, using intra-operative
ultrasound. In this video, the ultrasound probe is tracked, a volume of data is compounded,
and used to improve the registration to pre-op CT, and enhance overlays.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/XPN8nkUylj8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Also note: usability. The monitors close at hand, and resumably draped with sterile film, to allow quick touchscreen.


Examples - Integrated BK Medical Ultrasound and Brainlab Navigation for Neurosurgery
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example, Dr. Michael Bartos gives a good explanation of integrating intra-op
ultrasound imaging from BK Medical, with their Brainlab navigation system.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/gU2yvMjnxhw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Examples - Vascular Surgery, Dr Tara Mastracci using Cydar Medical
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dr Tara Mastracci at UCL talks about `Cydar Medical <http://cydarmedical.com>`_ for `vascular surgery <https://www.youtube.com/watch?v=vmPTcf8VowE&feature=emb_err_watch_on_yt>`_.


Examples - Siemens Hybrid OR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example gave a good overview of some of the surgeon's perspectives on having
more imaging, in the OR.

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/S5Buqqsytso" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Examples - Leica ARVeo
^^^^^^^^^^^^^^^^^^^^^^

There is increased uses of newer imaging devices like flourescence imaging, and
eventually photo-accoustic imaging. Here we see how such imaging is added
directly into the operating microscope.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/mUTg7G9XwGk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Some Thoughts
^^^^^^^^^^^^^

* You have to understand how a surgeon uses their imaging, BEFORE building a guidance system that is unnecessary.
* Consider the frequency, and reasoning. Its normally a few key points during a long operating.
* A CAS system has to integrate with the workflow, so there are often a lot of imaging parameters that are then hard to tweak on a guidance system.



