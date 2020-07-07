.. _CameraCalibration:

Intrinsic camera parameters calibration
=======================================

In order to map the camera coordinates to pixel coordinates (to map virtual objects in the real world), we need to find the intrinsic camera parameters.
The following image shows a representation of the elements involved in a camera calibration.

.. figure:: intrinsic_extrinsic.png
  :alt: Intrinsic camera parameters calibration
  :width: 600
  
  Intrinsic camera parameters calibration

Intrinsic parameters include: 

- Scale factor (often equal to 1)
- Focal length (distance between the centre of projection an the image plane)
- principal point (assume pixel 0,0 to be at the centre of the image)
- Skew (when the principal point is not exactly at the centre of the image plane)
- Geometric distortion (due to the lens).

Assuming the following pinhole camera model:

.. figure:: pinhole_model.png
  :alt: Pinhole model
  :width: 600
  
  Pinhole model

To map a 2D point *(u,v)* to a 3D point *(X,Y,Z)* the following equation needs to be solved:

.. figure:: camera_eq1.png

Where *s* is the scaling factor, *[R t]* the extrinsic camera parameters (*R* the rotation and *t* the translation of the camera to the world frame) and *K* corresponds to the intrinsic camera parameters, and is defined as follows:

.. figure:: camera_eq2.png

Where *f* is the focal length, *m* the scaling factor in *x* and *y* (usually 1) and *(u,v)* the principal point.

The general idea to solve this equation is to take several images of a particular pattern (e.g., chessboard) from different positions and extract features from the images (e.g., corners or dots).
Then, the equation can be solved in order to find the camera parameters.

`Behnam Asadi`_ provides a couple of good videos explaining how to find the intrinsic camera parameters (until min. 16.36):

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/oFZQykvEw14" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

and also a clear explanation on Zhang's method [Zhang2000]_, which is the most widely used:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hxbQ-F8u08U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Calibration Exercise
--------------------

As part of our `Medical Image Computing Summer School`_ we wrote a new tutorial
where you can calibrate your laptop webcam, using your mobile phone, perfect for remote learning,
or completing this part at home!

Follow this link: :ref:`SummerSchoolCameraCalibration`.


.. _`Behnam Asadi`: https://www.youtube.com/user/behnamasadi/videos
.. _`Medical Image Computing Summer School`: https://medicss.cs.ucl.ac.uk/
