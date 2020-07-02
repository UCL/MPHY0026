.. _SummerSchoolCameraCalibration:

Camera Calibration
==================

Introduction
------------

This is the `SciKit-Surgery`_ tutorial on video camera calibration.
It was developed as a 2 hour tutorial for online delivery during the 2020
`Medical Image Computing Summer School`_ hosted by UCL.
The concepts taught are very relevant to any video camera calibration scenario,
as found in computer assisted surgery, photogrammetry, computer vision and so on.

The tutorial is divided into five sections:

* Installation and familiarisation with the software (20 minutes)
* Understanding what a camera model is (40 minutes, mostly reading)
* Calibrate a webcam (30 minutes)
* Evaluate the accuracy of a calibration (30 minutes)
* Discussion and writing up results (30 minutes)


Learning Objectives
-------------------

After completing the tutorial students should be able to:

* Explain what is meant by camera calibration
* Be able to design a protocol to accurately calibrate a camera
* Be able to list common sources of error that cause poor calibration
* Explain why calibration accuracy depends on depth from the camera


Assumed Knowledge
-----------------

`SciKit-SurgeryBARD`_ is Python software, it is assumed that pupils have a working Python installation and are able to install packages.
If this tutorial has been installed as part of the `MPHY0026`_ module, then `SciKit-SurgeryBARD`_ software should have already been installed.
If not you should be able to install `SciKit-SurgeryBARD`_ using:

::

    pip install scikit-surgerybard

and the source code can be obtained with

::

    git clone https://github.com/UCL/scikit-surgerybard


Related Tutorials
-----------------

This tutorial was designed to replace the video camera calibration session of the `BARD calibration tutorial`_,
to enable remote delivery when the students do not have access to a calibration target or a printer.


What is Camera Calibration?
--------------------------

"Geometric camera calibration", also called "camera resectioning" is the process of
selecting a suitable model that mimics the physical process of image formation,
and then determining the parameters of that model.

The name is often simplified to "camera calibration", but be aware that
people working in photogrammetry use this term to refer to photometric
camera calibration, which is used to map the colour values to standard scales.

For the remainder of this tutorial, we will use the term "camera calibration",
to refer to "geometric camera calibration.

For a simple overview, please read:

  - `Matlab Tutorial`_
  - `OpenCV Tutorial`_

Key take-home points:

  - The most common model, is the `Pinhole Camera Model`_, but others exist.
  - The most common formulation, Zhang's method, models distortion parameters, and intrinsic parameters. It's common because its widely implemented, e.g. MATLAB and OpenCV.
  - Distortion parameters can be used to remove tangential or radial distortion
  - The intrinsic parameters can then be used to map from 3D coordinates in front of the camera, to 2D pixel coordinates.
  - The reason to do all this, is so that the camera can be used to measure objects in real-world units (e.g. millimetres), or measure it's own position relative to other objects in real-world units (e.g. millimetres).

There are many examples on YouTube (search 'Camera Calibration').
However, most use an accurately printed calibration target.

The purpose of this tutorial, is to demonstrate this concept at home.

Calibrate Your Webcam
---------------------

In this section, we will calibrate a webcam. We envisage that most people can use
a laptop camera.

First choose a calibration target:

  - if you have a printer, download a `6mm calibration target` and print it, and attach it to something flat, e.g. old CD case.
  - or use your phone. Search google images for "camera calibration chessboard". Download an image, display it as large as possible on your phone. Measure the size of the squares with a ruler.

Then, check you have the correct parameters:

  - open doc/summerschool/camera_calibration/video_calib_chessboard.json in a text editor
  - Open CV detects 'internal corners', not the outer most ones. So, the grid below is 9 x 6.

.. figure:: https://docs.opencv.org/2.4/_images/fileListImage.jpg
  :alt: OpenCV 9 x 6 grid
  :width: 600

  An `OpenCV calibration grid`_, from opencv.org, which is is BSD licensed, shows a 9 (wide) x 6 (high) grid, counting the internal corners.

  - Edit the config file to specify the "corners" and the "square size in mm" to match your chessboard.

