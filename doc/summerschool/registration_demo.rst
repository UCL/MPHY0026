.. _FidRegistrationTutorial

Fiducial Registration Tutorial
==============================

Introduction
------------

This is the `SciKit-Surgery`_ tutorial on fiducial marker based registration. 
It was developed as a two hour tutorial for online delivery during the 2020 
`Medical Imaging Summer School`_ hosted by UCL, but should be more broadly useable.
The concepts taught are directly applicable to fiducial marker based registration
as applied to image guided interventions, and are more broadly applicable to 
other registration and calibrations where a good understanding of residual errors 
is required. 

The tutorial makes used the Python application `SciKit-SurgeryFRED`_.
The tutorial is divided into four sections:

* Familiarisation with the software and the relevant statistics (45 minutes)
* Analysis of data generated in the first section (45 minutes)
* Playing a game using the software (10 minutes)
* Discussion and writing up results (20 minutes)

Learning Objectives
^^^^^^^^^^^^^^^^^^^

After completing the tutorial students should be able to:

* Explain what is meant by the terms Fiducial Localisation Error (FLE), Target Registration Error (TRE) and Fiducial Registration Error (FRE)
* Be familiar derivation of statistics for the expected value of the TRE and FRE.
* Produce data showing how different statistics may be used to estimate the likely TRE for a single registration.
* Explain why FRE may be used to assess registration accuracy.
* Explain why FRE may not be a useful predictor of TRE.


Assumed Knowledge
^^^^^^^^^^^^^^^^^

`SciKit-SurgeryFRED`_ is Python software, it is assumed that pupils have a working Python installation and are able to install packages. If this tutorial has been installed as part of the `MPHY0026`_ module, then `SciKit-SurgeryFRED`_ should have already been installed. If not you should be able to install `SciKit-SurgeryFRED`_ using:

:: 

    pip install scikit-surgeryfred

and the source code installed with

:: 

    git clone https://github.com/UCL/scikit-surgeryfred


Related Tutorials
^^^^^^^^^^^^^^^^^

This tutorial was designed to replace the point based registration session of the `SciKit-SurgeryBARD`_ tutorial, to enable remote delivery when the students do not have access to a suitable phantom or printer.


Part 1 Introduction to Registration with SciKit-SurgeryFRED
-----------------------------------------------------------

Start scikit-surgeryfred, if you've installed it via pip you should be able to run 

:: 

    sksurgeryfred https://github.com/UCL/scikit-surgeryfred/raw/master/data/brain512.png

or 

:: 

    python -m sksurgeryfred https://github.com/UCL/scikit-surgeryfred/raw/master/data/brain512.png

If you've cloned the repository you should be able to run.

::

    tox
    source .tox/py37/bin/activate
    python sksurgeryfred.py data/brain512.png

The first argument should point to a png image. We've supplied a MRI of a brain, but it other images are possible.

.. figure:: scikit-surgeryfred_0.png
  :width: 100%

  Figure 1: SciKit-SurgeryFRED opens a window with two scenes, at left is the preoperative image (MRI) with a target point marked in red. At right is the intra-operative scene where only the patient outline is visible. We will use fiducial based registration to locate the target point on the intraoperative scene.

You can watch the SciKit-SurgeryFRED video:

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/t_6CH5uroYo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

On staring SciKit-SurgeryFRED you should see two images side by side as in Figure 1. The pre-operative image at
left has a target identified in red. The idea is to locate the target on the intraoperative image at right, where we can only see the patient's outline. Locating the target in the intraoperative image is done here using fiducial marker based registration. Mouse clicking on either image will place a fiducial marker on each image, defining a point correspondence between the two images.

.. figure:: scikit-surgeryfred_1.png
  :width: 100%

  Figure 2: Clicking on either image places a fiducial marker (in green) defining a point correspondence between the images

.. figure:: scikit-surgeryfred_1_zoom.png
  :width: 100%

  Figure 3: SciKit-SurgeryFRED adds a Fiducial Localisation Error to the marker in the intraoperative image. The zoomed in region shows the cross hair where the marker is in the pre-operative image, and the green circle where we have located it. The difference between the circle and cross hair centre is the FLE for this marker.


Point based registration requires at least three points to work. So keep adding marker points. At this point you may want to revisit the literature on point based registration, [Fitzpatrick1998]_, [Fitzpatrick2001]_, and  [Maurer1998]_ and consider where to place the fiducial markers to best effect. 

