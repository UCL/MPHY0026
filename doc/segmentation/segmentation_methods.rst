.. _SegmentationAndModelling:

Segmentation and Modelling
==========================

What is Segmentation?
^^^^^^^^^^^^^^^^^^^^^

"Segmentation is the process of partitioning an image into different meaningful segments."
(`Wikipedia <https://en.wikipedia.org/wiki/Medical_image_computing#Segmentation>`_).

* In the example below, of a T1 weighted MR scan of a brain, a meningioma has been identified.
* So the image is partitioned into pixels that correspond to meningioma, and pixels that are not meningioma.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/e/e4/MeningiomaMRISegmentation.png
  :alt: Segmentation of a meningioma
  :width: 600

  Figure: Segmentation of a meningioma, visualised in `3D slicer <https://www.slicer.org/>`_, by RKikinis on Wikimedia, is licensed under `CC BY-SA 3.0`_.

Also called:

* Labelling: Each partition is assigned a separate label, either binary: background=0, meningioma=255.
* Or multiple labels like Freesurfer:

.. figure:: https://upload.wikimedia.org/wikipedia/commons/9/9e/Brainanim.gif
  :alt: Software package Freesurfer identifies multiple regions of the brain from T1 MRI.
  :width: 600

  Figure: The software package `FreeSurfer <https://surfer.nmr.mgh.harvard.edu/>`_ segments/labels many regions of the brain, by LarrabeeMGH on Wikimedia, licensed under `CC BY-SA 4.0`_.


From statistics/machine learning literature, also called "Classification", as you identify pixels
as belonging to a certain class.

Representation:

* Pixel mask
* Contour definition (list of points)
* Implicit surface (distance to zero-crossing)


Its a BIG field
^^^^^^^^^^^^^^^

There are:

* many image types
* many things being imaged
* many artefacts

Add in factors like, user dependent error, and hence:

* There are many many research papers on segmentation.
* Even review papers are split into sub-specialities.


Traditional Methods
^^^^^^^^^^^^^^^^^^^

Impossible to cover here. Most covered in other courses at UCL. Brief discussion?

* Thresholding
* Region growing
* Texture classification
* K-Means, EM
* Atlas based


Model-Based Methods
^^^^^^^^^^^^^^^^^^^

The main categories of model-based methods are:

* `Snakes - Parametric Deformable Models <https://en.wikipedia.org/wiki/Active_contour_model>`_
* `Level Sets - Non-Parametric Deformable Models <https://en.wikipedia.org/wiki/Level-set_method>`_
* Statistical Shape Models (SSM) (next page and :ref:`Workshop3SSM`).


More Recent Methods
^^^^^^^^^^^^^^^^^^^

* Supervised deep-learning
* Unsupervised deep-learning
* AI-assisted manual annotation (`MITK + NVidia Clara <https://www.youtube.com/watch?v=T0Pjki4vXx0>`_).


Difficult For CAS?
^^^^^^^^^^^^^^^^^^

* Abnormal growths, so different shapes in training set compared to test set, or normal population
* Post-op, metal artefacts, missing sections of anatomy
* Low volume cases (one-by-one, each case different)
* Class imbalance (lots of examples of good/healthy population, compared to few in diseased groups)
* Often end up with manual post-processing


What Tools Can I Use?
^^^^^^^^^^^^^^^^^^^^^

* `ITK-SNAP <http://www.itksnap.org/pmwiki/pmwiki.php>`_.
* `3D Slicer <https://www.slicer.org/>`_.
* `MITK <http://mitk.org/wiki/MITK>`_.
* `OSIRIX <https://www.osirix-viewer.com/>`_, or the open-source `Horos <https://horosproject.org/>`_.


Commercial Services Exist
^^^^^^^^^^^^^^^^^^^^^^^^^

* `Visible Patient <http://www.visiblepatient.com>`_
* `Mevis Distant Services <https://www.mevis.de/en/solutions/professional/mevis-distant-services-mds/>`_

Think carefully about the cost-benefit of segmenting your own,
and if training a Deep Learning model, will you outperform others
with much larger datasets?


Segmentation of Pre-Op data
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have segmented/labelled/outlined:

* Measure size/volume/length pre-operatively
* Plan operation
* Intra-operatively, visualise where it is. (More on visualisation later).


Segmentation of Intra-Op data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Video segmentation: e.g. Liver/Not-Liver, use to track specific objects
* Used to filter points: e.g. surface reconstruction only on things that are liver
* Ultrasound measurements: ??

So, the use-cases pre-operatively, and intra-operatively are very different.

* Different time constraints
* Non-real time versus real time etc.


Cautionary Tale
^^^^^^^^^^^^^^^

* There are many computer vision papers in deep learning
* Additionally, there is a huge interest in segmentation in medical imaging
* [Ronneberger2015]_ proposed U-Net in 2015, which is widely used
* Many more medical imaging networks were subsequently developed
* The MICCAI `Medical Segmentation Decathlon <https://decathlon-10.grand-challenge.org/>`_, challenge essentially wanted researchers to develop 1 algorithm to work well on multiple datasets.
* [Isensee2018]_ created nnU-Net (No New Net), which embeds a UNet in a robust training scheme.
* Current `leaderboard <https://decathlon-10.grand-challenge.org/evaluation/results/>`_.
* Segmentation methods that work, normally do so becauses of large quantities of labelled data. The rest are still research projects.
* Methods that work in computer vision, with datasets > 1 milion, or >10 million images etc., often do not translate to medical imaging, as datasets are often much smaller.

.. _`CC BY-SA 3.0`: https://creativecommons.org/licenses/by-sa/3.0
.. _`CC BY-SA 4.0`: https://creativecommons.org/licenses/by-sa/4.0