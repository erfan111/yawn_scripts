## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats

font = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 18}
font_label = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 18}

plt.rc('font', **font)
# plt.rc('legend', fontsize=11)

convertfunc = lambda x: float(x[0:-2])
menu = list(np.genfromtxt(sys.argv[1], delimiter=',',  converters={0: convertfunc}))
yawn = list(np.genfromtxt(sys.argv[2], delimiter=',',  converters={0: convertfunc}))
menu_single = list(np.genfromtxt(sys.argv[3], delimiter=',',  converters={0: convertfunc}))
yawn_single = list(np.genfromtxt(sys.argv[4], delimiter=',',  converters={0: convertfunc}))
# print(a)
data = [[],[]]
data2 = []
for j in range(0,len(menu), 2):
	sum1 = int(menu[j])
	sum1+= int(menu[j+1])
	data[0].append(sum1)


for j in range(0, len(yawn), 2):
	sum1 = int(yawn[j])
	sum1+= int(yawn[j+1])
	data[1].append(sum1)

data2.append(menu_single)
data2.append(yawn_single)

fig, axs = plt.subplots(figsize=(7,6))
# axs.boxplot(a, sym='k+', positions=pos,
#                 notch=1, bootstrap=5000)


boxprops = dict(linewidth=3)
medianprops = dict(linestyle='-.', linewidth=2.5, color='firebrick')
meanpointprops = dict(marker='D', markeredgecolor='black',
                      markerfacecolor='firebrick')
meanlineprops = dict(linewidth=2.5)
whiskerprops = dict(linewidth=3)

axs.boxplot(data, 0, '', boxprops=boxprops, medianprops=meanlineprops, whiskerprops=whiskerprops)
# axs.set_aspect(1.5)
# axs.set_title("don't show\noutlier points")
axs.set_ylabel('Power Consumption (Watt)')
# plt.title('Power Consumption of Memcached in different Loads')
axs.set_xticklabels(['Menu', "Yawn"])
axs.grid('on',axis='y')
# axs.set_title("NUMA Package Power Consumption")
# ax2.set_title("Single CPU Package Power Consumption")
plt.savefig('idle_numa.png', format='png', dpi=300, bbox_inches='tight')
fig, ax2 = plt.subplots(figsize=(7,6))


ax2.boxplot(data2, 0, '', boxprops=boxprops, medianprops=meanlineprops, whiskerprops=whiskerprops)
# axs.set_aspect(1.5)
# axs.set_title("don't show\noutlier points")
ax2.set_ylabel('Power Consumption (Watt)')
# plt.title('Power Consumption of Memcached in different Loads')
ax2.set_xticklabels(['Menu', "Yawn"])
ax2.grid('on',axis='y')

# #plt.savefig('avg.png', format='png', dpi=300)
plt.savefig('idle_nonnuma.png', format='png', dpi=300, bbox_inches='tight')

plt.show()
