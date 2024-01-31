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
* many artifacts like `intensity inhomogeneity <https://core.ac.uk/download/pdf/192793342.pdf>`_, `beam hardening <https://radiopaedia.org/articles/beam-hardening?lang=gb>`_ and artifacts caused by metal.

In addition, add in factors like, user dependent error, and hence:

* There are many many research papers on segmentation.
* Even review papers are split into sub-specialities.


Pixel-Based Methods
^^^^^^^^^^^^^^^^^^^

While many methods have arguably been superseded in the medical domain
by methods using machine learning, it is still worth spending
some time investigating these classical methods, as it gives you an
appreciation of all the things that can go wrong. Most of the same
issue can go wrong with machine learning methods too. While machine
learning can learn more complicated functions than you or I could
explicitly program, it would be still be foolish to assume that machine
learning is a panacea for all segmentation issues.


Image Thresholding
~~~~~~~~~~~~~~~~~~

Firsly, here is an introduction to Segmentation from a range of tutorials at
`Bioimage Analysis <https://www.ibiology.org/techniques/bioimage-analysis/>`_.

While this tutorial refers to biological images, rather than medical
images, the concepts are the same.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/jLd2I2adQtw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

How does this work in practice for some medical imaging? Here, Dr Clarkson
gives a short overview:


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/7OoZDsdL8cA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Once you start thinking about individual pixels in the image, it's important to
appreciate the histogram of image intensities. This video from the `Udacity YouTube channel <https://www.youtube.com/watch?v=6pX3II2eVs0>`_,
gives a useful introduction:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/6pX3II2eVs0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Following from simple thresholding then, and your understanding of the image histogram,
a method that seeks to automatically pick nice thresholds is `Otsu's method <https://en.wikipedia.org/wiki/Otsu%27s_method>`_.
In the following video, Dr Clarkson gives an overview of how it might apply in medical imaging:


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/6o-RxuCPNiI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Region growing
~~~~~~~~~~~~~~

One of the problems with `image thresholding <https://en.wikipedia.org/wiki/Thresholding_(image_processing)>`_,
is that it's a global method, with no concept of connectivity. In other words, the
algorithms do not consider that if adjacent pixels have the same intensity, they
are likely to be part of the same object. Region growing algorithms
aim to start from a seed point, and iteratively add pixels to the segmented
volume, based on connectivity, and various heuristics, like whether or
not adjacent pixels are within a close enough intensity range.

Here, is a demonstration of `region growing algorithms <https://en.wikipedia.org/wiki/Region_growing>`_:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/T-iDHz2ZHzg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


K-Means
~~~~~~~

K-Means is a common method, not just in image-processing, but in data-clustering in general.
Here is an introduction from the wonderful `Computerphile <https://www.youtube.com/user/Computerphile>`_ channel:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/yR7k19YBqiw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Most general descriptions of K-means illustrate the algorithm on a 2D scatter plot.
In a 2D scatter plot, there are two variables of interest, so each of the K-means
is a vector of length 2. However, when used in image segmentation, of a single image,
a single variable is used to denote the image intensity of each pixel.
In the 1D case, you are essentially doing K-means, looking for K values
representing peaks on the histogram of image intensities.


Atlas-Based methods
^^^^^^^^^^^^^^^^^^^

Another class of methods, fairly popular for a while in medical imaging, was that of
atlas-based methods. An atlas is a reference image that has been accurately segmented,
that you can consider to be a reference or template for all other segmentations. The
atlas may be made from a single image, or from some process of averaging/combining
a large number of scans and extracting an average image and segmenting that.
The segmentation is often done manually, as this process is used to bootstrap
the segmentation of a large database of other images.

For a single image atlas, the general process could be something like:

* Identify a reference image. e.g. a healthy control subject of average age.
* Manually segment the image, as accurately as possible.
* For a new image that needs to be segmented, first register (align) it to the atlas
* Copy the atlas labels onto the image that needs segmenting

In the following video,
`Prof. Paul Yushkevich <https://www.med.upenn.edu/apps/faculty/index.php/g275/p2693923>`_
who worked on `ITK Snap <http://www.itksnap.org/pmwiki/pmwiki.php>`_, one of the most
popular segmentation tools, gives an overview of Atlas Based Segmentation methods.


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/XB1XKj5QdDc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Model-Based Methods
^^^^^^^^^^^^^^^^^^^

The main categories of model-based methods are:

