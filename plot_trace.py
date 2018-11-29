## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.interpolate import spline


font = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 14}
font_label = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 13}

plt.rc('font', **font)
plt.rc('legend', fontsize=11)

convertfunc = lambda x: float(x[0:-2])

latency_off_file = np.genfromtxt(sys.argv[1], delimiter=',')
latency_menu_file = np.genfromtxt(sys.argv[2], delimiter=',')
latency_yawn_file = np.genfromtxt(sys.argv[3], delimiter=',')
power_off_file = np.genfromtxt(sys.argv[4], delimiter=',', converters={0: convertfunc})
power_menu_file = np.genfromtxt(sys.argv[5], delimiter=',', converters={0: convertfunc})
power_yawn_file = np.genfromtxt(sys.argv[6], delimiter=',', converters={0: convertfunc})

x = [i[0] for i in latency_off_file]
off_avg = [i[1] for i in latency_off_file]
menu_avg = [i[1] for i in latency_menu_file]
off_95 = [i[2] for i in latency_off_file]
menu_95 = [i[2] for i in latency_menu_file]
off_99 = [i[3] for i in latency_off_file]
menu_99 = [i[3] for i in latency_menu_file]
yawn_99 = [i[3] for i in latency_yawn_file]
off_999 = [i[4] for i in latency_off_file]
menu_999 = [i[4] for i in latency_menu_file]
yawn_999 = [i[4] for i in latency_yawn_file]


fig, (ax1, ax2, ax3) = plt.subplots(3,1,figsize=(14,8))

for i in range(len(x)):
    x[i] /= 1000
x1 = np.arange(1,91,1)
xnew = np.linspace(x1.min(),x1.max(),300)
power_smooth = spline(x1,x,xnew)


ax1.set_ylabel("Request Rate\n (x" + r'$10^3$' + " RPS)",**font_label)# ax1.set_xlabel("Min")
ax1.grid()
# ax1.set_xticks(np.arange(0,91,10))
ax1.set_xticklabels([])
ax1.set_yticks(np.arange(0,80,10))
ax1.set_yticklabels(np.arange(0,80,10))
ax1.set_xlim(1,90)
p1 = ax1.plot(xnew, power_smooth, 'm-', linewidth=3)

p2 ,p3, p4 = ax2.plot(x1, off_99, x1, menu_99, x1, yawn_99, linewidth=3)
ax2.set_ylabel('99th Latency (us)')
# ax2.set_xlabel('Min')
ax2.grid()
# ax2.set_xticks(np.arange(0,91,10))
ax2.set_xticklabels([])
ax2.set_yticks(np.arange(80,200,20))
# ax2.set_xticklabels(np.arange(0,91,10))
ax2.set_xlim(1,90)
step2 = 90/(len(power_off_file))
step3 = 90/(len(power_menu_file))
step4 = 90/(len(power_yawn_file))
x2 = np.arange(1, 91, step2)
x3 = np.arange(1, 91, step3)
x4 = np.arange(1, 91, step4)
p5, p6, p7 = ax3.plot(x2, power_off_file, x3, power_menu_file, x4, power_yawn_file, linewidth=3)
ax3.set_ylabel('Power (Watt)', labelpad=15)
ax3.set_xlabel('Time (min)')
ax3.grid()
tick = [0,10,20,30,40,50,60,70,80,90]
ax3.set_xticks(np.arange(1,101,10))
ax3.set_xticklabels(tick)
ax3.set_xlim(2,91)
# ax2.title('Request Latency of different loads')
# plt.xticks(ind, ('20%', '30%', '40%', '50%'))
# plt.yticks(np.arange(0, 800, 10))
ax1.legend((p2, p3, p4), ('C-states Disabled','Menu', 'Yawn'), loc='center',
           ncol=3,bbox_to_anchor=(0., 1.1, 1., .110))
# plt.legend((p1, p2,p3,p4,p5,p6), ('menu-95', 'yawn-95','menu-99th', 'yawn-99th', 'menu-99.9', 'yawn-99.9'))
# plt.legend((p1, p2), ('On-avg', 'Off-avg'))
plt.savefig('trace.png', format='png', dpi=300, bbox_inches='tight')
plt.show()
