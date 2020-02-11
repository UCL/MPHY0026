# -*- coding: utf-8 -*-

""" Harness to run grab pointer application. """


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