* `Snakes - Parametric Deformable Models <https://en.wikipedia.org/wiki/Active_contour_model>`_
* `Level Sets - Non-Parametric Deformable Models <https://en.wikipedia.org/wiki/Level-set_method>`_
* Statistical Shape Models (SSM) (next page and :ref:`Workshop3SSM`).


Neural Network Based Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In recent years, since the `2012 ImageNet competition <https://en.wikipedia.org/wiki/ImageNet>`_ for example,
machine learning and specifically deep learning have had great success at many computer vision tasks,
including image segmentation, which in the deep learning literature is called semantic segmentation.

However, this simply cannot be a course on deep learning, or semantic segmentation. In
this section of the notes, we just provide links to external resources that would give
you an overview of how a neural network can be used to segment an image.


Convolutional Neural Networks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What to put in this section, as it could be a whole lifetime of study!

Here follows a list of resources that are useful to get up-to-speed with using Neural Networks.

* `A Keras tutorial from DataCamp <https://www.datacamp.com/community/tutorials/deep-learning-python>`_ illustrates what a neuron is.
* `A Keras tutorial on semantic segmentation <https://divamgupta.com/image-segmentation/2019/06/06/deep-learning-semantic-segmentation-keras.html>`_ as an introduction to segmentation.
* `Stanford University cs231n course is popular <http://cs231n.stanford.edu/>`_
* `Coursera Deep Learning Specialization <https://www.coursera.org/specializations/deep-learning>`_
* `TensorFlow tutorials <https://www.tensorflow.org/tutorials>`_
* `MICCAI Education Challenge resources <http://www.miccai.org/education/material/>`_
* The `Deep Learning <https://www.deeplearningbook.org/>`_ book.
* Simon Prince's new `Understanding Deep Learning <https://udlbook.github.io/udlbook/>`_ book.
* Dr. Yipeng Hu's `tutorials <https://github.com/YipengHu/MPHY0041/tree/main/tutorials>`_ from the course "Machine Learning in Medical Imaging (`MPHY0041 <https://www.ucl.ac.uk/module-catalogue/modules/machine-learning-in-medical-imaging/MPHY0041>`_)" at UCL.
* Dr. Yipeng Hu's `tutorials on segmentation <https://github.com/YipengHu/MPHY0043/tree/main/tutorials/segmentation>`_ from the course "Artificial Intelligence for Surgery and Intervention (`MPHY0043 <https://www.ucl.ac.uk/module-catalogue/modules/artificial-intelligence-for-surgery-and-intervention-MPHY0043>`_)" at UCL.

To get started with your first network is not too hard. For example,
(Even!) Prof. Clarkson coded up a `UNet here <https://github.com/UCL/scikit-surgerytf/blob/master/sksurgerytf/models/rgb_unet.py>`_,
as part of his own learning process. But the real trick to "getting good", is to practice on real problems.
So, its not something you can just read. You need a project, and to be actively doing it.


Combining Neural Networks and Manual Annotation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Medical Images are still difficult to segment, even with the power of Artificial Intelligence
and Deep Neural Networks. This is mainly due to a relative lack of data. In computer vision
for example, algorithms can be trained on millions of images, but in the medical community,
we might be dealing with only 100's or at best 1000's of images.

So, there is still a justification for training a neural network to partially segment
things, and combining the network with manual input from the user for a
manually-guided + AI hybrid.


Specific Challenges for CAS
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Segmentation has additional problems that are specific to Computer Assisted Surgery (CAS):

* Abnormal growths, so different shapes in training set compared to test set, or normal population
* Post-op, metal artefacts, missing sections of anatomy
* Low volume cases (one-by-one, each case different)
* Class imbalance (lots of examples of good/healthy population, compared to few in diseased groups)

As a consequence, you still often end up with manual post-processing


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

Once you have segmented/labelled/outlined, you can:

* Use segmented models to measure size/volume/length pre-operatively.
* Plan operation in terms of what to target, and what to avoid.
* Intra-operatively, visualise where the target is. (More on visualisation later).


Segmentation of Intra-Op data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Segmentation can also be used intra-operatively, live, in real-time to aid
things like computer vision based algorithms.

For example:

* Video segmentation: e.g. in laparoscopic video, identify Liver/Not-Liver, use to track specific objects
* Used segmentation to filter points: e.g. having identified Liver/Not-Liver, only do surface reconstruction on things that are Liver.

So, the use-cases pre-operatively, and intra-operatively are very different.

* Different time constraints
* Non-real time versus real time etc.

.. _`CC BY-SA 3.0`: https://creativecommons.org/licenses/by-sa/3.0
.. _`CC BY-SA 4.0`: https://creativecommons.org/licenses/by-sa/4.0