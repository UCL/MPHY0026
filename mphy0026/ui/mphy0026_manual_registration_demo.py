# -*- coding: utf-8 -*-

""" manual registration demo app. """

import sys
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QSizePolicy
import cv2
import vtk
import numpy as np
import sksurgeryvtk.models.vtk_surface_model as sm
import sksurgeryvtk.widgets.vtk_overlay_window as ow


#pylint:disable=no-member
class ManualRegistrationMainWidget(QtWidgets.QWidget):
    """
    ManualRegistrationMainWidget to just enable a VTK window and interactor.
    """
    def __init__(self,
                 background_file,
                 model_file,
                 camera_file
                 ):
        super().__init__()

        if not background_file:
            raise ValueError("Background image must be specified")
        if not model_file:
            raise ValueError("VTK model must be specified")
        if not camera_file:
            raise ValueError("Camera matrix must be specified")

        self.setContentsMargins(0, 0, 0, 0)
        self.viewer = ow.VTKOverlayWindow()
        self.viewer_size_policy = \
            QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.viewer.setSizePolicy(self.viewer_size_policy)

        self.interactor_style = vtk.vtkInteractorStyleTrackballActor()
        self.viewer.SetInteractorStyle(self.interactor_style)

        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.addWidget(self.viewer)

        background = cv2.imread(background_file)
        model = sm.VTKSurfaceModel(model_file, [1.0, 1.0, 1.0], opacity=0.5)
        camera_matrix = np.loadtxt(camera_file)

        self.viewer.set_video_image(background)
        self.viewer.set_camera_matrix(camera_matrix)
        self.viewer.add_vtk_models([model])


class ManualRegistrationMainWindow(QtWidgets.QMainWindow):
    """
    ManualRegistrationMainWindow.
    """
    def __init__(self,
                 background,
                 model,
                 camera
                 ):
        """
        Constructor, puts ManualRegistrationMainWidget in window.
        """
        super().__init__()
        self.main_widget = ManualRegistrationMainWidget(background,
                                                        model,
                                                        camera
                                                        )
        self.setCentralWidget(self.main_widget)
        self.setContentsMargins(0, 0, 0, 0)


def run_app(background,
            model,
            camera):
    """
    Function that launches the manual_registration main window shown above.

    :return: application exit code
    """

    # Need this for all the Qt magic.
    app = QtWidgets.QApplication([])

    # This is a simple way of increasing the font size of all buttons globally.
    font = QtGui.QFont()
    font.setPointSize(20)
    app.setFont(font)

    # App is just one window, containing one widget, defined above.
    window = ManualRegistrationMainWindow(background,
                                          model,
                                          camera
                                          )
    window.setContentsMargins(0, 0, 0, 0)
    window.show()

    # Start event loop.
    return sys.exit(app.exec_())
