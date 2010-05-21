#! /usr/bin/python
import roslib
roslib.load_manifest('pr2_mechanism_controllers')
roslib.load_manifest('actionlib')

import rospy
import actionlib
from actionlib_msgs.msg import *
from pr2_controllers_msgs.msg import *

rospy.init_node('single_joint_position', anonymous=True)

client = actionlib.SimpleActionClient('torso_controller/position_joint_action',    
                                      SingleJointPositionAction)
client.wait_for_server()

client.send_goal(SingleJointPositionGoal(position = 0.0))
client.wait_for_result()
if client.get_state() == GoalStatus.SUCCEEDED:
    print "Success"
