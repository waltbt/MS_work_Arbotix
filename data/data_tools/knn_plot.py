#!/usr/bin/env python


import matplotlib.pyplot as plt
# from matplotlib import cm
# from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os
import json

plt.style.use('seaborn-whitegrid')
"""
IR Sensor
"""
# neighbors = range(1,25)
# bad = [0.64, 0.69, 0.83, 0.79, 0.85, 0.83, 0.94, 0.91, 0.93, 0.89, 1.0, 0.94, 0.94, 0.90, 0.94, 0.94, 0.94, 0.90, 0.89, 0.90, 0.89,0.90, 0.94, 0.94]
# success = [0.77, 0.86, 0.78, 0.82, 0.80, 0.83, 0.79, 0.84, 0.78, 0.79, 0.78, 0.80, 0.79, 0.82, 0.79, 0.80, 0.79, 0.81, 0.79, 0.82, 0.79, 0.81, 0.79, 0.80]
# title_name = 'IR - Accuracy of Prediction and the k-value'
# save_file = 'ir_knn_k_value.png'

"""
IR Sensor 2
"""
# neighbors = range(1,25)
# bad = [0.75, 0.71, 0.78, 0.73, 0.75, 0.73, 0.79, 0.76, 0.75, 0.74, 0.76, 0.73, 0.77, 0.75, 0.77, 0.75, 0.75, 0.74, 0.77, 0.77, 0.76, 0.77, 0.76, 0.76]
# success = [0.85, 0.95, 0.88, 0.93, 0.85, 0.88, 0.87, 0.88, 0.85, 0.86, 0.83, 0.86, 0.85, 0.85, 0.85, 0.85, 0.85, 0.86, 0.85, 0.87, 0.83, 0.85, 0.83, 0.83]
# title_name = 'IR - Accuracy of Prediction and the k-value'
# save_file = 'ir_knn_k_value_2.png'

"""
TOF Sensor
"""
# neighbors = range(1,25)
# bad = [0.75, 0.68, 0.82, 0.75, 1.0, 1.0, 1.0, 0.95, 1.0, 0.90, 0.94, 0.95, 1.0, 1.0, 1.0, 0.94, 1.0, 0.95, 1.0, 0.95, 1.0, 0.94, 0.94, 0.94]
# success = [0.92, 0.96, 0.92, 0.92, 0.93, 0.93, 0.92, 0.93, 0.93, 0.93, 0.91, 0.93, 0.93, 0.93, 0.92, 0.91, 0.92, 0.93, 0.93, 0.93, 0.90, 0.91, 0.89, 0.89]
# title_name = 'TOF - Accuracy of Prediction and the k-value'
# save_file = 'TOF_knn_k_value.png'

"""
TOF Sensor - No lux
"""
# neighbors = range(1,25)
# bad = [0.78, 0.74, 0.9, 0.85, 0.87, 0.87, 0.87, 0.84, 0.87, 0.87, 0.93, 0.89, 0.89, 0.86, 0.89, 0.89, 0.92, 0.86, 0.92, 0.89, 0.92, 0.89, 0.92, 0.86]
# success = [0.97, 0.97, 0.97, 0.97, 0.94, 0.96, 0.96, 0.96, 0.94, 0.94, 0.93, 0.93, 0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.92]
# title_name = 'TOF (NL) - Accuracy of Prediction and the k-value'
# save_file = 'TOF_NL_knn_k_value.png'

"""
IR_color all
"""
# neighbors = range(1,25)
# bad = [0.72, 0.67, 0.75, 0.71, 0.73, 0.69, 0.7, 0.71, 0.72, 0.72, 0.71, 0.69, 0.69, 0.7, 0.69, 0.69, 0.69, 0.69, 0.68, 0.67, 0.67, 0.68, 0.7, 0.71]
# success = [0.77, 0.88, 0.85, 0.89, 0.8, 0.87, 0.79, 0.89, 0.84, 0.87, 0.82, 0.83, 0.83, 0.85, 0.82, 0.83, 0.82, 0.82, 0.8, 0.81, 0.78, 0.8, 0.78, 0.81]
# title_name = 'IR-Color-All - Accuracy of Prediction and the k-value'
# save_file = 'ir_color_all_knn_k_value.png'

"""
IR_color rgb
"""
# neighbors = range(1,25)
# bad = [0.71, 0.67, 0.76, 0.72, 0.74, 0.72, 0.77, 0.78, 0.79, 0.77, 0.81, 0.81, 0.8, 0.79, 0.81, 0.77, 0.77, 0.75, 0.77, 0.76, 0.8, 0.77, 0.79, 0.78]
# success = [0.76, 0.81, 0.78, 0.78, 0.75, 0.78, 0.77, 0.83, 0.82, 0.84, 0.81, 0.86, 0.78, 0.82, 0.8, 0.8, 0.8, 0.84, 0.8, 0.85, 0.83, 0.84, 0.82, 0.82]
# title_name = 'IR-Color-rgb - Accuracy of Prediction and the k-value'
# save_file = 'ir_color_rgb_knn_k_value.png'

