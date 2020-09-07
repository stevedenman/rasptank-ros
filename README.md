# Adeept RaspTank ROS package

This ROS package provides support for the RaspTank robot from Adeept.

## Use

You will need to enable the Camera and I2C (for the Motor HAT) on the Raspberry PI.

Clone the repository into a catkin workspace and build.

There is also a docker image, and the latest build should be available from GitHub Packages;

```sh
docker pull docker.pkg.github.com/stevedenman/rasptank-ros/rasptank:arm32v7:melodic
```

The docker image has been tested running on a host running Raspbian. There are some groups and device permissions that need setting in-order that the GPIO pins and camera can be accessed. I'm not sure if the groups will necessarily be the same on other host OS.

## To-do

- Improve motor control.
- Add OpenCV for image processing for object recognition and tracking.
- Arm motor control.
- LED's.
