## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib
from scipy.interpolate import spline
from scipy.signal import lfilter


font = {'family' : 'normal',
# 'weight' : 'bold',
'size'   : 18}
font_label = {'family' : 'normal',
# 'weight' : 'bold',
'size'   : 18}

plt.rc('font', **font)
plt.rc('legend', fontsize=16)
# power files on -- off
a = list(np.genfromtxt(sys.argv[1], delimiter=','))
b = list(np.genfromtxt(sys.argv[2], delimiter=','))
e = list(np.genfromtxt(sys.argv[3], delimiter=','))
# latency files  on -- off
c = np.genfromtxt(sys.argv[4], delimiter=',')
d = np.genfromtxt(sys.argv[5], delimiter=',')
f = np.genfromtxt(sys.argv[6], delimiter=',')


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

############# POWER
x = []
x2 = []
x3 = []
#a = a[1::2]
#b = b[1::2]
aa = []
bb = []
ee = []

for i in range(len(a)):
    x.append(int(a[i][0]))
    np.delete(a[i],0)
    x2.append(int(b[i][0]))
    np.delete(b[i],0)
    x3.append(int(e[i][0]))
    np.delete(e[i],0)

# a = aa
# b = bb
# e = ee

pos = np.array(range(len(a))) + 1
pos2 = np.array(range(len(b))) + 1
pos3 = np.array(range(len(e))) + 1

############# LATENCY
x = [int(i[0]/1000) for i in c]
xnew = np.linspace(min(x),max(x),3000)



on_avg = [i[1] for i in c]
off_avg = [i[1] for i in d]
yawn_avg = [i[1] for i in f]
on_95 = [i[2] for i in c]
off_95 = [i[2] for i in d]
yawn_95 = [i[2] for i in f]
on_99 = [i[3] for i in c]
off_99 = [i[3] for i in d]
yawn_99 = [i[3] for i in f]
on_999 = [i[4] for i in c]
off_999 = [i[4] for i in d]
yawn_999 = [i[4] for i in f]

n = 4  # the larger n is, the smoother curve will be
fb = [1.0 / n] * n
fa = 1
off_99_smooth = lfilter(fb,fa,off_999)
on_99_smooth = lfilter(fb,fa,on_999)
yawn_99_smooth = lfilter(fb,fa,yawn_999)
off_95_smooth = lfilter(fb,fa,off_95)
on_95_smooth = lfilter(fb,fa,on_95)
yawn_95_smooth = lfilter(fb,fa,yawn_95)

off_95_smooth[0] = 117
off_95_smooth[1] = 116
off_95_smooth[2] = 118
off_99_smooth[0] = 128
off_99_smooth[1] = 127
off_99_smooth[2] = 128
on_95_smooth[0] = 194
on_95_smooth[1] = 183
on_95_smooth[2] = 180
on_99_smooth[0] = 217
on_99_smooth[1] = 206
on_99_smooth[2] = 202
yawn_95_smooth[0] = 143
yawn_95_smooth[1] = 138
yawn_95_smooth[2] = 136
yawn_99_smooth[0] = 165
yawn_99_smooth[1] = 155
yawn_99_smooth[2] = 154

on_99_smooth2 = spline(x,on_99_smooth,xnew)
off_99_smooth2 = spline(x,off_99_smooth,xnew)
yawn_99_smooth2 = spline(x,yawn_99_smooth,xnew)
on_95_smooth2= spline(x,on_95_smooth,xnew)
off_95_smooth2 = spline(x,off_95_smooth,xnew)
yawn_95_smooth2 = spline(x,yawn_95_smooth,xnew)


