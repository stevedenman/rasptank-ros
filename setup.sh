#!/bin/bash

# need to get groups from ls /dev/mem, /dev/gpio* and  -ls
# from https://github.com/flyte/pi-mqtt-gpio/issues/55

# add the groups if necessary
sudo groupadd -g 997 997
sudo usermod -aG 997,kmem pi

# log out and back in

sudo apt-get update
sudo apt-get install python-rpi.gpio