"""
IR_color k (Color temp)
"""
# neighbors = range(1,25)
# bad = [0.66, 0.61, 0.74, 0.65, 0.67, 0.64, 0.68, 0.67, 0.72, 0.74, 0.74, 0.76, 0.78, 0.79, 0.78, 0.78, 0.79, 0.78, 0.79, 0.78, 0.8, 0.78, 0.78, 0.76]
# success = [0.85, 0.93, 0.85, 0.9, 0.86, 0.89, 0.86, 0.91, 0.88, 0.91, 0.89, 0.93, 0.92, 0.95, 0.88, 0.93, 0.9, 0.93, 0.9, 0.93, 0.93, 0.93, 0.93, 0.93]
# title_name = 'IR-Color-K- Accuracy of Prediction and the k-value'
# save_file = 'ir_color_k_knn_k_value.png'

"""
TOF_color rgb
"""
# neighbors = range(1,25)
# bad = [0.64, 0.66, 0.67, 0.64, 0.68, 0.67, 0.74, 0.71, 0.74, 0.7, 0.72, 0.71, 0.72, 0.7, 0.72, 0.7, 0.72, 0.7, 0.72, 0.72, 0.74, 0.72, 0.74, 0.74]
# success = [0.84, 0.9, 0.83, 0.84, 0.83, 0.84, 0.85, 0.85, 0.84, 0.83, 0.84, 0.85, 0.84, 0.83, 0.84, 0.83, 0.84, 0.83, 0.84, 0.84, 0.84, 0.84, 0.84, 0.84]
# title_name = 'IR-Color-rgb- Accuracy of Prediction and the k-value'
# save_file = 'tof_color_rgb_knn_k_value.png'

"""
TOF_color all
"""
# neighbors = range(1,25)
# bad =
# success =
# title_name = 'TOF-Color-all- Accuracy of Prediction and the k-value'
# save_file = 'tof_color_all_knn_k_value.png'

"""
TOF_color k (Color temp)
"""
# neighbors = range(1,25)
# bad =
# success =
# title_name = 'TOF-Color-K- Accuracy of Prediction and the k-value'
# save_file = 'tof_color_k_knn_k_value.png'

"""
IR 1 Sensor
"""
neighbors = range(1,25)
bad = [0.63, 0.58, 0.65, 0.64, 0.65, 0.63, 0.63, 0.63, 0.62, 0.62, 0.63, 0.63, 0.63, 0.62, 0.63, 0.64, 0.65, 0.63, 0.63, 0.62, 0.63, 0.63, 0.66, 0.63]
success = [0.84, 0.89, 0.84, 0.87, 0.83, 0.87, 0.85, 0.89, 0.83, 0.85, 0.85, 0.89, 0.85, 0.87, 0.85, 0.87, 0.84, 0.85, 0.82, 0.82, 0.81, 0.85, 0.8, 0.84]
title_name = 'IR 1 Sensor - Accuracy of Prediction and the k-value'
save_file = 'ir_1_sensor_knn_k_value.png'

"""
IR 2 Sensor
"""
neighbors = range(1,25)
bad = [0.76, 0.69, 0.78, 0.74, 0.8, 0.79, 0.84, 0.83, 0.85, 0.84, 0.84, 0.84, 0.86, 0.86, 0.86, 0.84, 0.88, 0.86, 0.87, 0.86, 0.85, 0.85, 0.85, 0.85]
success = [0.76, 0.8, 0.8, 0.86, 0.8, 0.85, 0.86, 0.88, 0.85, 0.86, 0.84, 0.88, 0.86, 0.86, 0.86, 0.86, 0.87, 0.86, 0.85, 0.86, 0.83, 0.85, 0.83, 0.85]
title_name = 'IR 2 Sensor - Accuracy of Prediction and the k-value'
save_file = 'ir_2_sensor_knn_k_value.png'


plt.plot(neighbors, success, label = 'Good Grip')
plt.plot(neighbors, bad, label = 'Bad Grip')
plt.ylim(0.55, 1.00)
plt.xlabel('k-value')
plt.ylabel('Accuracy of Prediction')
plt.title(title_name)
plt.legend(loc='lower right')

os.chdir('/home/ben/gripper_proj_2/data/plots/')
plt.savefig(save_file)

plt.show()
