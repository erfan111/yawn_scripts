## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt

# a = [3,5,56,6,78,57,85,85,474,25,34,67,34,43,54,3,35,54,23]
# b = [80,80,80,80,80, 80]

a = np.genfromtxt(sys.argv[1], delimiter=',')
# print(a, len(a))
b = np.genfromtxt(sys.argv[2], delimiter=',')
c = []
for i in b:
    c.append(i/1000000)
# print(c, len(c))

x = range(len(a))
# x2 = range(1, len(a)+600, 387)
x2 = list(range(len(c)))
prev = 0
step = (len(a)//len(b))
for i in range(len(x2)):
    x2[i] = prev + step
    prev = x2[i]
x2[0] = -150
x2[-1] = x[-1]+500

fig, ax1 = plt.subplots()
ax1.set_xlabel('time')
ax1.tick_params(axis='y', labelcolor='tab:red')
plt.ylabel('Latency (us)')
# plt.title('Memcache')
plt.xticks([])
# plt.yticks(np.arange(0, 800, 10))
plt.grid()
p1= ax1.plot(x, a, 'ro')
ax1.set_ylabel('Latency (us)', color='tab:red')
ax2 = ax1.twinx()
ax2.set_ylabel('Utilization', color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')
p2= ax2.plot(x2, c, 'b')
d = np.zeros(len(x2))
ax2.fill_between(x2,c, where=c > d, alpha=0.3)
# p2= plt.plot()
#p1,p2 = plt.plot(x, on_999, 'g', x, off_999, 'g:')
ax2.set_yticks(np.arange(0, 101, 10))
plt.legend()
#plt.legend((p1, p2), ('On-999', 'Off-999'))
plt.savefig('aloneLatency.png', format='png', dpi=300)
plt.show()
