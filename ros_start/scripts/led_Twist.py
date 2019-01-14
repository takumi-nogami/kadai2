#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('led_Twist')
pub = rospy.Publisher('led', Twist, queue_size=10)
rate = rospy.Rate(0.1)
while not rospy.is_shutdown():
    led = Twist()
    led.linear.x = 500.0
    led.angular.z = 0.0
    print led
    pub.publish(led)
    rate.sleep()
