.. _Workshop1PBR:

Point Based Registration
========================

Learning Objectives
^^^^^^^^^^^^^^^^^^^

On completion of this workshop, the student will be able to:

* Appreciate several systems in action, or through demonstrations
* Understand practical issues of layout and setup
* Compute FLE, FRE, Residual Error, TRE


System Demos
^^^^^^^^^^^^

* 10 mins - Overview of SmartTarget system (Rachael Rodell, Ultrasound Lab)
* 10 mins - Overview of Medtronic, point/surface based registration (Jonathan Shapey, Mock OR)
* 10 mins - Overview of SmartLiver (Matt, Mock OR)


Overview
^^^^^^^^

The general principles of the workshop are listed below.

* X mins - Use 4-quadrant viewer (e.g. NiftyIGI, MITK, Slicer), to locate fiducials in CT scan. Measure time to do this. Measure FLE. Compare inter-user variability.
* X mins - Identify a suitable Window/Level for CT image, convert to Min/Max intensity value.
* X mins - Grab pointer locations. Measure FLE of tracker/pointer. Investigate variance with angle (optical tracker), jitter, location in tracking volume etc.
* X mins - Compute Point-Based Registration mapping from Tracker to Image space.
* X mins - Visualise tracked pointer in 4 quadrant view.
* X mins - Collect data for ICP.
* X mins - Run ICP without initialisation - should fail.
* X mins - Run ICP with initialisation - should succeed.
* X mins - Compare matrices for PBR and ICP - should be similar.
* X mins - Compare visualisation for PBR and ICP - which is best? Can you see a difference?
* X mins - Analyse partial surfaces for ICP - can we see how it fails?
* X mins - Report back results

Then more specific instructions are given for

* :ref:`Workshop1Lego` using Lego.
* :ref:`Workshop1Pelvis`, using a UCL pelvis phantom.
* :ref:`Workshop1Head`, using a UCL head phantom.

The main reason for providing 3 setups is to reduce waiting time.
The workshop can also be repeated for each setup, and compared between groups.

Please report back the timings, so we can update the instructions above.
