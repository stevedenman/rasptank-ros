ARG ARCH=arm32v7
ARG ROS_DISTRO=melodic

FROM ${ARCH}ros:${ROS_DISTRO}

SHELL ["/bin/bash","-c"]

RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \
        sudo \
        nano \
        net-tools \
        # For use with rosdep
        python-pip \
        # Clear apt-cache to reduce image size
        && rm -rf /var/lib/apt/lists/*

# Create local catkin workspace
ENV CATKIN_WS=/root/catkin_ws
RUN mkdir -p $CATKIN_WS/src
WORKDIR $CATKIN_WS/src

COPY ** $CATKIN_WS/src/rasptank/

# Add robot packages to local catkin workspace
RUN source /opt/ros/${ROS_DISTRO}/setup.bash \
    # Update apt-get because its cache is always cleared after installs to keep image size down
    && apt-get update \
    # Install dependencies
    && cd $CATKIN_WS \
    && rosdep install -y --from-paths . --ignore-src --rosdistro ${ROS_DISTRO} \
    # Build catkin workspace
    && catkin_make \
    # Clear apt-cache to reduce image size
    && rm -rf /var/lib/apt/lists/*

COPY ./ros_catkin_entrypoint.sh /
ENTRYPOINT ["/ros_catkin_entrypoint.sh"]
CMD ["roslaunch rasptank rasptank"]
