#!/usr/bin/env python

import copy
import time
import rospy
import numpy as np
#from gt_header import *
#from kinematics_header import *
#from kinematics import *
from std_msgs.msg import Empty # Used to call for sensor readings
from std_msgs.msg import Bool # Used for gripper
#from std_msgs.msg import String
from std_msgs.msg import Int32 #used to return button value

from arm_control.msg import command
from arm_control.msg import IR_sensor_data
from arm_control.msg import TOF_sensor_data
from arm_control.msg import color_sensor_data


import json
import random
import os
from sklearn.neighbors import KNeighborsClassifier

import pickle

# 20Hz
SPIN_RATE = 20

# UR3 home location
home = np.radians([120, -90, 90, -90, -90, 0])
# Set for red ovoid target
test_home = [0.3, 0.25, 0.12 +.015] #Set the home position for testing - all movement is relative to this
test_home_over = [0.3, 0.25, 0.17]

# UR3 current position, using home position for initialization
current_position = copy.deepcopy(home)

# Other Global Variables
test_pt_list = [] # A list of x,y,z points that will be tested for the current configuration

test_pt_list_ver = []

button_data = -1 # Buttons used to log gripper status and control program

sensor_TOF_reading = [-1, -1, -1, -1.0, -1.0, -1.0] # Sensor TOF reading from arduino
sensor_IR_reading = [-1, -1, -1] # Sensor IR reading from arduino
sensor_color_reading = [-1, -1, -1, -1, -1, -1.0] # Sensor color reading from arduino

OFF_LINE = True

IR_sensor = False
TOF_sensor = False
color_sensor = False


thetas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


current_io_0 = False
current_position_set = False

"""
################################################################################
The Start of code
################################################################################
"""


class sensor_data_struct():
    def __init__(self, point, IR_data, TOF_data, color_data, button_data):
        self.pt = point
        self.IR = IR_data
        self.TOF = TOF_data
        self.color = color_data
        self.button = button_data

"""
################################################################################
Callback Functions
"""



"""
Receives data from buttons pushed
"""
def button_callback(msg):
    global button_data
    button_data = msg.data

"""
Returns the range data from the IR sensor
"""
def sensor_IR_callback(msg):
    global sensor_IR_reading
    sensor_IR_reading[0] = msg.sensor_reading[0]
    sensor_IR_reading[1] = msg.sensor_reading[1]
    sensor_IR_reading[2] = msg.sensor_reading[2]

"""
Returns the range data from the TOF sensor
"""
def sensor_TOF_callback(msg):
    global sensor_TOF_reading
    sensor_TOF_reading[0] = msg.range_reading[0]
    sensor_TOF_reading[1] = msg.range_reading[1]
    sensor_TOF_reading[2] = msg.range_reading[2]
    sensor_TOF_reading[3] = msg.lux_reading[0]
    sensor_TOF_reading[4] = msg.lux_reading[1]
    sensor_TOF_reading[5] = msg.lux_reading[2]

"""
Returns the range data from the TOF sensor
"""
def sensor_color_callback(msg):
    global sensor_color_reading
    sensor_color_reading[0] = msg.rgb_values[0]
    sensor_color_reading[1] = msg.rgb_values[1]
    sensor_color_reading[2] = msg.rgb_values[2]
    sensor_color_reading[3] = msg.rgb_values[3]
    sensor_color_reading[4] = msg.color_temp
    sensor_color_reading[5] = msg.lux

