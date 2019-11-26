References
==========

This page shows a core list of papers that will be covered during the course.
They are essential reading. The reader does not need to memorise all of each
paper, but should know of each papers existence, memorise the key message from
each paper and understand how to apply the main findings of each paper.

Other papers, are listed on the :ref:`AdditionalResources` page.


Reviews and Background
----------------------

.. [ClearyPeters2010] Kevin Cleary and Terry Peters, **"Image-Guided Interventions: Technology Review and Clinical Applications"**, http://dx.doi.org/10.1146/annurev-bioeng-070909-105249


Application Examples
--------------------

The above review papers contains several "firsts". These examples, below, will be used for case
studies. You don't have to read all of each paper. In class, we will discuss the main system
components, and the necessary coordinate conversions, calibrations, tracking issues
and hence, estimate likely sources of error.

.. [Edwards2000] Philip J. Edwards, Andrew P. King, Calvin R. Maurer, Jr., Darryl A. de Cunha, David J. Hawkes, Derek L. G. Hill, Ron P. Gaston, Michael R. Fenlon, **"Design and Evaluation of a System for Microscope-Assisted Guided Interventions (MAGI)"**, http://dx.doi.org/10.1109/42.896784

.. [Feuerstein2008] Marco Feuerstein, Thomas Mussack, Sandro M. Heining, Nassir Navab, **"Intraoperative Laparoscope Augmentation for Port Placement and Resection Planning in Minimally Invasive Liver Resection"**, http://dx.doi.org/10.1109/TMI.2007.907327

.. [Kang2014] Xin Kang, Mahdi Azizian, Emmanuel Wilson, Kyle Wu, Aaron D. Martin, Timothy D. Kane, Craig A. Peters, Kevin Cleary, Raj Shekhar, **"Stereoscopic augmented reality for laparoscopic surgery"**, http://dx.doi.org/10.1007/s00464-014-3433-x

.. [Thompson2015] Stephen Thompson, Johannes Totz, Yi Song, Stian Johnsen, Danail Stoyanov, Sebastien Ourselin, Kurinchi Gurusamy, Crispin Schneider, Brian Davidson, David Hawkes, Matthew J Clarkson, **"Accuracy Validation of an Image Guided Laparoscopy System for Liver Resection"**, http://dx.doi.org/10.1117/12.2080974

.. [Hu2016] Yipeng Hu, Veeru Kasivisvanathan, Lucy A. M. Simmons, Matthew J. Clarkson, Stephen A. Thompson, Taimur T. Shah, Hashim U. Ahmed, Shonit Punwani, David J. Hawkes, Mark Emberton, Caroline M. Moore, Dean C. Barratt, **"Development and Phantom Validation of a 3-D-Ultrasound-Guided System for Targeting MRI-Visible Lesions During Transrectal Prostate Biopsy"**, http://dx.doi.org/10.1109/TBME.2016.2582734


Imaging
-------

.. [Elson2010] Daniel Elson, Guang-Zhong Yang, **"The Principles and Role of Medical Imaging in Surgery"**, http://dx.doi.org/10.1007/978-3-540-71915-1_39


Segmentation
------------

There is a large body of literature, and many reviews, such as [Sharma2010]_. In this course, we cover some
classical methods [Sharma2010]_, statistical shape models [Heimann2009]_, and an example of
a more modern machine learning method [Ronneberger2015]_, which led to [Isensee2018]_ which won the
medical image decathlon challenge [Simpson2019]_.

.. [Heimann2009] Tobias Heimann, Hans-Peter Meinzer, **"Statistical shape models for 3D medical image segmentation"**, http://dx.doi.org/10.1016/j.media.2009.05.004

.. [Sharma2010] Neeraj Sharma and Lalit M. Aggarwal, **"Automated medical image segmentation techniques."**, http://dx.doi.org/10.4103/0971-6203.58777

.. [Ronneberger2015] Olaf Ronneberger, Philipp Fischer and Thomas Brox, **"U-Net: Convolutional Networks for Biomedical Image Segmentation"**, http://dx.doi.org/10.1007/978-3-319-24574-4_28


Point-Based Registration
------------------------

