#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point

def callback(vel):
    v = vel.x
    print v

rospy.init_node('vel_subscriber')
sub = rospy.Subscriber('velocity', Point, callback)
rospy.spin()