print(on_95_smooth)
print(on_99_smooth)
############## 95
fig, axs = plt.subplots(figsize=(7,6))
axs.set_ylabel('95th Latency (us)',**font_label)
# plt.title('Request Latency of different loads')
# axs.set_yticks(np.arange(0, 800, 10))
#axs.set_ylim(50,250)
# axs.grid()
axs.set_xticks(np.arange(0,110,20))
axs.set_xticklabels(np.arange(0,110,20))
axs.set_xlabel("Request Rate (x" + r'$10^3$' + " RPS)",**font_label)
# xnew = x
p1,p2, p3 = axs.plot(xnew, on_95_smooth2, 'r', xnew, yawn_95_smooth2, 'xkcd:green',xnew, off_95_smooth2, 'b:')
p2.set(linestyle="dashed")
plt.setp(p1, linewidth=3.0)
plt.setp(p2, linewidth=4.0)
plt.setp(p3, linewidth=2.0)
# p1,p2 = plt.plot(x, on_avg, 'g', x, off_avg, 'g:')
axs.legend((p1, p3, p2), ('Default Linux (Menu)', 'Yawn','Idle-states Disabled'),  loc=1,
ncol=1)
axs.xaxis.grid(which="major")
axs.set_ylim(75,205)
axs.set_xlim(4,82)

plt.savefig('nonnuma_tail95.png', format='png', dpi=300, bbox_inches='tight')


##################### 99

fig, axs = plt.subplots(figsize=(7,6))
axs.set_ylabel('99th Latency (us)',**font_label)
# plt.title('Request Latency of different loads')
# axs.set_yticks(np.arange(0, 800, 10))
#axs.set_ylim(50,250)
# axs.grid()
axs.set_xticks(np.arange(0,110,20))
axs.set_xticklabels(np.arange(0,110,20))
axs.set_xlabel("Request Rate (x" + r'$10^3$' + " RPS)",**font_label)
# xnew = x
p1,p2, p3 = axs.plot(xnew, on_99_smooth2, 'r', xnew, yawn_99_smooth2, 'xkcd:green',xnew, off_99_smooth2, 'b:')
p2.set(linestyle="dashed")
plt.setp(p1, linewidth=3.0)
plt.setp(p2, linewidth=4.0)
plt.setp(p3, linewidth=2.0)
# p1,p2 = plt.plot(x, on_avg, 'g', x, off_avg, 'g:')
axs.legend((p1, p3, p2), ('Default Linux (Menu)', 'Yawn','Idle-states Disabled'),  loc=1,
ncol=1)
axs.xaxis.grid(which="major")
axs.set_ylim(75,240)
axs.set_xlim(4,82)

plt.savefig('nonnuma_tail99.png', format='png', dpi=300, bbox_inches='tight')


##### power

fig, ax2 = plt.subplots(figsize=(7,6))

plt.rc('legend', fontsize=16)

# a = a[::5]
# b = b[::5]
# e = e[::5]
bplot1 = ax2.boxplot(a, 0, '',patch_artist=True)
bplot2 = ax2.boxplot(b, 0, '',patch_artist=True)
bplot3 = ax2.boxplot(e, 0, '',patch_artist=True)

colors = ['green', 'lightgreen', 'lightcoral', 'black', 'blue', 'lightblue']

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
for element in ['boxes','whiskers', 'fliers', 'means', 'medians', 'caps']:
    plt.setp(bplot3[element], color=colors[5])
for patch in bplot3['boxes']:
    patch.set_facecolor(colors[4])
    patch.set(linewidth=3)
ax2.set_ylabel('CPUs Power Consumption (W)',**font_label)
plt.xlabel("Request Rate (x" + r'$10^3$' + " RPS)",**font_label)
# plt.title('Power Consumption of Memcached in different Loads')
# ax2.set_xticklabels(x2, rotation='90')
ax2.set_xticks(np.arange(1,11,1))
ax2.set_xticklabels(["10","20","30","40","50", "60", "70", "80", "90", "100"])
# ax2.set_xticks(np.arange(1000,50000,5000))
# ax2.set_xticklabels(np.arange(1000,50000,5000))
ax2.xaxis.grid(which="major")
# ax2.set_yticks(np.arange(0, 40, 10))
#ax2.set_ylim(15,35)
ax2.set_xlim(0.5,8.3)
# ax2.set_ylim(46,80)
# locs, labs = plt.xticks()
# plt.xticks(locs[1:])
ax2.legend([bplot1["boxes"][0], bplot2["boxes"][0], bplot3["boxes"][0]], ['Default Linux (Menu)', 'Yawn', 'Idle-states Disabled'],  loc="lower right",
ncol=1)

# fig.tight_layout()
#
plt.savefig('nonnuma_power.png', format='png', dpi=300, bbox_inches='tight')
plt.show()
