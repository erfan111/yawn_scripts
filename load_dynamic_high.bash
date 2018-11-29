#!/usr/bin/env bash
#scc@scc10:~/power_project$ ssh root@10.254.254.100 '(echo -ne '0x2710'; sleep 1000d) > /dev/network_throughput </dev/null 2>/dev/null &'
#scc@scc10:~/power_project$ ssh root@10.254.254.100 'pkill sleep'
#scc@scc10:~/power_project$ x=$( printf "%x" 10000 ) ; echo $x
echo "" > $1
echo "experiment started"
ssh root@10.254.254.100 '/home/erfan/rapl_read/reader.bash > test.log &'
temp=$(/home/scc/mutilate/mutilate -s 10.254.254.100 -loadonly)
for i in 10000 15000 20000 45000 30000 15000 30000 35000 45000 75000 50000 35000 15000 25000 35000 45000 40000 35000 30000 25000 30000 40000 55000 50000 55000 65000 75000 100000 80000 60000 55000 45000 40000 30000 35000 30000 35000 30000 20000 20000 25000 30000 35000 5000 10000 35000 90000 50000 80000 75000 70000 50000 60000 60000 55000 50000 40000 45000 35000 45000 50000 35000 30000 25000 20000 5000 5000 10000 30000 50000 45000 50000 100000 95000 90000 80000 70000 80000 85000 65000 60000 45000 30000 35000 30000 5000 10000 15000 10000 20000
do
    temp=$(/home/scc/mutilate/mutilate -t 60 -c 25 -T 25 -w 20 -q $i -s 10.254.254.100 -noload -i fb_ia)
    echo -n "$i," >> $1
    echo $temp | awk '{ printf "%s,%s,%s,%s\n", $13,$19,$20,$21}' >> $1
    echo $temp | awk '{ printf "avg=%s 95th=%s 99=%s 99.9=%s\n", $13,$19,$20,$21 }'
done
ssh root@10.254.254.100 'pkill reader.bash'
scp root@10.254.254.100:/root/test.log "power.csv"
ssh root@10.254.254.100 'rm test.log'
ssh root@10.254.254.100 'pkill sleep'

echo "experiment finished"
