.. _RegistrationMetrics:

Registration Metrics
====================

In this section we cover the key metrics used for measuring and reporting
registration error. This work was pioneered by
`Prof. Mike Fitzpatrick <https://engineering.vanderbilt.edu/bio/michael-fitzpatrick>`_
at `Vanderbilt <https://www.vanderbilt.edu/vise/visepeople/michael-fitzpatrick/>`_.
A large part of CAS evaluation methodology and subsequent success in the OR has
been born from the ability to understand the errors present in image-guidance system.


Fiducial Localisation Error (FLE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FLE is the error in measuring the position of each fiducial / landmark.

.. math::

   \frac{ \sum_{t=0}^{N}f(t,k) }{N}

* Applies to image (CT/MR) and physical space, each with different distribution
* May have non-Gaussian or biased distribution
* Tracker accuracy varies throughout physical measurement volume
* Its UNKNOWN: We ESTIMATE it via repeated measurements.


Fiducial Registration Error (FRE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FRE is the difference between the registered fiducial position and the
actual fiducial position, expressed as an RMS error.

.. math::

   \frac{ \sum_{t=0}^{N}f(t,k) }{N}

* Again, its an estimate, because we can only measure the position of fiducials with a certain accuracy.


Target Registration Error (TRE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TRE is the difference between the predicted position of target and the actual
position of the target (e.g. tumour), where target means a point not used
for registration. Normally expressed as an RMS error.

.. math::

   \frac{ \sum_{t=0}^{N}f(t,k) }{N}

What do we use as a target?

* Use a 'spare' (i.e. leave-one-out approach) fiducial? Only on phnatoms.
* Centre of a tumour? Affected by localisation error.
* How many?
* What distribution?

Estimating TRE from FRE
^^^^^^^^^^^^^^^^^^^^^^^


FRE And TRE Are Uncorrelated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do Not Claim FRE as TRE
^^^^^^^^^^^^^^^^^^^^^^^

* Sometimes you cannot measure TRE. i.e. points on internal organs.
* So, in practice you only have FLE and then FRE.
* So you must report it as FRE. Not anything that sounds like TRE
* Don't do "The accuracy of my system is X" where X is in fact FRE


FRE And TRE Can Underestimate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




