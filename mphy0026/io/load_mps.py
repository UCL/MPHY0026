# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import numpy as np


def load_mps(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    points = root[1]
    time_series = points[0]
    tmp = {}
    for point in time_series.findall('point'):
        i = point.find('id').text
        x = point.find('x').text
        y = point.find('y').text
        z = point.find('z').text
        tmp[int(i)] = (float(x), float(y), float(z))
    ids = np.zeros(len(tmp.keys()), dtype=int)
    result = np.zeros((len(tmp.keys()), 3))
    counter = 0
    for k in tmp.keys():
        ids[counter] = k
        result[counter][0] = tmp[k][0]
        result[counter][1] = tmp[k][1]
        result[counter][2] = tmp[k][2]
        counter = counter + 1
    return ids, result
