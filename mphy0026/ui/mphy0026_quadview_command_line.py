# coding=utf-8

""" Command line processing for QuadView visualisation. """

import argparse

from mphy0026 import __version__
from mphy0026.ui.mphy0026_quadview_app import run_quadview


def main(args=None):
    """ Entry point for mphy0026_quadview application. """

    parser = argparse.ArgumentParser(
        description='MPHY0026 - QuadView')

    parser.add_argument("-v", "--volume",
                        required=True,
                        help='Volume image'
                        )

    parser.add_argument("-r",
                        "--registration",
                        required=True,
                        help='Text (.txt) file of volume-to-tracker '
                             'transformation'
                        )

    parser.add_argument("-c",
                        "--config",
                        required=True,
                        help='Config for your tracked pointer'
                        )

    parser.add_argument("-o",
                        "--offset",
                        required=True,
                        help='Comma separated x,y,z of tracker offset'
                        )

    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "--version",
        action='version',
        version='MPHY0026 - QuadView version ' + friendly_version_string)

    args = parser.parse_args(args)

    run_quadview(args.volume,
                 args.registration,
                 args.config,
                 args.offset
                 )
