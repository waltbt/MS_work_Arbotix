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
dump_filename = 'IR_combined_data.txt'
# dump_filename = 'IR_test_data.txt' 
for i in [1,2,3,4,5]:
    filename = 'IR_data_' + str(i) + '.txt'
    with open(filename, 'r') as filehandle:
        data_set = pickle.load(filehandle)
    for data in data_set:
        if data.button == 0:
            berry_set.append(data.IR[0:3] + ['success!'])
        else:
            berry_set.append(data.IR[0:3] + ['Bad Grip'])
"""
TOF Sensor
"""
# dump_filename = 'TOF_combined_data.txt'
# dump_filename = 'TOF_test_data.txt'
# dump_filename = 'TOF_NL_combined_data.txt' # NO lux
# for i in [1,2,3,4,5]:
#     filename = 'TOF_data_' + str(i) + '.txt'
#     with open(filename, 'r') as filehandle:
#         data_set = pickle.load(filehandle)
#     for data in data_set:
#         if data.button == 0:
#             # berry_set.append(data.TOF[0:6] + ['success!'])
#             berry_set.append(data.TOF[0:3] + ['success!']) # No lux
#         else:
#             # berry_set.append(data.TOF[0:6] + ['Bad Grip'])
#             berry_set.append(data.TOF[0:3] + ['Bad Grip']) #No lux

"""
IR and Color Sensor - Need think about what data I want to use here.
"""
# dump_filename = 'IR_Color_k_combined_data.txt'
# for i in [1,2,3,4,5]:
#     filename = 'IR_Color_data_' + str(i) + '.txt'
#     with open(filename, 'r') as filehandle:
#         data_set = pickle.load(filehandle)
#     for data in data_set:
#         if data.button == 0:
#             berry_set.append(data.IR[0:2] + [data.color[4]] + ['success!'])
#         else:
#             berry_set.append(data.IR[0:2] + [data.color[4]] + ['Bad Grip'])

"""
TOF and Color Sensor - Need think about what data I want to use here.
"""
# # dump_filename = 'TOF_Color_rgb_combined_data.txt'
# # dump_filename = 'TOF_Color_k_combined_data.txt'
# dump_filename = 'TOF_Color_all_combined_data.txt'
# for i in [1,2,3,4,5]:
#     filename = 'TOF_Color_data_' + str(i) + '.txt'
#     with open(filename, 'r') as filehandle:
#         data_set = pickle.load(filehandle)
#     for data in data_set:
#         if data.button == 0:
#             # berry_set.append(data.TOF[0:2] + data.TOF[3:5] + data.color[0:3] + ['success!'])
#             # berry_set.append(data.TOF[0:2] + data.color[0:3] + ['success!']) # rgb
#             # berry_set.append(data.TOF[0:2] + [data.color[4]] + ['success!']) # k
#             berry_set.append(data.TOF[0:2] + data.color[0:6] + ['success!']) # all
#
#         else:
#             # berry_set.append(data.TOF[0:2] + data.TOF[3:5] + data.color[0:3] + ['Bad Grip'])
#             # berry_set.append(data.TOF[0:2] + data.color[0:3] + ['Bad Grip']) # rgb
#             # berry_set.append(data.TOF[0:2] + [data.color[4]] + ['Bad Grip']) # k
#             berry_set.append(data.TOF[0:2] + data.color[0:6] + ['Bad Grip']) # all


# leaf_set =[]
# #filename = 'Tabbed_leaf.txt'
# filename = 'Basic_leaf.txt'
# with open(filename, 'r') as filehandle:
#     leaf_data = pickle.load(filehandle)
#
# for data in leaf_data:
#     leaf_set.append(data.IR[0:3]+ ['leaf'])

comb_data = berry_set #+ leaf_set

os.chdir('/home/ben/gripper_proj_2/data/combined_data/')
with open(dump_filename, 'w') as filehandle:
        json.dump(comb_data, filehandle)
