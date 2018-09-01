#!/bin/bash
status=1
while true
do
  temp=`cat /sys/kernel/yawn/spare_status`
#  echo $temp
  if [[ $temp -ne $status ]];
  then
    if [[ $temp -eq 1 ]];
    then
        echo 1 > /sys/devices/system/cpu/cpu6/online
	echo 1 > /sys/devices/system/cpu/cpu7/online
    else
        echo 0 > /sys/devices/system/cpu/cpu6/online
	echo 0 > /sys/devices/system/cpu/cpu7/online

    fi
    status=$temp
  fi
 sleep 2
done
