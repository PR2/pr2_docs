#! /bin/bash
set -x

#rxplot /joint_states/position[23] /joint_states/effort[23]
rxplot -b 120 /r_gripper_controller/state/process_value /r_gripper_controller/state/command