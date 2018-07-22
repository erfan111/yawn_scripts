## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats

a = list(np.genfromtxt(sys.argv[1], delimiter=','))
print(a)

x = []
for i in range(len(a)):
    x.append(int(a[i][0]))
    np.delete(a[i],0)

data = [
[13,11.5,12.2,11,11,11.2],
[13,11.5,12.2,11,11,11.2],
[13,11.5,12.2,11,11,11.2],
[13,11.5,12.2,11,11,11.2],
[13,11.5,12.2,11,11,11.2],
[13,11.5,12.2,11,11,11.2]
]

# treatments = [e1, e2, e3, e4]
# med1, CI1 = fakeBootStrapper(1)
# med2, CI2 = fakeBootStrapper(2)
# medians = [None, None, med1, med2]
# conf_intervals = [None, None, CI1, CI2]

pos = np.array(range(len(a))) + 1


fig, axs = plt.subplots()
# axs.boxplot(a, sym='k+', positions=pos,
#                 notch=1, bootstrap=5000)
axs.boxplot(a, 0, '')
# axs.set_title("don't show\noutlier points")
plt.ylabel('Energy (J)')
plt.title('Power Consumption of Memcached in different Loads')
axs.set_xticklabels(x, rotation='90')
plt.grid(axis='both', which='both')
# plt.xticks(x)
# #plt.yticks(np.arange(0, 800, 10))
# plt.grid()
# #p1,p2,p3,p4,p5,p6,p7,p8 = plt.plot(x, on_avg, 'r', x, off_avg, 'r:', x, on_95, 'y',x, off_95, 'y:', x, on_99, 'b',x, off_99, 'b:', x, on_999, 'g', x, off_999, 'g:')
# if(len(sys.argv) >2):
# 	p1,p2 = plt.plot(x, a, 'g', x, b, 'g:')
# 	plt.legend((p1, p2), ('File1', 'File2'))
# else:
# 	p1 = plt.plot(x, a, 'g')
# 	plt.legend((p1), ('File1'))
# #plt.legend((p1, p2,p3,p4,p5,p6,p7,p8), ('On-Avg', 'Off-Avg' ,'On-95th', 'Off-95th','On-99th', 'Off-99th', 'On-99.9', 'Off-99.9'))
#
# #plt.savefig('avg.png', format='png', dpi=300)
plt.show()
