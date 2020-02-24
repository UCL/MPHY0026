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
3. Load the image ```tests\data\pelvis\pelvis_cropped.nii``
4. Adjust the window/level (right hand, vertical slider), to get a good contrast, write these numbers for later, e.g. 962, 122. Remember this is Level/Window, convert to Min/Max.
5. Write down the 3D location (look on bottom status bar), of each of 4 points in order
6. Save the 4 points as 4 rows of x y z (space separated) into a text file of your choice
7. Compare with ```tests\data\pelvis\pelvis_cropped_ct_fiducial_markers.txt```
8. If you didn't achieve this first step, continue using ```tests\data\pelvis\pelvis_cropped_ct_fiducial_markers.txt```
9. Repeat step 5, 6 multiple times to estimate FLE at each point.

Caveat:

* Compare ```tests\data\pelvis\pelvis_nii_ct_fiducial_markers.txt``` with ```tests\data\pelvis\pelvis_cropped_ct_fiducial_markers.txt```. They are different.
* VTK does not load the origin, or the orientation of each axis, as it wasn't designed for medical file formats.
* So for simplicity, we switched to a .nii file which does not have a non-zero origin.
* In practice, ALWAYS be aware that various file format conversions can forget/miss things like the origin in space, voxel dimensions etc.


2. Locate 4 fiducials in order in Physical Space
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The Pointer tip offset is at ```-17.91 0.95 -157.72```, and is stored in file ```tests\data\pelvis\optical-pointer-offset.txt```. You will learn pivot calibration next week.
* Ensure the tracker is on
* Place the pointer in the first fiducial, facing the tracker
* Use the command line tool to grab one point

```
python mphy0026_grab_pointer.py -t vega -p /c/Users/SmartLiver/SmartLiver/config/8700340.rom -o tests/data/pelvis/opt
ical-pointer-offset.txt -f 1 -n 1 -d p1.txt
```
i.e. 1 frame per second, and collect 1 sample, save to file ```p1.txt```

* Grab 3 remaining points
* Concatenate all 4 points into a single file. In gitbash.exe that would be:

```
cat p1.txt p2.txt p3.txt p4.txt > tracker.txt
```

3. Register Physical Space to Image Space
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Given CT landmarks in a file called ct.txt and tracker landmarks in a file called tracker.txt, you can compute Arun's method as:

```
 python mphy0026_registration.py -f ct.txt -m tracker.txt -o tracker-to-ct-using-PBR.txt
```

The program reports FRE, which typically should be < 1, mostly < 0.75

(Note: CT points can be saved for later use. Physical space points cannot. Someone might move the phantom or tracker in between runs.)

4. Display Registered CT scan With Pointer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* This can now be visualised

```
python mphy0026_quadview.py -v tests/data/pelvis/pelvis_cropped.nii  -reg tracker-to-ct-using-PBR.txt -p /c/Users/Sma
rtLiver/SmartLiver/config/8700340.rom -min 901 -max 1023 -o tests/data/pelvis/optical-pointer-offset.txt  -t vega
```

5. Grab Data for ICP
^^^^^^^^^^^^^^^^^^^^

The same pointer program can also grab multiple frames of data. The VEGA hardware works up to 250 fps.
We haven't yet tested the speed via Python. Lets assume 30 fps

So, if we want 900 points of data, at 30 frames per second that is about 30 seconds.

* Assign 1 person to be dragging the pointer.
* Place the pointer on the pelvis phantom.
* Start grabbing data

```
 python mphy0026_grab_pointer.py -t vega -p /c/Users/SmartLiver/SmartLiver/config/8700340.rom -o tests/data/pelvis/opt
ical-pointer-offset.txt  -f 30 -n 900 -d surface.txt
```

* The person dragging the pointer should not lift/remove from the surface, as the tracker will keep tracking.
* If the tracker fails to detect the pointer, the output on console will stop.
* Once complete the file ```surface.txt``` should contain 900 rows of point data.

6. Register ICP data to VTK surface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The program used above to register will also do ICP. Once you have collected surface.txt, do:

```
python mphy0026_registration.py -f tests/data/pelvis/pelvis_cropped_decimated.vtk -m surface.txt -o tracker-to-ct-usi
ng-ICP.txt
```

* Look at the residual. Does it look high/low.
* You could test the alignment, but using the ```tracker-to-ct-using-ICP.txt``` in place of the point-based one above.
* Its probably bad due to poor initialisation.
* So, use the Point-Based Registration to initialise:

```
 python mphy0026_registration.py -f tests/data/pelvis/pelvis_cropped_decimated.vtk -m surface.txt -o tracker-to-ct-usi
ng-ICP.txt -i tracker-to-ct-using-PBR.txt
```

* The residual should be much lower, and you can re-run the quad viewer to confirm its registered.




