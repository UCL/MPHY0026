# coding=utf-8

""" Harness to run QuadView application. """

import os
import numpy as np
import sksurgerycore.io.load_mps as lmps
import mphy0026.algorithms.registration as reg


def run_quadview(volume,
                 registration,
                 config,
                 offset):
    """
    Runs a basic 4 quadrant view with a tracked pointer.

    :param volume: filename/directory containing a volume (eg. CT) image
    :param registration: .txt file containing volume-to-tracker transformation
    :param config: tracker config (e.g. rom file, ArUco file, EM tracker port)
    :param offset: string containing x,y,z of pointer offset.
    :return:
    """

    print("QuadView: ")
    print("  volume = ", volume)
    print("  registration = ", registration)
    print("  config = ", config)
    print("  offset = ", offset)
