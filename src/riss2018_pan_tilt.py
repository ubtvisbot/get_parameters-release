#!/usr/bin/env 

import rospy
from std_msgs.msg import Bool 
from std_msgs.msg import UInt16

# ros publishers
pub_servo_pan = rospy.Publisher('/servo_pan', UInt16, queue_size=1)
pub_servo_tilt = rospy.Publisher('/servo_tilt', UInt16, queue_size=1)
pub_laser_on_off = rospy.Publisher('/laser_on_off', Bool, queue_size=1)

def stop():
  global pub
  print "Stopping the motor."
  pub_servo_pan.publish(UInt16(90))
  pub_servo_tilt.publish(UInt16(90))
  pub_laser_on_off.publish(Bool(0))

def init():
  global pub, filtered_range_value, latest_range_value
  rospy.init_node('servo_control', anonymous=False)
  rospy.on_shutdown(stop)
  rate = rospy.Rate(10)
  # in python, spin() only polls for shutdown, hence is_shutdown() 
  # instead of spin().
  init_tilt_value = 110
  end_tilt_value = 125
  init_pan_value = 80
  end_pan_value = 100
  pub_laser_on_off.publish(Bool(1))
  current_tilt_value = init_tilt_value
  current_pan_value = init_pan_value
  tilt_direction = 1
  pan_direction = 1
  while not rospy.is_shutdown():
    
    pub_servo_pan.publish(UInt16(current_pan_value))
    pub_servo_tilt.publish(UInt16(current_tilt_value))

    if( tilt_direction == 1 ):
      current_tilt_value = current_tilt_value + 1
    else:
      current_tilt_value = current_tilt_value - 1

    if( pan_direction == 1 ):
      current_pan_value = current_pan_value + 1
    else:
      current_pan_value = current_pan_value - 1

    if(current_pan_value == end_pan_value ):
      pan_direction = 0
    elif(current_pan_value == init_pan_value ):
      pan_direction = 1

    if(current_tilt_value == end_tilt_value ):
      tilt_direction = 0
    elif(current_tilt_value == init_tilt_value):
      tilt_direction = 1

    rate.sleep()

if __name__ == '__main__':
    try:
        init()
    except rospy.ROSInterruptException:
        pass
    
