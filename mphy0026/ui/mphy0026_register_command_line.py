# coding=utf-8

""" Command line processing for Point-Based registration. """

import argparse

from mphy0026 import __version__
from mphy0026.ui.mphy0026_register_app import run_registration


def main(args=None):
    """ Entry point for mphy0026_register application. """

    parser = argparse.ArgumentParser(
        description='MPHY0026 - Registration')

    parser.add_argument("-f", "--fixed",
                        required=True,
                        help='Fixed points, either .mps or .txt'
                        )

    parser.add_argument("-m",
                        "--moving",
                        required=True,
                        help='Moving points, either .mps or .txt'
                        )

    parser.add_argument("-o",
                        "--output",
                        help='Output .txt file containing 4x4 transformation'
                        )

    parser.add_argument("-i",
                        "--initialise",
                        required=False,
                        help='Input .txt file containing 4x4 '
                             'transformation to initialise ICP'
                        )

    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "--version",
        action='version',
        version='MPHY0026 - Registration version ' + friendly_version_string)

    args = parser.parse_args(args)

    run_registration(args.fixed,
                     args.moving,
                     args.output,
                     args.initialise
                     )
