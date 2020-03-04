"""Functions to support MedPhys Taught Module workshop on
calibration and tracking
"""

import csv
import xml.dom.minidom
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def _read_csv_text(csvfile):
    skip_comments = lambda row: row[0] != '#'
    return csv.reader(filter(skip_comments, csvfile), delimiter=" ")


def load_intrinsic(filein):
    """
    loads a text file formatted, consisting of a 3x3
    projection project matrix, followed by a row of
    distortion coefficients.
    :return: intrinsic, distortion
    """
    projection = np.zeros((1, 3))
    distortion = np.zeros((1, 5))
    with open(filein, 'rt') as csvfile:
        reader = _read_csv_text(csvfile)
        rownumber = 1
        for row in reader:
            #some files have blanks at the end of each line
            if rownumber < 4:
                while len(row) > 3:
                    row.pop()
            else:
                while len(row) > 5:
                    row.pop()

            parsed_row = np.array([float(col) for col in row])
            if rownumber == 1:
                projection = parsed_row
            else:
                if rownumber < 4:
                    projection = np.concatenate((projection, parsed_row),
                                                axis=0)
                else:
                    distortion = parsed_row
            rownumber += 1

    projection = np.reshape(projection, (3, 3))
    distortion = np.reshape(distortion, (1, 5))

    return projection, distortion


def load_model_points(filein):
    """
    loads a four column text file
    :params: filename
    :return: array of points
    """
    model_points = np.zeros((4))
    with open(filein, 'rt') as csvfile:
        reader = _read_csv_text(csvfile)
        rownumber = 1
        for row in reader:
            point = np.array([float(col) for col in row])
            if rownumber == 1:
                model_points = point
            else:
                model_points = np.concatenate((model_points, point), axis=0)
            rownumber += 1

    cols = int(model_points.shape[0]/(rownumber - 1))

    model_points = np.reshape(model_points, (rownumber-1, cols))
    return model_points


def load_matrix(filein):
    """
    matrix loader
    :param: filename
    :return: matrix
    """
    matrix = np.zeros((1, 4))
    with open(filein, 'rt') as csvfile:
        reader = _read_csv_text(csvfile)
        rownumber = 1
        for row in reader:
            #some files have blanks at the end of each line
            while len(row) > 4:
                row.pop()

            mat_row = np.array([float(col) for col in row])
            if rownumber == 1:
                matrix = mat_row
            else:
                matrix = np.concatenate((matrix, mat_row), axis=0)
            rownumber += 1

    cols = int(matrix.shape[0]/(rownumber - 1))

    matrix = np.reshape(matrix, (rownumber - 1, cols))
    return matrix


def load_matrix_as_point(filename):
    """
    loads the last column of a 4x4 matrix as a 1 by 4
    point, i.e. it discards any rotational data.
    :param: filename
    :return: 1x4 point
    """
    point = np.zeros((1, 4))
    with open(filename, 'rt') as csvfile:
        reader = _read_csv_text(csvfile)
        rownumber = 0
        for row in reader:
            #some files have blanks at the end of each line
            while len(row) > 4:
                row.pop()

            point[0, rownumber] = row.pop()
            rownumber += 1

    return point


def multiply_points_by_matrix(points_in, matrix):
    """Multiply a matrix of point vectors by
    a 4x4 matrix
    :param: An n by 4 matrix of n points, the first
            column is the point ID
    :param: A 4x4 matrix
    :return: An n by 4 matrix of n transformed points
    """
    points = points_in[:, 1:4]
    rows = points.shape[0]
    ids = np.reshape(points_in[:, 0], (rows, 1))
    ones = np.reshape(np.ones(rows), (rows, 1))
    homogenous_pts = np.transpose(np.concatenate((points, ones), axis=1))

    hom_pts_out = np.transpose(np.matmul(matrix, homogenous_pts))
    pts_out = hom_pts_out[:, 0:3]
    pts_out_with_id = np.concatenate((ids, pts_out), axis=1)
    return pts_out_with_id

def project(lens_3d, intrinsic):
    """
    Projects 3D points relative to the lens to screen points
    :param: n by 4 matrix n 3D in camera coordinates. First column is the
            point ID
    :param: the camera's intrinsic parameters
    :return n by 3 matrix of 2D points on screen coordinates. First column
            is the point ID
    """
    points_3d = lens_3d[:, 1:4]
    rows = points_3d.shape[0]
    ids = np.reshape(lens_3d[:, 0], (rows, 1))

    points_3d = np.transpose(points_3d)
    normalised_points = np.divide(points_3d, points_3d[2, :])
    projected_points = np.transpose(np.matmul(intrinsic, normalised_points))
    projected_points = projected_points[:, 0:2]
    projected_points_with_ids = np.concatenate((ids, projected_points), axis=1)

    return projected_points_with_ids

