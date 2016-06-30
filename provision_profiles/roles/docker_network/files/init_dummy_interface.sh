#!/bin/bash

/sbin/modprobe dummy
/sbin/ip link set name eth10 dev dummy0
/sbin/ifconfig eth10 hw ether 00:22:22:ff:ff:ff
/sbin/ifconfig eth10 192.168.10.1 netmask 255.255.255.0 up
