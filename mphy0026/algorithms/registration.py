# coding=utf-8

""" Module for computing a Point/Surface-based registration of point sets. """

import sksurgerycore.algorithms.procrustes as pr
import sksurgerycore.transforms.matrix as ma


def register_point_sets(fixed_points, moving_points):
    """
    Computes the registration of 2 point sets.

    :param fixed_points: Nx3 array of points
    :param moving_points:  Nx3 array of points.
    :return: 4x4 ndarray, FRE
    """
    rotation, translation, fre = pr.orthogonal_procrustes(fixed_points,
                                                          moving_points)

    transform = ma.construct_rigid_transformation(rotation, translation)

    return transform, fre
