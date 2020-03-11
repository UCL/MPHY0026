# coding=utf-8

""" Command line processing for grab pointer app. """

import argparse

from mphy0026 import __version__
from mphy0026.ui.mphy0026_grab_pointer_app import run_grab_pointer


def main(args=None):
    """ Entry point for mphy0026_grab_pointer application. """

    parser = argparse.ArgumentParser(
        description='MPHY0026 - Grab Pointer')

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
                             'or ArUco tag number.'
                        )

    parser.add_argument("-o",
                        "--offset",
                        required=True,
                        help='Comma separated x,y,z of pointer offset.'
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

    parser.add_argument("-m",
                        "--mean",
                        dest='mean',
                        action='store_true')

    parser.add_argument("-reg",
                        "--registration",
                        required=False,
                        help='Registration transformation. Tracker to image.')

    parser.add_argument("-fid",
                        "--fiducials",
                        required=False,
                        help='Fiducials, in image space.')

    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "--version",
        action='version',
        version='MPHY0026 - Grab Pointer version ' + friendly_version_string)

    args = parser.parse_args(args)

    run_grab_pointer(args.tracker,
                     args.pointer,
                     args.reference,
                     args.offset,
                     args.fps,
                     args.number,
                     args.dump,
                     args.mean,
                     args.registration,
                     args.fiducials
                     )
