#!/usr/bin/env python

import numpy as np
import json

filename = "/home/ben/gripper_proj_py/data/char_test_points.txt"

test_pt_list =[]


x_list = np.linspace(-3,3,19)
y_list = np.linspace(-3,3,19)
z_list = np.linspace(0,6,19)




for z in z_list:
    for x in x_list:
        for y in y_list:
            test_pt_list.append([x/100.0, y/100.0, -z/100.0])

print(len(test_pt_list))

with open(filename, 'w') as filehandle:
    json.dump(test_pt_list, filehandle)
