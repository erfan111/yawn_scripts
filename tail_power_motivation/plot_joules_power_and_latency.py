## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib
font = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 20}
font_label = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 20}

plt.rc('font', **font)
plt.rc('legend', fontsize=20)
# power files on -- off
a = list(np.genfromtxt(sys.argv[1], delimiter=','))
b = list(np.genfromtxt(sys.argv[2], delimiter=','))
# latency files  on -- off
c = np.genfromtxt(sys.argv[3], delimiter=',')
d = np.genfromtxt(sys.argv[4], delimiter=',')


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

############# POWER
x = []
x2 = []
a = a[1::2]
b = b[1::2]
for i in range(len(a)):
    x.append(int(a[i][0]))
    np.delete(a[i],0)
    x2.append(int(b[i][0]))
    np.delete(b[i],0)

pos = np.array(range(len(a))) + 1
pos2 = np.array(range(len(b))) + 1

############# LATENCY
x = [int(i[0]/1000) for i in c]

on_avg = [i[1] for i in c]
off_avg = [i[1] for i in d]
on_95 = [i[2] for i in c]
off_95 = [i[2] for i in d]
on_99 = [i[3] for i in c]
off_99 = [i[3] for i in d]
on_999 = [i[4] for i in c]
off_999 = [i[4] for i in d]

##############
fig, axs = plt.subplots(figsize=(7,6))
axs.set_ylabel('Latency (us)',**font_label)
# plt.title('Request Latency of different loads')
# axs.set_yticks(np.arange(0, 800, 10))
axs.set_ylim(50,250)
# axs.grid()
axs.set_xticks(np.arange(0,60,10))
axs.set_xticklabels(np.arange(0,110,20))
axs.set_xlabel("Request Rate (x" + r'$10^3$' + " RPS)",**font_label)

p1,p2, p3, p4 = axs.plot(x, on_999, 'k', x, off_999, 'xkcd:azure', x, on_95, 'k:', x, off_95, 'xkcd:azure')
p4.set(linestyle='dotted')
plt.setp(p1, linewidth=3.0)
plt.setp(p2, linewidth=3.0)
plt.setp(p3, linewidth=2.0)
plt.setp(p4, linewidth=2.0)
# plt.setp(p3, linewidth=3.0)
# plt.setp(p4, linewidth=3.0)
# p1,p2 = plt.plot(x, on_avg, 'g', x, off_avg, 'g:')
axs.legend((p1, p2, p3, p4), ('Default Linux-' + r'$99.9^{th}$', 'C-states Disabled-' + r'$99.9^{th}$','Default Linux-' + r'$95^{th}$', 'C-states Disabled-' + r'$95^{th}$'),  loc=1,
           ncol=1)

axs.set_xlim(1,50)
axs.xaxis.grid(which="major")
plt.savefig('pow_lat_lat.png', format='png', dpi=300, bbox_inches='tight')

fig, ax2 = plt.subplots(figsize=(7,6))


bplot1 = ax2.boxplot(a, 0, '',patch_artist=True)
bplot2 = ax2.boxplot(b, 0, '',patch_artist=True)

colors = ['blue', 'dodgerblue', 'red', 'black']

for element in ['boxes','whiskers', 'fliers', 'means', 'medians', 'caps']:
    plt.setp(bplot2[element], color=colors[1])
for patch in bplot2['boxes']:
    patch.set_facecolor(colors[0])
    patch.set(linewidth=3)
for element in ['boxes','whiskers', 'fliers', 'means', 'medians', 'caps']:
    plt.setp(bplot1[element], color=colors[3])
for patch in bplot1['boxes']:
    patch.set_facecolor(colors[2])
    patch.set(linewidth=3)
ax2.set_ylabel('CPU Power Consumption (W)',**font_label)
plt.xlabel("Request Rate (x" + r'$10^3$' + " RPS)",**font_label)
# plt.title('Power Consumption of Memcached in different Loads')
# ax2.set_xticklabels(x2, rotation='90')
ax2.set_xticks(np.arange(1,21,1))
ax2.set_xticklabels(["1", "10","20","30","40","50", "60", "70", "80", "90", "100"])
# ax2.set_xticks(np.arange(1000,50000,5000))
# ax2.set_xticklabels(np.arange(1000,50000,5000))
ax2.xaxis.grid(which="major")
# ax2.set_yticks(np.arange(0, 40, 10))
ax2.set_ylim(20,34)
ax2.set_xlim(0,11)

# locs, labs = plt.xticks()
# plt.xticks(locs[1:])
ax2.legend([bplot1["boxes"][0], bplot2["boxes"][0]], ['Default Linux (Menu)', 'C-states Disabled'], loc=4)

# fig.tight_layout()
#
plt.savefig('pow_lat_pow.png', format='png', dpi=300, bbox_inches='tight')
plt.show()
