# coding=utf-8

""" Harness to run Point/Surface-based registration algorithms. """

import os
import numpy as np
import sksurgeryvtk.models.vtk_surface_model as sm
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
    elif extension == '.vtk':
        model = sm.VTKSurfaceModel(file_name, (1.0, 1.0, 1.0))
        points = model.get_points_as_numpy()
    else:
        points = np.loadtxt(file_name)
    return points


def register_points(fixed_points,
                    moving_points):
    """
    Registers point sets and returns the 4x4 transformation and error measure.
    If the number of points is the same, will do Arun 1987, else, PCL's ICP.
    The output transform transforms moving points into the coordinate space of
    the fixed points.

    :param fixed_points: Nx3 ndarray of fixed points
    :param moving_points: Mx3 ndarray of moving points
    :return: 4x4 ndarray transform, FRE from point based, or residual from ICP.
    """

    transform = np.eye(4)

    if fixed_points.shape[0] == moving_points.shape[0]:
        transform, error = reg.register_point_sets(fixed_points, moving_points)
        print("Orthogonal Procrustes: ")
        print("  Transform = ", transform)
        print("  Fiducial Registration Error = ", error)
    else:
#        transformed_source_points = copy.deepcopy(moving_points)
        raise NotImplementedError("Need to fix ICP registration in this code!")

#        error = sks.icp(moving_points.astype(float),
#                        fixed_points.astype(float),
#                        1000,                # Number of iterations
#                        sys.float_info.max,  # Max correspondence distance
#                        0.0000001,           # Transformation epsilon
#                        0.0000001,           # Cost function epsilon
#                        False,               # Use LM-ICP
#                        transform,
#                        transformed_source_points)
#        print("Iterative Closest Point: ")
#        print("  Transform = ", transform)
#        print("  Residual = ", error)

    return transform, error


def load_points_and_register(fixed_points_file,
                             moving_points_file,
                             output_4x4_file=None,
                             initialise_4x4_file=None
                             ):
    """
    Loads points from file, registers, and optionally outputs transform.

    :param fixed_points_file: .vtk, .mps or .txt file of fixed points.
    :param moving_points_file: .vtk, .mps or .txt file of moving points.
    :param output_4x4_file: output file, to write 4x4 transform to.
    :param initialise_4x4_file: input file, to provide initialisation for ICP
    :return: 4x4 transform, FRE from point based, or residual from ICP.
    """

    fixed_points = load_file_of_points(fixed_points_file)
    moving_points = load_file_of_points(moving_points_file)

    initialise_transform = None

    if initialise_4x4_file is not None:
        # Can be simplified - exercise for the student ;-)
        initialise_transform = np.loadtxt(initialise_4x4_file)
        print("Initialising with:" + str(initialise_transform))
        homogenous_moving_points = np.ones((moving_points.shape[0],
                                            moving_points.shape[1] + 1,
                                            ))
        homogenous_moving_points[:, :-1] = moving_points
        transposed_moving_points = np.transpose(homogenous_moving_points)
        moving_points = np.matmul(initialise_transform,
                                  transposed_moving_points)
        moving_points = np.transpose(moving_points)
        moving_points = moving_points[:, 0:3]

    transform, error = register_points(fixed_points, moving_points)

    if initialise_transform is not None:
        transform = np.matmul(transform, initialise_transform)

    if output_4x4_file is not None:
        np.savetxt(output_4x4_file, transform)

    return transform, error
