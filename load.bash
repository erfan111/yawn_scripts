#!/usr/bin/env bash

## usage ./load.bash output.csv
echo "" > $1
for i in `seq $2 $3 $4`
do
    echo "experiment started with rate=$i"

    temp=$(/home/scc/mutilate/mutilate -s 10.254.254.100 -T 4 -c 25 -t 60 -D 4 -C 4 -a 10.254.254.13 -q $i -a localhost)
    echo -n "$i," >> $1
    echo $temp | awk '{ printf "%s,%s,%s,%s\n", $13,$19,$20,$21}' >> $1
    #echo $temp | awk '{ printf "avg=%s 95th=%s 99th=%s 99.9=%s\n", $13,$19,$20,$21 }'
    sleep 15
done
echo "experiment finished"
