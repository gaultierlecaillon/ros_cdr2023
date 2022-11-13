#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node('n_chronos')

    pub = rospy.Publisher("/t_robot", String, queue_size=10)

    rate = rospy.Rate(2)  # 2Hz (2/s)

    while not rospy.is_shutdown():
        msg = String()
        msg.data = "Hi, this is chrono"
        pub.publish(msg)
        rate.sleep()

    rospy.loginfo("Node n_chrono has been stopped")
