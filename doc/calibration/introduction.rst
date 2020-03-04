.. _Introduction:

Introduction
============

As seen in the previous chapter, tracking systems are an important component of CAIs. 
However, the sensors/markers cannot be positioned at the exact position we need to track (e.g., end of an endoscope, camera, etc ...).
Therefore, in most applications, we need to find the geometrical relationship between two coordinate systems (e.g, tracking and the tip of a tracked tool, tracking and a camera, ...). 
This process is called calibration and finds the parameters that are not known because they cannot be measured directly.
The calibration process can provide a rigid (translation and rotation) or affine (scaling, rotation and translation) transformation relating two coordinate systems, by measuring the relation indirectly. 
A good calibration process will depend on the instruments being tracked, the tracking system chosen and the accuracy needed for a specific clinical application.

Types of calibration in surgery
-------------------------------

Calibration processes can be grouped as follows:

* **Pivot calibration**: Finds the transformation between a tracking system and the tip of a tool.
* **Hand-eye calibration**: Finds the transformation between a tracking system and a camera.
* **Intrinsic camera parameters calibration**: Finds the intrinsic camera parameters.

The next sections describe the details of these calibration processes.
