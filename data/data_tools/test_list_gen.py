#!/usr/bin/env python

import json

#filename = "/home/ben/gripper_proj_py/data/Basic_Ovoid_Medium_training.txt"
# filename = "/home/ben/gripper_proj_py/data/Basic_Ovoid_Large_training.txt"
# filename = "/home/ben/gripper_proj_py/data/Basic_Sphere_Medium_training.txt"
# filename = "/home/ben/gripper_proj_py/data/Basic_Sphere_Large_training.txt"
# filename = "/home/ben/gripper_proj_py/data/Basic_Ovoid_Small_training.txt"
# filename = "/home/ben/gripper_proj_py/data/Basic_Sphere_Small_training.txt"
filename = "/home/ben/gripper_proj_py/data/Tabbed_Sphere_Large_training.txt" #2.5cm??


test_pt_list =[]

base_list_plus = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
base_list_neg = [-0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, -0.9]


x_list = [0.0] + base_list_plus + base_list_neg + [1.0, 2.0, 3.0,-1.0, -2.0, -3.0]
y_list = [0.0] + base_list_plus + base_list_neg + [1.0, 2.0, 3.0,-1.0, -2.0, -3.0]
z_list = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]


radius_list = [] # The radius of the circle at each level
for z in z_list:
    #radius_list.append(0.6*z + 0.5)
    radius_list.append(1.0*z + 0.3) #For Sphere Medium
    #radius_list.append(3.0) #For Sphere Medium


for i in [1, 2, 3]:
    for a in base_list_plus:
        x_list.append(i+a)
        x_list.append(-(i+a))
        y_list.append(i+a)
        y_list.append(-(i+a))




rad_index = 0
for z in z_list:
    for a in x_list:
        for b in y_list:
            if (a**2 + b**2)**(0.5) < radius_list[rad_index]:
                test_pt_list.append([a/100.0, b/100.0, z/100.0])
    rad_index += 1

print(len(test_pt_list))

with open(filename, 'w') as filehandle:
    json.dump(test_pt_list, filehandle)
