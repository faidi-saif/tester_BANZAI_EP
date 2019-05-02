#!/bin/bash
CAM_IP="192.168.0.202"
TARGET_DIR=~/Desktop/test_capt

files=$(ssh root@${CAM_IP} ls /tmp/fuse_d/DCIM/100GOPRO/)
sleep 1
echo " getting files $files from camera"
for file in $files ;  do
   wget  ${CAM_IP}:8042/DCIM/100GOPRO/$file -O ${TARGET_DIR}/$file
   #scp  ${CAM_IP}:8042/DCIM/100GOPRO/$file -O ${TARGET_DIR}/$file
done