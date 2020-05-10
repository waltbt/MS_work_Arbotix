#!/usr/bin/env python

import numpy as np
import os

import json
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import random

class sensor_data_struct():
    def __init__(self, point, IR_data, TOF_data, color_data, button_data):
        self.pt = point
        self.IR = IR_data
        self.TOF = TOF_data
        self.color = color_data
        self.button = button_data



# comb_data = []
# leaf_set = []
berry_set = []



os.chdir('/home/ben/gripper_proj_2/data/data_saved/')

"""
IR Sensor
"""
# dump_filename = 'IR_combined_data.txt'
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
fig = 1
neighbors = range(1,25)
for a in [50,100,150,200,250,300,350,400,450]:
    properties = []
    labels = []
    data_set = random.sample(berry_set, a)
    for data in data_set:
        properties.append(data[0:3])
        labels.append(data[-1])

    properties_train, properties_test, labels_train, labels_test = train_test_split(properties, labels, test_size=0.20)

    scaler = StandardScaler()
    scaler.fit(properties_train)

    properties_train = scaler.transform(properties_train)
    properties_test = scaler.transform(properties_test)

    prec_bad = []
    prec_good = []

    for i in range(1,25):
        # print("Number of Neighbors: ", i)
        classifier = KNeighborsClassifier(n_neighbors=i)
        classifier.fit(properties_train, labels_train)

        labels_pred = classifier.predict(properties_test)


        cf = confusion_matrix(labels_test, labels_pred)
        # print(cf)
        # print("Report")
        # print(classification_report(labels_test, labels_pred))
        prec_bad.append(round(float(cf[0,0])/(cf[0,0]+cf[1,0]),2))
        prec_good.append(round(float(cf[1,1])/(cf[1,1]+cf[0,1]),2))

    title_name = 'data size test '
    # plt.figure(fig)
    fig += 1
    good_label = 'Good Grip - ' + str(a) + ' training points'
    bad_label = 'Bad Grip - ' + str(a) + ' training points'
    plt.plot(neighbors, prec_good, label = good_label)
    plt.plot(neighbors, prec_bad, label = bad_label, linestyle='--')
    # plt.ylim(0.60, 1.00)
    plt.xlabel('k-value')
    plt.ylabel('Accuracy of Prediction')
    plt.title(title_name + str(a))
lgd = plt.legend(bbox_to_anchor=(1.05, 1.0, 1.1, 0.1), loc='upper left')
# plt.tight_layout()

os.chdir('/home/ben/gripper_proj_2/data/plots/')
plt.savefig('test.png', bbox_extra_artists=(lgd), bbox_inches='tight')

plt.show()
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

# comb_data = berry_set #+ leaf_set
#
# os.chdir('/home/ben/gripper_proj_2/data/combined_data/')
# with open(dump_filename, 'w') as filehandle:
#         json.dump(comb_data, filehandle)
