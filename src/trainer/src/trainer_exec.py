#!/usr/bin/env python

import copy
# import time
import rospy
import numpy as np

from std_msgs.msg import Empty # Used to call for sensor readings
from std_msgs.msg import Bool # Used for gripper
from std_msgs.msg import Int32 # Used to return button value

from trainer.msg import IR_sensor_data
from trainer.msg import TOF_sensor_data
from trainer.msg import color_sensor_data
from arm_control.msg import position


import json #Used for point data
import random
import os

import pickle

# 20Hz
SPIN_RATE = 20

# arm home location
home = [0.051+0.040+0.113,-0.0657,0.093+0.038+0.144-0.0491 ,0]#[0.048+0.040+0.115,-0.066,0.093+0.038+0.143-0.048 ,0]
away = [0.10, -0.2, 0.20, 0]
# Set for red ovoid target
test_home = [0.25, -0.066, 0.15] #Set the home position for testing - all movement is relative to this
test_home_over = [0.3, 0.25, 0.17]


# Other Global Variables
test_pt_list = [] # A list of x,y,z points that will be tested for the current configuration

test_pt_list_ver = []

button_data = -1 # Buttons used to log gripper status and control program

sensor_TOF_reading = [-1, -1, -1, -1.0, -1.0, -1.0] # Sensor TOF reading from arduino
sensor_IR_reading = [-1, -1, -1] # Sensor IR reading from arduino
sensor_color_reading = [-1, -1, -1, -1, -1, -1.0] # Sensor color reading from arduino


IR_sensor = False
TOF_sensor = False
color_sensor = False

move_complete = False

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

def move_complete_callback(msg):
    global move_complete
    move_complete = msg.data


def move_arm(pos_cmd, pos):
    global move_complete
    move_complete = False
    pos_cmd.publish(pos)
    while(move_complete==False):
        pass
"""
Main Menu
"""
def print_menu():

    print("Menu: ")
    print("0: Exit Program")
    print("1: Train")
    print("2: Find z-height")
    print("3: Open Gripper")
    print("4: Close Gripper")
    print("5: Read TOF sensor")
    print("6: Read IR Sensor")
    print("7: Read color sensor")
    print("8: Training - Leafs")
    print("9: Characterize Sensor")
    print("10: Distance test - Dead")
    print("11: Home the arm")
    print("12: Move arm out of the way")
    # print("13: Servo test")
    # print("14: Move to point")





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

"""
This is the main function for training.
"""
def train(pos_cmd, sen_IR_cmd, sen_TOF_cmd, sen_color_cmd, grp_cmd):

    """
    find out what test we are conducting
    load up the correct test cycle_testpoints
    call the correct test function???
    """
    # global test_pt_list
    global button_data
    global sensor_TOF_reading
    global sensor_IR_reading
    global sensor_color_reading
    global TOF_sensor
    global IR_sensor
    global color_sensor
    global home

    number_of_points = raw_input("How many training points? ")
    start_z = raw_input("Starting z? ")
    filename = file_menu()
    # open output file and read in test points
    with open('data/test_points/' + 'Basic_Ovoid_Medium_training.txt', 'r') as filehandle:
        test_pt_list_temp = json.load(filehandle)

    test_pt_list = random.sample(test_pt_list_temp, int(number_of_points))


    data_collected = []
    tracker = 1
    for pt in test_pt_list:
        print("Moving to ", pt)
        x_d = pt[0] + home[0]
        y_d = pt[1] + home[1]
        z_d = pt[2] + float(start_z)
        z_over = float(start_z) + 0.03

        # Move above position
        move_arm(pos_cmd,[x_d, y_d, z_over, 0])
        # Move to position
        move_arm(pos_cmd,[x_d, y_d, z_d, 0])
        # Initialize the sensor values
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

        # Move back above position
        move_arm(pos_cmd,[x_d, y_d, z_over, 0])

    with open('data/' + filename + '_data.txt', 'w') as filehandle:
        #json.dump(data_collected, filehandle)
        pickle.dump(data_collected, filehandle)



    print("Moving arm out of the way")
    move_arm(pos_cmd, home)


"""
Make one rading of the TOF sensor
"""
def read_TOF_sensor(sen_cmd):
    global sensor_TOF_reading
    # Gather sensor data
    sen_cmd.publish()
    while sensor_TOF_reading[0] == -1:
        pass
    data = copy.copy(sensor_TOF_reading)
    sensor_TOF_reading = [-1, -1, -1, -1.0, -1.0, -1.0]
    print(data)
    return data

"""
Make one rading of the IR sensor
"""
def read_IR_sensor(sen_cmd):
    global button_data
    global sensor_IR_reading

    # Gather sensor data
    sen_cmd.publish()
    while sensor_IR_reading[0] == -1:
        pass
    data = copy.copy(sensor_IR_reading)
    sensor_IR_reading = [-1, -1, -1]
    # print("IR Read")
    return data

