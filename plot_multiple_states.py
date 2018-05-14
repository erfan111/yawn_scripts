## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.interpolate import spline

a = np.genfromtxt(sys.argv[1], delimiter=',')

b = np.genfromtxt(sys.argv[2], delimiter=',')

c = np.genfromtxt(sys.argv[3], delimiter=',')

d = np.genfromtxt(sys.argv[4], delimiter=',')



x = [i[0] for i in a]
on_avg = [i[1] for i in a]
off_avg = [i[1] for i in b]
c6_avg = [i[1] for i in c]
c3_avg = [i[1] for i in d]
on_95 = [i[2] for i in a]
off_95 = [i[2] for i in b]
c6_95 = [i[2] for i in c]
c3_95 = [i[2] for i in d]
on_99 = [i[3] for i in a]
off_99 = [i[3] for i in b]
c6_99 = [i[3] for i in c]
c3_99 = [i[3] for i in d]
on_999 = [i[4] for i in a]
off_999 = [i[4] for i in b]
c6_999 = [i[4] for i in c]
c3_999 = [i[4] for i in d]

plt.ylabel('Latency (us)')
plt.title('Request Latency of different loads 99th')
ind = range(50000,300000,10000)
plt.xticks(ind, rotation='vertical')

#plt.yticks(np.arange(12000, 13000, 100))
plt.grid()
#p1,p2,p3,p4,p5,p6 = plt.plot(x, on_avg, 'r', x, off_avg, 'r:', x, on_99, 'b',x, off_99, 'b:', x, on_999, 'g', x, off_999, 'g:')
#p1,p2 = plt.plot(x, on_999, 'g', x, off_999, 'g:')

xnew = np.linspace(min(x),max(x),10) #300 represents number of points to make between T.min and T.max

smooth_on_avg = spline(x,on_avg,xnew)
smooth_c6_avg = spline(x,c6_avg,xnew)
smooth_c3_avg = spline(x,c3_avg,xnew)
smooth_off_avg = spline(x,off_avg,xnew)


p1,p2, p3, p4 = plt.plot(x, on_999, x, c6_999, x, c3_999, x, off_999)
#p1,p2, p3, p4 = plt.plot(x, on_99, x, c6_99, x, c3_99, x, off_99)
#p1,p2, p3, p4 = plt.plot(x, on_95, x, c6_95, x, c3_95, x, off_95)
#p1,p2, p3, p4 = plt.plot(xnew, smooth_on_avg, xnew, smooth_c6_avg, xnew, smooth_c3_avg, xnew, smooth_off_avg)


#plt.legend((p1, p2,p3,p4,p5,p6), ('On-Avg', 'Off-Avg' ,'On-99th', 'Off-99th', 'On-99.9', 'Off-99.9'))
#plt.legend((p1, p2), ('On-999', 'Off-999'))
plt.legend((p1, p2, p3, p4), ('On', 'C6-off', 'C6&C3-off', 'All Off'))

plt.show()
