# coding=utf-8

""" CLI for BARD chessboard overlay demo. """

import argparse

from mphy0026 import __version__
from mphy0026.ui.mphy0026_chessboard_overlay_app \
    import run_chessboard_overlay


def main(args=None):

    """ Entry point for bardChessboardOverlay application. """

    parser = argparse.ArgumentParser(
        description='Basic Augmented Reality Demo - '
                    'Video Chessboard Oerlay')

    parser.add_argument("-c", "--config",
                        required=True,
                        type=str,
                        help="Configuration file containing the parameters.")

    parser.add_argument("-d", "--calib_dir",
                        required=True,
                        type=str,
                        help="Directory containing calibration data.")

    parser.add_argument("-o", "--overlay_offset",
                        required=False,
                        type=int,
                        default=0,
                        help="Offset of overlaid image from chessboard")

    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "--version",
        action='version',
        version='scikit-surgerybard version ' + friendly_version_string)

    args = parser.parse_args(args)

    run_chessboard_overlay(args.config, args.calib_dir, args.overlay_offset)
