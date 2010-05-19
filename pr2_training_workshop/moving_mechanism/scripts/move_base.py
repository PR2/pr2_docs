#! /usr/bin/python
import time
import roslib
roslib.load_manifest('rospy')
roslib.load_manifest('geometry_msgs')
import rospy
from geometry_msgs.msg import *

rospy.init_node('move_the_base', anonymous=True)

pub = rospy.Publisher('base_controller/command', Twist)
time.sleep(1)

movement = Twist()
movement.linear.x = 0.1
start_time = rospy.get_rostime()
while rospy.get_rostime() < start_time + rospy.Duration(3.0):
    pub.publish(movement)
    time.sleep(0.01)
pub.publish(Twist())  # Stop
