#!/usr/bin/env python  

import rospy
import tf

if __name__ == '__main__':

    rospy.init_node('example_tf_listener')

    listener = tf.TransformListener()

    rate = rospy.Rate(1.0)

    while not rospy.is_shutdown():
        try:
            # link2 with reference to link1
            reference_frame = '/link1'
            query_frame = '/link2'
            # rospy.Time(0) will look-up latest available transform
            (translation,rotation) = listener.lookupTransform(reference_frame, query_frame, rospy.Time(0))
	    print "translation: "+str(translation)
            print "rotation: "+str(rotation)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        rate.sleep()