Now, we can run the main calibration program.

If you've cloned the repository you should be able to run.

::

    tox
    source .tox/py36/bin/activate
    bard


The calibration program can be run with the command:

::

    bardVideoCalibration -c doc/summerschool/camera_calibration/video_calib_chessboard.json

The calibration process is best explained via a video:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/AAkuYGBV7GA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Use 'c' to 'capture' an image, and 'q' to 'quit'. If you want to save your data, use the '-s' option
to specify an output folder, and optionally '-p' to specify a filename prefix.


Exercises
---------

Now you can calibrate your camera, you can perform many of these to get
a feel for various problems.

* Calibrate with 5 images, very close. What is the re-projection error?
* Calibrate with 5 images, far away. Is the re-projection error better/worse?
* Dim the lights. Does the software detect the chessboard? If so, is the reprojection error better/worse?
* What if you 'capture' an image, while your hand is moving/wobbling? Too much blur, and the software fails to detect. But what if it does detect points. Are they good points?


How Good Is A Calibration?
--------------------------

The camera calibration process matches 3D chessboard coordinates to 2D image coordinates,
and minimises the sum-of-squares re-projection error. Therefore, the re-projection error
is a poor way to evaluate the quality of your calibration, as the re-projection error is
what was minimised during the calibration. Re-projection error also has the units of pixels.

The bardVideoCalibration software takes subsequent pairs of images and tries to triangulate
the position of the chessboard corners, measuring the error in 3D. The smaller the number
the better. The units are in millimetres, so at least it corresponds to a physically meaningful
measurement of error.

However, once calibrated, the camera should be able to be used as a measuring device.
So, in this section we will try to assess the quality of the calibration, measuring
actual physical movements. In other words, if we move the chessboard by 1mm, does
the camera calibration measure it as a 1mm shift, or something else?

First, do a calibration, saving the data to a specific folder:

::

    bardVideoCalibration -c doc/summerschool/camera_calibration/video_calib_chessboard.json -s some_folder_name

Then, you can evaluate the quality of the registration using:

::

    bardVideoCalibrationChecker -c doc/summerschool/camera_calibration/video_calib_chessboard.json -d some_folder_name

where the '-d' option specifies the directory where you stored your calibration data in the step before.


Again, best seen via a video:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/AAkuYGBV7GA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Exercises
---------

So, given you can calibrate your camera, and assess the accuracy thereof, there are some
exercises for the reader.

  - Task 1
  - Task 2


Caveat: The point of this tutorial is to illustrate the concepts. In practice,
with modern cameras being quite good, you may get surprisingly good results, and not be able
to adequately measure when you have a bad calibration!! Alternatively, the
practicalities of doing this at home might mean, you cannot move the camera
a sufficient distance, or sufficiently accurately, like you could do in the lab.

Your mileage may vary. Good luck.

Further Reading
---------------

Add some references.

.. _`SciKit-Surgery`: https://github.com/UCL/scikit-surgery/wikis/home
.. _`SciKit-SurgeryBARD`: https://github.com/UCL/scikit-surgerybard
.. _`BARD calibration tutorial`: https://scikit-surgerybard.readthedocs.io/en/latest/02_1_Calibrate_Your_Camera.html
.. _`Medical Image Computing Summer School`: https://medicss.cs.ucl.ac.uk/
.. _`MPHY0026`: https://mphy0026.readthedocs.io/en/latest/
.. _`Matlab Tutorial`: https://www.mathworks.com/help/vision/ug/camera-calibration.html
.. _`OpenCV Tutorial`: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html
.. _`Pinhole Camera Model`: https://en.wikipedia.org/wiki/Pinhole_camera_model
.. _`6mm calibration target`: https://github.com/UCL/scikit-surgerybard/blob/master/data/calibrationGrids/calibrationgrid-6mm.pdf
.. _`OpenCV calibration grid`: https://docs.opencv.org/2.4/_images/fileListImage.jpg
.. _`emailing me`: m.clarkson@ucl.ac.uk
