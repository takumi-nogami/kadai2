#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point

rospy.init_node('vel_publisher')
pub = rospy.Publisher('velocity', Point, queue_size=10)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    vel = Point()
    vel.x = 500
    vel.y = 0
    vel.z = 0
    print vel
    pub.publish(vel)
    rate.sleep()
