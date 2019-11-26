#!/usr/bin/env python

# this is the main ROS Python client module (aka library)
import rospy
from std_msgs.msg import Bool
from std_msgs.msg import UInt16
from std_msgs.msg import String

# let's define a function we will use later
def shutdownFunction():
    print "we are done here."
    rospy.loginfo("shutdown...")

# when the python interpreter runs this script
# this is the section that gets run as main
if __name__ == '__main__':

    print("beging getting parameters")

    # let the master know about our name
    rospy.init_node("riss")
    rospy.loginfo("beging getting parameters")

    # define and fill out some messages
    publisherDataType = rospy.get_param("/node_1_pub_uint16/publisher_data_type")
    waitDuration = rospy.get_param("/node_1_pub_uint16/wait_duration")
    publisherDataInt = rospy.get_param("/node_1_pub_uint16/publisher_data_int")

    rospy.loginfo("publisherInt is %s", publisherDataInt)
    rospy.loginfo(isinstance(publisherDataInt, float))
    rospy.loginfo(isinstance(publisherDataType, str))
	
    # define a duration of 1 second
    myDuration = rospy.Duration(waitDuration,0)

    if( publisherDataType == "bool" ):
        msg = Bool()
        msg.data = 0
        myPublisher = rospy.Publisher('~my_ros_topic', Bool, queue_size=5)
        rospy.loginfo("msg is %d", msg.data)
        rospy.loginfo("publisherDataType is %d", publisherDataType)
    elif( publisherDataType == "uint16" ):
        msg = UInt16()
        msg.data = 10
        myPublisher = rospy.Publisher('~my_ros_topic', UInt16, queue_size=5)
        rospy.loginfo("msg is %d", msg.data)
        rospy.loginfo("publisherDataType == uint16 is: %s", publisherDataType)
    else:
        msg = String()
        msg.data = "publisher data type was not bool or uint16."
        myPublisher = rospy.Publisher('~my_ros_topic', String, queue_size=5)
        rospy.loginfo("msg is %s", msg.data)
        rospy.loginfo("publisherDataType is %s", publisherDataType)

    # wait for Ctrl-C and loop until then
    while not rospy.is_shutdown():
        # print a message for feedback
        rospy.loginfo("looping...")
        rospy.loginfo(waitDuration)
        
        # publish messages
        myPublisher.publish(msg)
        
        # wait for 1 second in between loops
        rospy.sleep(myDuration)

    # if we are here, it means you hit Ctrl-C
    # let's call a function before we shutdown this node
    rospy.on_shutdown(shutdownFunction)

