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

