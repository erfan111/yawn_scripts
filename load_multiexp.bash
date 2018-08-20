#!/usr/bin/env bash

## usage ./load.bash output.csv
#echo "" > $1

for j in `seq 1 1 5`
do
	echo "" > "t$j.csv"
	for i in `seq 1000 5000 101000`
	do
    	echo "experiment started with rate=$i"

    	temp=$(/home/erfan/mutilate/mutilate -s 10.254.254.100 -T 25 -c 25 -t 50 -w 5 -q $i -i fb_ia)
    	echo -n "$i," >> "t$j.csv"
    	echo $temp | awk '{ printf "%s,%s,%s,%s\n", $13,$19,$20,$21}' >> "t$j.csv"
    	echo $temp | awk '{ printf "avg=%s 95th=%s 99th=%s 99.9=%s\n", $13,$19,$20,$21 }'
    	sleep 15
	done
	sleep 30
done
python3 aggregate.py 5 21  new_on.csv
cp t*.csv new_on/
rm t*.csv
echo "experiment on finished"

: <<'END'
ssh root@10.254.254.100 cpupower idle-set -d 4
sleep 10
for j in `seq 1 1 5`
do
        echo "" > "t$j.csv"
        for i in `seq 1000 1000 50000`
        do
        echo "experiment started with rate=$i"

        temp=$(/home/scc/mutilate/mutilate -s 10.254.254.100 -T 4 -c 25 -t 40 -D 4 -C 4 -a 10.254.254.13 -q $i -a localhost)
        echo -n "$i," >> "t$j.csv"
        echo $temp | awk '{ printf "%s,%s,%s,%s\n", $13,$19,$20,$21}' >> "t$j.csv"
        echo $temp | awk '{ printf "avg=%s 95th=%s 99th=%s 99.9=%s\n", $13,$19,$20,$21 }'
        sleep 15
        done
        sleep 60
done
python aggregate.py 5 50  "new_c6.csv"
cp t*.csv new_c6off/
rm t*.csv
echo "experiment c6 off finished"

ssh root@10.254.254.100 cpupower idle-set -d 3
sleep 10
for j in `seq 1 1 5`
do
        echo "" > "t$j.csv"
        for i in `seq 1000 1000 50000`
        do
        echo "experiment started with rate=$i"

        temp=$(/home/scc/mutilate/mutilate -s 10.254.254.100 -T 4 -c 25 -t 40 -D 4 -C 4 -a 10.254.254.13 -q $i -a localhost)
        echo -n "$i," >> "t$j.csv"
        echo $temp | awk '{ printf "%s,%s,%s,%s\n", $13,$19,$20,$21}' >> "t$j.csv"
        echo $temp | awk '{ printf "avg=%s 95th=%s 99th=%s 99.9=%s\n", $13,$19,$20,$21 }'
        sleep 15
        done
        sleep 60
done
python aggregate.py 5 50  "new_c3.csv"
cp t*.csv new_c3off/
rm t*.csv
echo "experiment c3 off finished"

ssh root@10.254.254.100 cpupower idle-set -d 2
ssh root@10.254.254.100 cpupower idle-set -d 1
ssh root@10.254.254.100 cpupower idle-set -d 0

sleep 10
for j in `seq 1 1 5`
do
        echo "" > "t$j.csv"
        for i in `seq 1000 1000 50000`
        do
        echo "experiment started with rate=$i"

        temp=$(/home/scc/mutilate/mutilate -s 10.254.254.100 -T 4 -c 25 -t 40 -D 4 -C 4 -a 10.254.254.13 -q $i -a localhost)
        echo -n "$i," >> "t$j.csv"
        echo $temp | awk '{ printf "%s,%s,%s,%s\n", $13,$19,$20,$21}' >> "t$j.csv"
        echo $temp | awk '{ printf "avg=%s 95th=%s 99th=%s 99.9=%s\n", $13,$19,$20,$21 }'
        sleep 15
        done
        sleep 60
done
python aggregate.py 5 50  new_off.csv
cp t*.csv new_off/
rm t*.csv
echo "experiment off finished"

END
