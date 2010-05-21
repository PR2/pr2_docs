#! /usr/bin/env python

import roslib
roslib.load_manifest('pr2_controllers_msgs')
roslib.load_manifest('actionlib')
from pr2_controllers_msgs.msg import *
import rospy
import actionlib.action_client
import termios, tty, sys, select

# My tricks for making Ctrl-C work seamlessly
import atexit
atexit.register(rospy.signal_shutdown, 'exit')


def getKey():
    settings = termios.tcgetattr(sys.stdin)
    try:
        #tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        return key
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)


def print_usage():
    print """Usage:

q - quit
h - print usage

                Base
     Translate          Rotate
         i               u  o
       j k l

 Head                        Laser
   e                      a - Scan quickly
 s d f                    z - Scan slowly

               Grippers
     Left                  Right
   p - open             [ - open
   ; - close            ' - close
   P - float            { - float
   : - close lightly    " - close lightly

Arms: Run trajectory 1, 2, 3, ...

"""



def main():
    print_usage()
    rospy.init_node('teleop_the_robot', disable_signals=True, anonymous=True)
    while True:
        key = getKey()
        #print "key:", key, ord(key)
        if key == 'q' or key == chr(3):
            return
        if key == 'h':
            print_usage()
        
        if key == 'i': # Base forward
            pass
        if key == 'k': # Base backwards
            pass
        if key == 'j': # Base left
            pass
        if key == 'l': # Base right
            pass
        if key == 'u': # Base yaw left
            pass
        if key == 'o': # Base yaw right
            pass

        if key == 'e': # Head up
            pass
        if key == 'd': # Head down
            pass
        if key == 's': # Head left
            pass
        if key == 'f': # Head right
            pass
        
        if key == 'a': # Laser quickly
            pass
        if key == 'z': # Laser slowly
            pass
        
        if key == 'p': # L gripper open
            pass
        if key == ';': # L gripper close
            pass
        if key == 'P': # L gripper float
            pass
        if key == ':': # L gripper close lightly
            pass
        if key == '[': # R gripper open
            pass
        if key == "'": # R gripper close
            pass
        if key == '{': # R gripper float
            pass
        if key == '"': # R gripper close lightly
            pass

        if key >= '1' and key <= '9':
            trajectory_number = int(key)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

