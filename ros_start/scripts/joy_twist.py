import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point

class JoyTwist(object):
    def __init__(self):
           self._joy_sub = rospy.Subscriber('joy', Joy, self.joy_callback, queue_size=1)
           self._stepper = rospy.Publisher('cmd_stepper', Point, queue_size=1)

    def joy_callback(self, joy_msg):
	if joy_msg.buttons[3] == 1:
            move = Point()
            move.x = joy_msg.axes[1]
            self._stepper.publish(move)
	if joy_msg.buttons[2] == 1:
            move = Point()
            move.z = joy_msg.axes[0]
            self._stepper.publish(move)
            move.x = joy_msg.axes[1]

if __name__ == '__main__':
    rospy.init_node('joy_twist')
    joy_twist = JoyTwist()
    rospy.spin()

