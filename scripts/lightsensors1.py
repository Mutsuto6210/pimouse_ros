#!/usr/bin/env python
import sys,rospy
from pimouse_ros.msg import LightSensorValues

print(LightSensorValues)
rospy.init_node('lightsensors')
