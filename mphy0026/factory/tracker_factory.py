# -*- coding: utf-8 -*-

""" Module for factory methods. """

import sksurgeryarucotracker.arucotracker as at
import sksurgerynditracker.nditracker as nt


def create_tracker(tracker_type, pointer, reference):
    """
    Logic for creating a tracker.

    :param tracker_type: string, must be one of [vega|aurora|aruco]
    :param pointer: .rom file, port number or ArUco tag number for pointer
    :param reference: .rom file, port number or ArUco tag number for reference
    :return: tracker object
    """
    if not tracker_type:
        raise ValueError("Tracker type must be specified")
    if tracker_type not in ('vega', 'aurora', 'aruco'):
        raise ValueError("Tracker type must be [vega|aurora|aruco]")
    if not pointer:
        raise ValueError("Pointer must be specified")

    tracker = None

    if tracker_type == 'aruco':
        tracker = at.ArUcoTracker({})
        tracker.start_tracking()
    else:
        tracker_config = dict()
        tracker_config['tracker type'] = tracker_type
        tracker_config['use quaternions'] = False

        if tracker_type == 'vega':
            tracker_config['ip address'] = '169.254.59.34'
            tracker_config['port'] = 8765

        config_name = 'romfiles'
        if tracker_type == 'aurora':
            config_name = 'ports to use'

        things_to_track = []
        things_to_track.append(pointer)
        if reference is not None:
            things_to_track.append(reference)
        tracker_config[config_name] = things_to_track

        print("Initialising NDI Tracker with:" + str(tracker_config))
        tracker = nt.NDITracker(tracker_config)
        tracker.start_tracking()

    if tracker is None:
        raise ValueError("Failed to instantiate tracker")

    return tracker
