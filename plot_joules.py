## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt

convertfunc = lambda x: float(x[0:-2])
a = np.genfromtxt(sys.argv[1],  converters={0: convertfunc})
print(a)
if(len(sys.argv) >2):
	b = np.genfromtxt(sys.argv[2],  converters={0: convertfunc})
	print(b)

x = range(len(a))
#on_avg = [i[1] for i in a]
#off_avg = [i[1] for i in b]
#on_95 = [i[2] for i in a]
#off_95 = [i[2] for i in b]
#on_99 = [i[3] for i in a]
#off_99 = [i[3] for i in b]
#on_999 = [i[4] for i in a]
#off_999 = [i[4] for i in b]
plt.ylabel('Energy (J)')
plt.title('Power Consumption of Memcached in different Loads')
plt.xticks(range(1000,51000,2000))
#plt.yticks(np.arange(0, 800, 10))
plt.grid()
#p1,p2,p3,p4,p5,p6,p7,p8 = plt.plot(x, on_avg, 'r', x, off_avg, 'r:', x, on_95, 'y',x, off_95, 'y:', x, on_99, 'b',x, off_99, 'b:', x, on_999, 'g', x, off_999, 'g:')
if(len(sys.argv) >2):
	p1,p2 = plt.plot(x, a, 'g', x, b, 'g:')
	plt.legend((p1, p2), ('File1', 'File2'))
else:
	p1 = plt.plot(x, a, 'g')
	plt.legend((p1), ('File1'))
#plt.legend((p1, p2,p3,p4,p5,p6,p7,p8), ('On-Avg', 'Off-Avg' ,'On-95th', 'Off-95th','On-99th', 'Off-99th', 'On-99.9', 'Off-99.9'))

#plt.savefig('avg.png', format='png', dpi=300)
plt.show()
