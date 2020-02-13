# -*- coding: utf-8 -*-

""" Harness to run grab pointer application. """

import time
from datetime import datetime
import numpy as np
import mphy0026.factory.tracker_factory as tf
import mphy0026.algorithms.compute_tracked_pointer_posn as pp


def run_grab_pointer(tracker_type,
                     pointer,
                     reference,
                     offset,
                     fps,
                     number,
                     dump,
                     mean
                     ):
    """
    Runs a simple grabbing loop, to sample data from a tracked pointer.

    :param tracker_type: string [vega|aurora|aruco]
    :param pointer: .rom file, port number or ArUco tag number for pointer
    :param reference: .rom file, port number or ArUco tag number for reference
    :param offset: string containing x,y,z of pointer offset.
    :param fps: number of frames per second
    :param number: number of samples
    :param dump: if specified, file to dump data to
    :param mean: if True will grab points and compute mean average
    :return:
    """

    print("Grab Pointer: ")
    print("  tracker_type = ", tracker_type)
    print("  pointer = ", pointer)
    print("  reference = ", reference)
    print("  offset = ", offset)
    print("  fps = ", fps)
    print("  number = ", number)
    print("  dump = ", dump)
    print("  mean = ", mean)

    if int(number) < 1:
        raise ValueError("The number of samples must be >=1")
    if int(fps) > 500:
        raise ValueError("The number of frames per second must be <= 500")
    tmp = offset.split(',')
    if len(tmp) != 3:
        raise ValueError("Pointer offset must be 3 comma separated values")
    pointer_offset = np.zeros((4, 1))
    pointer_offset[0][0] = float(tmp[0])
    pointer_offset[1][0] = float(tmp[1])
    pointer_offset[2][0] = float(tmp[2])
    pointer_offset[3][0] = 1.0

    tracker = tf.create_tracker(tracker_type, pointer, reference)

    frames_per_second = int(fps)
    ms_per_loop = 1000.0/float(frames_per_second)
    number_of_samples = int(number)

    counter = 0
    samples = np.ndarray((number_of_samples, 3))
    while counter < number_of_samples:
        start = datetime.now()

        tracker_frame = tracker.get_frame()

        pointer_posn = pp.compute_tracked_pointer_posn(tracker_frame,
                                                       tracker_type,
                                                       pointer,
                                                       reference,
                                                       pointer_offset
                                                       )
        if pointer_posn is not None:
            samples[counter, :] = pointer_posn
            counter = counter + 1
            print(str(counter) + ":" + str(pointer_posn))

        end = datetime.now()
        elapsed = end - start
        sleeptime_ms = ms_per_loop - (elapsed.total_seconds() * 1000.0)

        if sleeptime_ms > 0:
            time.sleep(sleeptime_ms / 1000)

    if mean:
        samples = np.mean(samples, axis=0)
        print("Mean is:" + str(samples))

    if dump:
        np.savetxt(dump, samples)
