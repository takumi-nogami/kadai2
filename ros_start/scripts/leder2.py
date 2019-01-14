#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('leder')

pub = rospy.Publisher('cmd_led', Int32, queue_size=10)
rate = rospy.Rate(1)
led = Int32()
led.data = 0

while not rospy.is_shutdown():
    if led.data == 0:
       pub.publish(led)
       led.data = 1
    elif led.data == 1:
       pub.publish(led)
       led.data = 0
    rate.sleep()
