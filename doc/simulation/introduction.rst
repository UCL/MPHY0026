.. _IntroductionSimulation:

Introduction
============

In this section, we introduce the idea of using simulations to understand the likely
performance of a given Computer Assisted Surgery (CAS) system.

As we have seen on this course, a CAS system has several
components. The end result is something
that is used in a complex environment, by a range of people, and depends on
many of the topics we have learnt:

* What type of images are available? See the :ref:`ImagingOverview` section.
* Is segmentation involved? See the :ref:`SegmentationAndModelling` section.
* What devices are tracked? See the :ref:`TrackingSection` section.
* How are they calibrated? See the :ref:`CalibrationSection` section.
* What is displayed on screen? See the :ref:`Graphics` section.
* How does the user interact? See the :ref:`HCIInANutshell` section.

So, a complete system can take a long time to develop.

Typically, the system design starts with an idea, and progresses through the following stages:

* Algorithm design, software only testing, or lab testing, lab evaluation. [Kang2014]_, [Thompson2015]_, [Hu2016]_.
* Animal testing. [Kang2014]_, [Thompson2015]_
* Human evaluation. [Edwards2000]_, [Prevost2019]_, [Hu2016]_.

and the timeframe for each stage is often measured in years.

As we have covered, at lot of current research is based around the geometry
of a system, and involves research into registration methods and calibration methods.

In this chapter we explore the idea that it would be wise to initially model the geometry of a system
so we understand the relative importance of each component part. For example,
in a liver surgery system ([Thompson2015]_), we have

* video intrinsic calibration
* video extrinsic (stereo) calibration
* tracking
* hand-eye calibration
* registration

In this scenario, which component has the most effect on the performance of the system?
If we had a good understanding of the geometric parameters, we can determine
clear specifications for when a component is 'good enough', and spend time wisely.

From an ethical point of view, performing simulations and lab work would also
save costly animal experiments, and reduce the risk of deploying systems that
are un-trustworthy into patient studies.