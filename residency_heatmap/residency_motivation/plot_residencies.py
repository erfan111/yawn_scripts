## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt
font = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 22}
font_label = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 22}

xfont_label = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 22}

plt.rc('font', **font)
plt.rc('legend', fontsize=24)
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

fig, ax = plt.subplots(figsize=(6,6))

# # print(b)
# for i in range(4):
#     b[i] = list(zip(*b[i]))
#     print(len(b[i]))
#     y = np.vstack(b[i])
#     print(y)
#     plt.subplot(2,4,i+1)
#     labels = ["BUSY","POLL", "c1", "c1e", "c3", "c6"]
#     plt.stackplot(x[i], y, labels=labels, colors=["b","m","r","y","g","k"])
#     if i==0:
#         plt.ylabel("% residency")
#     plt.legend(prop={'size': 6})
#     plt.xlim(1000,50000)
#     plt.ylim(0,100)
#     plt.title("Core" + str(i))
# for i in range(4,8):
#     b[i] = list(zip(*b[i]))
#     print(len(b[i]))
#     y = np.vstack(b[i])
#     print(y)
#     plt.subplot(2,4,i+1)
#     labels = ["BUSY","POLL", "c1", "c1e", "c3", "c6"]
#     plt.stackplot(x[i], y, labels=labels, colors=["b","m","r","y","g","k"])
#     plt.xlabel("Rate (QPS)")
#     if i ==4:
#         plt.ylabel("% residency")
#     plt.legend(prop={'size': 6})
#     plt.xlim(1000,50000)
#     plt.ylim(0,100)
#     plt.title("Core" + str(i))
xx = 1
b[xx] = list(zip(*b[xx]))
# print(len(b[i]))
y = np.vstack(b[xx])
print(y)
# for i in range(len(x[1])):
#     x[1][i] = x[1][i]/1000
labels = ["BUSY","POLL", "C1", "C1e", "C3", "C6"]
plt.stackplot(x[1], y, labels=labels, colors=["khaki","gold","orange","red","darkred", "black"])
plt.ylabel("% Residency", **font_label)
plt.legend(bbox_to_anchor=(1.50, 1), prop={'size': 22})
plt.xlim(1000,50000)
plt.ylim(0,100)
plt.ticklabel_format(style='sci')
# labels = [item.get_text() for item in ax.get_xticklabels()]
labels = ["","10","20","30","40","50"]
ax.set_xticklabels(labels, **xfont_label)
# print(label)
plt.xlabel("Request Rate (x" + r'$10^3$' + " RPS)", **font_label)
# plt.title("Core" + str(i))
plt.savefig('resid.png', format='png', dpi=300, bbox_inches='tight')
plt.show()


# plt.show()
