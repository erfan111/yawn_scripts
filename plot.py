## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt

a = np.genfromtxt(sys.argv[1], delimiter=',')
print(a)
b = np.genfromtxt(sys.argv[2], delimiter=',')
print(b)

x = [i[0] for i in a]
on_avg = [i[1] for i in a]
off_avg = [i[1] for i in b]
on_95 = [i[2] for i in a]
off_95 = [i[2] for i in b]
on_99 = [i[3] for i in a]
off_99 = [i[3] for i in b]
on_999 = [i[4] for i in a]
off_999 = [i[4] for i in b]
plt.ylabel('Latency (us)')
plt.title('Request Latency of different loads')
# plt.xticks(ind, ('20%', '30%', '40%', '50%'))
plt.yticks(np.arange(0, 800, 10))
plt.grid()
p1,p2,p3,p4,p5,p6= plt.plot(x, on_95, 'r', x, off_95, 'r:', x, on_99, 'b',x, off_99, 'b:', x, on_999, 'g', x, off_999, 'g:')
# p1,p2 = plt.plot(x, on_avg, 'g', x, off_avg, 'g:')
plt.legend((p1, p2,p3,p4,p5,p6), ('menu-95', 'yawn-95','menu-99th', 'yawn-99th', 'menu-99.9', 'yawn-99.9'))
# plt.legend((p1, p2), ('On-avg', 'Off-avg'))
#plt.savefig('avg.png', format='png', dpi=300)
plt.show()