There are two popular methods [Arun1987]_, [Horn1987]_ and obviously others, but functionally there is little difference between them [Eggert1998]_.
Students need to understand terms and acronyms like FLE, FRE and TRE [Fitzpatrick1998]_ and crucially, that FRE and TRE are uncorrelated [Fitzpatrick2001]_.

.. [Arun1987] K. S. Arun, T. S. Huang, S. D. Blostein, **"Least-Squares Fitting of Two 3-D Point Sets"**, http://dx.doi.org/10.1109/TPAMI.1987.4767965

.. [Horn1987] Berthold K. P. Horn, **"Closed-form solution of absolute orientation using unit quaternions"**, http://dx.doi.org/10.1364/JOSAA.4.000629

.. [Eggert1998] D. W. Eggert, A. Lorusso, R. B. Fisher, **"Estimating 3-D rigid body transformations: a comparison of four major algorithms"**, http://dx.doi.org/10.1007/s001380050048

.. [Fitzpatrick1998] J. Michael Fitzpatrick, Jay B. West, Calvin R. Maurer, Jr., **"Predicting Error in Rigid-Body Point-Based Registration"**, http://dx.doi.org/10.1109/42.736021

.. [Fitzpatrick2001] J. Michael Fitzpatrick, Jay B. West, **"The Distribution of Target Registration Error in Rigid-Body Point-Based Registration"**, http://dx.doi.org/10.1109/42.952729

.. [West2004] Jay B. West, Calvin R. Maurer, Jr., **"Designing Optically Tracked Instruments for Image-Guided Surgery"**, http://dx.doi.org/10.1109/TMI.2004.825614


Surface-Based Registration
--------------------------

An essential reference is the Iterative Closest Point algorithm (ICP) [BeslMcKay1992]_, which has 8000+ citations.
It has been extended and tweaked in many fields, but in Image-Guided Surgery, perhaps the most relevant is
the anisotropic adaptation [LenaMaierHein2011]_, followed by global optimisation [Yang2015]_.

.. [BeslMcKay1992] Paul J. Besl and Neil D. McKay, **"A Method for Registration of 3-D Shapes"**, http://dx.doi.org/10.1109/34.121791

.. [LenaMaierHein2011] Lena Maier-Hein, Alfred M. Franz, Thiago R. dos Santos, Mirko Schmidt, Markus Fangerau, Hans-Peter Meinzer, J. Michael Fitzpatrick, **"Convergent Iterative Closest-Point Algorithm to Accomodate Anisotropic and Inhomogenous Localization Error"**, http://dx.doi.org/10.1109/TPAMI.2011.248

.. [Yang2015] Jiaolong Yang, Hongdong Li, Dylan Campbell and Yunde Jia, **"Go-ICP: A Globally Optimal Solution to 3D ICP Point-Set Registration"**, http://dx.doi.org/10.1109/TPAMI.2015.2513405


Tracking Systems
----------------

These are the main accuracy assessment papers, from authors at NDI.

.. [Frantz2003] D. D. Frantz, A. D. Wiles, S. E. Leis and S. R. Kirsch, **"Accuracy assessment protocols for electromagnetic tracking systems"**, http://dx.doi.org/10.1088/0031-9155/48/14/314

.. [Wiles2004] Andrew D. Wiles, David G. Thompson and Donald D. Frantz, **"Accuracy assessment and interpretation for optical tracking systems"**, http://dx.doi.org/10.1117/12.536128

.. [Xiao2018] Guofang Xiao, Ester Bonmati, Stephen Thompson, Joe Evans, John Hipwell, Daniil Nikitichev, Kurinchi Gurusamy, Sébastien Ourselin, David J Hawkes, Brian Davidson, Matthew J Clarkson **"Electromagnetic tracking in image‐guided laparoscopic surgery: Comparison with optical tracking and feasibility study of a combined laparoscope and laparoscopic ultrasound system"**, https://doi.org/10.1002/mp.13210

Calibration
-----------

Pivot Calibration
~~~~~~~~~~~~~~~~~

.. [Birkfellner1998] Wolfgang Birkfellner, Franz Watzinger, Felix Wanschitz, Rolf Ewers, Helman Bergmann, **"Calibration of Tracking Systems in a Surgical Engironment"**, http://dx.doi.org/10.1109/42.736028

