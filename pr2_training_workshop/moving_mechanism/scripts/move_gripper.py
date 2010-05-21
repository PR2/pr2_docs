#! /usr/bin/python
import roslib
roslib.load_manifest('pr2_mechanism_controllers')
roslib.load_manifest('actionlib')

import rospy
import actionlib
from actionlib_msgs.msg import *
from pr2_controllers_msgs.msg import *

rospy.init_node('move_the_gripper', anonymous=True)

client = actionlib.SimpleActionClient(
    'r_gripper_controller/gripper_action', Pr2GripperCommandAction)
client.wait_for_server()

client.send_goal(Pr2GripperCommandGoal(
        Pr2GripperCommand(position = 0.0, max_effort = -1)))
client.wait_for_result()

result = client.get_result()
did = []
if client.get_state() != GoalStatus.SUCCEEDED:
    did.append("failed")
else:
    if result.stalled: did.append("stalled")
    if result.reached_goal: did.append("reached goal")
print ' and '.join(did)
