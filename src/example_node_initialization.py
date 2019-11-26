#!/usr/bin/env python

# this is the main ROS Python client module (aka library)
import rospy

# let's define a function we will use later
def shutdownFunction():
    print "we are done here."

# when the python interpreter runs this script
# this is the section that gets run as main
if __name__ == '__main__':
    # let the master know about our name
    rospy.init_node("riss")

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

