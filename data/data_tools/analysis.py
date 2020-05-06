#!/usr/bin/env python

import matplotlib.pyplot as plt
import json
import numpy as np

#filename = 'Old_data/Basic_Ovoid_Medium_ver_data (12_23).txt'
#filename = 'Old_data/Basic_Ovoid_Medium_ver_data (12_23_set2).txt'
filename = 'Old_data/Basic_Ovoid_Medium_data_1_8_set_1.txt'
#filename = 'Old_data/test.txt'

success = [0]*65
fail = [0]*65

with open(filename, 'r') as filehandle:
    data_set_t1 = json.load(filehandle)

filename = 'Old_data/Basic_Ovoid_Medium_data_1_8_set_2.txt'
with open(filename, 'r') as filehandle:
    data_set_t2 = json.load(filehandle)

filename = 'Old_data/Basic_Ovoid_Medium_data_1_8_set_3.txt'
with open(filename, 'r') as filehandle:
    data_set_t3 = json.load(filehandle)

filename = 'Old_data/Basic_Ovoid_Medium_data_1_8_set_4.txt'
with open(filename, 'r') as filehandle:
    data_set_t4 = json.load(filehandle)

filename = 'Old_data/Basic_Ovoid_Medium_data_1_8_set_5.txt'
with open(filename, 'r') as filehandle:
    data_set_t5 = json.load(filehandle)

data_set = data_set_t1 + data_set_t2 + data_set_t3 + data_set_t4 + data_set_t5

for data in data_set:
    if data[-1] == 0: #success
        success[data[5]]+=1
    else:
        fail[data[5]]+=1

# evenly sampled time at 200ms intervals
t = np.arange(0., 65., 1)

# red dashes, blue squares and green triangles
plt.plot(t, success, 'ro', t, fail, 'bo')
plt.show()
