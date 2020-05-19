#!/usr/bin/env python

import numpy as np
import os

import json
import pickle



class sensor_data_struct():
    def __init__(self, point, IR_data, TOF_data, color_data, button_data):
        self.pt = point
        self.IR = IR_data
        self.TOF = TOF_data
        self.color = color_data
        self.button = button_data



comb_data = []
leaf_set = []
berry_set = []

os.chdir('/home/ben/gripper_proj_2/data/data_saved/')

"""
IR Sensor
"""
# dump_filename = 'IR_combined_data.txt'
# dump_filename = 'IR_test_data.txt'
# dump_filename = 'IR_combined_leaf_data.txt'
# dump_filename = 'IR_final_test_data.txt'
# dump_filename = 'IR_final_test_leaf_data.txt'
# dump_filename = 'IR_test_leaf_data.txt'
# for i in [6]:#[1,2,3,4,5]:
#     filename = 'IR_data_' + str(i) + '.txt'
#     with open(filename, 'r') as filehandle:
#         data_set = pickle.load(filehandle)
#     for data in data_set:
#         if data.button == 0:
#             berry_set.append(data.IR[0:3] + ['Good Grip'])
#         else:
#             berry_set.append(data.IR[0:3] + ['Bad Grip'])
"""
TOF Sensor - Don't use lux
"""
# dump_filename = 'TOF_combined_data.txt'
# dump_filename = 'TOF_test_data.txt'
# dump_filename = 'TOF_final_test_data.txt'
# dump_filename = 'TOF_combined_leaf_data.txt'
# dump_filename = 'TOF_test_leaf_data.txt'
# dump_filename = 'TOF_final_test_leaf_data.txt'
# for i in [1,2,3,4,5]:
#     filename = 'TOF_data_' + str(i) + '.txt'
#     with open(filename, 'r') as filehandle:
#         data_set = pickle.load(filehandle)
#     for data in data_set:
#         if data.button == 0:
#             berry_set.append(data.TOF[0:3] + ['Good Grip']) # No lux
#         else:
#             berry_set.append(data.TOF[0:3] + ['Bad Grip']) #No lux

"""
IR and Color Sensor -Just RGB
"""
# # dump_filename = 'IR_Color_k_combined_data.txt'
# dump_filename = 'IR_Color_rgb_test_data.txt'
# for i in [6]: #[1,2,3,4,5]:
#     filename = 'IR_Color_data_' + str(i) + '.txt'
#     with open(filename, 'r') as filehandle:
#         data_set = pickle.load(filehandle)
#     for data in data_set:
#         if data.button == 0:
#             berry_set.append(data.IR[0:2] + data.color[0:3] + ['Good Grip'])
#         else:
#             berry_set.append(data.IR[0:2] + data.color[0:3] + ['Bad Grip'])

"""
TOF and Color Sensor - No lux and just RGB.
"""
# dump_filename = 'TOF_Color_rgb_combined_data.txt'
dump_filename = 'TOF_Color_rgb_test_data.txt'
# dump_filename = 'TOF_Color_rgb_final_test_data.txt'
# dump_filename = 'TOF_Color_k_combined_data.txt'
# dump_filename = 'TOF_Color_all_combined_data.txt'
for i in [6]: #[1,2,3,4,5]:
    filename = 'TOF_Color_data_' + str(i) + '.txt'
    with open(filename, 'r') as filehandle:
        data_set = pickle.load(filehandle)
    for data in data_set:
        if data.button == 0:
            # berry_set.append(data.TOF[0:2] + data.TOF[3:5] + data.color[0:3] + ['Good Grip'])
            berry_set.append(data.TOF[0:2] + data.color[0:3] + ['Good Grip']) # rgb
            # berry_set.append(data.TOF[0:2] + [data.color[4]] + ['Good Grip']) # k
            # berry_set.append(data.TOF[0:2] + data.color[0:6] + ['Good Grip']) # all

        else:
            # berry_set.append(data.TOF[0:2] + data.TOF[3:5] + data.color[0:3] + ['Bad Grip'])
            berry_set.append(data.TOF[0:2] + data.color[0:3] + ['Bad Grip']) # rgb
            # berry_set.append(data.TOF[0:2] + [data.color[4]] + ['Bad Grip']) # k
            # berry_set.append(data.TOF[0:2] + data.color[0:6] + ['Bad Grip']) # all




# filename = 'IR_leaf_final_test.txt'
# filename = 'IR_leaf.txt'
# with open(filename, 'r') as filehandle:
#     data_set = pickle.load(filehandle)
# for data in data_set:
#     berry_set.append(data.IR[0:3] + ['Leaf'])


# filename = 'TOF_leaf.txt'
# # filename = 'TOF_leaf_test.txt'
# # filename = 'TOF_leaf_final_test.txt'
# with open(filename, 'r') as filehandle:
#     data_set = pickle.load(filehandle)
# for data in data_set:
#     # berry_set.append(data.IR[0:3] + ['Leaf'])
#     berry_set.append(data.TOF[0:3] + ['Leaf']) # No lux

# comb_data = berry_set

os.chdir('/home/ben/gripper_proj_2/data/combined_data/')
with open(dump_filename, 'w') as filehandle:
        json.dump(berry_set, filehandle)
