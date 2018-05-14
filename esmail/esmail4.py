## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt

a = np.genfromtxt(sys.argv[1], delimiter=',')
# print(a, len(a))
b = np.genfromtxt(sys.argv[2], delimiter=',')
c = []
for i in b:
    c.append(i/1000000)
# print(c, len(c))
e = list(np.genfromtxt(sys.argv[3], delimiter=','))
while(len(e) > len(c)):
	e.pop()
f = []
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

i = list(np.genfromtxt(sys.argv[5], delimiter=','))
while(len(i) > len(h)):
	i.pop()
j = []
index = 0
for ii in i:
    j.append((ii/1000000)+h[index])
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
ax1.set_xlabel('time')
ax1.tick_params(axis='y', labelcolor='tab:red')
plt.ylabel('Latency (us)')
plt.xticks([])
# plt.yticks(np.arange(0, 800, 10))
plt.grid()

ax1.set_ylabel('Latency (us)', color='tab:red')
ax2 = ax1.twinx()
ax2.set_ylabel('Utilization', color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')
# p2= ax2.plot(x2, c, 'b')
# p3= ax2.plot(x2, f, 'b')
# p4= ax2.plot(x2, h, 'g')
p5= ax2.plot(x2, j, 'b')
d = np.zeros(len(x2))
ax2.fill_between(x2,c, where=c > d, alpha=0.2, color='yellow', zorder=2)
ax2.fill_between(x2,f, c, alpha=0.2, color='gray', zorder=2)
ax2.fill_between(x2,h, f, alpha=0.2, color='magenta', zorder=3)
ax2.fill_between(x2,f, j, alpha=0.2, color='blue', zorder=4)
# p2= plt.plot()
#p1,p2 = plt.plot(x, on_999, 'g', x, off_999, 'g:')
ax2.set_yticks(np.arange(0, 101, 10))
plt.legend()
p1= ax1.plot(x, a, 'ro', zorder=10)
#plt.legend((p1, p2), ('On-999', 'Off-999'))
plt.savefig('LatencyAlongside.png', format='png', dpi=300)

plt.show()
