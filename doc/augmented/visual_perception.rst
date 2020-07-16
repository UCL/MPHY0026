.. _VisualPerception:

Visual Perception
=================

One of the main problems in augmented reality, is that projecting
computer graphics on top of video, or optics is unconvincing for the human
visual system.

Most typically: If merged with video the artificial graphics appear in front of video, even if you are well calibrated
such that the rendering is at the correct depth.

So, what research has there been, in the medical domain?

Relatively little: [Wang2017]_, mentioned [Sielhorst2006]_ and [KerstenOertel2015]_.


This video discusses more:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/aiurkMNGhJM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


At the end of the video, it is mentioned that volume rendering could be used to
give photorealistic effects. Historically this has not been possible in realtime.

However, since 2018, when NVidia released their real-time volume rendering
capability, you can create awesome graphics in real time.

(see `these <https://developer.nvidia.com/rtx/raytracing>`_ pages, especially
the videos at the bottom)

But even if you can do the rendering properly, what does the surgeon expect to see?

We need a collaboration between surgeons, technologists and HCI specialists, not just cool graphics!
So this area is very much work in progress.
