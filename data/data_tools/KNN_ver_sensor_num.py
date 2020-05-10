#!/usr/bin/env python

import os
import json

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

properties = []
labels = []

"""
Import datasets
"""

os.chdir('/home/ben/gripper_proj_2/data/combined_data/')


filename = 'IR_combined_data.txt'
size_of_data = 3
#
# filename = 'TOF_combined_data.txt'
# size_of_data = 6

# filename = 'IR_Color_all_combined_data.txt'
# size_of_data = 8

# filename = 'IR_Color_rgb_combined_data.txt'
# size_of_data = 5
#
# filename = 'IR_Color_k_combined_data.txt'
# size_of_data = 3

# filename = 'TOF_Color_rgb_combined_data.txt'
# size_of_data = 5

# filename = 'TOF_NL_combined_data.txt' # No lux
# size_of_data = 3

with open(filename, 'r') as filehandle:
    data_set = json.load(filehandle)


for data in data_set:
    properties.append(data[0:2])
    labels.append(data[-1])



properties_train, properties_test, labels_train, labels_test = train_test_split(properties, labels, test_size=0.20)

scaler = StandardScaler()
scaler.fit(properties_train)

properties_train = scaler.transform(properties_train)
properties_test = scaler.transform(properties_test)

prec_bad = []
prec_good = []

for i in range(1,25):
    print("Number of Neighbors: ", i)
    classifier = KNeighborsClassifier(n_neighbors=i)
    classifier.fit(properties_train, labels_train)

    labels_pred = classifier.predict(properties_test)


    cf = confusion_matrix(labels_test, labels_pred)
    print(cf)
    print("Report")
    print(classification_report(labels_test, labels_pred))
    prec_bad.append(round(float(cf[0,0])/(cf[0,0]+cf[1,0]),2))
    prec_good.append(round(float(cf[1,1])/(cf[1,1]+cf[0,1]),2))

print("Bad precision")
print(prec_bad)
print("Good precision")
print(prec_good)