def _distort_point(point, distortion):
    """
    Distorts a 2D point according to a five parameter distortion
    :param: a 2D point
    :param: a 1x5 distortion array [r1, r2, t1, t3, r3]
    :return: the distorted 2D point
    """
    radius = np.linalg.norm(point)
    rfactor = 1 + distortion[0, 0] * radius**2 + \
              distortion[0, 1] * radius**4 + \
              distortion[0, 4] * radius**6
    rdpixels = np.multiply(point[0:2], rfactor)

    twoponexy = point[0] * point[1] * 2 * distortion[0, 2]
    twoptwoxy = point[0] * point[1] * 2 * distortion[0, 3]
    xfactor = twoponexy + distortion[0, 3] * (radius**2 + 2 * point[0]**2)
    yfactor = twoptwoxy + distortion[0, 2] * (radius**2 + 2 * point[1]**2)

    tdrdpixels = rdpixels + ([xfactor, yfactor])

    return tdrdpixels

def distort(lens_3d, distortion):
    """
    Distorts a 2D point according to a five parameter distortion
    :param: a 2D point
    :param: a 1x5 distortion array [r1, r2, t1, t3, r3]
    :return: the distorted 2D point
    """
    points = lens_3d[:, 1:4]
    rows = points.shape[0]
    ids = np.reshape(lens_3d[:, 0], (rows, 1))
    points = np.transpose(points)
    norm_points = np.divide(points, points[2, :])

    for row in range(0, rows):
        norm_points[0:2, row] = _distort_point(norm_points[0:2, row],
                                               distortion)

    distorted_points = np.transpose(norm_points)
    return np.concatenate((ids, distorted_points), axis=1)


def calculate_errors(screen_points, projected_points):
    """
    Finds corresponding points in each input list, and
    calculates the distances between each list
    """
    screen_rows = screen_points.shape[0]
    projected_rows = projected_points.shape[0]
    deltas = np.zeros((screen_rows, 2))
    count = 0
    for srow in range(0, screen_rows):
        point_id = screen_points[srow, 0]
        count += 1
        for prow in range(0, projected_rows):
            if point_id == projected_points[prow, 0]:
                deltas[srow, :] = np.subtract(screen_points[srow, 1:3],
                                              projected_points[prow, 1:3])
                break
            if prow == projected_rows - 1:
                print("NO MATCH for ", point_id)

    return deltas


def plot_errors(image_file_name, projected_points, screen_points,
                crop_to_image=True):
    """
    Creates a visualisation of the projected and
    detected screen points
    """
    img = mpimg.imread(image_file_name)
    _, ax1 = plt.subplots(figsize=(12, 8))
    ax1.imshow(img)
    if crop_to_image:
        ax1.set_ylim([0, img.shape[0]])
        ax1.set_xlim([0, img.shape[1]])
    ax1.scatter(projected_points[:, 1], projected_points[:, 2])
    ax1.scatter(screen_points[:, 1], screen_points[:, 2])


class InteractiveMeasure:
    """A class to handle mouse press events, outputting the
    distance to a target point.
    """
    def __init__(self, fig, point):
        self.point = point
        self.cid = fig.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        print('%s click: xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single',
               event.xdata, event.ydata))
        screen_p = np.array((1, 2))
        screen_p[0] = event.xdata
        screen_p[1] = event.ydata
        print("distance = ", np.linalg.norm(screen_p - self.point))


def plot_errors_interactive(image_file_name, projected_point,
                            crop_to_image=True):
    """
    Creates a visualisation of the projected and
    detected screen points, which you can click on
    to measure distances
    """
    img = mpimg.imread(image_file_name)
    fig, ax1 = plt.subplots(figsize=(12, 8))
    ax1.imshow(img)
    if crop_to_image:
        ax1.set_ylim([0, img.shape[0]])
        ax1.set_xlim([0, img.shape[1]])
    #this is just going to show the first point in an array.
    #Could get clever and search for nearest point on click?
    ax1.scatter(projected_point[0, 1], projected_point[0, 2])

    _ = InteractiveMeasure(fig, (projected_point[0, 1], projected_point[0, 2]))

    plt.show()


def picked_object_reader(filename, points_only=True):
    """
    processes an xml picked object file.
    :param: the filename, and optional flag to only process point landmarks
    :return: an nx4 array of landmarks, first column is point id
    """
    doc = xml.dom.minidom.parse(filename)
    picked_objects = doc.getElementsByTagName("picked_object")

    point_array = np.array((0, 4), dtype=float)
    for picked_obj in picked_objects:
        if not points_only or not picked_obj.getAttribute("line"):
            points = picked_obj.getElementsByTagName("coordinate")
            ident = picked_obj.getElementsByTagName("id")
            for point in points:
                coords = point.getAttribute("xyz")
                coord_array = np.array([float(col) for col in coords])

                coord_array = np.concatenate((ident, coord_array), axis=1)

                point_array = np.concatenate((point_array, coord_array), axis=0)

    return point_array


def picked_object_directory_reader(directory, points_only=True):
    """
    processes an xml picked object directory
    :param: directory name, and optional flag to only process point landmarks
    :return: an nx4 array of landmarks, first column is point id
    """
    point_array = np.array((0, 4), dtype=float)
    filenames = glob.glob(directory + './???????????????????_*Points.xml')

    for filename in filenames:
        points = picked_object_reader(filename, points_only)
        point_array = np.concatenate((point_array, points), axis=0)

    return point_array
