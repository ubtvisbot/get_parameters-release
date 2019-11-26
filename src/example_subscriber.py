#!/usr/bin/env python

# this is the main ROS Python client module (aka library)
import rospy
from std_msgs.msg import UInt16
from std_msgs.msg import Bool

# define callback functions
def uint16Callback(msg):
    print "uint16 callback: "
    print msg.data
    print ""

def boolCallback(msg):
    print "bool callback: "
    print msg.data
    print ""

# let's define a function we will use later
def shutdownFunction():
    print "we are done here."

# when the python interpreter runs this script
# this is the section that gets run as main
if __name__ == '__main__':
    # let the master know about our name
    rospy.init_node("riss_node_2")

    # define message subscribers
    rospy.Subscriber('unsigned_integer_topic', UInt16, uint16Callback)
    rospy.Subscriber('bool_topic', Bool, boolCallback)

    # define a duration of 1 second
    oneSecond = rospy.Duration(1,0)

    # wait for Ctrl-C and loop until then
    while not rospy.is_shutdown():
        # print a message for feedback
        print "looping..."
        # wait for 1 second in between loops
        rospy.sleep(oneSecond)

    # if we are here, it means you hit Ctrl-C
    # let's call a function before we shutdown this node
    rospy.on_shutdown(shutdownFunction)