"""
Make one rading of the color sensor
"""
def read_color_sensor(sen_cmd):
    global sensor_color_reading
    # Gather sensor data
    sen_cmd.publish()
    while sensor_color_reading[0] == -1:
        pass
    data = copy.copy(sensor_color_reading)
    sensor_color_reading = [-1, -1, -1, -1, -1, -1.0]
    # print("Color Read")
    return data

"""
Collect data for leaves and branches
"""
def leaf_test(pos_cmd, sen_IR_cmd, sen_TOF_cmd, sen_color_cmd):
    global button_data
    global sensor_TOF_reading
    global sensor_IR_reading
    global sensor_color_reading
    global TOF_sensor
    global IR_sensor
    global color_sensor
    global home

    close_sensor_TOF = [-1, -1, -1, -1.0, -1.0, -1.0]
    close_sensor_IR = [-1,-1,-1]
    close_sensor_color = [-1, -1, -1, -1, -1, -1.0]
    pt = [-1,-1,-1]
    tracker = 0
    data_collected = []
    print("Moving to home")

    # Move above position
    move_arm(pos_cmd, home)
    # Create a file name
    filename = file_menu()
    # Read number of cycles
    num_cycles = 20
    for a in range(num_cycles):
        # Press button to advance
        print("Press button to take reading.")
        while button_data == -1:
            pass
        # Read the sensors
        presensor_TOF = [-1, -1, -1, -1.0, -1.0, -1.0]
        presensor_IR = [-1,-1,-1]
        presensor_color = [-1, -1, -1, -1, -1, -1.0]

        if(TOF_sensor == True):
            presensor_TOF = read_TOF_sensor(sen_TOF_cmd)
        if(IR_sensor == True):
            presensor_IR = read_IR_sensor(sen_IR_cmd)
        if(color_sensor == True):
            presensor_color = read_color_sensor(sen_color_cmd)

        rospy.sleep(0.2)

        print(tracker)
        tracker += 1
        # data_collected.append(sensor)
        #data_collected.append(sensor_data_struct(pt, sensor_IR, sensor_TOF, sensor_color, "leaf"))
        # data_collected.append(sensor_data_struct(pt, sensor_IR, sensor_TOF, sensor_color, "leaf"))
        data_collected.append(sensor_data_struct(pt, presensor_IR + close_sensor_IR, presensor_TOF + close_sensor_TOF, presensor_color + close_sensor_color, "plant"))
        button_data = -1

    # with open('data/' + filename + '_leaf.txt', 'w') as filehandle:
    # with open('data/' + filename + '_leaf_test.txt', 'w') as filehandle:
    with open('data/' + filename + '_leaf_final_test.txt', 'w') as filehandle:
        #json.dump(data_collected, filehandle)
        pickle.dump(data_collected, filehandle)


"""
This is used to collect data of how a single sensor behaves.
"""
def char_test(pos_cmd, sen_IR_cmd, sen_TOF_cmd):
    global home
    start_z = raw_input("Starting z? ")
    data_collected = []
    #local_home = [home[0], home[1], 0.15]#[0.3, 0.25, 0.12-.028]#Offset to reach top of target
    #Bring in a bunch of test points
    os.chdir('/home/ben/gripper_proj_2/data/')

    #Move to each point and take a Reading

    # x_list = np.linspace(-3,3,31)/100.0
    # y_list = np.linspace(-3,3,31)/100.0
    # z_list = np.linspace(0,6,13)/100.0
    move_arm(pos_cmd,home)

    x_list = np.linspace(-1,1,21)/100.0
    y_list = np.linspace(-1,1,21)/100.0
    z_list = np.linspace(0,2,21)/100.0

    for z in z_list:
        print(z)
        for y in y_list:
            for x in x_list:
                x_d = home[0] + x
                y_d = home[1] + y
                z_d = float(start_z) + z +0.01
                move_arm(pos_cmd,[x_d, y_d, z_d, 0])
                rospy.sleep(0.1)
                # IR_data = read_IR_sensor(sen_IR_cmd)
                # data_collected.append([x,y,z]+[IR_data[0]])
                TOF_data = read_TOF_sensor(sen_TOF_cmd)
                data_collected.append([x,y,z]+[TOF_data[0],TOF_data[3]])
    #Save the data in a file
    # with open('IR_char_data.txt', 'w') as filehandle:
    #     json.dump(data_collected, filehandle)
    with open('TOF_char_data.txt', 'w') as filehandle:
        json.dump(data_collected, filehandle)


