#!/usr/bin/env bash

## usage ./x.bash start step end
for i in `seq $1 $2 $3`
do
    echo "experiment started with rate=$i"
    ssh root@10.254.254.121 '/home/erfan/rapl_read/read_residencies.bash > test.log &'
    temp=$(/home/erfan/mutilate/mutilate -t 60 -T 8 -D 4 -C 4 -c 4 -q $i -s 10.254.254.121 -w 10 -i fb_ia -a 10.254.254.10 -a 10.254.254.9 --save=test.csv --noload)
    scp root@10.254.254.121:/root/test.log "rate$i.log"
    ssh root@10.254.254.121 'rm test.log'
    sleep 15
done
python3 aggregate_residencies.py $1 $3 $2
echo "experiment finished"
