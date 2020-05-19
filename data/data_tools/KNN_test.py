#!/usr/bin/env python

import os
import json

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
# from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
# import seaborn as sn
# import pandas as pd

properties_train = []
labels_train = []

properties_test = []
labels_test = []

"""
Import datasets
"""

os.chdir('/home/ben/gripper_proj_2/data/combined_data/')


filename = 'IR_combined_data.txt'
filename_test = 'IR_final_test_data.txt'
size_of_data = 3
#
# filename = 'TOF_combined_data.txt'
# filename_test = 'TOF_final_test_data.txt'
# size_of_data = 6

# filename = 'IR_Color_all_combined_data.txt'
# size_of_data = 8

# filename = 'IR_Color_rgb_combined_data.txt'
# size_of_data = 5
#
# filename = 'IR_Color_k_combined_data.txt'
# size_of_data = 3

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


classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(properties_train, labels_train)

labels_pred = classifier.predict(properties_test)


cf = confusion_matrix(labels_test, labels_pred)
print(cf)
print("Report")
print(classification_report(labels_test, labels_pred))



# labels = [bad,success]
#
# df_cm = pd.DataFrame(array, labels, labels)
# # plt.figure(figsize=(10,7))
# sn.set(font_scale=1.4) # for label size
# sn.heatmap(df_cm, annot=True, annot_kws={"size": 16}) # font size
#
# plt.show()
# disp = plot_confusion_matrix(classifier, properties_test, labels_test,
#                              cmap=plt.cm.Blues,
#                              normalize=None)
# disp.ax_.set_title('A')
#
# # print(title)
# print(disp.confusion_matrix)
#
# plt.show()
