# -*- coding: utf-8 -*-

""" Harness to run Template Calibration application. """

import numpy as np
import mphy0026.factory.tracker_factory as tf
import mphy0026.algorithms.compute_tracked_pointer_posn as pp


def template_calibration(tracker_type,
                         pointer,
                         reference,
                         offset,
                         dump
                         ):
    """
    Computes the pointer tip, using a Template Calibration method.

    :param tracker_type: string [vega|aurora|aruco]
    :param pointer: .rom file, port number or ArUco tag number for pointer
    :param reference: .rom file, port number or ArUco tag number for reference
    :param offset: string containing x,y,z of divot in reference coordinates
    :param dump: if specified, file to dump data to
    """
    tracker = tf.create_tracker(tracker_type, pointer, reference)
    tracker_frame = tracker.get_frame()

    pointer_tip = pp.compute_tracked_pointer_posn(tracker_frame,
                                                  tracker_type,
                                                  pointer,
                                                  reference,
                                                  offset,
                                                  calibration_mode=True
                                                  )

    print("Pointer tip is:" + str(pointer_tip))

    if dump:
        np.savetxt(dump, pointer_tip)
