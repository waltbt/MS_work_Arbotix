#!/usr/bin/env python


import json
from sklearn.neighbors import KNeighborsClassifier

properties = []
labels = []

# Importing the training data
filename = 'gripper_data.txt'
with open(filename, 'r') as filehandle:
    data_set = json.load(filehandle)

# splitting the training data into properties and labels
for data in data_set:
    properties.append(data[0:3])
    labels.append(data[-1])

#test_value = [[88, 74, 95]]

test_value = [[25, 32, 50]] # Test value is what would come in from the sensors

neigh = KNeighborsClassifier(n_neighbors=5)

neigh.fit(properties, labels)

"""
Everything above this is set up and should be done on initialization.

Below this, should be done everytime the end effector has finished moving and
believes that it is in the correct location.
"""

output = neigh.predict(test_value) # Output is the result that we want to send to labview

print(output[0])