"""
Move the arm to a given point
"""
def move_arm(pub_cmd, loop_rate, dest, vel, accel):

    global thetas
    global SPIN_RATE
    global OFF_LINE

    error = 0
    spin_count = 0
    at_goal = 0
    if OFF_LINE == False:
        driver_msg = command()
        driver_msg.destination = dest
        driver_msg.v = vel
        driver_msg.a = accel
        driver_msg.io_0 = False # current_io_0 (Alawys leave the gripper off)
        pub_cmd.publish(driver_msg)

        loop_rate.sleep()

        while(at_goal == 0):

            if( abs(thetas[0]-driver_msg.destination[0]) < 0.0005 and \
                abs(thetas[1]-driver_msg.destination[1]) < 0.0005 and \
                abs(thetas[2]-driver_msg.destination[2]) < 0.0005 and \
                abs(thetas[3]-driver_msg.destination[3]) < 0.0005 and \
                abs(thetas[4]-driver_msg.destination[4]) < 0.0005 and \
                abs(thetas[5]-driver_msg.destination[5]) < 0.0005 ):

                at_goal = 1
                #rospy.loginfo("Goal is reached!")

            loop_rate.sleep()

            if(spin_count >  SPIN_RATE*5):

                pub_cmd.publish(driver_msg)
                rospy.loginfo("Just published again driver_msg")
                spin_count = 0

            spin_count = spin_count + 1

    return error


"""
Main Menu
"""
def print_menu():

    print("Menu: ")
    print("0: Exit Program")
    print("1: Train")
    print("2: Open Gripper")
    print("3: Home the arm")
    print("4: Move arm out of the way")
    print("5: Read TOF sensor")
    print("6: Read IR Sensor")
    print("7: Test Leafs")
    print("8: Prediction Test")
    print("9: Characterize Sensor")
    print("10: Distance test")
    print("11: Read color sensor")
    print("12: LED on")
    print("13: LED off")
    print("14: servo test")


def cycle_testpoints(pub_cmd, sen_IR_cmd, sen_TOF_cmd, sen_color_cmd, grp_cmd, loop_rate, filename):
    global test_pt_list
    global button_data
    global sensor_TOF_reading
    global sensor_IR_reading
    global sensor_color_reading
    global TOF_sensor
    global IR_sensor
    global color_sensor

    data_collected = []
    vel = 4.0
    accel = 4.0
    #print(test_pt_list)
    tracker = 1
    for pt in test_pt_list:
        print("Moving to ", pt)
        x_d = pt[0] + test_home[0]
        y_d = pt[1] + test_home[1]
        z_d = pt[2] + test_home[2]
        z_over = z_d + 0.05

        theta_d_over = lab_invk(x_d, y_d, z_over, 90)
        move_arm(pub_cmd, loop_rate, theta_d_over, vel, accel)
        theta_d = lab_invk(x_d, y_d, z_d, 90)
        move_arm(pub_cmd, loop_rate, theta_d, vel, accel)

        presensor_TOF = [-1, -1, -1, -1.0, -1.0, -1.0]
        presensor_IR = [-1,-1,-1]
        presensor_color = [-1, -1, -1, -1, -1, -1.0]
        close_sensor_TOF = [-1, -1, -1, -1.0, -1.0, -1.0]
        close_sensor_IR = [-1,-1,-1]
        close_sensor_color = [-1, -1, -1, -1, -1, -1.0]

        #Perform tests before closing gripper
        if(TOF_sensor == True):
            presensor_TOF = read_TOF_sensor(sen_TOF_cmd)
        if(IR_sensor == True):
            presensor_IR = read_IR_sensor(sen_IR_cmd)
        if(color_sensor == True):
            presensor_color = read_color_sensor(sen_color_cmd)
        # Close gripper
        grp_cmd.publish(True)
        rospy.sleep(0.5)
        # Gather data after closing gripper
        if(TOF_sensor == True):
            close_sensor_TOF = read_TOF_sensor(sen_TOF_cmd)
        if(IR_sensor == True):
            close_sensor_IR = read_IR_sensor(sen_IR_cmd)
        if(color_sensor == True):
            close_sensor_color = read_color_sensor(sen_color_cmd)

        # Gather button data
        print(tracker)
        tracker += 1
        print("Status of the grip: good (green), bad (red) or end test (yellow)")
        while button_data == -1:
            pass
        #print(presensor)
        #print(close_sensor)
        #data_collected.append(pt + presensor_IR + close_sensor_IR + presensor_TOF + close_sensor_TOF + presensor_color + close_sensor_color + [button_data])
        data_collected.append(sensor_data_struct(pt, presensor_IR + close_sensor_IR, presensor_TOF + close_sensor_TOF, presensor_color + close_sensor_color, button_data))
        button_data = -1

        # open gripper
        grp_cmd.publish(False)

        # Move over
        theta_d_over = lab_invk(x_d, y_d, z_over, 90)
        move_arm(pub_cmd, loop_rate, theta_d_over, vel, accel)

    with open('data/' + filename + '_data.txt', 'w') as filehandle:
        #json.dump(data_collected, filehandle)
        pickle.dump(data_collected, filehandle)


