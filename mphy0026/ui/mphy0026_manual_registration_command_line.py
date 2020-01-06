# -*- coding: utf-8 -*-

""" Command line processing prior to launching manual registration demo. """

import argparse
from mphy0026 import __version__
from mphy0026.ui.mphy0026_manual_registration_demo import run_app


def create_manual_reg_parser():
    """
    Creates the program parser.
    :return: argparse.ArgumentParser()
    """
    parser = argparse.ArgumentParser(description='model2camera')

    parser.add_argument("-b", "--background",
                        required=True,
                        type=str,
                        help="Background image.")

    parser.add_argument("-m", "--model",
                        required=True,
                        type=str,
                        help="Model file name (e.g. vtk surface)")

    parser.add_argument("-c", "--camera",
                        required=True,
                        type=str,
                        help="Camera matrix [3x3] file name")

    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "-v", "--version",
        action='version',
        version='mphy0026_manual_registration version '
                + friendly_version_string)
    return parser


def main(args=None):
    """
    Entry point for the manual registration demo application.
    """
    parser = create_manual_reg_parser()
    parsed_args = parser.parse_args(args)
    run_app(parsed_args.background,
            parsed_args.model,
            parsed_args.camera)