def distance_test(pos_cmd, sen_IR_cmd, sen_TOF_cmd):
    global home
    start_z = raw_input("Starting z? ")
    data_collected = []
    # local_home = [0.048+0.040+0.115,-0.066,float(start_z) ,0]#[0.25, -0.066, 0.10]#[0.3, 0.25, 0.12-.028] #Offset to reach top of target
    #Bring in a bunch of test points
    os.chdir('/home/ben/gripper_proj_2/data/')


    data_set = np.linspace(0,6,61)/100.0
    #Move to each point and take a Reading
    for point in data_set:
        x_d = home[0]
        y_d = home[1]
        z_d = float(start_z) + point
        move_arm(pos_cmd,[x_d, y_d, z_d, 0])
        rospy.sleep(0.2)
        # IR_data = read_IR_sensor(sen_IR_cmd)
        # data_collected.append([point]+[IR_data[0]])
        TOF_data = read_TOF_sensor(sen_TOF_cmd)
        data_collected.append([point]+[TOF_data[0],TOF_data[3]])
    #Save the data in a file
    # with open('IR_distance_data.txt', 'w') as filehandle:
    #     json.dump(data_collected, filehandle)
    with open('TOF_distance_data.txt', 'w') as filehandle:
        json.dump(data_collected, filehandle)


def find_z(pos_cmd):
    global home
    move_arm(pos_cmd,home)
    print("Current z: ", home[2])
    while(1):
        new_z = raw_input("New z? (or -1 to quit)")

        if float(new_z)<0:
            break
        else:
            x_d = home[0]
            y_d = home[1]
            z_d = float(new_z)
            move_arm(pos_cmd,[x_d, y_d, z_d, 0])


"""
################################################################################
The Main function
################################################################################
"""
def main():

    global home
    global away
    global SPIN_RATE

    # Initialize ROS node
    rospy.init_node('trainer_node') #?????????????
    loop_rate = rospy.Rate(SPIN_RATE)

    # Arduino
    ## Gripper Control
    gripper_command = rospy.Publisher('toggle_gripper', Bool, queue_size=10)

    ## Button Information
    sub_button = rospy.Subscriber('button_ret', Int32, button_callback)

    ## Talking to sensor
    sen_IR_command = rospy.Publisher('sensor_call/IR', Empty, queue_size=10)
    sen_TOF_command = rospy.Publisher('sensor_call/TOF', Empty, queue_size=10)
    sen_color_command = rospy.Publisher('sensor_call/color', Empty, queue_size=10)
    sensor_IR_sub = rospy.Subscriber('sensor_ret/IR', IR_sensor_data, sensor_IR_callback)
    sensor_TOF_sub = rospy.Subscriber('sensor_ret/TOF', TOF_sensor_data, sensor_TOF_callback)
    sensor_color_sub = rospy.Subscriber('sensor_ret/color', color_sensor_data, sensor_color_callback)

    # Arbotix
    # Controlling the arm
    position_command = rospy.Publisher('arm_control/position', position, queue_size=10)
    move_complete_sub = rospy.Subscriber('arm_control/move_complete', Bool, move_complete_callback)


    # Check if ROS is ready for operation
    while(rospy.is_shutdown()):
        print("ROS is shutdown!")

    # rospy.loginfo("Sending Goals ...")


    while(1):
        print_menu()
        input_string = raw_input("Enter choice or 0 to quit.")
        print("You entered " + input_string + "\n")

        if(int(input_string) == 1):
            print("Training...")
            train(position_command, sen_IR_command, sen_TOF_command, sen_color_command, gripper_command)
        elif (int(input_string) == 2):
            find_z(position_command)
        elif (int(input_string) == 3):
            print("Opening gripper")
            gripper_command.publish(False)
        elif (int(input_string) == 4):
            print("Closing gripper")
            gripper_command.publish(True)
        elif (int(input_string) == 5):
            print("Read TOF")
            print(read_TOF_sensor(sen_TOF_command))
        elif (int(input_string) == 6):
            print("Read IR")
            print(read_IR_sensor(sen_IR_command))
        elif (int(input_string) == 7):
            print("Read Color Sensor")
            print(read_color_sensor(sen_color_command))
        elif (int(input_string) == 8):
            leaf_test(position_command, sen_IR_command, sen_TOF_command, sen_color_command)
        elif (int(input_string) == 9):
            char_test(position_command, sen_IR_command,sen_TOF_command)
        elif (int(input_string) == 10):
            distance_test(position_command, sen_IR_command,sen_TOF_command)
        elif (int(input_string) == 11):
            print("Moving arm to home")
            move_arm(position_command,home)
        elif (int(input_string) == 12):
            print("Moving arm out of the way")
            move_arm(position_command,away)
        elif (int(input_string) == 13):
            pass
        elif (int(input_string) == 14):
            # input_pose_str = raw_input("Enter pose 2048 2048 2048 90 90 90.")
            # input_pose = input_pose_str.split()
            # #input_pose = list(input_pose)
            # for i in range(0, len(input_pose)):
            #     input_pose[i] = int(input_pose[i])
            # pose_command.publish(input_pose)
            pass
        elif (int(input_string) == 15):
            # input_pose_str = raw_input("Enter x, y, z, theta_yaw (radians).")
            # input_pose = input_pose_str.split()
            # #input_pose = list(input_pose)
            # for i in range(0, len(input_pose)):
            #     input_pose[i] = float(input_pose[i])
            # print(input_pose)
            # test_input_pose = IK_fun(input_pose[0],input_pose[1],input_pose[2],input_pose[3])
            # print(test_input_pose)
            # pose_command.publish(test_input_pose)
            pass

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
