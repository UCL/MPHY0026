# coding=utf-8

""" Command line processing for overlay visualisation. """

import argparse

from mphy0026 import __version__
from mphy0026.ui.mphy0026_overlay_app import run_overlay


def main(args=None):
    """ Entry point for mphy0026_overlay application. """

    parser = argparse.ArgumentParser(
        description='MPHY0026 - Overlay')

    parser.add_argument("-reg",
                        "--registration",
                        required=False,
                        help='Text (.txt) file of tracker-to-image '
                             'transformation'
                        )

    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "--version",
        action='version',
        version='MPHY0026 - overlay version ' + friendly_version_string)

    args = parser.parse_args(args)

    run_overlay()
