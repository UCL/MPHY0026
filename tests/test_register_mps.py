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

    # ICP should complete, but produce a poor registration, as the starting point is poor.
    transform1, fre1 = ra.load_points_and_register('tests/data/pelvis/pelvis_cropped_decimated.vtk',
                                                   'tests/data/pelvis/Tracker_Surface_Scan.txt')

    # So, we can compute a point based registration.
    transform2, fre2 = ra.load_points_and_register('tests/data/pelvis/pelvis_cropped_ct_fiducial_markers.txt',
                                                   'tests/data/pelvis/Tracker_Fiducial_Markers.txt')

    # The above transform2 is saved in Tracker_to_pelvis_cropped.txt
    point_based_result = np.loadtxt('tests/data/pelvis/Tracker_to_pelvis_cropped.txt')
    assert np.allclose(transform2, point_based_result)

    # So, we can use transform2, or the previously saved result to initialise ICP.
    transform3, fre3 = ra.load_points_and_register('tests/data/pelvis/pelvis_cropped_decimated.vtk',
                                                   'tests/data/pelvis/Tracker_Surface_Scan.txt',
                                                   initialise_4x4_file='tests/data/pelvis/Tracker_to_pelvis_cropped.txt')

    assert fre3 < fre1
    assert np.allclose(transform2, transform3, rtol=0.1, atol=0.1)
