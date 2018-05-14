## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt

a = np.genfromtxt(sys.argv[1], delimiter=',')

b = np.genfromtxt(sys.argv[2], delimiter=',')
c = []
for i in b:
    c.append(i/1000000)

e = list(np.genfromtxt(sys.argv[3], delimiter=','))
f = []
while(len(e) > len(c)):
	e.pop()

index = 0
for i in e:
    f.append((i/1000000)+c[index])
    index+=1

g = list(np.genfromtxt(sys.argv[4], delimiter=','))
while(len(g) > len(f)):
	g.pop()
h = []
index = 0
for i in g:
    h.append((i/1000000)+f[index])
    index+=1

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
# ax1.set_axis_off()
ax1.set_xlabel('time')

plt.ylabel('Latency (us)')
# plt.yticks(np.arange(0, 800, 10))

# ax1.set_ylabel('Latency (us)', color='tab:red')
ax1.set_ylabel('Utilization', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')
# p2= ax2.plot(x2, c, 'b')
# p3= ax2.plot(x2, f, 'b')
p4= ax1.plot(x2, h, 'b')
d = np.zeros(len(x2))
ax1.fill_between(x2,c, where=c > d, alpha=0.2, color='yellow', zorder=2)
ax1.fill_between(x2,f, c, alpha=0.2, color='red', zorder=2)
ax1.fill_between(x2,h, f, alpha=0.2, color='blue', zorder=3)
# ax2.fill_between(x2,f, j, alpha=0.2, color='blue', zorder=4)
# p2= plt.plot()
#p1,p2 = plt.plot(x, on_999, 'g', x, off_999, 'g:')
plt.legend()
plt.xticks([])

# p1= ax1.plot(x, a, 'ro', zorder=10)
#plt.legend((p1, p2), ('On-999', 'Off-999'))
plt.grid()
plt.savefig('vmUtils.png', format='png', dpi=300)

plt.show()
