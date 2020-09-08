#!/bin/bash

IMAGE_NAME=rasptank-ros
ARCH=arm32v7
ROS_DISTRO=melodic

docker build \
    --build-arg ARCH=$ARCH/ \
    --build-arg ROS_DISTRO=$ROS_DISTRO \
    -t docker.pkg.github.com/stevedenman/rasptank-ros/$IMAGE_NAME:$ARCH-$ROS_DISTRO \
    .

docker push docker.pkg.github.com/stevedenman/rasptank-ros/$IMAGE_NAME:$ARCH-$ROS_DISTRO
