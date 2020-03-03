.. _Introduction:

Introduction
============

The process to find the geometrical relationship between a two coordinate systems (e.g, tracking system and the tip of a tracked tool) is called calibration. 
These parameters are not known as they cannot be measured directly, therefore we need to find them.
The calibration process provides a rigid (translation and rotation) or affine (scaling, rotation and translation) transformation relating the two coordinate systems, by measuring the relation indireclty. 
A good calibration process will depend on the instruments being tracked, the tracking system chosen and the accuracy needed for a specific clinical application.

Types of calibration
--------------------

Calibration processes can be grouped as follows:

* **Pivot calibration**: Finds the transformation between a tracking system and the tip of a tool.
* **Hand-eye calibration**: Finds the transformation between a tracking system and a camera.
* **Video camera parameters calibration**: Finds the intrinsic camera parameters.

The next sections describe the details of these calibration processes.
