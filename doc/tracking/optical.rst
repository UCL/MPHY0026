.. _Optical:

Optical tracking
================

Introduction
------------

Optical tracking involve the use of cameras (usually in a fixed position) to localise markers fixed in a rigid body shape (moving object) that is tracked in real-time. The cameras and tracked markers need to be in line-of-sight.
This system is the most popular so far in surgical interventions mainly due to its accuracy and reliability, however, the required line-of-sight between cameras and markers make this technology not adequate for  interventions where the object of interest is inside the human body (e.g., endoscope, catheter, etc.).

Types of systems
----------------

The main optical tracking systems used in surgery can be divided in to main groups: video tracking and IR-based tracking. The following sections describe these types of optical tracking.

Video tracking systems
^^^^^^^^^^^^^^^^^^^^^^

Video tracking systems track a fiducial marker with a printed pattern on it (e.g., white/black squares) from video images taken from one or multiple calibrated cameras.

(TODO: Picture of markers here)

Infra-red-based tracking systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Infra-red cameras are used as optical markers can be tracked easier due to the elimination of ambient light. There systems can be divided in two types:

* **Active optical trackers**: Markers (usually LEDs) emit infra-reds using different firing sequences that are activated by an electrical current (including wireless). The system has a central unit that detects the markers from each camera and employs triangulation in order to find a 6 DOF position.

* **Passive optical trackers**: Retro-reflective spheres are illuminated and detected by the infra-red cameras. The spheres are attached to a rigid body with a unique geometry for each tracked device.

System components
-----------------

The system components of an optical tracking system are: 

* One or multiple cameras: The camera capture range defines the tracking volume where the markers can move and be tracked
* A system unit which may be comprised of other units (for infra-red-based systems only): The system units performs all the processing of the images captures by the camera and provides the 3D position of the markers.
* Markers: Will be fixed to the tools that need to be tracked. Each tool must have a different marker.
* A computer: Takes the processed tracked data from the system unit in order to provide assistance to the surgical procedure.

The following picture show how the different components are connected.

.. figure:: infrared_tracking.png
  :alt: Main system components of an infra-red optical tracking system
  :width: 600
  
  Main system components of an infra-red optical tracking system

