#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Bool
from time import sleep

class Master(object):
    def __init__(self):
        self._order = rospy.Publisher('cmd_order', Float32, queue_size=10)
        self._end = rospy.Subscriber('cmd_end', Float32, self.end_callback, queue_size=10)
        self._fg = Float32()
    
    def end_callback(self, end_msg):
        if end_msg.data == 0:
            print "OK fg = 0"
            self._fg.data = 0
            self._order.publish(self._fg)
            sleep(5)
        if end_msg.data == 1:
            print "OK fg = 1"
            self._fg.data = 1
            self._order.publish(self._fg)
            sleep(5)
        if end_msg.data == 2:
  	    print "OK fg = 2"
            self._fg.data = 2
	    self._order.publish(self._fg)
            sleep(5)
   	if end_msg.data == 3:
	    print "OK fg = 3"
	    self._fg.data = 3
	    self._order.publish(self._fg)
            sleep(5)
        if end_msg.data == 4:
            print "OK fg = 4"
            self._fg.data = 4
            self._order.publish(self._fg)


if __name__ == '__main__':
   rospy.init_node('master')
   master = Master()
   rospy.spin()




