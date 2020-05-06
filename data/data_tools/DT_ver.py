#!/usr/bin/env python

import os
import json


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix


properties = []
labels = []

"""
Import datasets
"""

os.chdir('/home/ben/gripper_proj_2/data/combined_data/')


filename = 'IR_combined_data.txt'
with open(filename, 'r') as filehandle:
    data_set = json.load(filehandle)

for data in data_set:
    properties.append(data[0:3])
    labels.append(data[-1])


properties_train, properties_test, labels_train, labels_test = train_test_split(properties, labels, test_size=0.20)

# scaler = StandardScaler()
# scaler.fit(properties_train)
#
# properties_train = scaler.transform(properties_train)
# properties_test = scaler.transform(properties_test)

clf = tree.DecisionTreeClassifier()

clf.fit(properties_train, labels_train)

#tree.plot_tree(clf.fit(properties_train, labels_train))

import graphviz
dot_data = tree.export_graphviz(clf, out_file=None,class_names=['A','B','C'])
graph = graphviz.Source(dot_data)
graph.render("IR1_data")

labels_pred = clf.predict(properties_test)


print(confusion_matrix(labels_test, labels_pred))
print(classification_report(labels_test, labels_pred))
