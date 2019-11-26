#!/usr/bin/env python

import rospy
from get_parameters.srv import *

def example_client(msg_to_print, some_float_value):
    rospy.wait_for_service('example_service')
    try:
        example_service = rospy.ServiceProxy('example_service', ExampleServiceDefinition)
        service_response = example_service(msg_to_print, some_float_value)
        return "the server said: " + service_response.messageBackToClient
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    print "Requesting the service to take its time..."
    print example_client("I am your client. Sending you 0.5.", 0.5)
    rospy.sleep(3.0)
    print example_client("It's me again... Your client. This time sending you 3.0.", 3.0)
