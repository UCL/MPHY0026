References
==========

This page shows a core list of papers that will be covered during the course.
They are essential reading. The reader does not need to memorise all of each
paper, but should know of each papers existence, memorise the key message from
each paper and understand how to apply the main findings of each paper.

Other papers, are listed on the :ref:`AdditionalResources` page.


Reviews and Background
----------------------

Review paper:

.. [ClearyPeters2010] Kevin Cleary and Terry Peters, "Image-Guided Interventions: Technology Review and Clinical Applications", http://dx.doi.org/10.1146/annurev-bioeng-070909-105249


Application Examples
--------------------

Lots more example papers needed, with overviews of complete clinical applications.


Coordinate Systems
------------------

Haven't seen a specific summary yet.


Imaging
-------

.. [Elson2010] Daniel Elson, Guang-Zhong Yang, "The Principles and Role of Medical Imaging in Surgery", http://dx.doi.org/10.1007/978-3-540-71915-1_39


Segmentation
------------

There is a large body of literature, and many reviews, such as [Sharma2010]_. In this course, we cover some
classical methods [Sharma2010]_, statistical shape models [Heimann2009]_, and an example of
a more modern machine learning method [Ronneberger]_, which led to [Isensee2018]_ which won the
medical image decathlon challenge [Simpson2019]_.

.. [Sharma2010] Neeraj Sharma and Lalit M. Aggarwal, "Automated medical image segmentation techniques.", http://dx.doi.org/10.4103/0971-6203.58777

.. [Heimann2009] Tobias Heimann, Hans-Peter Meinzer, "Statistical shape models for 3D medical image segmentation", http://dx.doi.org/10.1016/j.media.2009.05.004

.. [Ronneberger] Olaf Ronneberger, Philipp Fischer and Thomas Brox, "U-Net: Convolutional Networks for Biomedical Image Segmentation", http://dx.doi.org/10.1007/978-3-319-24574-4_28


Point-Based Registration
------------------------

There are two popular methods [Arun1987]_, [Horn1987]_ and obviously others, but not much between them [Eggert1998]_.
Students need to understand terms and acronyms like FLE, FRE and TRE [Fitzpatrick1998]_ and crucially, that FRE and TRE are uncorrelated [Fitzpatrick2001]_.

.. [Arun1987] K. S. Arun, T. S. Huang, S. D. Blostein, "Least-Squares Fitting of Two 3-D Point Sets", http://dx.doi.org/10.1109/TPAMI.1987.4767965

.. [Horn1987] Berthold K. P. Horn, "Closed-form solution of absolute orientation using unit quaternions", http://dx.doi.org/10.1364/JOSAA.4.000629

.. [Eggert1998] D. W. Eggert, A. Lorusso, R. B. Fisher, "Estimating 3-D rigid body transformations: a comparison of four major algorithms", http://dx.doi.org/10.1007/s001380050048

.. [Fitzpatrick1998] J. Michael Fitzpatrick, Jay B. West, Calvin R. Maurer, Jr., "Predicting Error in Rigid-Body Point-Based Registration", http://dx.doi.org/10.1109/42.736021

.. [Fitzpatrick2001] J. Michael Fitzpatrick, Jay B. West, "The Distribution of Target Registration Error in Rigid-Body Point-Based Registration", http://dx.doi.org/10.1109/42.952729

.. [West2004] Jay B. West, Calvin R. Maurer, Jr., "Designing Optically Tracked Instruments for Image-Guided Surgery", http://dx.doi.org/10.1109/TMI.2004.825614


Surface-Based Registration
--------------------------

An essential reference is the Iterative Closest Point algorithm (ICP) [BeslMcKay1992]_, which has 8000+ citations.
It has been extended and tweaked in many fields, but in Image-Guided Surgery, perhaps the most relevant is
the anisotropic adaptation [LenaMaierHein2011]_, followed by global optimisation [Yang2015]_.

.. [BeslMcKay1992] Paul J. Besl and Neil D. McKay, "A Method for Registration of 3-D Shapes", http://dx.doi.org/10.1109/34.121791

