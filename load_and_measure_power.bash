#!/usr/bin/env bash

## usage ./load.bash tail.csv power.csv start step end
echo "" > $1
var=0
for i in `seq $2 $3 $4`
do
    echo "experiment started with rate=$i"
    ssh root@10.254.254.100 '/home/erfan/rapl_read/reader.bash > test.log &'
    temp=$(/home/erfan/Documents/programming/mutilate/mutilate -t 5 -q $i -s 110.254.254.100)
    ssh root@10.254.254.100 '/home/erfan/rapl_read/reader.bash > test.log &'
    scp root@10.254.254.100:/root/test.log "rate$i.log"
    ssh root@10.254.254.100 'rm test.log'
    echo -n "$i," >> $1
    echo $temp | awk '{ printf "%s,%s,%s\n", $13,$20,$21}' >> $1
    echo $temp | awk '{ printf "avg=%s 99th=%s 99.9=%s\n", $13,$20,$21 }'
    ((var++))
    sleep 15
done
python3 aggregate_power.py $2 $4 $3
echo "experiment finished"