.. figure:: scikit-surgeryfred_3.png
  :width: 100%

  Figure 4: With 3 or more fiducial markers place, SciKit-SurgeryFRED is able to peform a point-based "Procrustes" registration between the two images. Note that the target is now present in the intraoperative together with a cross hair. Similarly to figure 3, the cross hair represents the actual position of the target, whereas the red circle is the estimated position using point based registration. The difference between the two centres if the Target Registration Error (TRE), in this case 2.18 mm ("Actual TRE").


You can add as many marker points as you like (SciKit-Surgery-FRED currently crashes after around 65 markers are placed) and see how the six measures (defined below) in the text boxes change. Placed markers cannot be deleted, but you can restart the registration with a new target by pressing 'r'. 

What the text boxes mean
^^^^^^^^^^^^^^^^^^^^^^^^

SciKitSurgery-FRED has four text boxes list six metrics, this is what they mean and how they should behave.

The first text box contains:

* "Number of Fids" is the number of fiducial markers placed, which should increase by one each time you click on the image.
* "Expected FLE" is the expected absolute value of the Fiducial Localisation Error. SciKit-SurgeryFRED models the FLE as a two dimensional isotropic normally distributed random variable. Each time a new registration is started (by starting the application or by pressing 'r') the standard deviation of the FLE is randomly selected from a uniform distribution between 0.5 and 5.0. Each time a fiducial is placed, its position is perturbed in two dimensions by this standard deviation. The expected absolute value of an FLE with a given standard deviation is calculated and is shown here.  

The second text box contains the expected values TRE and FRE as derived by [Fitzpatrick1998]_.

* "Expected FRE" is the expected value of the fiducial localisation error. This the expected absolute value of he fiducial registration error as defined in equation 10 of [Fitzpatrick1998]_. FRE is a function of the expected FLE and the number of fiducial markers. FLE should increase slightly as the number of fiducial markers increases.

.. figure:: fre_equation_10.png
  :width: 50%

* "Expected TRE" is the expected value of the target registration error. This the expected absolute value of he target registration error as defined in equation 46 of [Fitzpatrick1998]_. TRE is a function of the FLE and the number and geometry of the fiducial markers. Although it should reduce gradually as more fiducial markers are placed, it can be greatly altered by where you place the markers. Try this many times and see what happens to expected TRE for different marker configurations.

.. figure:: tre_equation_46.png
  :width: 50%

The third text box contains:

* "Actual TRE", this is the actual measured Target Registration Error. It is the distance between the position of the target determined by registration and the actual position of the target. It is this value that will determine the effectiveness of an intervention, however in practice it cannot be known. It can only be measured in experiments where a second imaging modality is used or in the case of SciKit-SurgeryFRED, by simulation. The aim of this tutorial is to investigate which of the other statistics provide the best estimate of the actual TRE.

The fourth box contains:

* "Actual FRE", this is the residual RMS distance between the registered point sets. It will largely depend on the FLE and the number of fiducial markers. Because it is easily measured it is often reported by commercial image guidance systems. However using the actual FRE as a measure of registration accuracy can be dangerous, as detailed succinctly in [Fitzpatrick2009]. More generally, the use of residual errors as a measure of accuracy (for registration and calibrations) is common in the literature, but is best avoided, for the same reasons.

Perform several registrations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Now take around 20 minutes to perform multiple registrations. See what patterns of fiducial markers give low TREs and what patterns give high TREs. Observe how the statistics change as you add more fiducial markers. Each time a registration is performed SciKit-Surgery will write the results to the log file "fred_results.log". Check that this file is present and that you can read it. Try and generate at least 100 registrations, the results of which will be used in the next section to look for correlations between the different statistics and the actual TRE.


Part 2 What Statistics are Useful in Predicting Actual TRE
----------------------------------------------------------

At the end of part 1 you should have created a logfile called "fred_results.log", which consists of a line for each successful registration, like:

::

    2020-06-23 14:21:01,019 - sksurgeryfred - INFO - success, 5.9342, 6.2639, 5.0875, 4.6176, 7.9979, 3
    2020-06-23 14:21:03,219 - sksurgeryfred - INFO - success, 2.0491, 7.1730, 4.7173, 5.6554, 7.9979, 4
    2020-06-23 14:21:04,150 - sksurgeryfred - INFO - success, 1.8424, 6.6209, 4.7914, 6.1951, 7.9979, 5
    2020-06-23 14:21:05,216 - sksurgeryfred - INFO - success, 0.8983, 6.8619, 4.7471, 6.5302, 7.9979, 6
    2020-06-23 14:21:06,315 - sksurgeryfred - INFO - success, 0.7015, 6.4242, 3.6960, 6.7594, 7.9979, 7
    2020-06-23 14:21:11,742 - sksurgeryfred - INFO - success, 11.1016, 4.6396, 26.8543, 3.1793, 5.5067, 3
    2020-06-23 14:21:12,820 - sksurgeryfred - INFO - success, 3.9498, 4.6584, 3.1586, 3.8939, 5.5067, 4

