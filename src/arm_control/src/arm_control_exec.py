#!/usr/bin/env python

import copy
#import time
import rospy
import numpy as np
import numpy.linalg as LA

from std_msgs.msg import Bool # Used for gripper


from arm_control.msg import command
from arm_control.msg import position


# 20Hz
SPIN_RATE = 20

# UR3 home location
home = [0.048+0.040+0.115,-0.066,0.093+0.038+0.143-0.048 ,0]

# UR3 current position, using home position for initialization
current_position = np.array([home[0],home[1], home[2]])
desired_position = np.array([home[0],home[1], home[2]])

move_flag = False
step_complete_flag = False
#thetas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


"""
################################################################################
The Start of code
################################################################################
"""


"""
################################################################################
Callback Functions
"""

def step_complete_callback(msg):
    global step_complete_flag
    step_complete_flag = msg.data

def move_arm_callback(msg):
    global desired_position
    global move_flag
    # print("Move arm callback")
    desired_position[0] = msg.point[0]
    desired_position[1] = msg.point[1]
    desired_position[2] = msg.point[2]
    move_flag = True




def IK_fun(pose_request):

    x = pose_request[0]
    y = pose_request[1]
    z = pose_request[2]
    theta_yaw_rad = pose_request[3]
    # print("Pose Req")
    # print(pose_request)

    theta = [None, None, None, None, None, None]

    l1 = 0.093+0.038
    l2 = 0.143
    l3 = 0.048
    l4 = 0.115
    l5 = 0.066
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
    global move_flag
    global current_position
    global desired_position
    global step_complete_flag

    # Initialize ROS node
    rospy.init_node('arm_control_node') #?????????????
    loop_rate = rospy.Rate(SPIN_RATE)

    # Arduino
    ## Gripper Control
    # gripper_command = rospy.Publisher('toggle_gripper', Bool, queue_size=10)

    position_sub = rospy.Subscriber('arm_control/position', position, move_arm_callback)
    move_command = rospy.Publisher('move_command', command, queue_size=20)
    step_complete_sub = rospy.Subscriber('arm_control/step_complete', Bool, step_complete_callback)
    move_complete_pub = rospy.Publisher('arm_control/move_complete', Bool, queue_size=10)
    # LED_command = rospy.Publisher('toggle_LED', Bool, queue_size=10)
    # move_command = rospy.Publisher('move_command', command, queue_size=10)

    # Check if ROS is ready for operation
    while(rospy.is_shutdown()):
        print("ROS is shutdown!")

    rospy.loginfo("Waiting in arm_control...")

    while(1):
        if move_flag == True:
            # current_position = np.array()
            # desired_position = np.array()
            # print("Step")
            slope_vec = desired_position - current_position

            desired_position_t = current_position

            complete_flag = False
            step = 0.005*slope_vec/LA.norm(slope_vec)

            while(complete_flag == False):
                step_complete_flag==False
                if LA.norm(desired_position_t - desired_position)< 0.005:
                    desired_position_t = desired_position
                    current_position = copy.copy(desired_position)
                    complete_flag = True
                    move_flag = False
                    move_complete_pub.publish(True)
                else:
                    desired_position_t = desired_position_t + step

                joint_angles = IK_fun(desired_position_t.tolist() + [0])
                move_command.publish(joint_angles)
                while(step_complete_flag==False):
                    #rospy.sleep(0.5)
                    pass
        else:
            # print(move_flag)
            rospy.sleep(0.1) #Without this it just sticks
            pass















if __name__ == '__main__':

    try:
        main()

    # When Ctrl+C is executed, it catches the exception
    except rospy.ROSInterruptException:
        pass
