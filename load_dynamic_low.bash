#!/usr/bin/env bash
#scc@scc10:~/power_project$ ssh root@10.254.254.100 '(echo -ne '0x2710'; sleep 1000d) > /dev/network_throughput </dev/null 2>/dev/null &'
#scc@scc10:~/power_project$ ssh root@10.254.254.100 'pkill sleep'
#scc@scc10:~/power_project$ x=$( printf "%x" 10000 ) ; echo $x
echo "" > $1
j=1
echo "experiment started"
ssh root@10.254.254.100 '/home/erfan/rapl_read/reader.bash > test.log &'
temp=$(/home/erfan/mutilate/mutilate -s 10.254.254.100 --loadonly)
for i in 10000 15000 20000 25000 30000 25000 30000 35000 30000 25000 30000 35000 40000 45000 40000 45000 40000 35000 30000 25000 30000 30000 25000 20000 25000 20000 20000 15000 15000 20000 15000 10000 15000 5000 10000 15000 15000 20000 15000 20000 25000 30000 35000 30000 30000 35000 40000 50000 55000 65000 70000 60000 55000 60000 55000 50000 40000 35000 40000 30000 10000 5000 10000 20000 25000 30000 40000 50000 60000 50000 45000 40000 30000 10000 10000 15000 20000 40000 35000 35000 30000 35000 30000 35000 30000 25000 15000 20000 25000 30000
do
    temp=$(/home/erfan/mutilate/mutilate -t 60 -c 25 -T 25  -q $i -w 20 -s 10.254.254.100 --noload -i fb_ia)
    echo -n "$i," >> $1
    echo $temp | awk '{ printf "%s,%s,%s,%s\n", $13,$19,$20,$21}' >> $1
    echo $temp | awk '{ printf "avg=%s 95th=%s 99=%s 99.9=%s\n", $13,$19,$20,$21 }'
    ((j++))
done
ssh root@10.254.254.100 'pkill reader.bash'
scp root@10.254.254.100:/root/test.log "power.csv"
ssh root@10.254.254.100 'rm test.log'
ssh root@10.254.254.100 'pkill sleep'

#python3 aggregate_power.py 1 90 1
#cat power.csv
echo "experiment finished"
