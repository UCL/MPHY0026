# -*- coding: utf-8 -*-

""" Module to point pointer computations. """

import numpy as np


def _get_aruco_item_index(handles, value):
    """
    From an array of handles, returns the index that matches the given value.
    :param handles: handles of tracked items returned from ArUco tracker.
    :param value: value to search for, essentially, a tag number
    :return: None or array index.
    """
    if handles is None or not handles:
        return None

    index_of_item = np.where(np.array(handles) == int(value))

    if index_of_item is None or not index_of_item:
        return None

    return index_of_item[0][0]


def _check_tracker_data(tracker_frame,
                        tracker_type,
                        pointer,
                        reference
                        ):

    """
    Checks what data is valid from tracker.

    :param tracker_frame: frame of data
    :param tracker_type: string [vega|aurora|aruco]
    :param pointer: config information for pointer
    :param reference: optional config information for reference
    :return:
    """
    if tracker_frame is None:
        raise ValueError("Failed to get data from tracker.")
    if not tracker_frame[4]: # ArUco returns empty list
        return None
    pointer_index = 0
    reference_index = 1
    tracking_pointer = False
    tracking_reference = False
    if tracker_type == 'aruco':
        pointer_index = _get_aruco_item_index(tracker_frame[0], pointer)

        if reference:
            reference_index = _get_aruco_item_index(tracker_frame[0], reference)

    if not np.isnan(tracker_frame[4][pointer_index]):
        tracking_pointer = True

    if reference is not None \
            and not np.isnan(tracker_frame[4][reference_index]):
        tracking_reference = True

    return tracking_pointer, tracking_reference, pointer_index, reference_index


def extract_pointer_offset(offset_as_filename):
    """
    Given a filename containing a pointer tip offset,
    returns 4x1 point as ndarray.
    """
    if not offset_as_filename:
        raise ValueError("Pointer offset filename must be specified")
    tmp = np.loadtxt(offset_as_filename)
    pointer_offset = np.zeros((4, 1))
    pointer_offset[0][0] = float(tmp[0])
    pointer_offset[1][0] = float(tmp[1])
    pointer_offset[2][0] = float(tmp[2])
    pointer_offset[3][0] = 1.0
    return pointer_offset


def compute_tracked_pointer_posn(tracker_frame,
                                 tracker_type,
                                 pointer,
                                 reference,
                                 offset,
                                 calibration_mode=False):
    """
    Computes the pointer position, or returns None if not enough items tracked.

    :param tracker_frame: tracker frame
    :param tracker_type: tracker type must be [vega|aurora|aruco]
    :param pointer: config information for pointer
    :param reference: optional config information for reference
    :param offset: 4x1 tip offset in pointer coordinate system
    :param calibration_mode: If True, you can calibrate pointer tip, using ref.
    :return: 1x3 ndarray of pointer tip
    """

    tracking_pointer, tracking_reference, pointer_index, reference_index \
        = _check_tracker_data(tracker_frame,
                              tracker_type,
                              pointer,
                              reference)

    if not tracking_pointer:
        raise ValueError("Not tracking pointer")

    if calibration_mode and not tracking_reference:
        raise ValueError("In calibration mode, the reference must be tracked.")

    pointer_posn = None

    # i.e. if we didn't intend to use a reference, and we are tracking pointer.
    if reference is None and tracking_pointer:

        pointer_to_world = tracker_frame[3][pointer_index]
        world_point = np.matmul(pointer_to_world, offset)
        world_point_transposed = (np.transpose(world_point))[0, 0:3]
        pointer_posn = world_point_transposed

    elif tracking_pointer and tracking_reference:

        pointer_to_world = tracker_frame[3][pointer_index]
        reference_to_world = tracker_frame[3][reference_index]

        print("Matt, pointer_to_world=" + str(pointer_to_world))
        print("Matt, reference_to_world=" + str(reference_to_world))

        if calibration_mode:
            print("Matt, calibration_mode")
            print("Matt, offset=" + str(offset))
            print("Matt, reference_to_world=" + str(reference_to_world))

            world_to_pointer = np.linalg.inv(pointer_to_world)
            divot_in_world = np.matmul(reference_to_world,
                                       offset)
            print("Matt, divot_in_world=" + str(divot_in_world))
            divot_in_pointer = np.matmul(world_to_pointer,
                                         divot_in_world)
            print("Matt, divot_in_pointer=" + str(divot_in_pointer))
            pointer_tip_transposed = \
                (np.transpose(divot_in_pointer))[0, 0:3]
            pointer_posn = pointer_tip_transposed
        else:
            world_to_reference = np.linalg.inv(reference_to_world)
            pointer_in_world = np.matmul(pointer_to_world,
                                         offset)
            pointer_in_ref = np.matmul(world_to_reference,
                                       pointer_in_world)
            pointer_in_ref_transposed = \
                (np.transpose(pointer_in_ref))[0, 0:3]
            pointer_posn = pointer_in_ref_transposed

    return pointer_posn
