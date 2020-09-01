#!/usr/bin/env python
import numpy, logging

import rospy
from geometry_msgs.msg import Twist

import RPi.GPIO as GPIO

class Motor():
    """Represents a single motor on the robot.
    Attributes:
        pin1 (int): GPIO pin number.
        pin2 (int): GPIO pin number.
        en (int): GPIO pin number.
    """
    def __init__(self, pin1, pin2, en):
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)

        self.pin1 = pin1
        self.pin2 = pin2
        self.en = en
        self.pwm = GPIO.PWM(en, 1000)

    def move(self, speed):
        try:
            speed = numpy.clip(speed, -99, 99)
            if speed > 0:
                # forward
                GPIO.output(self.pin1, GPIO.LOW)
                GPIO.output(self.pin2, GPIO.HIGH)
                self.pwm.start(0)
                self.pwm.ChangeDutyCycle(speed)
            elif speed < 0:
                # backward
                GPIO.output(self.pin1, GPIO.HIGH)
                GPIO.output(self.pin2, GPIO.LOW)
                self.pwm.start(100)
                self.pwm.ChangeDutyCycle(speed)
            else:
                # stop
                GPIO.output(self.pin1, GPIO.LOW)
                GPIO.output(self.pin2, GPIO.LOW)
                GPIO.output(self.en, GPIO.LOW)
        except Exception:
            logging.info('Failed to set new motor speed.', exc_info=True)

class Motors():

    right = Motor
    left = Motor

    def stop():
        """
        Stop all motors
        """
        self.left_motor.move(0)
        self.right_motor.move(0)

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        Motor_Left_EN    = 4
        Motor_Right_EN    = 17

        Motor_Left_Pin1  = 18
        Motor_Left_Pin2  = 27
        Motor_Right_Pin1  = 14
        Motor_Right_Pin2  = 15

        self.left = Motor(Motor_Left_Pin1, Motor_Left_Pin2, Motor_Left_EN)
        self.right = Motor(Motor_Right_Pin1, Motor_Right_Pin2, Motor_Right_EN)

    def move(leftSpeed, rightSpeed):
        """ 
        Move the robot motors.

        Attributes:
            leftSpeed (int): range -100 to 100
            rightSpeed (int): range -100 to 100
        """
        self.left_motor.move(leftSpeed)
        self.right_motor.move(rightSpeed)

class Tracks():

    def __init__(self):

        rospy.init_node('tracks', anonymous=True)

        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)
    
        # set the width of the robot.
        # used when converting twist into motor velocity.
        self.w = rospy.get_param("~base_width", 0.2)
    
        # self.pub_lmotor = rospy.Publisher('lwheel_vtarget', Float32,queue_size=10)
        # self.pub_rmotor = rospy.Publisher('rwheel_vtarget', Float32,queue_size=10)
        rospy.Subscriber('cmd_vel', Twist, self.twistCallback)
    
        self.rate = rospy.get_param("~rate", 50)
        self.timeout_ticks = rospy.get_param("~timeout_ticks", 2)
        self.left = 0
        self.right = 0

        self.motors = Motors()

    def spin(self):
    
        r = rospy.Rate(self.rate)
        idle = rospy.Rate(10)
        then = rospy.Time.now()
        self.ticks_since_target = self.timeout_ticks
    
        while not rospy.is_shutdown():
            while not rospy.is_shutdown() and self.ticks_since_target < self.timeout_ticks:
                self.spinOnce()
                r.sleep()
            idle.sleep()
                
    def spinOnce(self):
    
        self.right = 1.0 * self.dx + self.dr * self.w / 2 
        self.left = 1.0 * self.dx - self.dr * self.w / 2
        # rospy.loginfo("publishing: (%d, %d)", left, right) 

        self.motors.right.move(self.right)
        self.motors.left.move(self.left)

        # self.pub_lmotor.publish(self.left)
        # self.pub_rmotor.publish(self.right)
            
        self.ticks_since_target += 1

    def twistCallback(self,msg):
        rospy.loginfo("-D- twistCallback: %s" % str(msg))
        self.ticks_since_target = 0
        self.dx = msg.linear.x
        self.dr = msg.angular.z
        self.dy = msg.linear.y

if __name__ == '__main__':
    """ main """
    tracks = Tracks()
    tracks.spin()
