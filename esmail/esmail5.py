## usage: python3 plot.py on.csv off.csv

import numpy as np
import sys
import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-l','--latency', type=int, help='latency files', default=0)
parser.add_argument('-u','--utilization', type=int, help='util files', default=0)
parser.add_argument('files', metavar='F', nargs='+',
                    help='files for the plot')

args = parser.parse_args()
if(len(args.files) != args.utilization + args.latency):
    print("number of input files doesn't equal the numbers you provided")
    sys.exit(1)
print(args)
###############################################################
master_file_index = 0
latency_matrix = []
latency_min_length = sys.maxsize
for i in range(args.latency):
    a = list(np.genfromtxt(args.files[master_file_index], delimiter=','))
    latency_matrix.append(a)
    master_file_index+=1
for i in range(len(latency_matrix)):
    if(len(latency_matrix[i]) < latency_min_length):
        latency_min_length = len(latency_matrix[i])
for i in range(len(latency_matrix)):
    while(len(latency_matrix[i]) > latency_min_length):
    	latency_matrix[i].pop()

util_matrix = []
min_length = sys.maxsize
umi = 0
for i in range(args.utilization):
    temp_np = list(np.genfromtxt(args.files[master_file_index], delimiter=','))
    if master_file_index == args.latency:
        min_length = len(temp_np)
    while(len(temp_np) > min_length):
    	temp_np.pop()
    temp_list = []
    if master_file_index == args.latency:
        for i in temp_np:
            temp_list.append(i/1000000)
    else:
        index = 0
        for i in temp_np:
            temp_list.append((i/1000000)+util_matrix[umi-1][index])
            index+=1
    util_matrix.append(temp_list)
    master_file_index+=1
    umi+=1

x = range(1)
if args.utilization != 0:
    x2 = list(range(len(util_matrix[0])))
colors=['red', 'blue','green','gray']
latency_colors=['r', 'b','m','y']
fig, ax1 = plt.subplots()
legend_elements = []
if args.latency != 0:
    x = range(len(latency_matrix[0]))
    if args.utilization != 0:
        prev = 0
        step = (len(latency_matrix[0])//len(util_matrix[0]))
        for i in range(len(x2)):
            x2[i] = prev + step
            prev = x2[i]
        x2[0] = -150
        x2[-1] = x[-1]+500
        plot_latency = []
        for i in range(len(latency_matrix)):
            plot_latency.append(ax1.plot(x, latency_matrix[i], latency_colors[i] + 'o', zorder=10))
            legend_elements.append(Line2D([0], [0], marker='o', color=latency_colors[i], label=args.files[i],
                   markerfacecolor=latency_colors[i], markersize=8, linestyle='none'))
        plt.ylabel('Latency (us)')
        ax1.tick_params(axis='y', labelcolor='tab:red')
        ax1.set_ylabel('Latency (us)', color='tab:red')
        ax1.set_xlabel('time')
        plt.xticks([])
        plt.grid()
        ax2 = ax1.twinx()
        ax2.set_ylabel('Utilization', color='tab:blue')
        ax2.tick_params(axis='y', labelcolor='tab:blue')
        print("len util mat", len(util_matrix), util_matrix)
        # p5= ax2.plot(x2, util_matrix[-1], 'b')
        d = np.zeros(len(x2))
        ax2.fill_between(x2,util_matrix[0], where=util_matrix[0] > d, alpha=0.2, color='yellow', zorder=2)
        legend_elements.append(Line2D([0], [0], color='yellow', lw=8, alpha=0.2, label=args.files[args.latency]))
        for i in range(1,len(util_matrix)):
            ax2.fill_between(x2,util_matrix[i], util_matrix[i-1], alpha=0.2, color=colors[i-1], zorder=2)
            legend_elements.append(Line2D([0], [0], color=colors[i-1], lw=8, alpha=0.2, label=args.files[args.latency+i]))
        ax2.set_yticks(np.arange(0, 101, 10))
    else:
        ax1.set_xlabel('time')
        plt.xticks([])
        axes = plt.gca()
        axes.set_ylim([0,400])      # EEERRFFAAANNNN
        plt.grid()
        ax1.set_ylabel('Latency (us)', color='tab:red')
        ax1.tick_params(axis='y', labelcolor='tab:red')
        plot_latency = []
        for i in range(len(latency_matrix)):
            plot_latency.append(ax1.plot(x, latency_matrix[i], latency_colors[i], zorder=10))
            legend_elements.append(Line2D([0], [0], marker='o', color=latency_colors[i], label=args.files[i],
                   markerfacecolor=latency_colors[i], markersize=8, linestyle='none'))
        plt.legend(["fvreg", "ergettg", "rfgregrt", "fgrtgrtet"])   # LEGEND ITEMS
else:
    ax1.set_xlabel('time')
    plt.xticks([])
    plt.grid()
    ax1.set_ylabel('Utilization', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    print("len util mat", len(util_matrix), util_matrix)
    # p5= ax1.plot(x2, util_matrix[-1], 'b')
    d = np.zeros(len(x2))
    ax1.fill_between(x2,util_matrix[0], where=util_matrix[0] > d, alpha=0.2, color='yellow', zorder=2)
    legend_elements.append(Line2D([0], [0], color='yellow', lw=8, alpha=0.2, label=args.files[0]))
    for i in range(1,len(util_matrix)):
        ax1.fill_between(x2,util_matrix[i], util_matrix[i-1], alpha=0.2, color=colors[i-1], zorder=2)
        legend_elements.append(Line2D([0], [0], color=colors[i-1], lw=8, alpha=0.2, label=args.files[i]))

fig, ax = plt.subplots(figsize=(10,0.4))
ax.legend(handles=legend_elements, loc=3, ncol=4, mode="expand", borderaxespad=0.)
ax.axis('off')
fig.savefig('legend.png', format='png', dpi=300)
#plt.savefig('LatencyAlongside.png', format='png', dpi=300)

plt.show()
