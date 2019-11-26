#!/usr/bin/env python

from get_parameters.srv import *
import rospy

def handle_example_service(req):
    print "A client said: " + req.messageToPrint
    print "A client sent me this float32 value: " + str(req.someFloatValue) 
    return ExampleServiceDefinitionResponse("I am the server and this is my response.")

if __name__ == "__main__":
    rospy.init_node('example_service_node')
    s = rospy.Service('example_service', ExampleServiceDefinition, handle_example_service)
    print "Ready to serve..."
    rospy.spin()
