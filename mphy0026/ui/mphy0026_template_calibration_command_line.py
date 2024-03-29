# coding=utf-8

""" Command line processing for Template Calibration. """

import argparse

from mphy0026 import __version__
import mphy0026.ui.mphy0026_template_calibration_app as tc


def main(args=None):

    """ Entry point for mphy0026_template_calibration application. """

    parser = argparse.ArgumentParser(
        description='MPHY0026 - Template Calibration')

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
                        required=True,
                        help='Reference .rom file, port number, '
                             'or ArUco tag number.'
                        )

    parser.add_argument("-o",
                        "--offset",
                        required=True,
                        type=str,
                        help='File containing x,y,z of calibration divot.'
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
                        default=100,
                        help='Number of samples.'
                        )

    parser.add_argument("-d",
                        "--dump",
                        required=False,
                        help='Output file, to write pointer tip to.'
                        )

    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "--version",
        action='version',
        version='MPHY0026 - Template Calibration version '
                + friendly_version_string)

    args = parser.parse_args(args)

    tc.run_template_calibration(args.tracker,
                                args.pointer,
                                args.reference,
                                args.offset,
                                args.fps,
                                args.number,
                                args.dump
                                )
