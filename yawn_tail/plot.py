## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.signal import lfilter
from scipy.interpolate import spline



font = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 14}
font_label = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 13}

plt.rc('font', **font)
plt.rc('legend', fontsize=11)
axs = plt.gca()
latency_off_file = np.genfromtxt(sys.argv[1], delimiter=',')
latency_menu_file = np.genfromtxt(sys.argv[2], delimiter=',')
latency_yawn_file = np.genfromtxt(sys.argv[3], delimiter=',')

x = [i[0]/1000 for i in latency_off_file]
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

xnew = np.linspace(min(x),max(x),300)

n = 3  # the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 1
off_99_smooth = lfilter(b,a,off_99)
menu_99_smooth = lfilter(b,a,menu_99)
yawn_99_smooth = lfilter(b,a,yawn_99)
off_99_smooth2 = spline(x,off_99_smooth,xnew)
menu_99_smooth2 = spline(x,menu_99_smooth,xnew)
yawn_99_smooth2 = spline(x,yawn_99_smooth,xnew)

plt.ylabel('99th Latency Percentile (us)')
plt.xlabel("Request Rate (x" + r'$10^3$' + " RPS)",**font_label)# ax1.set_xlabel("Min")
# plt.xticks(ind, ('20%', '30%', '40%', '50%'))
plt.yticks(np.arange(50, 300, 50))
# plt.ytick_labels(np.arange(50, 300, 10))
plt.grid('on', axis="x")
p1,p2,p3 = plt.plot(xnew, menu_99_smooth2, 'r', xnew, off_99_smooth2, 'b:', xnew, yawn_99_smooth2, 'g--', linewidth=3)
# p1,p2 = plt.plot(x, on_avg, 'g', x, off_avg, 'g:')
axs.set_xlim(6,100)
axs.set_ylim(50,250)
plt.legend((p1, p2, p3), ('Menu', 'C-states Disabled','Yawn', 'yawn-99th'))
# plt.legend((p1, p2), ('On-avg', 'Off-avg'))
plt.savefig('yawn_latency.png', format='png', dpi=300, bbox_inches='tight')
plt.show()
