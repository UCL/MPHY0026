# coding=utf-8

""" Harness to run Point/Surface-based registration algorithms. """

import os
import numpy as np
import sksurgerycore.io.load_mps as lmps
import mphy0026.algorithms.registration as reg


def load_file_of_points(file_name):
    """
    Loads an MITK .mps file, or .txt file (rows of x y z).
    :param file_name: string containing path to a valid file
    :return: Nx3 ndarray
    """
    extension = os.path.splitext(file_name)[1]
    if extension == '.mps':
        _, points = lmps.load_mps(file_name)
    else:
        points = np.loadtxt(file_name)
    return points


def run_registration(fixed_points_file,
                     moving_points_file,
                     output_file):
    """
    Registers point sets, optionally saves the 4x4 transform to file
    and returns the 4x4 transformation and FRE.

    :param fixed_points_file: .mps or .txt file of fixed points
    :param moving_points_file: .mps or .txt file of moving points
    :param output_file: .txt file of 4x4 transformation
    :return: 4x4 transform, FRE
    """

    fixed_points = load_file_of_points(fixed_points_file)
    moving_points = load_file_of_points(moving_points_file)
    transform, fre = reg.register_point_sets(fixed_points, moving_points)

    if output_file:
        np.savetxt(output_file, transform)

    print("Orthogonal Procrustes: ")
    print("  Transform = ", transform)
    print("  Fiducial Registration Error = ", fre)

    return transform, fre
