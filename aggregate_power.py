import sys
import numpy as np
import os

convertfunc = lambda x: float(x[0:-2])
power_matrix=[]
rates = []
for i in range(int(sys.argv[1]), int(sys.argv[2])+int(sys.argv[3]), int(sys.argv[3])):
    power_matrix.append(np.genfromtxt("rate"+str(i)+".log",  converters={0: convertfunc}))
    rates.append(i)
    os.remove("rate"+str(i)+".log")

with open("power.csv", "w") as f:
    for i in range(len(power_matrix)):
        f.write("{}".format(rates[i]))
        for j in range(len(power_matrix[i])):
            f.write(",")
            f.write("{}".format(power_matrix[i][j]))
        f.write("\n")
