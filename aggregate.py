import numpy as np
import sys
import statsmodels.api as sm

if len(sys.argv) <= 1:
	print("python  aggregate.py  [number of experiments] [number_of rates]  [output file]")
	sys.exit(1)
num_of_rates = int(sys.argv[2])
num_of_exp = int(sys.argv[1])

latency_matrix = []
for i in range(num_of_exp):
	latency_matrix.append(list(np.genfromtxt("t{}.csv".format(i+1), delimiter=',')))
print(latency_matrix[0])
rates = [ i[0] for i in latency_matrix[0] ]
agg_avg = []
agg_95 = []
agg_99 = []
agg_999 = []

for rate in range(num_of_rates):
	temp_sum = 0
	agg_avg.append(0)
        agg_95.append(0)
        agg_99.append(0)
        agg_999.append(0)
	for experiment in range(num_of_exp):
		agg_avg[rate] += latency_matrix[experiment][rate][1]
		agg_95[rate] += latency_matrix[experiment][rate][2]
		agg_99[rate] += latency_matrix[experiment][rate][3]
        	agg_999[rate] += latency_matrix[experiment][rate][4]

with open(sys.argv[3], "w") as f:
	for i in range(len(rates)):
		f.write("{},{},{},{},{}\n".format(rates[i], agg_avg[i]/num_of_exp, agg_95[i]/num_of_exp, agg_99[i]/num_of_exp, agg_999[i]/num_of_exp))
