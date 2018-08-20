## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats

a = list(np.genfromtxt(sys.argv[1], delimiter=',',usecols=np.arange(0,12), invalid_raise = False))
b = list(np.genfromtxt(sys.argv[2], delimiter=',',usecols=np.arange(0,12), invalid_raise = False))
print(a)

x = []
x2 = []
for i in range(len(a)):
    x.append(int(a[i][0]))
    np.delete(a[i],0)
    x2.append(int(b[i][0]))
    np.delete(b[i],0)

# treatments = [e1, e2, e3, e4]
# med1, CI1 = fakeBootStrapper(1)
# med2, CI2 = fakeBootStrapper(2)
# medians = [None, None, med1, med2]
# conf_intervals = [None, None, CI1, CI2]

pos = np.array(range(len(a))) + 1
pos2 = np.array(range(len(b))) + 1


fig, axs = plt.subplots()
# axs.boxplot(a, sym='k+', positions=pos,
#                 notch=1, bootstrap=5000)
bplot1 = axs.boxplot(a, 0, '',patch_artist=True)
bplot2 = axs.boxplot(b, 0, '',patch_artist=True)

colors = ['pink', 'lightblue', 'lightgreen']
for patch in bplot1['boxes']:
    patch.set_facecolor(colors[0])
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
axs.legend([bplot1["boxes"][0], bplot2["boxes"][0]], ['MENU', 'YAWN'])
#
# #plt.savefig('avg.png', format='png', dpi=300)
plt.show()
