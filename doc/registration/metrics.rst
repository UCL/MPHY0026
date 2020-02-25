.. _RegistrationMetrics:

Registration Metrics
====================

In this section we cover the key metrics used for measuring and reporting
registration error. This work was largely pioneered by a group at
`Vanderbilt <https://www.vanderbilt.edu/vise/visepeople/michael-fitzpatrick/>`_
and especially by the group led by
`Prof. Mike Fitzpatrick <https://engineering.vanderbilt.edu/bio/michael-fitzpatrick>`_.
A large part of CAS evaluation methodology and subsequent success in the OR has
been born from the ability to understand the errors present in image-guidance system.

Registration Evaluation is nicely covered by Ziv Yaniv in Chapter 6,
and section 6.4 of :ref:`bookClearyPeters`.

For MPHY0026, none of these formula need memorizing.

Evaluation Criteria
^^^^^^^^^^^^^^^^^^^

When preparing this section, I (Matt) naturally jumps to thoughts of
FLE, FRE, TRE, covered below. But thanks to Ziv, it's worth discussing these
additional criteria first:

1. Fast - real-time
2. Accurate - [Maurer1998]_.
3. Robust - :math:`N/2`, meaning over half the data must be outliers to break the registration
4. Automatic - No user interaction
5. Reliable - Given clinical expectation, the registration is deemed a success

Open Discussion.


Fiducial Localisation Error (FLE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* FLE is the error in determining the position of each fiducial / landmark [Maurer1998]_.
* FLE "is essentially the root-mean-square distance between the exact and calculated fiducial positions" [Maurer1993]_.

.. math::

  \sigma_{fl}^2 = E( \lVert {\bf e}_{fl} \rVert^2 )

* FLE is different for Image and Physical space


*Questions*

What are the assumptions here?

What errors exist in practice?


* Measurements may have non-Gaussian or biased distribution
* Note that optical tracker accuracy varies throughout physical measurement volume
* Remember that FLE is UNKNOWN. We ESTIMATE it via repeated measurements.


Fiducial Registration Error (FRE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For point sets :math:`{\bf p}_j` and :math:`{\bf q}_j` and tranform :math:`T`, point-based registration minimises:

.. math::

    d(T)^2 = \frac{1}{N} \sum_{j=1}^{N} \lVert {\bf q}_j - T({\bf p}_j) \rVert^2


So FRE is the minimum of this function. i.e. "the distance between corresponding
fiducials after registration and transformation" [Maurer1998]_.

*Questions*

Refer to [Maurer1998]_ directly

Look at design of fiducials for image space and physical space

What do you notice?


Target Registration Error (TRE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TRE is "the distance between homologous points other than the centroids of fiducials" [Fitzpatrick1998]_.

* Normally expressed as RMS error, like FRE
* Points must not be a point used for Point Based Registration.
* Registration accuracy not dependent on patient
* So, validation can be done on phantoms - key for commercial adoption
* So, in a lab validation, you normally use extra landmarks, which are used as targets with which to measure TRE
* In the literature, we also see clinical targets, centroids of tumour etc.


Estimating TRE from FRE
^^^^^^^^^^^^^^^^^^^^^^^

The seminal paper by Fitzpatrick et al [Fitzpatrick1998]_ re-derived the following:

.. math::

    E(FRE^2) = \frac{(n-2) E(FLE^2)}{n}

where :math:`n` is the number of fiducials and :math:`E` means *Expectation*.

The main result of the paper was a formula to predict TRE from TRE:

.. math::

    E(TRE^2({\bf p}) = \frac{E(FRE^2)}{(n-2} \left 1 + \frac{1}{3} \sum_{i=1}^3 \frac{d_k^2}{f_k^2} \right

where :math:`{\bf p}` is a target point, :math:`d_k^2} the squared distance between the target
and the :math:`k`th principal axis and :math:`f_k^2` is the mean squared distance between the fiducial
points and the same axis.

The last formula is often used in designing optically tracked tools [West2004]_, and for estimating
the errors at a distance from a tool, e.g. endoscope [Shahidi2002]_.

FRE And TRE Are Uncorrelated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* In [Fitzpatrick2009]_ Mike Fitzpatrick shows that FRE and TRE are uncorrelated
* Proven mathematically, assuming independent Gaussian noise
* Demonstrated in simulation

Strong advice: Do not use FRE as an indicator of accuracy


FRE And TRE Can Underestimate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The above papers assume independent, Gaussian noise on fiducials.
There is a body of work analysing PBR when the noise is not so:
[Batchelor2000]_, [Wiles2008]_, [Moghari2009]_, [Danilchenko2010]_
and also for tracking [Fitzpatrick2009]_ which is covered next week.

* Nice illustration of clinical evaluation: [Shamir2009]_ from 2009.
* Possibly underestimated due to non-Guassian effects
* Illustrates how much work (15 years) done on PBR, and validation.


Do Not Claim FRE as TRE
^^^^^^^^^^^^^^^^^^^^^^^

* Sometimes you cannot measure TRE. i.e. points on internal organs.
* So, in practice you only have FLE and then FRE.
* So you must report it as FRE. Not anything that sounds like TRE.
* Don't say "The accuracy of my system is X" where X is in fact FRE.
