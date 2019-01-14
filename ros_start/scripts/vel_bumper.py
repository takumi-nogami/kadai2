#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent

rospy.init_node('vel_bumper')
pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

def callback(bumper):
    print bumper
    vel = Twist()
    vel.linear.x = -1.0
    pub.publish(vel)

sub = rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, callback)

while not rospy.is_shutdown():
    vel = Twist()
    direction = raw_imput('f: forward, b: backward, l:left, r')