def file_menu():
    global TOF_sensor
    global IR_sensor
    global color_sensor

    while(1):
        print("0: Exit Menu")
        print("1: IR")
        print("2: TOF")
        print("3: IR + Color")
        print("4: TOF + Color")
        print("5: IR + TOF + Color")
        sensor_type_raw = raw_input("Sensor Config: ")
        if(int(sensor_type_raw) == 1):
            print("IR")
            sensor_type = "IR"
            TOF_sensor = False
            color_sensor = False
            IR_sensor = True
            break
        if(int(sensor_type_raw) == 2):
            print("TOF")
            sensor_type = "TOF"
            TOF_sensor = True
            color_sensor = False
            IR_sensor = False
            break
        if(int(sensor_type_raw) == 3):
            print("IR + Color")
            sensor_type = "IR_Color"
            TOF_sensor = False
            color_sensor = True
            IR_sensor = True
            break
        if(int(sensor_type_raw) == 4):
            print("TOF + Color")
            sensor_type = "TOF_Color"
            color_sensor = True
            TOF_sensor = True
            IR_sensor = False
            break
        if(int(sensor_type_raw) == 5):
            print("IR + TOF + Color")
            sensor_type = "IR_TOF_Color"
            color_sensor = True
            TOF_sensor = True
            IR_sensor = True
            break
        elif (int(sensor_type_raw) == 0):
            print("Exiting...")
            return 0 #??? Is this right?
        else:
            print("Please just enter the character 0 1 or 2 \n\n")

    filename = sensor_type

    return filename



def train(pub_cmd, sen_IR_cmd, sen_TOF_cmd, sen_color_cmd, grp_cmd, loop_rate):

    """
    find out what test we are conducting
    load up the correct test cycle_testpoints
    call the correct test function???
    """
    global test_pt_list

    number_of_points = raw_input("How many training points? ")

    filename = file_menu()
    # open output file and read in test points
    with open('data/test_points/' + 'Basic_Ovoid_Medium_training.txt', 'r') as filehandle:
        test_pt_list_temp = json.load(filehandle)

    test_pt_list = random.sample(test_pt_list_temp, int(number_of_points))
    #print(test_pt_list)
    cycle_testpoints(pub_cmd, sen_IR_cmd, sen_TOF_cmd, sen_color_cmd, grp_cmd, loop_rate, filename)
    print("Moving arm out of the way")
    theta_home_over = lab_invk(test_home_over[0], test_home_over[1], test_home_over[2], 90)
    move_arm(pub_cmd, loop_rate, theta_home_over, 4.0, 4.0)
    move_arm(pub_cmd, loop_rate, home, 4.0, 4.0)

def read_TOF_sensor(sen_cmd):
    global sensor_TOF_reading
    # Gather sensor data
    sen_cmd.publish()
    while sensor_TOF_reading[0] == -1:
        pass
    #while sensor_TOF_reading[1] == -1:
        #pass
    data = copy.copy(sensor_TOF_reading)
    sensor_TOF_reading = [-1, -1, -1, -1.0, -1.0, -1.0]
    print("TOF Read")
    return data

def read_IR_sensor(sen_cmd):
    global button_data
    global sensor_IR_reading

    # Gather sensor data
    sen_cmd.publish()
    while sensor_IR_reading[0] == -1:
        pass
    data = copy.copy(sensor_IR_reading)
    sensor_IR_reading = [-1, -1, -1]
    print("IR Read")
    return data


