#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('leder')
pub_1 = rospy.Publisher('stepper', Int32, queue_size=10)
rate = rospy.Rate(5)
fg = 0
while not rospy.is_shutdown():
    led_num1 = Int32()
    led_num2 = Int32()
    if fg == 0:
        led_num1.data = 0
	led_num2.data = 0
	pub_1.publish(led_num1)
        pub_2.publish(led_num2)
        fg = 1
	rate.sleep()
    if fg == 1:
        led_num1.data = 1
	led_num2.data = 1
	pub_1.publish(led_num1)
	pub_2.publish(led_num2)
	fg = 0
	rate.sleep()
