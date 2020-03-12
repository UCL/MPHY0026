# coding=utf-8

""" Command line processing for pivot calibration app. """

import argparse

from mphy0026 import __version__
from mphy0026.ui.mphy0026_pivot_calib_app import run_pivot_calibration


def main(args=None):
    """ Entry point for mphy0026_pivot_calib application. """

    parser = argparse.ArgumentParser(
        description='MPHY0026 - Pivot Calibration')

    parser.add_argument("-t",
                        "--tracker",
                        required=True,
                        help='Tracker type [vega|aurora|aruco]'
                        )

    parser.add_argument("-p",
                        "--pointer",
                        required=True,
                        help='Pointer .rom file, port number, '
                             'or ArUco tag number.')

    parser.add_argument("-r",
                        "--reference",
                        required=False,
                        help='Reference .rom file, port number, '
                             'or ArUco tag number of tracked reference object.'
                        )

    parser.add_argument("-f",
                        "--fps",
                        required=False,
                        default=20,
                        help='Frames per second.'
                        )

    parser.add_argument("-n",
                        "--number",
                        required=False,
                        default=1,
                        help='Number of samples.'
                        )

    parser.add_argument("-d",
                        "--dump",
                        required=False,
                        help='Dump data to file.'
                        )

    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "--version",
        action='version',
        version='MPHY0026 - Pivot Calibration version '
                + friendly_version_string)

    args = parser.parse_args(args)

    run_pivot_calibration(args.tracker,
                          args.pointer,
                          args.reference,
                          args.fps,
                          args.number,
                          args.dump
                          )
