# -*- coding: utf-8 -*-

""" Harness to run pivot calibration application. """

#pylint: disable=duplicate-code

import time
from datetime import datetime
import numpy as np
import mphy0026.factory.tracker_factory as tf
import mphy0026.algorithms.compute_tracked_pointer_posn as pp


def run_pivot_calibration(tracker_type,
                          pointer,
                          reference,
                          offset,
                          fps,
                          number,
                          dump
                          ):
    """
    Runs a simple grabbing loop, to sample data from a tracked pointer
    and tracked calibration object (like Medtronic, CASCination etc).

    :param tracker_type: string [vega|aurora|aruco]
    :param pointer: .rom file, port number or ArUco tag number for pointer
    :param reference: .rom file, port number or ArUco tag number for reference
    :param offset: string containing x,y,z of calibration divot.
    :param fps: number of frames per second
    :param number: number of samples
    :param dump: if specified, file to dump data to
    """

    print("Grab Pointer: ")
    print("  tracker_type = ", tracker_type)
    print("  pointer = ", pointer)
    print("  reference = ", reference)
    print("  offset = ", offset)
    print("  fps = ", fps)
    print("  number = ", number)
    print("  dump = ", dump)

    if int(number) < 1:
        raise ValueError("The number of samples must be >=1")
    if float(fps) > 500:
        raise ValueError("The number of frames per second must be <= 500")

    divot_offset = pp.extract_pointer_offset(offset)

    tracker = tf.create_tracker(tracker_type, pointer, reference)

    frames_per_second = float(fps)
    ms_per_loop = 1000.0/frames_per_second
    number_of_samples = int(number)

    counter = 0
    samples = np.ndarray((number_of_samples, 3))

    print('Starting acquisition of {number_of_samples} \
          points in {ms_per_loop / 1000} seconds...')

    while counter < number_of_samples:
        start = datetime.now()

        tracker_frame = tracker.get_frame()

        # Yay! Exercise for the reader. A classic lecturing trick.

        # Grab both matrices.
        # Compute relative tracker position (i.e. pointer-to-reference).
        # Store big array.

        # This timing stuff is just to delay the loop, so we get
        # approximately the right sampling rate, without extra threads.
        end = datetime.now()
        elapsed = end - start
        sleeptime_ms = ms_per_loop - (elapsed.total_seconds() * 1000.0)

        if sleeptime_ms > 0:
            time.sleep(sleeptime_ms / 1000)

    # Now compute pivot calibration.
    # See, scikit-surgerycore.algorithms.pivot

    # Save offset.
    if dump:
        np.savetxt(dump, samples)
