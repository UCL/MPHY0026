.. _RANSAC:

RANSAC Paradigm
===============

The RANSAC plgorithm was first introduced by Fischler and Bolles in [FischlerBolles1981]_.


Video
^^^^^

This is a nice explanation by Behnam Asadi from YouTube.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/UKhh_MmGIjM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


RANSAC is Not Least Trimmed Squares
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Typically in Least Squares (LS) fitting, we use all the data to fit a model.
* In `Least Trimmed Squares <https://link.springer.com/article/10.1007/s00453-012-9721-8>`_, you compute LS, throw away a percentage of bad data, then recompute, and repeat.
* Fischler and Bolles show, this can still fail, as the initial model can be affected by the bad data.
* They wanted a more robust method.


The Paradigm
^^^^^^^^^^^^

Given a model that requires a minimum of :math:`n` points to compute a solution,
and a set of data points :math:`P` where :math:`\#(P) \ge n`:

1. Select a random  subset of :math:`n` data points from :math:`P` to form :math:`S1`
2. Instantiate the model :math:`M1`
3. Determine the set :math:`S1*` within error threshold of model :math:`M1`, and count the members of :math:`S1*`. This is the *consensus* set.
4. If :math:`\#(S1*)` greater than a threshold :math:`t`, use :math:`S1*` to compute a new model :math:`M1*`
5. If :math:`\#(S1*)` is less than :math:`t`, select a new random subset :math:`S2` and repeat.
6. If after :math:`k` iterations, no consensus set with :math:`t` or more members has been found, solve with the largest consensus set, or terminate with failure.

Parameters:

* :math:`e`: error threshold to determine which points are inliers
* :math:`t`: minimum number of inliers to accept as forming a valid model
* :math:`k`: number of iterations to try

Referring to paper:

* :math:`w`: probability that any given point is within error tolerance of model
* :math:`z`: certainty that at least one of our subsets contains error free data

So,

.. math::

  ( 1 - w^n )^k = ( 1 - z)

gives:

.. math::

  k = \frac{log(1-z)}{log(1-w^n)}

For example, if we think that 20 percent of the data is bad, the probability of picking a good data point
is :math:`w = 0.8`. If we want 99 percent confidence that we will end up with a good model then,
:math:`z = 0.99`. So, in a line fitting problem, :math:`n = 2`, so the number of iterations :math:`k` we should
attempt should be:

.. math::

  k = \frac{log(1-0.99)}{log(1-0.8^2)}

which is :math:`k = 4.5`, so at least 5 iterations should be made.

Alternatively, the paper derives the expectation of :math:`k` as:

.. math::

  E(k) = w^{-n}

and the standard deviation of :math:`k` to be:

.. math::

  SD(k) = (sqrt(1 - w^n)) * (1 / w^n)

which in the same example gives, a mean of 1.56, a SD of 0.9, so if we wanted mean plus 3 standard deviations, its we'd need 5 iterations again.

With poor data, say :math:`w = 0.5`, we'd need approx 16 iterations.


From [FischlerBolles1981]_, you could terminate early the first
time you get a consensus set larger than a minimum size, i.e. threshold :math:`t`,
or if you don't get over :math:`t`, just pick the largest consensus set you found.

It depends if you want to finish early, or fit the most data, so in practice, implementations may differ.

For another explanation, see `Ziv Yaniv's example <https://yanivresearch.info/writtenMaterial/RANSAC.pdf>`_, which
uses RANSAC to solve for parameters of a hyperplane and hypersphere, and discusses various implementation details.


Widely Applicable
^^^^^^^^^^^^^^^^^

* It's not a specific algorithm
* It's a way of solving model fitting problems
* So, problem and implementation specific
* e.g. Pivot calibration, pose estimation, line fitting

Notebooks
^^^^^^^^^

Have a play with the provided :ref:`Notebooks`.

scikit-surgery provides the main algorithms:

.. code::

    # Note that the scikit-surgery libraries provide pivot and RANSAC.
    import sksugerycalibration.algorithms.pivot as p   # AOS Pivot algorithm and a RANSAC version.
    import sksurgerycore.transforms.matrix as m  # For creating 4x4 matrices.

so the algorithms are `here <https://github.com/UCL/scikit-surgerycalibration/blob/master/sksurgerycalibration/algorithms/pivot.py>`_
and the matrix utilities are `here <https://github.com/UCL/scikit-surgerycore/-/blob/master/sksurgerycore/transforms/matrix.py>`_.

and can be installed with:

.. code::

    pip install scikit-surgerycalibration

