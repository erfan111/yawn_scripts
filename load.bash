#!/usr/bin/env bash

## usage ./load.bash output.csv
echo "" > $1
for i in `seq $2 $3 $4`
do
    echo "experiment started with rate=$i"

    temp=$(/home/erfan/mutilate/mutilate -t 60 -T 8 -Q 1000 -D 4 -C 4 -c 4 -q $i -s 10.254.254.121 -w 10 -i fb_ia -a 10.254.254.10 -a 10.254.254.9 --save=test.csv --noload)
    echo -n "$i," >> $1
    echo $temp | awk '{ printf "%s,%s,%s,%s\n", $13,$19,$20,$21}' >> $1
    echo $temp | awk '{ printf "avg=%s 95th=%s 99th=%s 99.9=%s\n", $13,$19,$20,$21 }'
    sleep 15
done
echo "experiment finished"
