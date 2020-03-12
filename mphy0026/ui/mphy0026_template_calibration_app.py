# -*- coding: utf-8 -*-

""" Harness to run Template Calibration application. """

#pylint: disable=duplicate-code

import time
from datetime import datetime
import numpy as np
import mphy0026.factory.tracker_factory as tf
import mphy0026.algorithms.compute_tracked_pointer_posn as pp


def template_calibration(tracker_type,
                         pointer,
                         reference,
                         offset,
                         fps,
                         number,
                         dump
                         ):
    """
    Computes the pointer tip, using a Template Calibration method.

    :param tracker_type: string [vega|aurora|aruco]
    :param pointer: .rom file, port number or ArUco tag number for pointer
    :param reference: .rom file, port number or ArUco tag number for reference
    :param offset: string containing x,y,z of divot in reference coordinates
    :param fps: frames per second
    :param number: number of samples to grab
    :param dump: if specified, file to dump data to
    """
    print("Template Calibration: ")
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

    print('Starting acquisition of ' + str(number_of_samples) \
          + ' points in ' + str(ms_per_loop / 1000) + ' seconds...')

    while counter < number_of_samples:
        start = datetime.now()

        tracker_frame = tracker.get_frame()

        pointer_tip = pp.compute_tracked_pointer_posn(tracker_frame,
                                                      tracker_type,
                                                      pointer,
                                                      reference,
                                                      divot_offset,
                                                      template_mode=True
                                                      )

        if pointer_tip is not None:
            samples[counter, :] = pointer_tip
            counter = counter + 1
            print(str(counter) + ":" + str(pointer_tip))

        end = datetime.now()
        elapsed = end - start
        sleeptime_ms = ms_per_loop - (elapsed.total_seconds() * 1000.0)

        if sleeptime_ms > 0:
            time.sleep(sleeptime_ms / 1000)

    if dump:
        np.savetxt(dump, samples)

    samples = np.mean(samples, axis=0, keepdims=True)
    print("Pointer offset from template calibration  is:" + str(samples))
