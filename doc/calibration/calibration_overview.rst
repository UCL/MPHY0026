Calibration
===========

Overview
--------

Pivot calibration
-----------------
Pivot calibration consist in rotating an instrument on a point.
The calculus can be doe in three different ways: Sphere fitting, Algebraic one step, and Algebraic two steps. These methods solve the same problem but with a different order.

(add figure here)

Sphere fitting
^^^^^^^^^^^^^^
The sphere fitting method assumes that the tool is rotating forming a sphere.
The equation of a sphere with origin x0, y0, z0 and a point on the surface (x,y,z) has the following equation:
(x-x0)2+(y-y0)2+(z-z0)2 = r2
If we expand this we get:
x2-2xx0+x02+y2-....
which is equivalent to:
x2+y2+z2=....

This can be written in a least-squares form:
[]=[]*[]

This can be easily solved using Python and the scipy.optimise.leastsq function.

Algebraic one step
^^^^^^^^^^^^^^^^^^

Algebraic two step
^^^^^^^^^^^^^^^^^^


Image-to-Marker
---------------

Ultrasound calibration
----------------------


* Hand-eye, video camera
