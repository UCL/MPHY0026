# -*- coding: utf-8 -*-

""" Harness to run overlay application. """

import sys
import vtk
import cv2
import random
import numpy as np
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QSizePolicy
import sksurgeryvtk.widgets.vtk_overlay_window as ow
import sksurgeryvtk.models.vtk_surface_model as sm



class OverlaywMainWindow(QtWidgets.QMainWindow):
    """
    OverlayMainWindow.
    """
    def __init__(self):
        """
        Constructor, puts OverlayMainWidget in window.
        """
        super().__init__()

        self.mode = "circle"
        self.model = None

        self.layout = QtWidgets.QVBoxLayout()
        self.frame = QtWidgets.QFrame()
        self.frame.setLayout(self.layout)
        self.setCentralWidget(self.frame)

        self.h_box = QtWidgets.QHBoxLayout()
        self.vtk_overlay_window = ow.VTKOverlayWindow()
        self.controls_box = QtWidgets.QHBoxLayout()

        self.h_box.addWidget(self.vtk_overlay_window)
        self.layout.addLayout(self.h_box)
        self.layout.addLayout(self.controls_box)
        
        self.add_group_box()
        self.add_opacity_slider()

        # Reset button
        self.button = QtWidgets.QPushButton('Move Target', self)
        self.button.clicked.connect(self.reset_models)
        self.layout.addWidget(self.button)

        self.target_actor = None

        self.window_width = 800
        self.window_height = 600
        self.setFixedSize(self.window_width, self.window_height)

        style = vtk.vtkInteractorStyleTrackballActor()
        self.vtk_overlay_window.SetInteractorStyle(style)

        # Setup text labels
        self.txtPosition = vtk.vtkTextActor()
        self.txtPosition.SetDisplayPosition(30, 60)
        self.txtPosition.GetTextProperty().SetFontSize(25)

        self.txtScale = vtk.vtkTextActor()
        self.txtScale.SetDisplayPosition(30, 30)
        self.txtScale.GetTextProperty().SetFontSize(25)

        self.reset_text_labels()

        self.vtk_overlay_window.foreground_renderer.AddActor(self.txtScale)
        self.vtk_overlay_window.foreground_renderer.AddActor(self.txtPosition)
        
        self.setup_target()
        self.setup_overlay()

        self.update()
        self.setContentsMargins(0, 0, 0, 0)

        # Handle the mouse button events.
        def interactionChange(obj, event):

            if event == "EndInteractionEvent":
                
                # position
                pos_ok = self.check_position()
                if pos_ok:
                    self.txtPosition.SetInput("Position: Aligned!!")
                else:
                    self.txtPosition.SetInput("Position: Not aligned")

                # scale
                
                scale_ok = self.check_scale()
                if scale_ok:
                    self.txtScale.SetInput("Size: Aligned!!")
                else:
                    self.txtScale.SetInput("Size: Not alinged")

                if pos_ok and scale_ok:
                    print(1)
                    self.vtk_overlay_window.background_renderer.SetBackground(0, 0.5, 0.5)
                else:
                    self.vtk_overlay_window.background_renderer.SetBackground(0, 0, 0)


        self.vtk_overlay_window._Iren.AddObserver("EndInteractionEvent", interactionChange)

    def show_controls_dialog(self):
        dialog = QtWidgets.QMessageBox()
        dialog.setText("Mouse Controls \n" \
                       "Left button: Rotate (x/y)\n" \
                       "Ctrl + Left button: Rotate (z)\n"\
                       "Right Button: Scale\n" \
                       "Middle Button: Move\n")
        dialog.exec_()

    def add_group_box(self):
        self.group_box = QtWidgets.QGroupBox("Select model")

        self.radio_btn_circle = QtWidgets.QRadioButton("Circle")
        self.radio_btn_liver = QtWidgets.QRadioButton("Liver")
        self.radio_layout = QtWidgets.QHBoxLayout()
        self.radio_layout.addWidget(self.radio_btn_circle)
        self.radio_layout.addWidget(self.radio_btn_liver)

        self.group_box.setLayout(self.radio_layout)
        self.layout.addWidget(self.group_box)

        self.radio_btn_circle.clicked.connect(self.circle_selected)
        self.radio_btn_liver.clicked.connect(self.liver_selected)
        self.radio_btn_circle.setChecked(True)

    def circle_selected(self):
        self.mode = "circle"
        self.reset_models()


    def liver_selected(self):
        self.mode = "liver"
        self.reset_models()

    def reset_models(self):
        self.setup_overlay()
        self.setup_target()
        self.vtk_overlay_window.background_renderer.SetBackground(0, 0, 0)
        self.update()

    def setup_overlay(self):

        if self.model:
            self.vtk_overlay_window.foreground_renderer.RemoveActor(
            self.model.actor)

        if self.mode == "circle":
            self.setup_circle_overlay()

        else:
            self.setup_liver_overlay()

        self.update()

    def setup_circle_overlay(self):

        sphere_model = 'tests/data/overlay/sphere.vtk'
        self.model = sm.VTKSurfaceModel(sphere_model, [0.5, 0.5, 0.5])
        self.vtk_overlay_window.add_vtk_models([self.model])

    def setup_liver_overlay(self):

        liver_model = 'tests/data/overlay/liver.vtk'
        self.model = sm.VTKSurfaceModel(liver_model, [1.0, 0.0, 0.0])
        self.vtk_overlay_window.add_vtk_models([self.model])

    def update(self):
        """ Re render the window."""
        self.vtk_overlay_window._RenderWindow.Render()

    def add_opacity_slider(self):
        """Create a QSlider that controls VTK model opactity"""

        self.opacity_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.opacity_slider.setMinimum(0)
        self.opacity_slider.setMaximum(100)
        self.opacity_slider.setSliderPosition(100)
        self.opacity_slider.valueChanged.connect(self.set_opacity)

        label = QtWidgets.QLabel('Opacity')

        self.controls_box.addWidget(label)
        self.controls_box.addWidget(self.opacity_slider)

        self.layout.addLayout(self.controls_box)

    def set_opacity(self, opacity_percent):
        """Set the opacity for all VTK models

        :param opacity_percent: Target opacity value, in %
        :type opacity_percent: int
        """

        opacity = opacity_percent / 100
        self.model.set_opacity(opacity)
        self.update()

    def setup_target(self):
        # Clear previously drawn circles
        if self.target_actor:
            self.vtk_overlay_window.foreground_renderer.RemoveActor(self.target_actor)

        if self.mode == "circle":
            self.draw_circle()
        
        else:
            self.set_target_liver()

        print(f'Circle: {self.target_actor.GetCenter()}')

        self.vtk_overlay_window.foreground_renderer.AddActor(self.target_actor)

        self.reset_text_labels()
        self.update()

    def set_target_liver(self):
        liver_model = 'tests/data/overlay/liver.vtk'
        self.target_model = sm.VTKSurfaceModel(liver_model, [0.5, 0.5, 0.5],
                                               pickable=False)
        self.target_actor = self.target_model.actor

        self.target_x = -300 + 600 * random.random()
        self.target_y = -200 + 400 * random.random()
        self.target_actor.SetOrigin(0, 0, 0)
        
        scale = 0.5 + random.random() * 1.0
        self.target_actor.SetScale(scale, scale, scale)

        self.target_actor.RotateX(180*random.random())
        self.target_actor.RotateY(90*random.random())
        
        self.target_actor.SetPosition(self.target_x, self.target_y, 0)


    def draw_circle(self):

        # Generate random position and size
        self.circle_radius = random.random() * 200 + 25
        self.target_x = -400 + self.circle_radius + (800 - 2*self.circle_radius) * random.random()
        self.target_y = -260 + self.circle_radius + (520 - 2*self.circle_radius) * random.random()
        print(self.target_x, self.target_y, self.circle_radius)
        """ Draw a circle at random coordinates in the window. """
        # Create a circle
        polygon_source = vtk.vtkRegularPolygonSource()
        # Comment this line to generate a disk instead of a circle.
        polygon_source.GeneratePolygonOff()
        polygon_source.SetNumberOfSides(50)
        polygon_source.SetRadius(self.circle_radius)
        polygon_source.SetCenter(self.target_x, self.target_y, 0.0)

        # mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(polygon_source.GetOutputPort())

        # actor
        self.target_actor = vtk.vtkActor()
        self.target_actor.SetMapper(mapper)

    def check_position(self):
        """ Check if overlay model is correctly aligned in x/y with the
        background. """
        
        if self.mode == "circle":
            position_model = self.model.actor.GetCenter()
            tol = 10

        else:
            position_model = self.model.actor.GetPosition()
            tol = 25

        x, y = position_model[0], position_model[1]

        if abs(x - self.target_x) < tol and abs(y - self.target_y) < tol:
            return True

        return False

    def check_scale(self):
        """ Check if the overlay is the correct size for the background image.
        """
        model_scale = self.model.actor.GetScale()[0]
        if self.mode == "circle":
            model_in_taget_space = 100 * model_scale * 3 / 2
            diff = abs(model_in_taget_space - self.circle_radius)
            tol = 3

        else:
            target_scale = self.target_actor.GetScale()[0]
            diff = 100 * abs(target_scale - model_scale)
            print(diff)
            tol = 7

        if  diff < tol:
            return True

        return False

    def reset_text_labels(self):
        self.txtPosition.SetInput("Position: Not aligned")
        self.txtScale.SetInput("Size: Not aligned")

def run_overlay():
    """

    """

    # Need this for all the Qt magic.
    app = QtWidgets.QApplication([])

    # This is a simple way of increasing the font size of all buttons globally.
    font = QtGui.QFont()
    font.setPointSize(12)
    app.setFont(font)

    # App is just one window, containing one widget, defined above.
    window = OverlaywMainWindow()
    #widget.setContentsMargins(0, 0, 0, 0)
    window.show()
    window.show_controls_dialog()

    # Start event loop.
    return sys.exit(app.exec_())
