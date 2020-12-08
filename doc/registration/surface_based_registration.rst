.. _SurfaceBasedRegistration:

Surface-Based Registration
==========================

Watch videos:

Examples - Surface Registration with Medtronic Stealthstation ENT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/RRawad44lvA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Examples - Surface Registration with Pathfinder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/vxd145vVknk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Examples - Surface Registration with Brainlab Z-touch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/C9ngfY97Bkg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Surface Reconstruction Methods:

* Dragging a pointer
* Laser-Pointer like Brainlab Z-touch
* Laser pointer [Fusaglia2016]_
* Stereo vision, surface reconstruction, stitching [Thompson2015]_


Key Papers
^^^^^^^^^^

* ICP Algorithm. [BeslMcKay1992]_.
* Variations for anisotropic noise, e.g. [LenaMaierHein2011]_
* Extensions to global alignment, e.g. [Yang2015]_


Algorithm - Iterative Closest Point (ICP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From section IV (A) in [BeslMcKay1992]_, they define:

* Data ( :math:`P` with :math:`N_p` points ) == Moving
* Model ( :math:`X` with :math:`N_x` points ) == Fixed

The algorithm incrementally updates a moving point set, performing the following steps 1-4 in a loop.
:math:`k` is the iteration counter.

0. Create Transformed Moving point set == Moving.
1. For each point in Transformed Moving point set, compute closest point in Fixed point set.
2. Compute Point-Based registration, mapping Original Moving to Fixed,
3. Apply transform to Original Moving to generate a new Transformed Moving
4. Terminate iteration when change in mean squared error < threshold

i.e.

0. Set :math:`P_0 = P`
1. Compute :math:`Y_k = C(P_k, X)`
2. Compute :math:`(q_k, d_k) = Q(P_0, Y_k)`
3. Apply :math:`P_{k+1} = q_k(P_0)`
4. Stop if :math:`d_{k} - d_{k+1} < \tau`, else go to 1

Works for points, line segments, curves, anything that can be converted to
be compatible with the concept of having a "closest point".


Failure Modes
^^^^^^^^^^^^^

Mainly a discussion:

* Where can this go wrong?
* What are obvious failure modes?


Optimisations
^^^^^^^^^^^^^

Worse case performance, finding the closest point is :math:`O(N_p * N_x)`.

* Line minimisations, see [BeslMcKay1992]_
* Parallelism (OpenMP)
* Faster point search - :ref:`additional_resources:Algorithm - K-D Tree`, mentioned in [Zhang1994]_ who also proposed ICP.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/TLxWtXEbtFE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>




