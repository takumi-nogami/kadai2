import rospy
from geometry_msgs.msg import Point

class Stepper(object):
    def __init__(self):
           self._dis = rospy.Subscriber('cmd_dis', Point, self.dis_callback, queue_size=1)
           self._stepper = rospy.Publisher('cmd_stepper', Point, queue_size=1)

    def dis_callback(self, dis_msg):
           step = Point()
           step.x = dis_msg.x / 0.275
           step.z = 137 * dis_msg.z * 3.14 / 360 / 0.275
           self._stepper.publish(step)
	

if __name__ == '__main__':
    rospy.init_node('stepper')
    stepper = Stepper()
    rospy.spin()

