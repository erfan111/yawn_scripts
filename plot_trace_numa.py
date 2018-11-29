## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt
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

convertfunc = lambda x: float(x[0:-2])

latency_off_file = np.genfromtxt(sys.argv[1], delimiter=',')
latency_menu_file = np.genfromtxt(sys.argv[2], delimiter=',')
latency_yawn_file = np.genfromtxt(sys.argv[3], delimiter=',')
power_off_file = np.genfromtxt(sys.argv[4], delimiter=',', converters={0: convertfunc})
power_menu_file = np.genfromtxt(sys.argv[5], delimiter=',', converters={0: convertfunc})
power_yawn_file = np.genfromtxt(sys.argv[6], delimiter=',', converters={0: convertfunc})

power_off = []
power_menu = []
power_yawn = []
for i in range(0, len(power_off_file), 2):
	sum1 = int(power_off_file[i])
	sum1+= int(power_off_file[i+1])
	power_off.append(sum1)
for i in range(0, len(power_menu_file), 2):
	sum1 = int(power_menu_file[i])
	sum1+= int(power_menu_file[i+1])
	power_menu.append(sum1)
for i in range(0, len(power_yawn_file), 2):
	sum1 = int(power_yawn_file[i])
	sum1+= int(power_yawn_file[i+1])
	power_yawn.append(sum1)

power_off_file = power_off
power_menu_file = power_menu
power_yawn_file = power_yawn

x = [i[0] for i in latency_menu_file]
off_avg = [i[1] for i in latency_off_file]
menu_avg = [i[1] for i in latency_menu_file]
off_95 = [i[2] for i in latency_off_file]
menu_95 = [i[2] for i in latency_menu_file]
yawn_95 = [i[2] for i in latency_yawn_file]
off_99 = [i[3] for i in latency_off_file]
menu_99 = [i[3] for i in latency_menu_file]
yawn_99 = [i[3] for i in latency_yawn_file]
off_999 = [i[4] for i in latency_off_file]
menu_999 = [i[4] for i in latency_menu_file]
yawn_999 = [i[4] for i in latency_yawn_file]


fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1,figsize=(14,11))

for i in range(len(x)):
    x[i] /= 1000
x1 = np.arange(1,91,1)
xnew = np.linspace(x1.min(),x1.max(),300)
power_smooth = spline(x1,x,xnew)


ax1.set_ylabel("Request Rate\n (x" + r'$10^3$' + " RPS)", labelpad=15,**font_label)# ax1.set_xlabel("Min")
ax1.grid()
# ax1.set_xticks(np.arange(0,91,10))
ax1.set_xticklabels([])
ax1.set_yticks(np.arange(0,80,10))
ax1.set_yticklabels(np.arange(0,80,10))
ax1.set_xlim(1,90)
p1 = ax1.plot(xnew, power_smooth, 'C1', linewidth=3)

n = 4  # the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 1
off_99_smooth = lfilter(b,a,off_99)
menu_99_smooth = lfilter(b,a,menu_99)
yawn_99_smooth = lfilter(b,a,yawn_99)
off_99_smooth2 = spline(x1,off_99_smooth,xnew)
menu_99_smooth2 = spline(x1,menu_99_smooth,xnew)
yawn_99_smooth2 = spline(x1,yawn_99_smooth,xnew)

p2 ,p3, p4 = ax2.plot(xnew, off_99_smooth2,'b:', xnew, menu_99_smooth2, 'r', xnew, yawn_99_smooth2, 'g--', linewidth=3)
ax2.set_ylabel(r'$99^{th}$' + 'Latency (us)')
# ax2.set_xlabel('Min')
ax2.grid()
# ax2.set_xticks(np.arange(0,91,10))
ax2.set_xticklabels([])
# ax2.set_yticks(np.arange(80,200,20))
# ax2.set_xticklabels(np.arange(0,91,10))
ax2.set_xlim(1,90)

n = 4  # the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 1
off_999_smooth = lfilter(b,a,off_999)
menu_999_smooth = lfilter(b,a,menu_999)
yawn_999_smooth = lfilter(b,a,yawn_999)
off_999_smooth2 = spline(x1,off_999_smooth,xnew)
menu_999_smooth2 = spline(x1,menu_999_smooth,xnew)
yawn_999_smooth2 = spline(x1,yawn_999_smooth,xnew)

# plt.plot(x, yy, linewidth=2, linestyle="-", c="b")  # smooth by filter

p8 ,p9, p10 = ax3.plot(xnew, off_999_smooth2,'b:', xnew, menu_999_smooth2, 'r', xnew, yawn_999_smooth2, 'g--', linewidth=3)
ax3.set_ylabel(r'$99.9^{th}$' + 'Latency (us)', labelpad=25)
# ax2.set_xlabel('Min')
ax3.grid()
# ax2.set_xticks(np.arange(0,91,10))
ax3.set_xticklabels([])
# ax3.set_yticks(np.arange(80,200,20))
# ax2.set_xticklabels(np.arange(0,91,10))
ax3.set_xlim(1,90)


step2 = 90/(len(power_off_file))
step3 = 90/(len(power_menu_file))
step4 = 90/(len(power_yawn_file))
x2 = np.arange(1, 91, step2)
x3 = np.arange(1, 91, step3)
x4 = np.arange(1, 91, step4)

off_power_smooth = lfilter(b,a,power_off_file)
menu_power_smooth = lfilter(b,a,power_menu_file)
yawn_power_smooth = lfilter(b,a,power_yawn_file)

p5, p6, p7 = ax4.plot(x2, off_power_smooth, 'b:', x3, menu_power_smooth, 'r', x4, yawn_power_smooth, 'g--', linewidth=3)
ax4.set_ylabel('Power (Watt)')
ax4.set_xlabel('Time (min)')
ax4.grid()
tick = [0,10,20,30,40,50,60,70,80,90]
ax4.set_xticks(np.arange(1,101,10))
ax4.set_xticklabels(tick)
ax4.set_xlim(2,91)
ax4.set_ylim(30,150)
# ax2.title('Request Latency of different loads')
# plt.xticks(ind, ('20%', '30%', '40%', '50%'))
# plt.yticks(np.arange(0, 800, 10))
ax1.legend((p2, p3, p4), ('C-states Disabled','Menu', 'Yawn'), loc='center',
           ncol=3,bbox_to_anchor=(0., 1.1, 1., .110))
# plt.legend((p1, p2,p3,p4,p5,p6), ('menu-95', 'yawn-95','menu-99th', 'yawn-99th', 'menu-99.9', 'yawn-99.9'))
# plt.legend((p1, p2), ('On-avg', 'Off-avg'))
plt.savefig('trace.png', format='png', dpi=300, bbox_inches='tight')
plt.show()
