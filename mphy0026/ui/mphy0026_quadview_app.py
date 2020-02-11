# -*- coding: utf-8 -*-

""" Harness to run QuadView application. """

import os
import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QSizePolicy
import sksurgeryarucotracker.arucotracker as at
import sksurgerynditracker.nditracker as nt
import sksurgeryvtk.widgets.vtk_reslice_widget as rw


class QuadViewMainWidget(QtWidgets.QWidget):
    """
    QuadViewMainWidget to enable a VTK window, load stuff, start QTimer etc.
    """
    def __init__(self,
                 volume,
                 registration,
                 offset,
                 config
                 ):
        super(QuadViewMainWidget, self).__init__()

        if not volume:
            raise ValueError("Volume image must be specified")
        if not registration:
            raise ValueError("Registration transform must be specified")
        if not offset:
            raise ValueError("Pointer offset must be specified")

        self.setContentsMargins(0, 0, 0, 0)

        if config is None:
            self.tracker = at.ArUcoTracker({})
            self.tracker.start_tracking()
        elif os.path.isfile(config):
            tracker_config = dict
            tracker_config['tracker type'] = 'vega'
            tracker_config['use quaternions'] = False
            tracker_config['ip address'] = '169.254.59.34'
            tracker_config['port'] = 8765
            tracker_config['romfiles'] = config
            self.tracker = nt.NDITracker(tracker_config)
        elif isinstance(int(config), int):
            tracker_config = dict
            tracker_config['tracker type'] = 'aurora'
            tracker_config['use quaternions'] = False
            tracker_config['ports to use'] = config
            self.tracker = nt.NDITracker(tracker_config)
        else:
            raise ValueError("Couldn't determine tracker type")

        self.viewer = rw.TrackedSliceViewer(volume, self.tracker)

        self.viewer_size_policy = \
            QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.viewer.setSizePolicy(self.viewer_size_policy)

        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.addWidget(self.viewer)

        self.viewer.start()


class QuadViewMainWindow(QtWidgets.QMainWindow):
    """
    QuadViewMainWindow.
    """
    def __init__(self,
                 volume,
                 registration,
                 offset,
                 config
                 ):
        """
        Constructor, puts QuadViewMainWidget in window.
        """
        super().__init__()
        self.main_widget = QuadViewMainWidget(volume,
                                              registration,
                                              offset,
                                              config
                                              )

        self.setCentralWidget(self.main_widget)
        self.setContentsMargins(0, 0, 0, 0)


def run_quadview(volume,
                 registration,
                 offset,
                 config):
    """
    Runs a basic 4 quadrant view with a tracked pointer.

    :param volume: filename/directory containing a volume (eg. CT) image
    :param registration: .txt file containing volume-to-tracker transformation
    :param offset: string containing x,y,z of pointer offset.
    :param config: tracker config (e.g. rom file, ArUco file, EM tracker port)
    :return:
    """

    print("QuadView: ")
    print("  volume = ", volume)
    print("  registration = ", registration)
    print("  offset = ", offset)
    print("  config = ", config)

    # Need this for all the Qt magic.
    app = QtWidgets.QApplication([])

    # This is a simple way of increasing the font size of all buttons globally.
    font = QtGui.QFont()
    font.setPointSize(20)
    app.setFont(font)

    # App is just one window, containing one widget, defined above.
    window = QuadViewMainWindow(volume,
                                registration,
                                offset,
                                config)
    window.setContentsMargins(0, 0, 0, 0)
    window.show()

    # Start event loop.
    return sys.exit(app.exec_())
