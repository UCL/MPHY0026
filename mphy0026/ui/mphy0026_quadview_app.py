# -*- coding: utf-8 -*-

""" Harness to run QuadView application. """

import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QSizePolicy
import sksurgeryvtk.widgets.vtk_reslice_widget as rw
import mphy0026.factory.tracker_factory as tf


class QuadViewMainWidget(QtWidgets.QWidget):
    """
    QuadViewMainWidget to enable a VTK window, load stuff, start QTimer etc.
    """
    def __init__(self,
                 volume,
                 registration,
                 tracker,
                 config,
                 offset
                 ):
        super(QuadViewMainWidget, self).__init__()

        if not volume:
            raise ValueError("Volume image must be specified")
        if not registration:
            raise ValueError("Registration transform must be specified")
        if not offset:
            raise ValueError("Pointer offset must be specified")
        tmp = offset.split(',')
        if len(tmp) != 3:
            raise ValueError("Pointer offset must be 3 comma separated values")
        self.pointer_offset = (float(tmp[0]), float(tmp[1]), float(tmp[2]))

        self.tracker = tf.create_tracker(tracker, config)

        self.viewer = rw.TrackedSliceViewer(volume, self.tracker)

        self.setContentsMargins(0, 0, 0, 0)
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
                 tracker,
                 config,
                 offset
                 ):
        """
        Constructor, puts QuadViewMainWidget in window.
        """
        super().__init__()
        self.main_widget = QuadViewMainWidget(volume,
                                              registration,
                                              tracker,
                                              config,
                                              offset
                                              )

        self.setCentralWidget(self.main_widget)
        self.setContentsMargins(0, 0, 0, 0)


def run_quadview(volume,
                 registration,
                 tracker,
                 config,
                 offset):
    """
    Runs a basic 4 quadrant view with a tracked pointer.

    :param volume: filename/directory containing a volume (eg. CT) image
    :param registration: .txt file containing volume-to-tracker transformation
    :param tracker: string [vega|aurora|aruco]
    :param config: tracker config (e.g. rom file, ArUco file, EM tracker port)
    :param offset: string containing x,y,z of pointer offset.
    :return:
    """

    print("QuadView: ")
    print("  volume = ", volume)
    print("  registration = ", registration)
    print("  tracker = ", tracker)
    print("  config = ", config)
    print("  offset = ", offset)

    # Need this for all the Qt magic.
    app = QtWidgets.QApplication([])

    # This is a simple way of increasing the font size of all buttons globally.
    font = QtGui.QFont()
    font.setPointSize(20)
    app.setFont(font)

    # App is just one window, containing one widget, defined above.
    window = QuadViewMainWindow(volume,
                                registration,
                                tracker,
                                config,
                                offset)
    window.setContentsMargins(0, 0, 0, 0)
    window.show()

    # Start event loop.
    return sys.exit(app.exec_())
