#!/usr/bin/env bash
#scc@scc10:~/power_project$ ssh root@10.254.254.100 '(echo -ne '0x2710'; sleep 1000d) > /dev/network_throughput </dev/null 2>/dev/null &'
#scc@scc10:~/power_project$ ssh root@10.254.254.100 'pkill sleep'
#scc@scc10:~/power_project$ x=$( printf "%x" 10000 ) ; echo $x

## usage ./load.bash tail.csv power.csv start step end
echo "" > $1
var=0
for i in `seq $2 $3 $4`
do
    echo "experiment started with rate=$i"
    #x=$( printf "%x" $(($i/8)) )
    ssh root@10.254.254.121 '(echo -ne '0x$i'; sleep 1000d) > /dev/network_throughput </dev/null 2>/dev/null &'
    sleep 5
    ssh root@10.254.254.121 '/home/erfan/rapl_read/reader.bash > test.log &'
    temp=$(/home/erfan/mutilate/mutilate -t 60 -c 8 -T 8 -q $i -i fb_ia -w 20 -s 10.254.254.121 )
    ssh root@10.254.254.121 'pkill reader.bash'
    scp root@10.254.254.121:/root/test.log "rate$i.log"
    ssh root@10.254.254.121 'rm test.log'
    ssh root@10.254.254.121 'pkill sleep'
    echo -n "$i," >> $1
    echo $temp | awk '{ printf "%s,%s,%s,%s\n", $13,$19,$20,$21}' >> $1
    echo $temp | awk '{ printf "avg=%s 95th=%s 99=%s 99.9=%s\n", $13,$19,$20,$21 }'
    ((var++))
    sleep 15
done
python3 aggregate_power.py $2 $4 $3
echo "experiment finished"
