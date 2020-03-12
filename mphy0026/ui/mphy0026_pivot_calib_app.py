# -*- coding: utf-8 -*-

""" Harness to run pivot calibration application. """

#pylint: disable=duplicate-code

import time
from datetime import datetime
import numpy as np
import mphy0026.factory.tracker_factory as tf
import mphy0026.algorithms.compute_tracked_pointer_posn as pp
from sksurgerycore.algorithms.pivot import pivot_calibration


def run_pivot_calibration(tracker_type,
                          pointer,
                          reference,
                          fps,
                          number,
                          dump
                          ):
    """
    Runs a simple grabbing loop, to sample data from a tracked pointer
    and tracked calibration object (like Medtronic, CASCination etc),
    and does pivot calibration.

    :param tracker_type: string [vega|aurora|aruco]
    :param pointer: .rom file, port number or ArUco tag number for pointer
    :param reference: .rom file, port number or ArUco tag number for reference
    :param fps: number of frames per second
    :param number: number of samples
    :param dump: if specified, file to dump data to
    """

    print("Grab Pointer: ")
    print("  tracker_type = ", tracker_type)
    print("  pointer = ", pointer)
    print("  reference = ", reference)
    print("  fps = ", fps)
    print("  number = ", number)
    print("  dump = ", dump)

    if int(number) < 1:
        raise ValueError("The number of samples must be >=1")
    if float(fps) > 500:
        raise ValueError("The number of frames per second must be <= 500")

    tracker = tf.create_tracker(tracker_type, pointer, reference)

    frames_per_second = float(fps)
    ms_per_loop = 1000.0/frames_per_second
    number_of_samples = int(number)

    counter = 0
    samples = np.ndarray((number_of_samples, 4, 4))

    print('Starting acquisition of ' + str(number_of_samples) \
          + ' points in ' + str(ms_per_loop / 1000) + ' seconds...')

    while counter < number_of_samples:
        start = datetime.now()

        tracker_frame = tracker.get_frame()

        tracking_pointer, tracking_reference, pointer_index, reference_index \
            = pp.check_tracker_data(tracker_frame,
                                    tracker_type,
                                    pointer,
                                    reference)

        if tracking_pointer and tracking_reference:

            pointer_matrix = tracker_frame[3][pointer_index]
            reference_matrix = tracker_frame[3][reference_index]

            # Compute relative tracker position (i.e. pointer-to-reference).
            pointer_to_reference = \
                np.linalg.inv(reference_matrix) @ pointer_matrix

            samples[counter, :, :] = pointer_to_reference
            counter = counter + 1

        # This timing stuff is just to delay the loop, so we get
        # approximately the right sampling rate, without extra threads.
        end = datetime.now()
        elapsed = end - start
        sleeptime_ms = ms_per_loop - (elapsed.total_seconds() * 1000.0)

        if sleeptime_ms > 0:
            time.sleep(sleeptime_ms / 1000)

    # Now compute pivot calibration.
    pointer_offset, rms = pivot_calibration(samples)

    # Save offset.
    if dump:
        np.savetxt(dump, pointer_offset.T)

    print("Pointer offset from pivot calibration: ",
          + str(pointer_offset.T) + ", RMS=" + str(rms))
