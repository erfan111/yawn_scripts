#!/bin/bash
status=1
while true
do
  temp=`cat /sys/kernel/yawn/cpu7_status`
  if [$temp -ne $status ]
    if [$temp -eq 1 ]
        echo 1 > /sys/devices/system/cpu/cpu7/online
    else
        echo 0 > /sys/devices/system/cpu/cpu7/online
    fi
    $state=$temp
  fi
 sleep 2
done