def read_color_sensor(sen_cmd):
    global sensor_color_reading
    # Gather sensor data
    sen_cmd.publish()
    while sensor_color_reading[0] == -1:
        pass
    data = copy.copy(sensor_color_reading)
    sensor_color_reading = [-1, -1, -1, -1, -1, -1.0]
    print("Color Read")
    return data

"""
Collect data for leaves and branches
"""
def leaf_test(sen_IR_cmd, sen_TOF_cmd, sen_color_cmd):
    global button_data
    global sensor_IR_reading
    tracker = 0
    data_collected = []
    # Create a file name
    filename = file_menu()
    # Read number of cycles
    num_cycles = raw_input("How many cycles?")
    for a in range(int(num_cycles)):
        # Press button to advance
        print("Press button to take reading.")
        while button_data == -1:
            pass
        # Read the sensors
        sensor_TOF = [-1, -1, -1, -1.0, -1.0, -1.0]
        sensor_IR = [-1,-1,-1]
        sensor_color = [-1, -1, -1, -1, -1, -1.0]

        if(TOF_sensor == True):
            sensor_TOF = read_TOF_sensor(sen_TOF_cmd)
        if(IR_sensor == True):
            sensor_IR = read_IR_sensor(sen_IR_cmd)
        if(color_sensor == True):
            sensor_color = read_color_sensor(sen_color_cmd)

        rospy.sleep(0.5)

        print(tracker)
        tracker += 1
        # data_collected.append(sensor)
        #data_collected.append(sensor_data_struct(pt, sensor_IR, sensor_TOF, sensor_color, "leaf"))
        data_collected.append(sensor_data_struct(pt, sensor_IR, sensor_TOF, sensor_color, "leaf"))


        button_data = -1

    with open('data/' + filename + '_leaf.txt', 'w') as filehandle:
        #json.dump(data_collected, filehandle)
        pickle.dump(data_collected, filehandle)



def char_test(pub_cmd, loop_rate, sen_IR_cmd):
    vel = 4.0
    accel = 4.0

    data_collected = []
    local_home = [0.3, 0.25, 0.12-.028]#Offset to reach top of target
    #Bring in a bunch of test points
    os.chdir('/home/ben/gripper_proj_py/data/')
    #filename = 'char_test_points.txt'
    #with open(filename, 'r') as filehandle:
    #    data_set_temp = json.load(filehandle)

    #Move to each point and take a Reading

    x_list = np.linspace(-3,3,31)/100.0
    y_list = np.linspace(-3,3,13)/100.0
    z_list = np.linspace(0,6,13)/100.0

    for z in z_list:
        for y in y_list:
            for x in x_list:
                x_d = local_home[0] + x
                y_d = local_home[1] + y
                z_d = local_home[2] + z
                theta_d = lab_invk(x_d, y_d , z_d , 90)
                move_arm(pub_cmd, loop_rate, theta_d, vel, accel)
                sen_IR_cmd.publish()
                while sensor_IR_reading[0] == -1:
                    pass
                data_collected.append(point+[sensor_IR_reading[0]])


    #Save the data in a file
    with open('IR_char_data.txt', 'w') as filehandle:
        json.dump(data_collected, filehandle)


def distance_test(pub_cmd, loop_rate, sen_IR_cmd):
    vel = 4.0
    accel = 4.0

    data_collected = []
    local_home = [0.3, 0.25, 0.12-.028] #Offset to reach top of target
    #Bring in a bunch of test points
    os.chdir('/home/ben/gripper_proj_py/data/')


    data_set = np.linspace(0,6,61)/100.0
    #Move to each point and take a Reading
    for point in data_set:
        x_d = local_home[0]
        y_d = local_home[1]
        z_d = local_home[2] + point



        theta_d = lab_invk(x_d, y_d , z_d , 90)
        move_arm(pub_cmd, loop_rate, theta_d, vel, accel)
        sen_IR_cmd.publish()
        while sensor_IR_reading[0] == -1:
            pass
        data_collected.append([point]+[sensor_IR_reading[0]])
    #Save the data in a file
    with open('IR_distance_data.txt', 'w') as filehandle:
        json.dump(data_collected, filehandle)


