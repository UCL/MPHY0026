# -*- coding: utf-8 -*-

""" Module for factory methods. """

import os
import sksurgeryarucotracker.arucotracker as at
import sksurgerynditracker.nditracker as nt


def create_tracker(tracker_type, config):
    """
    Logic for creating a tracker.

    :param tracker_type: string, must be one of [vega|aurora|aruco]
    :param config: comma separated list of rom files, ports, or tag numbers
    :return: tracker object
    """
    if not tracker_type:
        raise ValueError("Tracker type must be specified")
    if tracker_type not in ('vega', 'aurora', 'aruco'):
        raise ValueError("Tracker type must be [vega|aurora|aruco]")
    if not config:
        raise ValueError("Config must be specified")

    items = config.split(',')
    if len(items) == 0:
        raise ValueError("Config doesn't contain items. Programming bug??")

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
        for item in items:
            if tracker_type != 'aurora':
                item = os.path.abspath(item)
            things_to_track.append(item)
        tracker_config[config_name] = things_to_track

        print("Initialising NDI Tracker with:" + str(tracker_config))
        tracker = nt.NDITracker(tracker_config)
        tracker.start_tracking()

    if tracker is None:
        raise ValueError("Failed to instantiate tracker")

    return tracker
