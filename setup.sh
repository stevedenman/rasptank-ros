#!/bin/bash

# need to get groups from ls /dev/mem, /dev/gpio* and  -ls
# from https://github.com/flyte/pi-mqtt-gpio/issues/55

# TODO: MOVE THIS TO DOCKERFILE

# add the groups if necessary
sudo groupadd -g 997 997
sudo usermod -aG 997,kmem pi

# for pi cam
sudo usermod -aG video pi

# log out and back in

