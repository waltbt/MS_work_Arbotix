#!/usr/bin/env python

import os
import json


# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

os.chdir('/home/ben/gripper_proj_2/data/combined_data/')

properties_train = []
labels_train = []
properties_test = []
labels_test = []

"""
Import datasets
"""

"""
IR
"""
# filename = 'IR_combined_data.txt'
# filename_test = 'IR_test_data.txt'
# size_of_data = 3
# crit = 'entropy'
# title_name = 'IR Accuracy of Prediction and the depth (DT/Entropy)'
# save_file = 'ir_dt_entropy_depth_value.png'

# filename = 'IR_combined_data.txt'
# filename_test = 'IR_test_data.txt'
# size_of_data = 3
# crit = 'geni'
# title_name = 'IR Accuracy of Prediction and the depth (DT/Gini)'
# save_file = 'ir_dt_gini_depth_value.png'


"""
TOF
"""
# filename = 'TOF_combined_data.txt'
# filename_test = 'TOF_test_data.txt'
# size_of_data = 3
# crit = 'entropy'
# title_name = 'TOF Accuracy of Prediction and the depth (DT/Entropy)'
# save_file = 'tof_dt_entropy_depth_value.png'


# filename = 'TOF_combined_data.txt'
# filename_test = 'TOF_test_data.txt'
# size_of_data = 3
# crit = 'gini'
# title_name = 'TOF Accuracy of Prediction and the depth (DT/Gini)'
# save_file = 'tof_dt_gini_depth_value.png'

"""
IR Color
"""
# filename = 'IR_Color_rgb_combined_data.txt'
# filename_test = 'IR_Color_rgb_test_data.txt'
# size_of_data = 5
# crit = 'entropy'
# title_name = 'IR Color Accuracy of Prediction and the depth (DT/Entropy)'
# save_file = 'ir_color_dt_entropy_depth_value.png'
#
# filename = 'IR_Color_rgb_combined_data.txt'
# filename_test = 'IR_Color_rgb_test_data.txt'
# size_of_data = 5
# crit = 'gini'
# title_name = 'IR Color Accuracy of Prediction and the depth (DT/Gini)'
# save_file = 'ir_color_dt_gini_depth_value.png'

"""
TOF Color
"""
# filename = 'TOF_Color_rgb_combined_data.txt'
# filename_test = 'TOF_Color_rgb_test_data.txt'
# size_of_data = 5
# crit = 'entropy'
# title_name = 'TOF Color Accuracy of Prediction and the depth (DT/Entropy)'
# save_file = 'tof_color_dt_entropy_depth_value.png'
#
# filename = 'TOF_Color_rgb_combined_data.txt'
# filename_test = 'TOF_Color_rgb_test_data.txt'
# size_of_data = 5
# crit = 'gini'
# title_name = 'TOF Color Accuracy of Prediction and the depth (DT/Gini)'
# save_file = 'tof_color_dt_gini_depth_value.png'

"""
IR TOF Color
"""

filename = 'IR_TOF_Color_rgb_combined_data.txt'
filename_test = 'IR_TOF_Color_rgb_test_data.txt'
size_of_data = 5
crit = 'entropy'
title_name = 'IR TOF Color Accuracy of Prediction and the depth (DT/Entropy)'
save_file = 'ir_tof_color_dt_entropy_depth_value.png'


# filename = 'IR_TOF_Color_rgb_combined_data.txt'
# filename_test = 'IR_TOF_Color_rgb_test_data.txt'
# size_of_data = 5
# crit = 'gini'
# title_name = 'IR TOF Color Accuracy of Prediction and the depth (DT/Gini)'
# save_file = 'ir_tof_color_dt_gini_depth_value.png'


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

prec_bad = []
prec_good = []

prec_bad_l = []
prec_good_l = []
prec_leaf_l = []
# properties_train, properties_test, labels_train, labels_test = train_test_split(properties, labels, test_size=0.20)

# scaler = StandardScaler()
# scaler.fit(properties_train)
#
# properties_train = scaler.transform(properties_train)
# properties_test = scaler.transform(properties_test)

# clf = tree.DecisionTreeClassifier(criterion='entropy')
# clf.fit(properties_train, labels_train)
# labels_pred = clf.predict(properties_test)
# cf = confusion_matrix(labels_test, labels_pred)
# print(cf)
# print(classification_report(labels_test, labels_pred))


for i in range(1,26):

    clf = tree.DecisionTreeClassifier(criterion=crit,max_depth=i)

    clf.fit(properties_train, labels_train)

    # tree.plot_tree(clf.fit(properties_train, labels_train))

    # import graphviz
    # dot_data = tree.export_graphviz(clf, out_file=None,class_names=['A','B','C'])
    # graph = graphviz.Source(dot_data)
    # graph.render("IR1_data")

    labels_pred = clf.predict(properties_test)

    cf = confusion_matrix(labels_test, labels_pred)

    print(cf)
    print(classification_report(labels_test, labels_pred))

    prec_bad.append(round(float(cf[0,0])/(cf[0,0]+cf[1,0]),2))
    prec_good.append(round(float(cf[1,1])/(cf[1,1]+cf[0,1]),2))
    # leaf data
    # prec_bad_l.append(round(float(cf[0,0])/(cf[0,0]+cf[1,0]+cf[2,0]),2))
    # prec_leaf_l.append(round(float(cf[2,2])/(cf[2,2]+cf[0,2]+cf[1,2]),2))
    # prec_good_l.append(round(float(cf[1,1])/(cf[1,1]+cf[0,1]+cf[2,1]),2))
# print("Bad precision")
# print(prec_bad_l)
# print("Good precision")
# print(prec_good_l)
# print("Leaf precision")
# print(prec_leaf_l)

print("Bad precision")
print(prec_bad)
print("Good precision")
print(prec_good)

neighbors = range(1,26)
plt.plot(neighbors, prec_good, label = 'Good Grip')
plt.plot(neighbors, prec_bad, label = 'Bad Grip')

# plt.plot(neighbors, prec_good_l, label = 'Good Grip')
# plt.plot(neighbors, prec_bad_l, label = 'Bad Grip')
# plt.plot(neighbors, prec_leaf_l, label = 'Leaf')
plt.ylim(0.65, 1.05)
plt.xlabel('Max Depth')
plt.ylabel('Accuracy of Prediction')
plt.title(title_name)
plt.legend(loc='lower right')
# plt.legend(loc='upper right')

os.chdir('/home/ben/gripper_proj_2/data/plots/')
plt.savefig(save_file)

plt.show()
