#!/usr/bin/env python

import os
import json

# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Perceptron
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
# properties = []
# labels = []
properties_train = []
labels_train = []

properties_test = []
labels_test = []
"""
Import datasets
"""

os.chdir('/home/ben/gripper_proj_2/data/combined_data/')

"""
IR
"""
filename = 'IR_combined_data.txt'
filename_test = 'IR_test_data.txt'
size_of_data = 3
# title_name = 'IR Accuracy of Prediction and the k-value'
# save_file = 'ir_perc.png'

# filename = 'IR_combined_leaf_data.txt'
# size_of_data = 3
#
"""
TOF
"""
# filename = 'TOF_combined_data.txt'
# filename_test = 'TOF_test_data.txt'
# size_of_data = 3
# title_name = 'TOF - Accuracy of Prediction and the k-value'
# save_file = 'tof_knn_k_value.png'

# filename = 'TOF_combined_data.txt'
# filename_test = 'TOF_test_data.txt'
# size_of_data = 2
# title_name = 'TOF - 2 Sensors - Accuracy of Prediction and the k-value'
# save_file = 'tof_2_sensor_knn_k_value.png'

# filename = 'TOF_combined_data.txt'
# filename_test = 'TOF_test_data.txt'
# size_of_data = 1
# title_name = 'TOF - 1 Sensor - Accuracy of Prediction and the k-value'
# save_file = 'tof_1_sensor_knn_k_value.png'

# filename = 'TOF_combined_leaf_data.txt'
# filename_test = 'TOF_test_leaf_data.txt'
# size_of_data = 3
# title_name = 'TOF - Accuracy of Prediction and the k-value with Leaves'
# save_file = 'tof_leaf_knn_k_value.png'


"""
IR Color
"""
# filename = 'IR_Color_all_combined_data.txt'
# filename_test = 'IR_Color_test_data.txt'
# size_of_data = 8

# filename = 'IR_Color_rgb_combined_data.txt'
# filename_test = 'IR_Color_rgb_test_data.txt'
# size_of_data = 5
# title_name = 'IR-Color - rgb - Accuracy of Prediction and the k-value'
# save_file = 'ir_color_rgb_knn_k_value.png'

# filename = 'IR_Color_k_combined_data.txt'
# size_of_data = 3

# filename = 'TOF_Color_rgb_combined_data.txt'
# size_of_data = 5


# with open(filename, 'r') as filehandle:
#     data_set = json.load(filehandle)
#
#
# for data in data_set:
#     properties.append(data[0:size_of_data])
#     labels.append(data[-1])

with open(filename, 'r') as filehandle:
    data_set = json.load(filehandle)

for data in data_set:
    properties_train.append(data[0:size_of_data])
    labels_train.append(data[-1])

with open(filename_test, 'r') as filehandle:
    data_set = json.load(filehandle)

for data in data_set:
    properties_test.append(data[0:size_of_data])
    labels_test.append(data[-1])

# properties_train, properties_test, labels_train, labels_test = train_test_split(properties, labels, test_size=0.20)



scaler = StandardScaler()
scaler.fit(properties_train)

properties_train = scaler.transform(properties_train)
properties_test = scaler.transform(properties_test)

classifier = Perceptron(tol=1e-3, random_state=0)
# clf.fit(X, y)
classifier.fit(properties_train, labels_train)
labels_pred = classifier.predict(properties_test)
cf = confusion_matrix(labels_test, labels_pred)
print(cf)
print("Report")
print(classification_report(labels_test, labels_pred))

# prec_bad = []
# prec_good = []
#
# prec_bad_l = []
# prec_good_l = []
# prec_leaf_l = []

# for i in range(1,26):
#     print("Number of Neighbors: ", i)
#     classifier = KNeighborsClassifier(n_neighbors=i)
#     classifier.fit(properties_train, labels_train)
#
#     labels_pred = classifier.predict(properties_test)
#
#
#     cf = confusion_matrix(labels_test, labels_pred)
#     print(cf)
#     print("Report")
#     print(classification_report(labels_test, labels_pred))
#     # prec_bad.append(round(float(cf[0,0])/(cf[0,0]+cf[1,0]),2))
#     # prec_good.append(round(float(cf[1,1])/(cf[1,1]+cf[0,1]),2))
#     # leaf data
#     prec_bad_l.append(round(float(cf[0,0])/(cf[0,0]+cf[1,0]+cf[2,0]),2))
#     prec_leaf_l.append(round(float(cf[2,2])/(cf[2,2]+cf[0,2]+cf[1,2]),2))
#     prec_good_l.append(round(float(cf[1,1])/(cf[1,1]+cf[0,1]+cf[2,1]),2))
# print("Bad precision")
# print(prec_bad_l)
# print("Good precision")
# print(prec_good_l)
# print("Leaf precision")
# print(prec_leaf_l)
#
# # print("Bad precision")
# # print(prec_bad)
# # print("Good precision")
# # print(prec_good)
#
# neighbors = range(1,26)
# # plt.plot(neighbors, prec_good, label = 'Good Grip')
# # plt.plot(neighbors, prec_bad, label = 'Bad Grip')
#
# plt.plot(neighbors, prec_good_l, label = 'Good Grip')
# plt.plot(neighbors, prec_bad_l, label = 'Bad Grip')
# plt.plot(neighbors, prec_leaf_l, label = 'Leaf')
# plt.ylim(0.65, 1.05)
# plt.xlabel('k-value')
# plt.ylabel('Accuracy of Prediction')
# plt.title(title_name)
# plt.legend(loc='lower right')
#
# os.chdir('/home/ben/gripper_proj_2/data/plots/')
# plt.savefig(save_file)
#
# plt.show()
