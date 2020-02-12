# -*- coding: utf-8 -*-

""" Harness to run grab pointer application. """

import time
from datetime import datetime
import numpy as np
import mphy0026.factory.tracker_factory as tf


def run_grab_pointer(tracker,
                     config,
                     offset,
                     fps,
                     number,
                     dump
                     ):
    """
    Runs a simple grabbing loop, to sample data from a tracked pointer.

    :param tracker: string [vega|aurora|aruco]
    :param config: tracker config (e.g. rom file, ArUco file, EM tracker port)
    :param offset: string containing x,y,z of pointer offset.
    :param fps: number of frames per second
    :param number: number of samples
    :param dump: if specified, file to dump data to
    :return:
    """

    print("Grab Pointer: ")
    print("  tracker = ", tracker)
    print("  config = ", config)
    print("  offset = ", offset)
    print("  fps = ", fps)
    print("  number = ", number)
    print("  dump = ", dump)

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

    tracker = tf.create_tracker(tracker, config)

    frames_per_second = int(fps)
    ms_per_loop = 1000.0/float(frames_per_second)
    number_of_samples = int(number)

    counter = 0
    samples = np.ndarray((number_of_samples, 3))
    while counter < number_of_samples:
        start = datetime.now()
        tracker_frame = tracker.get_frame()

        # Aruco returns empty list if nothing tracker, NDI returns 'NaN' (I think)
        anything_tracked = False if tracker_frame[3] == None or tracker_frame == 'NaN' else True
        if not anything_tracked:
            continue

        if len(tracker_frame[3]) == 1:
            if not np.isnan(tracker_frame[4][0]):
                pointer_to_world = tracker_frame[3][0]
                world_point = np.multiply(pointer_to_world, pointer_offset)
                print(np.transpose(world_point))
                samples[counter,:] = (np.transpose(world_point))[3, 0:3]
                counter = counter + 1
                time.sleep(1)
        elif len(tracker_frame[3]) == 2:
            if not np.isnan(tracker_frame[4][0]) and not \
                    np.isnan(tracker_frame[4][1]):
                pointer_to_world = tracker_frame[3][0]
                reference_to_world = tracker_frame[3][1]
                world_to_reference = np.linalg.inv(reference_to_world)
                pointer_in_world = np.multiply(pointer_to_world,
                                               pointer_offset)
                pointer_in_ref = np.multiply(world_to_reference,
                                             pointer_in_world)
                samples[counter,:] = (np.transpose(world_point))[3, 0:3]
                counter = counter + 1
        else:
            raise ValueError("We should only be tracking 2 objects")
        end = datetime.now()
        elapsed = end - start
        sleeptime_ms = ms_per_loop - (elapsed.total_seconds() * 1000.0)

        if sleeptime_ms > 0:
            time.sleep(sleeptime_ms / 1000)

    if dump:
        np.savetxt(dump, samples)
