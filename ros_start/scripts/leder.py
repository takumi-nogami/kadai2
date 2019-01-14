#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

class Led(object):
	def __init__(self):
		self.led_pub = rospy.Publisher('cmd_led', Int32, led_callback, queue=1)
		self.led_sub = rospy.Subscriber('cmd_instruct', Int32, queue=1)

	def led_callback(msg):
		led = Int32()
		fg = 1
		if msg == 1:
			rate = rospy.Rate(1)
			for i in range(100):
				if fg == 0:
					led.data == 0
					led_pub.publish(led)
					fg = 1
					rate.sleep()
				if fg == 1:
					led.data == 1
					led_pub.publish(led)
					fg = 0
					rate.sleep()


rospy.init_node('leder')
pub0 = rospy.Publisher('led0', Int32, queue_size=1000)
pub1 = rospy.Publisher('led1', Int32, queue_size=1000)
sub = rospy.Subscriber('chatter', Int32, callback)
rospy.spin()
