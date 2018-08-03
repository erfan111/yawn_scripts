import sys
import numpy as np
import os

convertfunc = lambda x: float(x[0:-2])
power_matrix=[]
rates = []
for i in range(int(sys.argv[1]), int(sys.argv[2])+int(sys.argv[3]), int(sys.argv[3])):
    power_matrix.append(np.genfromtxt("rate"+str(i)+".log", delimiter=","))
    rates.append(i)
    #os.remove("rate"+str(i)+".log")
f = []
for k in range(8):
    f.append(open("residency" + str(k) + ".csv", "w"))

for i in range(len(power_matrix)):  # i = rate 1000
    for k in range(8):      # k = cpu 3
        f[k].write("{}".format(rates[i]))
        for j in range(len(power_matrix[i][k])):
            f[k].write(",")
            f[k].write("{}".format(power_matrix[i][k][j]))
        f[k].write("\n")

for k in range(8):
    f[k].close()