.. [Yaniv2015] Ziv Yaniv, **"Which pivot calibration?"**, http://dx.doi.org/10.1117/12.2081348

.. [Ma2017] Buton Ma, Niloofar Banihaveb, Joy Choi, Elvis C. S. Chen, Amber L. Simpson, **"Is pose-based pivot calibration superior to sphere fitting?"**, http://dx.doi.org/10.1117/12.2256050


Video Calibration
~~~~~~~~~~~~~~~~~

.. [Tsai1987] Roger Y. Tsai, **"A Versatile Camera Calibration Techniaue for High-Accuracy 3D Machine Vision Metrology Using Off-the-shelf TV Cameras and Lenses"**, http://dx.doi.org/10.1109/JRA.1987.1087109

.. [Zhang2000] Zhengyou Zhang, **"A Flexible New Technique for Camera Calibration"**, http://dx.doi.org/10.1109/34.888718


Hand-Eye Calibration
~~~~~~~~~~~~~~~~~~~~

.. [Tsai1989] Roger Y. Tsai and Reimar K. Lenz, **"A New Technique for Fully Autonomous and Efficient 3D Robotics Hand/Eye Calibration"**, http://dx.doi.org/10.1109/70.34770

.. [Malti2013] Abed Malti, Joao Pedro Barreto, **"Hand-eye and radial distortion calibration for rigid endoscopes"**, http://dx.doi.org/10.1002/rcs.1478

.. [Thompson2016] Stephen Thompson, Danail Stoyanov, Crispin Schneider, Kurinchi Gurusamy, Sébastien Ourselin, Brian Davidson, David Hawkes and Matthew J. Clarkson, **"Hand–eye calibration for rigid laparoscopes using an invariant point"**, http://dx.doi.org/10.1007/s11548-016-1364-9


Ultrasound Calibration
~~~~~~~~~~~~~~~~~~~~~~

.. [Mercier2005] Laurence Mercier, Thomas Lango, Frank Lindseth and D. Louis Collins, **"A Review of Calibration Techniques for Freehand 3-D Ultrasound Systems." http://dx.doi.org/10.1016/j.ultrasmedbio.2004.11.015

.. [Hsu2009] Po-Wei Hsu, Richard W. Prager, Andrew H. Gee and Graham M. Treece,  **"Freehand 3D Ultrasound Calibration: A Review"**, http://dx.doi.org/10.1007/978-3-540-68993-5_3


Timing Calibration
~~~~~~~~~~~~~~~~~~

.. [Lasso2014] Andras Lasso, Tamas Heffter, Adam Rankin, Csaba Pinter, Tamas Ungi, Gabor Fichtinger, **"PLUS: Open-Source Toolkit for Ultrasound-Guided Intervention Systems"**,  http://dx.doi.org/10.1109/TBME.2014.2322864


Visualisation
-------------

.. [Bichlmeier2010] Christoph Bichlmeier, Felix Wimmer, Sandro Michael Heining and Nassir Navab, **"Contextual Anatomic Mimesis Hybrid In-Situ Visualization Method for Improving Multi-Sensory Depth Perception in Medical Augmented Reality"**, http://dx.doi.org/10.1109/ISMAR.2007.4538837

.. [Hansen2010] Christian Hansen, Jan Wieferich, Felix Ritter, Christian Rieder, Heinz-Otto Peitgen, **"Illustrative visualization of 3D planning models for augmented reality in liver surgery"**, http://dx.doi.org/10.1007/s11548-009-0365-3

.. [KerstenOertel2013] Marta Kersten-Oertel, Pierre Jannin and D. Louis Collins, **"The state of the art of visualization in mixed reality image-guided surgery"**, http://dx.doi.org/10.1016/j.compmedimag.2013.01.009

.. [KerstenOertel2015] Marta Kersten-Oertel, Ian Gerard, Simon Drouin, Kelvin Mok, Denis Sirhan, David S. Sinclair, D. Louis Collins, **"Augmented reality in neurovascular surgery: feasibility and first uses in the operating room"**, http://dx.doi.org/10.1007/s11548-015-1163-8


User Interface
--------------

