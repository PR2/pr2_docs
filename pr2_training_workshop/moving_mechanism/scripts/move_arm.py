#! /usr/bin/python
import roslib
roslib.load_manifest('pr2_mechanism_controllers')
roslib.load_manifest('actionlib')

import rospy
import actionlib
from actionlib_msgs.msg import *
from pr2_controllers_msgs.msg import *
from trajectory_msgs.msg import *
from math import pi

rospy.init_node('move_the_arm', anonymous=True)

client = actionlib.SimpleActionClient('r_arm_controller/joint_trajectory_action', JointTrajectoryAction)
client.wait_for_server()


g = JointTrajectoryGoal()
g.trajectory.header.stamp = rospy.Time.now() + rospy.Duration(0.2)  # Start in 200 ms
g.trajectory.joint_names = ['r_shoulder_pan_joint', 'r_shoulder_lift_joint',
                            'r_upper_arm_roll_joint',
                            'r_elbow_flex_joint', 'r_forearm_roll_joint',
                            'r_wrist_flex_joint', 'r_wrist_roll_joint']
g.trajectory.points.append(
    JointTrajectoryPoint(positions = [0, 0, 0, -0.15, 0, -0.1, 0],
                         velocities = [0, 0, 0, 0, 0, 0, 0],
                         time_from_start = rospy.Duration(3.0)))
g.trajectory.points.append(
    JointTrajectoryPoint(positions = [0, 1.0, 0, -2.0, pi, -1.0, 0],
                         velocities = [0, 0, 0, 0, 0, 0, 0],
                         time_from_start = rospy.Duration(4.5)))

client.send_goal(g)
client.wait_for_result()

if client.get_state() == GoalStatus.SUCCEEDED:
    print "Succeeded"
else:
    print "Failed"
