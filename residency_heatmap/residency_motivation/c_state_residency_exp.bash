#!/usr/bin/env bash

## usage ./x.bash start step end
for i in `seq $1 $2 $3`
do
    echo "experiment started with rate=$i"
    ssh root@10.254.254.100 '/home/erfan/rapl_read/read_residencies.bash > test.log &'
    temp=$(/home/erfan/mutilate/mutilate -t 60 -c 25 -T 25 -q $i -w 20 -s 10.254.254.100 -i fb_ia)
    scp root@10.254.254.100:/root/test.log "rate$i.log"
    ssh root@10.254.254.100 'rm test.log'
    sleep 15
done
python3 aggregate_residencies.py $1 $3 $2
echo "experiment finished"
