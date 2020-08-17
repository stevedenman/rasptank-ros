#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

import RPi.GPIO as GPIO
import time

Tr = 11
Ec = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Ec, GPIO.IN)

def checkdist():       #Reading distance
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(Ec, GPIO.IN)
    GPIO.output(Tr, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Tr, GPIO.LOW)
    while not GPIO.input(Ec):
        pass
    t1 = time.time()
    while GPIO.input(Ec):
        pass
    t2 = time.time()
    return round((t2-t1)*340/2,2)

def ultrasonic():
    pub = rospy.Publisher('ultrasonic', Float64, queue_size=10)
    rospy.init_node('ultrasonic', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        distance = checkdist()
        distance_str = "ultrasonic: %s" % distance
        rospy.loginfo(distance_str)
        pub.publish(distance)
        rate.sleep()

if __name__ == '__main__':
    try:
        ultrasonic()
    except rospy.ROSInterruptException:
        pass
