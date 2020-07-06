.. _SystemExamples:

System Examples
===============

Learning Objectives
-------------------

Upon completion of this section, the student will

* Understand the system topology of several CAS systems


Introduction
------------

In this section, we skim through some specifically chosen papers
to further understand some systems that have been developed
for CAS.

First though, Prof. Terry Peters gives examples from the Robarts Image-Guided Surgery Lab, in Ontario.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/FQEluqyR-SY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Pointer-Based 4 Quadrant View
-----------------------------

The 4-quadrant view with a pointer is the classic implementation of image-guidance, see [Galloway1993]_.

To see this in action, on YouTube we find an example from the Mayfield Brain & Spine channel, using Brainlab systems:


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/_BFTK6LWH5g" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

By the end of Lecture 1, and Workshop 1, we will build our own, very basic prototype!


Classroom Exercise
------------------

In groups of 1,2,3, take a skim through the following papers and identify:

* the clinical need
* the engineering solution
* the component parts
* coordinate systems (if you don't know what that is yet, skip it).

Questions to discuss:

* What do the papers say about system accuracy, and how is accuracy measured?
* What types of images used for guidance?
* How are the images are displayed to the surgeon
* How does the user/surgeon interact with the system?

Gather round and present a summary to each other.

The papers below are chosen to cover a variety of applications
(neuro, abdominal), devices (microscope, laparoscope), intra-operative imaging (video, X-ray, ultrasound).
Feel free to suggest your own papers, and contribute suggestions to this course!

Ultrasound On Video
^^^^^^^^^^^^^^^^^^^

[Kang2014]_: Ultrasound Augmented Reality (AR) system for laparoscopic liver surgery.


Pre-op data In The Operating Microscope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Edwards2000]_: The MAGI system, augmented reality in the operating microscope, for brain surgery.

See also: :ref:`additional_resources:Leica ARVeo with Brainlab`


Pre-op data On Video
^^^^^^^^^^^^^^^^^^^^

[Prevost2019]_: The CASCination system. Similarly, [Thompson2015]_, with the UCL SmartLiver system, for laparoscopic liver surgery.
Here the CASCination paper is better for clinical pictures, but the Thompson paper shows the coordinate systems.


X-ray, CT guidance in the OR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Feuerstein2008]_: TUM X-ray, CT system.


Freehand Ultrasound with MR
^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Hu2016]_: Freehand ultrasound system for prostate biopsy.


.. _`Robarts Image-Guided Surgery Lab`: http://www.robarts.ca/index.php/image-guided-surgery-lab
