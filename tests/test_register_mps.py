# -*- coding: utf-8 -*-

""" Tests for registering .mps files"""

import six
import pytest
import numpy as np
import mphy0026.ui.mphy0026_register_app as ra


def test_register_pointset_to_self():

    transform, fre = ra.load_points_and_register('tests/data/liver_phantom/ct_landmarks.mps',
                                                 'tests/data/liver_phantom/ct_landmarks.mps')
    assert np.allclose(transform, np.eye(4))


def test_mps_and_txt_give_same_result():

    transform1, fre1 = ra.load_points_and_register('tests/data/pelvis/pelvis_cropped_ct_fiducial_markers.mps',
                                                   'tests/data/pelvis/Tracker_Fiducial_Markers.txt')

    transform2, fre2 = ra.load_points_and_register('tests/data/pelvis/pelvis_cropped_ct_fiducial_markers.txt',
                                                   'tests/data/pelvis/Tracker_Fiducial_Markers.txt')

    assert np.allclose(transform1, transform2)


def test_pcl_icp():

    # Should complete, but produce a poor registration.
    transform1, fre1 = ra.load_points_and_register('tests/data/pelvis/pelvis_cropped_decimated.vtk',
                                                   'tests/data/pelvis/Tracker_Surface_Scan.txt')

    # So, we initialise with point based:
    transform2, fre2 = ra.load_points_and_register('tests/data/pelvis/pelvis_cropped_decimated.vtk',
                                                   'tests/data/pelvis/Tracker_Surface_Scan.txt',
                                                   initialise_4x4_file='tests/data/pelvis/Tracker_to_pelvis_cropped.txt')

    print("Matt, transform1=" + str(transform1))
    print("Matt, fre1=" + str(fre1))
    print("Matt, transform2=" + str(transform2))
    print("Matt, fre2=" + str(fre2))
