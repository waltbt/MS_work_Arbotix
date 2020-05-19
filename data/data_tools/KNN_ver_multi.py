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

test_num =25
neighbors = range(1,25)
total_bad = np.zeros(24)
total_good = np.zeros(24)
for a in range(0,test_num):
    properties = []
    labels = []
    # data_set = random.sample(berry_set, a)
    for data in berry_set:
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
    # print(prec_bad)
    # print(total_bad)
    total_bad += np.asarray(prec_bad)
    total_good += np.asarray(prec_good)

total_bad = total_bad/test_num
total_good = total_good/test_num
title_name = 'data size test '

good_label = 'Good Grip'
bad_label = 'Bad Grip'
plt.plot(neighbors, prec_good, label = good_label)
plt.plot(neighbors, prec_bad, label = bad_label)
# plt.ylim(0.60, 1.00)
plt.xlabel('k-value')
plt.ylabel('Accuracy of Prediction')
plt.title(title_name )
plt.legend(loc='lower right')
# plt.tight_layout()

# os.chdir('/home/ben/gripper_proj_2/data/plots/')
# plt.savefig('test.png', bbox_extra_artists=(lgd), bbox_inches='tight')

plt.show()
