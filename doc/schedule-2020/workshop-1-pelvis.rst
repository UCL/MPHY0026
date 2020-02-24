.. _Workshop1Pelvis:

Workshop 1: UCL Pelvis Phantom, Optical Tracker, Windows
========================================================

Assumes you have installed

* `gitbash.exe <https://git-scm.com/>`_.
* `NiftyIGI.exe <https://github.com/NifTK/NifTK/releases>`_.
* `MPHY0026 repo <https://weisslab.cs.ucl.ac.uk/WEISSTeaching/MPHY0026>`_.


1. Locate 4 fiducials in order in CT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the pelvis phantom, there are 4 fiducials. They are numbered.
2. Run NiftyIGI.exe (or similar medical image viewer of your choice).
3. Load the image ```tests\data\pelvis\pelvis_cropped.gipl.gz``
4. Write down the 3D location (look on bottom status bar), of each of 4 points in order
5. Save the 4 points as 4 rows of x y z (space separated) into a text file of your choice
6. Compare with ```tests\data\pelvis\pelvis_cropped_ct_fiducial_markers.txt```
7. If you didn't achieve this first step, continue using ```tests\data\pelvis\pelvis_cropped_ct_fiducial_markers.txt```
8. Repeat step 4, 5 multiple times to estimate FLE at each point.

Caveat:

* Compare ```tests\data\pelvis\pelvis_nii_ct_fiducial_markers.txt``` with ```tests\data\pelvis\pelvis_cropped_ct_fiducial_markers.txt```. They are different.
* VTK does not load the origin, or the orientation of each axis, as it wasn't designed for medical file formats.
* So for simplicity, we switched to a .gipl.gz file which also does not load origin or orientations.
* In practice, ALWAYS be aware that various file format conversions can forget/miss things like the origin in space, voxel dimensions etc.


2. Locate 4 fiducials in order in Physical Space
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The Pointer tip offset is at ```-17.91 0.95 -157.72```, and is stored in file ```tests\data\pelvis\optical-pointer-offset.txt```. You will learn pivot calibration next week.
* Ensure the tracker is on


