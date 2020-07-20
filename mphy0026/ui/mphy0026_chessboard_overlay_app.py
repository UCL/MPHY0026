# coding=utf-8

""" Application to detect chessboards, and project video feed
back onto the image plane. """

import sys
import numpy as np
import cv2
import vtk
from PySide2.QtCore import QTimer
from PySide2 import QtWidgets

from sksurgerycore.configuration.configuration_manager import \
    ConfigurationManager
import sksurgeryimage.calibration.chessboard_point_detector as cpd
from sksurgerybard.algorithms.bard_config_algorithms import \
    configure_camera
from sksurgeryvtk.widgets.vtk_overlay_window import VTKOverlayWindow
import sksurgeryvtk.camera.vtk_camera_model as cm

# pylint: disable=too-many-branches, too-many-instance-attributes

class ChessboardOverlay():
    """Chessboard Overlay App"""
    def __init__(self, configuration, calib_dir, overlay_offset):

        source = configuration.get("source", 1)
        corners = configuration.get("corners")
        self.size = configuration.get("square size in mm")
        window_size = configuration.get("window size")
        self.overlay_offset = overlay_offset

        _, self.intrinsics, self.distortion, _ = \
            configure_camera(configuration, calib_dir)

        if corners is None:
            raise ValueError("You must specify the number of internal corners")

        if self.size is None:
            raise ValueError("You must specify the size of each square in mm.")

        if window_size is None:
            raise ValueError("You must specify the window size.")

        if self.intrinsics is None:
            raise ValueError("Couldn't load intrinsic parameters")

        if self.distortion is None:
            raise ValueError("Couldn't load self.distortion parameters")

        self.corners = (corners[0], corners[1])

        self.detector = cpd.ChessboardPointDetector(self.corners, self.size)
        self.num_pts = corners[0] * corners[1]

        self.cap = cv2.VideoCapture(int(source))

        if not self.cap.isOpened():
            raise RuntimeError("Failed to open camera:" + str(source))

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, window_size[0])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, window_size[1])

        print("Video feed set to ("
              + str(window_size[0]) + " x " + str(window_size[1]) + ")")

        self.vtk_overlay_window = VTKOverlayWindow()
        self.timer = None
        self.update_rate = 15

        self.ultrasound_actor = vtk.vtkImageActor()
        self.ultrasound_actor.SetInputData(
            self.vtk_overlay_window.image_importer.GetOutput())
        self.vtk_overlay_window.foreground_renderer.AddActor(
            self.ultrasound_actor)

        f_x = self.intrinsics[0, 0]
        c_x = self.intrinsics[0, 2]
        f_y = self.intrinsics[1, 1]
        c_y = self.intrinsics[1, 2]
        width, height = window_size[0], window_size[1]

        #pylint:disable=line-too-long
        cm.set_camera_intrinsics(self.vtk_overlay_window.get_foreground_renderer(),
                                 self.vtk_overlay_window.get_foreground_camera(),
                                 width,
                                 height,
                                 f_x,
                                 f_y,
                                 c_x,
                                 c_y,
                                 1,
                                 1000)

    def start(self):
        """Show the overlay widget and
        set a timer running"""
        self.vtk_overlay_window.show()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000.0 / self.update_rate)

    def update(self):
        """ QTimer Callback function. """
        #captured_positions = np.zeros((0, 3))

        _, frame = self.cap.read()
        #undistorted = cv2.undistort(frame, self.intrinsics, self.distortion)
        #num_pts = self.corners[0] * self.corners[1]

        _, object_points, image_points = \
            self.detector.get_points(frame)
        if image_points.shape[0] > 0:
            img = cv2.drawChessboardCorners(frame, self.corners,
                                            image_points,
                                            self.num_pts)

            retval, rvec, tvec = cv2.solvePnP(object_points,
                                              image_points,
                                              self.intrinsics,
                                              None)
            if retval:

                self.vtk_overlay_window.set_camera_matrix(self.intrinsics)

                rotation = cv2.Rodrigues(rvec)[0]

                pos = -rotation.T @ tvec
                pos[0] -= self.overlay_offset

                mat = np.ones((4, 4))
                mat[:3, :3] = rotation.T
                mat[:3, 3] = pos.T

                vtk_matrix = vtk.vtkMatrix4x4()
                vtk_matrix.DeepCopy(mat.ravel())

                self.ultrasound_actor.SetScale(0.075, 0.075, 1.0)
                self.vtk_overlay_window.set_video_image(img)
                self.vtk_overlay_window.set_camera_pose(mat)

            else:
                print("Failed to solve PnP")
                self.vtk_overlay_window.set_video_image(frame)

        else:
            print("Failed to detect points")
            self.vtk_overlay_window.set_video_image(frame)

        #pylint:disable=protected-access
        self.vtk_overlay_window._RenderWindow.Render()

def run_chessboard_overlay(config_file, calib_dir, overlay_offset):
    """
    Simple app that detects a calibration pattern, runs
    solvePnP, and overlays VTK models.

    :param config_file: mandatory location of config file, containing params.
    """

    if config_file is None or len(config_file) == 0:
        raise ValueError("Config file must be provided.")
    if calib_dir is None or len(calib_dir) == 0:
        raise ValueError("Calibration directory must be specified")

    # Need this for all the Qt magic.
    app = QtWidgets.QApplication([])

    configurer = ConfigurationManager(config_file)
    configuration = configurer.get_copy()

    window = ChessboardOverlay(configuration, calib_dir, overlay_offset)
    window.start()

    # Start event loop.
    return sys.exit(app.exec_())
