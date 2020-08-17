#!/usr/bin/env python
# license removed for brevity

import rospy
from sensor_msgs.msg import Image 

from picamera import PiCamera
from time import sleep


def capture():
    camera = PiCamera()
    # camera.start_preview()
    # it’s important to sleep for at least two seconds before capturing 
    # an image, because this gives the camera’s sensor time to sense the light levels.
    # sleep(5)
    camera.capture()


if __name__ == '__main__':
    try:
        capture()
    except rospy.ROSInterruptException:
        pass