def IK_fun(x,y,z,theta_yaw_rad):

    theta = [None, None, None, None, None, None]

    l1 = 0.093+0.038
    l2 = 0.143
    l3 = 0.048
    l4 = 0.115
    l5 = 0.066+
    l6 = 0.048
    l7 = 0.040
    l8 = 0 # need to set

    x_cen = x - l7*np.cos(theta_yaw_rad)
    y_cen = y - l7*np.sin(theta_yaw_rad)
    z_cen = z + l8 + l6

    R = np.sqrt(x_cen**2 + y_cen**2)
    alpha = np.arctan2(y_cen, x_cen)
    beta = np.arcsin(l5/R)

    theta1 = alpha + beta

    theta6 = theta1 - theta_yaw_rad + np.pi/2
    x_4cen = x_cen - l5*np.sin(theta1)
    y_4cen = y_cen + l5*np.cos(theta1)
    z_4cen = z_cen
    d = z_4cen - l1
    D1 = np.sqrt(x_4cen**2 + y_4cen**2 + d**2)
    D2 = np.sqrt(l2**2 + l3**2)
    D3 = np.sqrt(x_4cen**2 + y_4cen**2)
    phi1 = np.arctan2(d,D3)
    #print(phi1)
    phi2 = loc(l4, D1, D2)
    #print(phi2)
    phi3 = np.arctan2(l3,l2)
    #print(np.rad2deg(phi3))
    theta2 = np.pi/2 - (phi1 + phi2 + phi3)
    gamma = loc(D1, l4, D2)
    theta3 = gamma - (phi3 + np.pi/2)
    theta4 = np.pi/2
    sigma = loc(D2, l4, D1)
    theta5 = sigma - phi1 + np.pi/2

    # print(theta1)
    # print(theta2)
    # print(theta3)
    # print(theta4)
    # print(theta5)
    # print(theta6)

    theta[0] = np.clip(int(2048 + (theta1/np.pi)*2048), 1024, 3072)
    theta[1] = np.clip(int(2048 + (theta2/np.pi)*2048), 1024, 3072)
    theta[2] = np.clip(int(2048 + (theta3/np.pi)*2048), 1024, 3072)
    theta[5] = np.clip(np.rad2deg(theta4) + 10, 0, 180) #Roll
    theta[4] = np.clip(np.rad2deg(theta5),0, 180) #pitch
    theta[3] = np.clip(np.rad2deg(theta6) + 2,0, 180) #Yaw

    return theta


def loc(opp,leg1,leg2):
    return np.arccos((opp**2 - leg1**2 - leg2**2)/(-2*leg1*leg2))


