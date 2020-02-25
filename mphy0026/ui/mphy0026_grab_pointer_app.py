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
                     mean,
                     registration,
                     fiducials
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
    :param registration: if this and fiducials supplied, will work out FLE
    :param fiducials: if this and registration supplied, will work out FLE
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
    print("  registration = ", registration)
    print("  fiducials = ", fiducials)

    if int(number) < 1:
        raise ValueError("The number of samples must be >=1")
    if float(fps) > 500:
        raise ValueError("The number of frames per second must be <= 500")
    pointer_offset = pp.extract_pointer_offset(offset)

    tracker = tf.create_tracker(tracker_type, pointer, reference)

    frames_per_second = float(fps)
    ms_per_loop = 1000.0/frames_per_second
    number_of_samples = int(number)

    counter = 0
    samples = np.ndarray((number_of_samples, 3))

    print(f'Starting acquisition of {number_of_samples} \
          points in {ms_per_loop / 1000} seconds...')

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
        samples = np.mean(samples, axis=0, keepdims=True)
        print("Mean is:" + str(samples))

    if dump:
        np.savetxt(dump, samples)

    if registration and fiducials:
        registration_matrix = np.loadtxt(registration)
        fiducials = np.loadtxt
        pointer_posn = np.mean(samples, axis=0, keepdims=True)
        pointer = np.ones((4, 1))
        pointer[0][0] = pointer_posn[0][0]
        pointer[1][0] = pointer_posn[0][1]
        pointer[2][0] = pointer_posn[0][2]
        pointer[3][0] = 1
        transformed_point = np.matmul(registration_matrix, pointer)
        transformed_point = (np.transpose(transformed_point))[:, 0:3]
        print("Point:" + str(transformed_point))

        for i in range(fiducials.shape[0]):
            squared = (fiducials[i][0] - transformed_point[0][0]) \
                    * (fiducials[i][0] - transformed_point[0][0]) \
                    + (fiducials[i][1] - transformed_point[0][1]) \
                    * (fiducials[i][1] - transformed_point[0][1]) \
                    + (fiducials[i][2] - transformed_point[0][2]) \
                    * (fiducials[i][2] - transformed_point[0][2])
            distance = np.sqrt(squared)
            print("Point:" + str(i)
                  + ", fiducial=" + str(fiducials[i])
                  + ", distance=" + str(distance)
                  )
