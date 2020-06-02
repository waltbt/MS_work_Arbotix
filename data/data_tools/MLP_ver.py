#!/usr/bin/env python

import numpy as np
import os
import json
#from sklearn import neighbors, datasets

# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

# properties = []
# labels = []
properties_train = []
labels_train = []

properties_test = []
labels_test = []

os.chdir('/home/ben/gripper_proj_2/data/combined_data/')
"""
Import datasets
"""

"""
Import datasets
"""
"""
IR
"""
# filename = 'IR_combined_data.txt'
# filename_test = 'IR_test_data.txt'
# size_of_data = 3
# test_set = [(3,),(2,),(1,),(3,3),(3,2),(3,1),(2,2),(2,1),(1,1)]
# size_array = [(3,1)]
"""
TOF
"""
filename = 'TOF_combined_data.txt'
filename_test = 'TOF_test_data.txt'
size_of_data = 3
test_set = [(3,),(2,),(1,),(3,3),(3,2),(3,1),(2,2),(2,1),(1,1)]
size_array = [(3,),(1,),(2,2)]

"""
IR Color
"""
# filename = 'IR_Color_rgb_combined_data.txt'
# filename_test = 'IR_Color_rgb_test_data.txt'
# size_of_data = 5
# test_set = [(5,),(4,),(3,),(2,),(1,),(5,5),(5,4),(5,3),(5,2),(5,1),(4,4),(4,3),(4,2),(4,1),(3,3),(3,2),(3,1),(2,2),(2,1),(1,1)]
# size_array = [(4,2)]

"""
TOF Color
"""
# filename = 'TOF_Color_rgb_combined_data.txt'
# filename_test = 'TOF_Color_rgb_test_data.txt'
# size_of_data = 5
# test_set = [(5,),(4,),(3,),(2,),(1,),(5,5),(5,4),(5,3),(5,2),(5,1),(4,4),(4,3),(4,2),(4,1),(3,3),(3,2),(3,1),(2,2),(2,1),(1,1)]
# size_array = [(5,3),(4,3)]

"""
IR TOF Color
"""

# filename = 'IR_TOF_Color_rgb_combined_data.txt'
# filename_test = 'IR_TOF_Color_rgb_test_data.txt'
# size_of_data = 5
# test_set = [(5,),(4,),(3,),(2,),(1,),(5,5),(5,4),(5,3),(5,2),(5,1),(4,4),(4,3),(4,2),(4,1),(3,3),(3,2),(3,1),(2,2),(2,1),(1,1)]
# size_array = [(1,)]

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

# filename = 'IR_combined_data.txt'
# with open(filename, 'r') as filehandle:
#     data_set = json.load(filehandle)


# for data in data_set:
#     properties.append(data[0:3])
#     labels.append(data[-1])
properties_train = np.asarray(properties_train)
properties_train = properties_train.astype(np.float64)

properties_test = np.asarray(properties_test)
properties_test = properties_test.astype(np.float64)


# properties_train, properties_test, labels_train, labels_test = train_test_split(properties, labels, test_size=0.20)

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
for i in test_set:
    print(i)
    mlp = MLPClassifier(hidden_layer_sizes=i, max_iter=1000, alpha=1e-4,
                        solver='sgd', verbose=False, random_state=1,
                        learning_rate_init=.1)

    mlp.fit(properties_train, labels_train)
    print("Training set score: %f" % mlp.score(properties_train, labels_train))
    print("Test set score: %f" % mlp.score(properties_test, labels_test))

    labels_pred = mlp.predict(properties_test)

    cf = confusion_matrix(labels_test, labels_pred)
    print(cf)
    print(classification_report(labels_test, labels_pred))
    if cf[0,0]+cf[1,0] != 0:
        bad_prec_str = bad_prec_str + ' & ' + str(round(float(cf[0,0])/(cf[0,0]+cf[1,0]),2))
    else:
        bad_prec_str = bad_prec_str + ' & ' + 'NA'
    if cf[1,1]+cf[0,1] != 0:
        good_prec_str = good_prec_str + ' & ' + str(round(float(cf[1,1])/(cf[1,1]+cf[0,1]),2))
    else:
        good_prec_str = good_prec_str + ' & ' + 'NA'
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

activation = ['identity', 'logistic', 'tanh', 'relu']
solver = ['lbfgs', 'sgd', 'adam']
for a in size_array:
    print(a)
    for i in activation:
        print(i)
        mlp = MLPClassifier(hidden_layer_sizes=a, max_iter=1000, alpha=1e-4,
                            solver='sgd', activation=i, verbose=False, random_state=1,
                            learning_rate_init=.1)

        mlp.fit(properties_train, labels_train)
        print("Training set score: %f" % mlp.score(properties_train, labels_train))
        print("Test set score: %f" % mlp.score(properties_test, labels_test))

        labels_pred = mlp.predict(properties_test)


        print(confusion_matrix(labels_test, labels_pred))
        print(classification_report(labels_test, labels_pred))

    for i in solver:
        print(i)
        mlp = MLPClassifier(hidden_layer_sizes=a, max_iter=1000, alpha=1e-4,
                            solver=i, verbose=False, random_state=1,
                            learning_rate_init=.1)

        mlp.fit(properties_train, labels_train)
        print("Training set score: %f" % mlp.score(properties_train, labels_train))
        print("Test set score: %f" % mlp.score(properties_test, labels_test))

        labels_pred = mlp.predict(properties_test)


        print(confusion_matrix(labels_test, labels_pred))
        print(classification_report(labels_test, labels_pred))