.. [LenaMaierHein2011] Convergent Iterative Closest-Point Algorithm to Accomodate Anisotropic and Inhomogenous Localization Error", http://dx.doi.org/10.1109/TPAMI.2011.248

.. [Yang2015] Jiaolong Yang, Hongdong Li, Dylan Campbell and Yunde Jia, "Go-ICP: A Globally Optimal Solution to 3D ICP Point-Set Registration", http://dx.doi.org/10.1109/TPAMI.2015.2513405


Tracking Systems
----------------

.. [Frantz2003] D. D. Frantz, A. D. WILES, S. E. Leis and S. R. Kirsch, "Accuracy assessment protocols for electromagnetic tracking systems", http://dx.doi.org/10.1088/0031-9155/48/14/314

.. [Wiles2004] Andrew D. Wiles, David G. Thompson and Donald D. Frantz, "Accuracy assessment and interpretation for optical tracking systems", http://dx.doi.org/10.1117/12.536128


Calibration
-----------

Pivot Calibration
~~~~~~~~~~~~~~~~~

.. [Birkfellner1998] Wolfgang Birkfellner, Franz Watzinger, Felix Wanschitz, Rolf Ewers, Helman Bergmann, "Calibration of Tracking Systems in a Surgical Engironment", http://dx.doi.org/10.1109/42.736028

.. [Yaniv2015] Ziv Yaniv, "Which pivot calibration?", http://dx.doi.org/10.1117/12.2081348

.. [Ma2017] Buton Ma, Niloofar Banihaveb, Joy Choi, Elvis C. S. Chen, Amber L. Simpson, "Is pose-based pivot calibration superior to sphere fitting?", http://dx.doi.org/10.1117/12.2256050


Video Calibration
~~~~~~~~~~~~~~~~~

.. [Tsai1987] Roger Y. Tsai, "A Versatile Camera Calibration Techniaue for High-Accuracy 3D Machine Vision Metrology Using Off-the-shelf TV Cameras and Lenses", http://dx.doi.org/10.1109/JRA.1987.1087109

.. [Zhang2000] Zhengyou Zhang, "A Flexible New Technique for Camera Calibration", http://dx.doi.org/10.1109/34.888718


Hand-Eye Calibration
~~~~~~~~~~~~~~~~~~~~

.. [Tsai1989] Roger Y. Tsai and Reimar K. Lenz, "A New Technique for Fully Autonomous and Efficient 3D Robotics Hand/Eye Calibration", http://dx.doi.org/10.1109/70.34770

.. [Malti2013] Abed Malti, Joao Pedro Barreto, "Hand-eye and radial distortion calibration for rigid endoscopes" http://dx.doi.org/10.1002/rcs.1478

.. [Thompson2016] Stephen Thompson, Danail Stoyanov, Crispin Schneider, Kurinchi Gurusamy, Sébastien Ourselin, Brian Davidson, David Hawkes and Matthew J. Clarkson, "Hand–eye calibration for rigid laparoscopes using an invariant point", http://dx.doi.org/10.1007/s11548-016-1364-9


Ultrasound Calibration
~~~~~~~~~~~~~~~~~~~~~~

.. [Mercier2005] Laurence Mercier, Thomas Lango, Frank Lindseth and D. Louis Collins, "A Review of Calibration Techniques for Freehand 3-D Ultrasound Systems." http://dx.doi.org/10.1016/j.ultrasmedbio.2004.11.015

.. [Hsu20] Po-Wei Hsu, Richard W. Prager, Andrew H. Gee and Graham M. Treece,  "Freehand 3D Ultrasound Calibration: A Review", http://dx.doi.org/10.1007/978-3-540-68993-5_3


Timing Calibration
~~~~~~~~~~~~~~~~~~

Need papers / examples.


Visualisation
-------------

.. [KerstenOertel2013] Marta Kersten-Oertel, Pierre Jannin and D. Louis Collins, "The state of the art of visualization in mixed reality image-guided surgery", http://dx.doi.org/10.1016/j.compmedimag.2013.01.009

  - First example 4 quadrant view? Popular in Neurosurgery

  - First example Augmented Reality

  - Understand Surface rendering / Volume rendering / how to mix?

  - Software Libraries


User Interface
--------------

