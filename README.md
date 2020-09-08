# Adeept RaspTank ROS package

This ROS package provides support for the RaspTank robot from Adeept.

## Use

You will need to enable the Camera and I2C (for the Motor HAT) on the Raspberry PI.

Clone the repository into a catkin workspace and build.

There is also a docker image, and the latest build should be available from GitHub Packages;

```sh
docker run --rm --device=/dev/mem --device=/dev/gpiomem --device=/dev/video0 -e "ROS_MASTER_URI=http://pi3:11311" docker.pkg.github.com/stevedenman/rasptank-ros/rasptank-ros:arm32v7-melodic
```

Or if you want to look inside the container;

```sh
docker run --rm -it --device=/dev/mem --device=/dev/gpiomem --device=/dev/video0 -e "ROS_MASTER_URI=http://pi3:11311" docker.pkg.github.com/stevedenman/rasptank-ros/rasptank-ros:arm32v7-melodic /bin/bash
```

The docker image has been tested running on a host running Raspbian. There are some groups and device permissions that need setting in-order that the GPIO pins and camera can be accessed. I'm not sure if the groups will necessarily be the same on other host OS.

## To-do

- Improve motor control.
- Add OpenCV for image processing for object recognition and tracking.
- Arm motor control.
- LED's.
