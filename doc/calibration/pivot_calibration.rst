.. _Pivot:

Pivot calibration
=================

Pivot calibration is the transformation between a tracked marker/sensor and the tip of a tool (e.g., pointer). 
This process consists in rotating the tracked instrument on a stationary point in order to localise the 3D position of the instrument's tip.
There are several ways to perform the pivot calibration, mainly: sphere fitting, algebraic one step, and algebraic two steps. 
All these methods solve exactly the same problem but taking the transformation in a different order. 
A review can be found here: [Yaniv2015]_. Yaniv et al. concluded that algebraic formulations were more precise
and more accurate than sphere fitting, but Ma et al. found that sphere fitting was superior when data was good
and algebraic methods degrade less when data is bad [Ma2017]_.


Sphere fitting
--------------

The sphere fitting method assumes that the tracked sensor/marker forms a sphere while is rotated (see figure below), where the marker is at the surface of the sphere and the tip of the tracked tool at the centre of the sphere (pivoting point).

.. figure:: pivot_calibration.png
  :alt: Transformations involved in a pivot calibration using an optical tracker
  :width: 600
  
  Transformations involved in a pivot calibration using an optical tracker

The equation of a sphere with origin at point *(x0, y0, z0)*, a point *(x,y,z)* on the surface and a radius *r* has the following equation:

.. figure:: pivot_eq1.png
  :height: 50

If we expand this equation we get:

.. figure:: pivot_eq2.png
  :height: 50
  
which in turn is equivalent to:

.. figure:: pivot_eq3.png
  :height: 50
  
Considering that we will have a list of *n* surface points, this can be written in a least-squares form *f=AC*:

Where 

.. figure:: pivot_eq4.png
	

This can be easily solved using Python or MATLAB functions, among others libraries.
For example, `SciKit-Surgery implements Pivot Calibration`_ using the above spherical
method, an algebraic one-step, and also using `RANSAC`_ to reduce outliers.

In the following video Dr. Clarkson explains and demonstrates how to do a pivot calibration:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/wIEbG6ya63I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Errors
------
The accuracy of this method depends on the shape of the tip of the tool, the length of the tool and the noise on the pivoting data.
When pivoting the tool on a stationary point on a flat surface, if the tip is not sharp enough(which very often is not sharp to avoid tissue damage) may lead to inaccuracies on the measurements.
One solutions is to use a soft surface to pivot the tool, however by doing that, the tip will be at the centre of the rotation instead of exactly at the tip.


Make Your Own
-------------

As part of our `Medical Image Computing Summer School`_ we wrote a new tutorial
where you can make your own pointer and calibrate it!

Follow this link: :ref:`SummerSchoolPivotCalibration`.


.. _`Medical Image Computing Summer School`: https://medicss.cs.ucl.ac.uk/
.. _`SciKit-Surgery implements Pivot Calibration`: https://github.com/UCL/scikit-surgerycalibration/blob/master/sksurgerycalibration/algorithms/pivot.py
.. _`RANSAC`: https://en.wikipedia.org/wiki/Random_sample_consensus#:~:text=Random%20sample%20consensus%20(RANSAC)%20is,the%20values%20of%20the%20estimates.