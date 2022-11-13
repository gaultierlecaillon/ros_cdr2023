#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback_receive_robot_data(msg):
    rospy.loginfo("Message Received:")
    rospy.loginfo(msg)


if __name__ == "__main__":
    rospy.init_node('n_strategy')

    sub = rospy.Subscriber("/t_robot", String, callback_receive_robot_data)

    rospy.spin()