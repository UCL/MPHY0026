# -*- coding: utf-8 -*-

""" Harness to run CT & overlay application. """

import sys
import os
import vtk
from PySide2 import QtWidgets
import sksurgeryvtk.models.vtk_surface_model as sm
import sksurgeryutils.common_overlay_apps as coa

#pylint:disable=no-member, too-many-instance-attributes
class OverlayMainWindow(coa.OverlayOnVideoFeed):
    """ OverlayMainWindow"""
    def __init__(self, video_source, input_volume, input_surface):
        super().__init__(video_source)

        # Start by loading some data.
        if os.path.isdir(input_volume):
            reader = vtk.vtkDICOMImageReader()
            reader.SetDirectoryName(input_volume)

        elif input_volume.endswith(('.nii', '.nii.gz')):
            reader = vtk.vtkNIFTIImageReader()
            reader.SetFileName(input_volume)

        else:
            raise TypeError("Invalid input volume specified")

        reader.Update()

        self.model = sm.VTKSurfaceModel(input_surface,
                                        [0.5, 0.5, 0.5], opacity=0.5)
        self.vtk_overlay_window.add_vtk_models([self.model])

         # Calculate the center of the volume
        self.x_min, self.x_max, self.y_min, self.y_max, self.z_min, self.z_max \
            = reader.GetExecutive().GetWholeExtent(
                reader.GetOutputInformation(0))

        self.num_x = self.x_max - self.x_min
        self.num_y = self.y_max - self.y_min
        self.num_z = self.z_max - self.z_min

        self.x_spacing, self.y_spacing, self.z_spacing = \
            reader.GetOutput().GetSpacing()
        self.x_0, self.y_0, self.z_0 = reader.GetOutput().GetOrigin()

        self.center =\
         [self.x_spacing * (self.x_min + 0.5 * (self.x_min + self.x_max)),
          self.x_spacing * (self.y_min + 0.5 * (self.y_min + self.y_max)),
          self.z_spacing * (self.z_min + 0.5 * (self.z_min + self.z_max))]

        self.reslice_center = \
        [-0.5 * self.x_spacing * (self.num_x - 1),
         -0.5 * self.y_spacing * (self.num_y - 1),
         -0.5 * self.z_spacing * (self.num_z - 1)]

        # Setup reslice driver
        self.reslice = vtk.vtkImageReslice()
        self.reslice.SetInputConnection(reader.GetOutputPort())

        # Specific values to make the skull example look nicer.
        self.reslice.SetOutputExtent(100, 400, 150, 400, 25, 175)
        self.reslice.SetOutputOrigin(self.reslice_center[0],
                                     self.reslice_center[1], 0)

        self.reslice.SetInterpolationModeToLinear()

        self.reslice_x_angle = 0
        self.reslice_y_angle = 0
        self.reslice_z_angle = 0

        # Create a greyscale lookup table
        table = vtk.vtkLookupTable()
        table.SetRange(-1000, 1000) # image intensity range
        table.SetValueRange(0.1, 0.9) # from black to white
        table.SetSaturationRange(0.0, 0.0) # no color saturation
        table.SetRampToLinear()
        table.Build()

        # Map the image through the lookup table
        color = vtk.vtkImageMapToColors()
        color.SetLookupTable(table)
        color.SetInputConnection(self.reslice.GetOutputPort())

        # Display the image
        self.reslice_actor = vtk.vtkImageActor()
        self.reslice_actor.GetMapper().SetInputConnection(color.GetOutputPort())

        self.vtk_overlay_window.add_vtk_actor(self.reslice_actor)

        self.update_reslice()

    def update_reslice(self):
        """ Reslice the volume based on the new angles.
        Thanks to https://markmail.org/message/ycfr246az23acrl7
        for tips on setting the translation correctly. """
        slice_transform = vtk.vtkTransform()
        slice_transform.Identity()

        slice_transform.Translate(-1 * self.reslice_center[0],
                                  -1 * self.reslice_center[1],
                                  -1 * self.reslice_center[2])
        slice_transform.RotateX(self.reslice_x_angle)
        slice_transform.RotateY(self.reslice_y_angle)
        slice_transform.RotateZ(self.reslice_z_angle)
        self.reslice.SetResliceTransform(slice_transform)

        actor_transform = vtk.vtkTransform()
        actor_transform.Identity()

        actor_transform.Translate(self.center)
        actor_transform.RotateZ(self.reslice_z_angle)
        actor_transform.RotateX(self.reslice_x_angle)
        actor_transform.RotateY(self.reslice_y_angle)
        self.reslice_actor.SetUserTransform(actor_transform)

        self.vtk_overlay_window.Render()

class MainWindow(QtWidgets.QMainWindow):
    """ MainWindow """
    def __init__(self, video_source, input_volume, input_surface):

        super().__init__()

        self.overlay_window = OverlayMainWindow(video_source,
                                                input_volume, input_surface)

        self.layout = QtWidgets.QHBoxLayout()

        self.layout.addWidget(self.overlay_window.vtk_overlay_window)
        self.setup_controls()


        self.frame = QtWidgets.QFrame()
        self.frame.setLayout(self.layout)
        self.setCentralWidget(self.frame)

    def setup_controls(self):
        """ Setup widgets for buttons etc."""
        self.controls = QtWidgets.QVBoxLayout()

        # Not really controlling x/y rotation, but good enough for a demo
        self.slider_x = QtWidgets.QSlider()
        self.slider_y = QtWidgets.QSlider()

        for slider in [self.slider_x, self.slider_y]:
            slider.setMinimum(-180)
            slider.setMaximum(180)
            slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
            slider.setTickInterval(45)
            slider.setSliderPosition(0)

        self.slider_x.valueChanged.connect(self.x_changed)
        self.slider_y.valueChanged.connect(self.y_changed)

        self.toggle_model_btn = QtWidgets.QPushButton("Toggle Model")
        self.toggle_slice_btn = QtWidgets.QPushButton("Toggle Slice")

        self.toggle_model_btn.clicked.connect(self.toggle_model)
        self.toggle_slice_btn.clicked.connect(self.toggle_slice)

        self.slider_layout = QtWidgets.QHBoxLayout()
        self.slider_layout.addWidget(self.slider_x)
        self.slider_layout.addWidget(self.slider_y)

        self.controls.addLayout(self.slider_layout)

        self.controls.addWidget(self.toggle_model_btn)
        self.controls.addWidget(self.toggle_slice_btn)


        self.layout.addLayout(self.controls)

    def toggle_model(self):
        """ Toggle model view"""
        self.overlay_window.model.toggle_visibility()

    def toggle_slice(self):
        """ Toggle slice view """
        actor = self.overlay_window.reslice_actor

        if actor.GetVisibility():
            actor.VisibilityOff()
        else:
            actor.VisibilityOn()

    def x_changed(self, x_value):
        """ Callbakc for x slider. """
        self.overlay_window.reslice_x_angle = x_value
        self.overlay_window.update_reslice()

    def y_changed(self, y_value):
        """ Callback for y slider"""
        self.overlay_window.reslice_y_angle = y_value
        self.overlay_window.update_reslice()

    def start(self):
        """ Start overlay window. """
        self.overlay_window.start()

def run_overlay():
    """
    Run the app
    """

    # Need this for all the Qt magic.
    app = QtWidgets.QApplication([])

    # App is just one window, containing one widget, defined above.

    # Not gauranteed to work well with data other than the skull test data.
    window = MainWindow(0, 'tests/data/skull/skull.nii',
                        'tests/data/skull/skull.vtk')
    window.show()
    window.start()

    # Start event loop.
    return sys.exit(app.exec_())
