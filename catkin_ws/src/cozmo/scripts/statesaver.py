#!/usr/bin/env python3

import numpy as np
import rospy
from std_msgs.msg import String, Int8

message="Save"

if __name__ == '__main__':
    pub = rospy.Publisher('normalstatesaver', String, queue_size=10)
    rospy.init_node('statesaver', anonymous=True)
    rate = rospy.Rate(5) # ROS Rate at 5Hz

    while not rospy.is_shutdown():
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()
