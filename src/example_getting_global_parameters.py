#!/usr/bin/env python

# this is the main ROS Python client module (aka library)
import rospy
from std_msgs.msg import Bool
from std_msgs.msg import UInt16
from std_msgs.msg import String

# let's define a function we will use later
def shutdownFunction():
    print "we are done here."

# when the python interpreter runs this script
# this is the section that gets run as main
if __name__ == '__main__':
    # let the master know about our name
    rospy.init_node("riss")

    # define and fill out some messages
    publisherDataType = rospy.get_param("/publisher_data_type")
    waitDuration = rospy.get_param("/wait_duration")
	
    # define a duration of 1 second
    myDuration = rospy.Duration(waitDuration,0)

    if( publisherDataType == "bool" ):
        msg = Bool()
        msg.data = 0
        myPublisher = rospy.Publisher('/my_ros_topic', Bool, queue_size=5)
    elif( publisherDataType == "uint16" ):
        msg = UInt16()
        msg.data = 10
        myPublisher = rospy.Publisher('/my_ros_topic', UInt16, queue_size=5)
        print(publisherDataType)
    else:
        msg = String()
        msg.data = "publisher data type was not bool or uint16."
        myPublisher = rospy.Publisher('/my_ros_topic', String, queue_size=5)

    # wait for Ctrl-C and loop until then
    while not rospy.is_shutdown():
        # print a message for feedback
        print "looping..."
        print(waitDuration)
        
        # publish messages
        myPublisher.publish(msg)
        
        # wait for 1 second in between loops
        rospy.sleep(myDuration)

    # if we are here, it means you hit Ctrl-C
    # let's call a function before we shutdown this node
    rospy.on_shutdown(shutdownFunction)

