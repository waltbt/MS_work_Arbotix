#!/usr/bin/env python

import os
import json

# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix

properties_train = []
labels_train = []
properties_test = []
labels_test = []

os.chdir('/home/ben/gripper_proj_2/data/combined_data/')
"""
Import datasets
"""
"""
IR
"""
# filename = 'IR_combined_data.txt'
# filename_test = 'IR_test_data.txt'
# size_of_data = 3
"""
TOF
"""
# filename = 'TOF_combined_data.txt'
# filename_test = 'TOF_test_data.txt'
# size_of_data = 3

"""
IR Color
"""
# filename = 'IR_Color_rgb_combined_data.txt'
# filename_test = 'IR_Color_rgb_test_data.txt'
# size_of_data = 5
"""
TOF Color
"""
# filename = 'TOF_Color_rgb_combined_data.txt'
# filename_test = 'TOF_Color_rgb_test_data.txt'
# size_of_data = 5

"""
IR TOF Color
"""

filename = 'IR_TOF_Color_rgb_combined_data.txt'
filename_test = 'IR_TOF_Color_rgb_test_data.txt'
size_of_data = 5


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

# scaler = StandardScaler()
scaler = StandardScaler()
scaler.fit(properties_train)

properties_train = scaler.transform(properties_train)
properties_test = scaler.transform(properties_test)

good_str_1 = ''
good_str_2 = ''
bad_str_1 = ''
bad_str_2 = ''
bad_prec_str = ''
good_prec_str = ''

type = ['rbf','poly','linear','sigmoid']
for a in type:
    print(a)
    classifier = svm.SVC(kernel= a)
    classifier.fit(properties_train, labels_train)

    labels_pred = classifier.predict(properties_test)

    cf = confusion_matrix(labels_test, labels_pred)
    print(cf)
    print(classification_report(labels_test, labels_pred))
    bad_prec_str = bad_prec_str + ' & ' + str(round(float(cf[0,0])/(cf[0,0]+cf[1,0]),2))
    good_prec_str = good_prec_str + ' & ' + str(round(float(cf[1,1])/(cf[1,1]+cf[0,1]),2))
    bad_str_1 = bad_str_1 + ' & ' + str(cf[0,0]) #Bad - Bad
    bad_str_2 = bad_str_2 + ' & ' + str(cf[1,0]) #Bad - Good
    good_str_1 = good_str_1 + ' & ' + str(cf[1,1]) #Good - Good
    good_str_2 = good_str_2 + ' & ' + str(cf[0,1]) #Good - Bad

print(good_str_1)
print(good_str_2)
print(bad_str_2)
print(bad_str_1)
print(good_prec_str)
print(bad_prec_str)