"""
################################################################################
The Main function
################################################################################
"""
def main():

    global home
    global SPIN_RATE

    # Initialize ROS node
    rospy.init_node('arm_control_node') #?????????????
    loop_rate = rospy.Rate(SPIN_RATE)
    # Initialize publisher for ur3/command with buffer size of 10
    #pub_command = rospy.Publisher('ur3/command', command, queue_size=10)

    # Initialize subscriber to ur3/position and callback fuction
    # each time data is published
    #sub_position = rospy.Subscriber('ur3/position', position, position_callback)

    # Arduino
    ## Gripper Control
    gripper_command = rospy.Publisher('toggle_gripper', Bool, queue_size=10)

    ## Button Information
    sub_button = rospy.Subscriber('button_ret', Int32, button_callback)

    ## Talking to sensor
    #error_sub = rospy.Subscriber('error_ret', String, error_callback)
    sen_IR_command = rospy.Publisher('sensor_call/IR', Empty, queue_size=10)
    sen_TOF_command = rospy.Publisher('sensor_call/TOF', Empty, queue_size=10)
    sen_color_command = rospy.Publisher('sensor_call/color', Empty, queue_size=10)
    sensor_IR_sub = rospy.Subscriber('sensor_ret/IR', IR_sensor_data, sensor_IR_callback)
    sensor_TOF_sub = rospy.Subscriber('sensor_ret/TOF', TOF_sensor_data, sensor_TOF_callback)
    sensor_color_sub = rospy.Subscriber('sensor_ret/color', color_sensor_data, sensor_color_callback)

    LED_command = rospy.Publisher('toggle_LED', Bool, queue_size=10)
    pose_command = rospy.Publisher('move_pose', command, queue_size=10)

    # Check if ROS is ready for operation
    while(rospy.is_shutdown()):
        print("ROS is shutdown!")

    rospy.loginfo("Sending Goals ...")


    #move_arm(pub_command, loop_rate, home, 4.0, 4.0)

    while(1):
        print_menu()
        input_string = raw_input("Enter choice or 0 to quit.")
        print("You entered " + input_string + "\n")

        if(int(input_string) == 1):
            print("Training...")
            train(pub_command, sen_IR_command, sen_TOF_command, sen_color_command, gripper_command, loop_rate)
        elif (int(input_string) == 2):
            print("Opening gripper")
            gripper_command.publish(False)
        elif (int(input_string) == 3):
            print("Moving arm to testing home")
            theta_home = lab_invk(test_home[0], test_home[1], test_home[2], 90)
            move_arm(pub_command, loop_rate, theta_home, 4.0, 4.0)
        elif (int(input_string) == 4):
            print("Moving arm out of the way")
            theta_home_over = lab_invk(test_home_over[0], test_home_over[1], test_home_over[2], 90)
            move_arm(pub_command, loop_rate, theta_home_over, 4.0, 4.0)
            move_arm(pub_command, loop_rate, home, 4.0, 4.0)
        elif (int(input_string) == 5):
            print("Read TOF")
            print(read_TOF_sensor(sen_TOF_command))
            #gather_data_ver(pub_command, sen_command, gripper_command, loop_rate)
        elif (int(input_string) == 6):
            print("Read IR")
            print(read_IR_sensor(sen_IR_command))
        elif (int(input_string) == 7):
            leaf_test(sen_IR_command, sen_TOF_command, sen_color_command)
        elif (int(input_string) == 8):
            prediction_test(sen_IR_command)
        elif (int(input_string) == 9):
            char_test(pub_command, loop_rate, sen_IR_command)
        elif (int(input_string) == 10):
            distance_test(pub_command, loop_rate, sen_IR_command)
        elif (int(input_string) == 11):
            print(read_color_sensor(sen_color_command))
        elif (int(input_string) == 12):
            LED_command.publish(True)
        elif (int(input_string) == 13):
            LED_command.publish(False)
        elif (int(input_string) == 14):
            input_pose_str = raw_input("Enter pose 2048 2048 2048 90 90 90.")
            input_pose = input_pose_str.split()
            #input_pose = list(input_pose)
            for i in range(0, len(input_pose)):
                input_pose[i] = int(input_pose[i])
            pose_command.publish(input_pose)
        elif (int(input_string) == 15):
            input_pose_str = raw_input("Enter x, y, z, theta_yaw (radians).")
            input_pose = input_pose_str.split()
            #input_pose = list(input_pose)
            for i in range(0, len(input_pose)):
                input_pose[i] = float(input_pose[i])
            print(input_pose)
            test_input_pose = IK_fun(input_pose[0],input_pose[1],input_pose[2],input_pose[3])
            print(test_input_pose)
            pose_command.publish(test_input_pose)
        elif (int(input_string) == 0):
            break
        else:
            print("Please just enter the character 1, 2, 3, ... \n\n")
            print_menu()











if __name__ == '__main__':

    try:
        main()
    # When Ctrl+C is executed, it catches the exception
    except rospy.ROSInterruptException:
        pass
