## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib import ticker
font = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 14}
font_label = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 10}

plt.rc('font', **font)
plt.rc('legend', fontsize=11)
convertfunc = lambda x: float(x[0:-2])
a = []
for i in range(8):
    a.append(np.genfromtxt("residency" + str(i) + ".csv",  delimiter=","))
b = []
x = []
for i in range(len(a)):
    temp = []
    xx = []
    for j in range(len(a[i])):
        temp2 = []
        sum = 0
        for k in range(len(a[i][j])):
            # print(a[i][j][k])
            if k ==0:
                xx.append(a[i][j][0])
            else:
                sum += round(a[i][j][k], 4)
                temp2.append(round(a[i][j][k], 4))
        temp2.insert(0,100-sum)
        temp.append(temp2)
    b.append(temp)
    x.append(xx)
a = []
for i in range(len(b)):
    temp = []
    for j in range(len(b[i])):
        sum = 0
        avg = 0
        for k in range(len(b[i][j])):
            # print(a[i][j][k])
            if k !=0:
                sum += round(b[i][j][k], 4)
                avg += round(b[i][j][k], 4) * (k+1)
        avg += (100-sum)
        avg /= 100
        temp.append(avg)
    a.append(temp)
# print("a", a)

fig, ax = plt.subplots(figsize=(8,4))
print("a", a)
im = plt.imshow(a, cmap='hot_r', interpolation='nearest',vmin=1, vmax=6)
ax.set_xticks(np.arange(0, 55, 5))
# ax.set_xlim(0,50)
ax.set_xticklabels(np.arange(0, 55, 5))
ax.set_xlabel("Request Rate (x" + r'$10^3$' + " RPS)")
ax.set_yticks(np.arange(0, 8, 1))
ax.set_yticklabels(np.arange(1, 9, 1), **font_label)
ax.set_ylabel("Core Number")

cbar = ax.figure.colorbar(im,ticks=[], orientation='horizontal', pad=0.2)
# tick_locator = ticker.MaxNLocator(nbins=3)
# cbar.locator = tick_locator
cbar.ax.invert_xaxis()
# cbar.ax.tick_params(labelsize=10)
# cbar.update_ticks()
# cbar.ax.set_xticklabels([])  # horizontal colorbar
cbar.set_label("Deeper Sleep                                                     Shallower Sleep")

plt.legend()

plt.savefig('heat.png', format='png', dpi=300, bbox_inches='tight')
plt.show()

# plt.show()
