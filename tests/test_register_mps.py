# -*- coding: utf-8 -*-

""" Tests for registering .mps files"""

import six
import pytest
import numpy as np
import mphy0026.ui.mphy0026_register_app as ra


def test_register_pointset_to_self():

    transform, fre = ra.run_registration('tests/data/liver_phantom/ct_landmarks.mps',
                                         'tests/data/liver_phantom/ct_landmarks.mps',
                                         None
                                         )
    assert np.allclose(transform, np.eye(4))


def test_register_pelvis_gipl():

    transform1, fre1 = ra.run_registration('tests/data/pelvis/pelvis_cropped_ct_fiducial_markers.mps',
                                           'tests/data/pelvis/Tracker_Fiducial_Markers.txt',
                                           None
                                           )

    transform2, fre2 = ra.run_registration('tests/data/pelvis/pelvis_cropped_ct_fiducial_markers.txt',
                                           'tests/data/pelvis/Tracker_Fiducial_Markers.txt',
                                           None
                                           )

    assert np.allclose(transform1, transform2)
