# -*- coding: utf-8 -*-

""" Harness to run QuadView application. """

import sys
import numpy as np
from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QSizePolicy
import sksurgeryvtk.widgets.vtk_reslice_widget as rw
import mphy0026.factory.tracker_factory as tf
import mphy0026.algorithms.compute_tracked_pointer_posn as pp


class PointerDrivenQuadViewer(rw.TrackedSliceViewer):
    """
    Overrides the TrackedSliceViewer to correctly check tracking data
    and update according to the position of a tracked pointer and
    optionally a tracked reference marker.
    """
    def __init__(self,
                 dicom_dir,
                 tracker_device,
                 tracker_type,
                 pointer,
                 reference,
                 pointer_offset
                 ):
        super(PointerDrivenQuadViewer, self).__init__(dicom_dir, tracker_device)
        self.tracker_type = tracker_type
        self.pointer = pointer
        self.reference = reference
        self.pointer_offset = pointer_offset

    def update_position(self):
        """
        Retrives tracking data, and computes pointer position.
        """
        tracker_frame = self.tracker.get_frame()
        pointer_posn = pp.compute_tracked_pointer_posn(tracker_frame,
                                                       self.tracker_type,
                                                       self.pointer,
                                                       self.reference,
                                                       self.pointer_offset
                                                       )
        if pointer_posn is not None:
            self.update_slice_positions(pointer_posn[0],
                                        pointer_posn[1],
                                        pointer_posn[2])


class QuadViewMainWidget(QtWidgets.QWidget):
    """
    QuadViewMainWidget to enable a VTK window, load stuff, start QTimer etc.
    """
    def __init__(self,
                 volume,
                 registration,
                 tracker_type,
                 pointer,
                 reference,
                 offset
                 ):
        super(QuadViewMainWidget, self).__init__()

        if not volume:
            raise ValueError("Volume image must be specified")
        if not registration:
            raise ValueError("Registration transform must be specified")
        pointer_offset = pp.extract_pointer_offset(offset)

        self.tracker_device = tf.create_tracker(tracker_type,
                                                pointer,
                                                reference)

        self.viewer = PointerDrivenQuadViewer(volume,
                                              self.tracker_device,
                                              tracker_type,
                                              pointer,
                                              reference,
                                              pointer_offset
                                              )

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
                 pointer,
                 reference,
                 offset
                 ):
        """
        Constructor, puts QuadViewMainWidget in window.
        """
        super().__init__()
        self.main_widget = QuadViewMainWidget(volume,
                                              registration,
                                              tracker,
                                              pointer,
                                              reference,
                                              offset
                                              )

        self.setCentralWidget(self.main_widget)
        self.setContentsMargins(0, 0, 0, 0)


def run_quadview(volume,
                 registration,
                 tracker,
                 pointer,
                 reference,
                 offset):
    """
    Runs a basic 4 quadrant view with a tracked pointer.

    :param volume: filename/directory containing a volume (eg. CT) image
    :param registration: .txt file containing volume-to-tracker transformation
    :param tracker: string [vega|aurora|aruco]
    :param pointer: .rom file, port number or ArUco tag number for pointer
    :param reference: .rom file, port number or ArUco tag number for reference
    :param offset: string containing x,y,z of pointer offset.
    :return:
    """

    print("QuadView: ")
    print("  volume = ", volume)
    print("  registration = ", registration)
    print("  tracker = ", tracker)
    print("  pointer = ", pointer)
    print("  reference = ", reference)
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
                                pointer,
                                reference,
                                offset)
    window.setContentsMargins(0, 0, 0, 0)
    window.show()

    # Start event loop.
    return sys.exit(app.exec_())
