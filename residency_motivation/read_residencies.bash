#!/bin/bash
sleep 45
cpupower monitor | tail -n8 | awk '{ printf "%s,%s,%s,%s,%s\n", substr($9,0,4),substr($10,0,4),substr($11,0,4),substr($12,0,4),$13 }'
