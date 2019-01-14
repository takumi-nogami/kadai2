#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from std_msgs.msg import Float32
from time import sleep

class Camera(object):
    def __init__(self):
        self._cam_end = rospy.Publisher('cmd_cam_end', Float32, queue_size=10)
        self._motor_start = rospy.Publisher('cmd_motor_start', Point, queue_size=10)
        self._hold_start = rospy.Publisher('cmd_hold_start', Float32, queue_size=10)
        self._cam_start = rospy.Subscriber('cmd_cam_start', Float32, self.cam_start_callback, queue_size=10)
        self._motor_end = rospy.Subscriber('cmd_motor_end', Float32, self.motor_end_callback, queue_size=10)
        self._hold_end = rospy.Subscriber('cmd_hold_end', Float32, self.hold_end_callback, queue_size=10)
        self._on = Float32()
        self._color = Float32()       
        self._fg = Float32()

    def cam_start_callback(self, cam_start_msg):
        self._fg = cam_start_msg.data
        point = Point()
        point.x = 460
        point.y = 700
        if self._fg == 1:
           point.z = 90
        elif self._fg == 3:
           point.z = -90 

        print "cam send to motor"

        self._motor_start.publish(point) #motorにx座標y座標を送信


    def motor_end_callback(self, motor_end_msg): #motorの動作が終了したことををこちら側でsubscribeする。
        if motor_end_msg.data == 1: #終了したという合図
           self._on.data = 1 
           print "motor end!!  hand start!!"
           self._hold_start.publish(self._on) #ハンドを取得するのを開始させる
        else:
           print "error"

    def hold_end_callback(self, hold_end_msg):
        if hold_end_msg.data == 1:
           point.x = -460
           point.y = 700
           if self._fg == 1:  
              point.z = 90
           elif self._fg == 3:
              point.z = -90
           self._motor_start.publish(point) #motorにx座標y座標を送信
           self._color.data = 1 #取得したボールの色に応じて（1(red) or 2(blue) or 3(yellow)）情報を送る
           print "hold end!!"
           self._cam_end.publish(self._color)
        else:
           print "error" 

if __name__ == '__main__':
   rospy.init_node('camera')
   camera = Camera()
   rospy.spin()