There is a time stamp and name, followed by 6 comma separated numbers. In order these are

::

    actual TRE, actual FRE, expected TRE, expected FRE, expected FLE, number of fiducial markers

You should be able to parse this data into the data analyse software of your choice and investigate what if any correlations exist between the different data. For convenience SciKit-SurgeryFRED comes with a basic plotting tool, which you can try as a start.

::
    
    python sksurgeryfred_plotter.py fred_results.log

or 

:: 
    
    sksurgeryfred_plotter fred_results.log

Should result in something like Figure 5.

.. figure:: plots.png
  :width: 100%

  Figure 5: Plots of the five statistics and their correlation with the Actual TRE, using sksurgeryfred_plotter.

Take some time now to interrogate this data. Some questions to consider;

* Are your results similar to those in figure 5?
* If you were trying to estimate the actual target registration error, which statistic is of most use?
* What level of uncertainty would there be in an individual registration?
* What are the practical implications of using these statistics? For example, while the actual FRE and the number of fiducial markers can always be determined, the other statistics require a prior knowledge of the expected FLE.
* If your results are similar to mine, why is there no correlation between FLE and actual TRE?
* Are there conditions when you might expect to see correlation between FLE and TRE?

Have a deeper dive through the data. What sort of probability distributions do the data fit? Are the assumptions used in our simulation valid in practice?

When you've looked at the data, you can have a go at part 3, where you'll try and apply what you've learned to some simulated surgery.


Part 3 Treatment Planning Simulation
------------------------------------

The last part of the tutorial is a game that highlights some of the issues that occur during image guided 
interventions. Here the image guided intervention has been simplified, your job is to place fiducial markers to
minimise target registration error, then use the knowledge you developed in parts 1 and 2 to adjust the ablation 
margin to maximise the treatment of the target and minimise damage to healthy tissue. Start by launching the game, something like. 

:: 

    sksurgeryfred_game https://github.com/UCL/scikit-surgeryfred/raw/master/data/brain512.png

Here's a video showing what to do:

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/ansH1w2ST-g" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    
    
The rules are:

* You are going to perform 20 image guided ablations. 
* You locate the target in the intraoperative image by placing up to 6 fiducial markers, using the same process as in part  1.
* You can change the treatment margin using the up and down arrow keys. Up to increase the margin, down to decrease.
* When you think you have the right margin you perform the ablation by pressing 'a'
* You will be awarded a score. If you treat 100% of the target you start with 1000 points, anything less than 100% and you start with 0 points. Points are then subtracted based on the amount of healthy tissue ablated. A large margin will increase the chances of 100% ablation, but increase the amount of healthy tissue ablated.
* Throughout the game you will be shown different statistics to help you make your decision. 
* For the first 4 ablations you are shown the actual TRE (this is for training purposes, you could not 
  know this during an actual ablation). Knowing the TRE makes it easy to set the margin, the margin just needs to 
  bigger than the TRE to ensure 100% treatment.
* You can then perform 16 more ablations, being shown different combinations of statistics that could be available 
  during an actual ablation. Your job is to use your knowledge of the predictive power of these statistics (gained 
  during part 1 and 2) to set the minimum effective margin. 
* Keep going until you get to the game over screen.

When you've finished have a look at the file 'fred_game.log'. It should contain a record of your scores together with 
a record of what statistics were visible for each score. Is there a link between the visible statistics and your scores?
Does it correspond to the correlations you might have found in part 2?

I would be grateful if you let me know your scores by `emailing me`_ 'fred_game.log', along with any comments on the 
usefulness of this tutorial.
 

.. _`SciKit-Surgery`: https://github.com/UCL/scikit-surgery/wikis/home
.. _`Medical Imaging Summer School`: https://medicss.cs.ucl.ac.uk/
.. _`SciKit-SurgeryFRED`: https://github.com/UCL/scikit-surgeryfred
.. _`MPHY0026`: https://mphy0026.readthedocs.io/en/latest/
.. _`SciKit-SurgeryBARD`: https://scikit-surgerybard.readthedocs.io/en/latest/02_4_Register_And_Ovelay.html
.. _`emailing me`: s.thompson@ucl.ac.uk

