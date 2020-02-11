# -*- coding: utf-8 -*-

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
        tracker_config = dict
        tracker_config['tracker type'] = tracker_type
        tracker_config['use quaternions'] = False

        if tracker_type == 'vega':
            tracker_config['ip address'] = '169.254.59.34'
            tracker_config['port'] = 8765

        for item in items:
            config_name = 'romfiles'
            if tracker_type == 'aurora':
                config_name = 'ports to use'

            if config_name in tracker_config.keys():
                tracker_config[config_name].append(item)
            else:
                tracker_config[config_name] = [item]
        tracker = nt.NDITracker(tracker_config)

    if tracker is None:
        raise ValueError("Failed to instantiate tracker")

    return tracker
