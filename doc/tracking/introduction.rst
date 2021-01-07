.. _IntroductionTracking:

Introduction
============

Tracking systems are fundamental for CAI as they allow us to track the position of a tool or device (e.g., laparoscope, endoscope, needle, ultrasound probe, video camera, ...) relative to the patient anatomy during a surgical procedure in 3D space and is a key enabling technology in CAI.

History
-------

We covered in the :ref:`History` section that stereotactic frames were developed
to establish a coordinate system to work within the brain, which led
to the field of stereotactic neurosurgery. Tracking systems typically refer to a
device to provide spatial coordinates that are dynamically updated.

So, key periods are:

* **1980s**: Mechanical digitizers/trackers become popular due to their use in CAS, especially in neurosurgery.
* **1990s**: Optical trackers are introduced in order to overcome clinical problems of previous tracking systems such as the ability to track multiple devices and sterilisation issues, evolving to very accurate devices. On of the main limitations of optical trackers is the line-of-sight requirement between the tracked markers and the camera. See :numref:`OpticalTrackersAtWEISS`.
* **Late 1990s, early 2000s**: The introduction of electromagnetic trackers allows to track devices without requiring a line-of-sight. See :numref:`EMTrackersAtWEISS`.

Types of tracking
-----------------

The most common tracking systems used in surgery can be grouped as follows:

* **Mechanical digitizers**: Transform a mechanical movement to a digital measurement. These digitizers are widely used in robotics, in order to move robot arms but also in other clinical applications such as prostate interventions (see picture below):

.. figure:: mechanical_digitiser.jpg
  :alt: Example of a mechanic digitizer to hold an ultrasound probe for prostate interventions, with a prostate phantom.
  :width: 300
  
  Example of a mechanical digitizer to hold an ultrasound probe for prostate interventions, with a prostate phantom.

* **Ultrasonic transducers**: Measures the time of an ultrasonic pulse from 3 sources into 3 microphones attached to a rigid body in order to calculate distances [Roberts1986]_.

* **Optical tracking**: Most popular tracking used in surgical interventions. Several cameras track several markers in a fixed geometry. See :ref:`Optical`.

* **Electromagnetic tracking**: Electromagnetically-tracked sensors can be tracked within an electromagnetic field. See :ref:`EM`.

* **Fiber-optic ultrasound**: Used in ultrasound interventions for research mainly. A fiber-optic ultrasound receiver communicates with an external ultrasound probe and allows us to localise needles during ultrasound interventions.

The video below shows an example from MICCAI 2016.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/GutD3Cc6LxA?start=2705" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


* **Accelerometers and gyroscopes**: Measure acceleration and angular velocity to determine the position. Is the same system used in mobile phones. Ultrasound probes from Clarius employ this system to reconstruct 2D ultrasound planes to 3D models.




