import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
import numpy as np
from matplotlib import cm
from numpy.random import randn
from matplotlib.colors import LinearSegmentedColormap

def custom_div_cmap(numcolors=11, name='custom_div_cmap',
                    mincol='blue', midcol='white', maxcol='red'):
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list(name=name,
                                             colors =[mincol, midcol, maxcol],
                                             N=numcolors)
    return cmap

def draw():
    fig, ax = plt.subplots()
    xlabels = [1,2,3,4,5,6,7,8,9,10]
    ylabels = [1,2,3,4,'fuck',6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    data = [
    [1,2,3,1,3,-1,-1,0,-3,2],
    [1,1,0,-1,-3,0,0,1,3,-2],
    [1,2,3,1,3,-1,-1,0,-3,2],
    [1,1,0,-1,-3,0,0,1,3,-2],
    [1,2,3,1,3,-1,-1,0,-3,2],
    [1,1,0,-1,-3,0,0,1,3,-2],
    [1,2,3,1,3,-1,-1,0,-3,2],
    [1,1,0,-1,-3,0,0,1,3,-2],
    [1,2,3,1,3,-1,-1,0,-3,2],
    [1,1,0,-1,-3,0,0,1,3,-2],
    [1,2,3,1,3,-1,-1,0,-3,2],
    [1,1,0,-1,-3,0,0,1,3,-2],
    [1,2,3,1,3,-1,-1,0,-3,2],
    [1,1,0,-1,-3,0,0,1,3,-2],
    [1,2,3,1,3,-1,-1,0,-3,2],
    [1,1,0,-1,-3,1,0,1,3,-2],
    [1,2,3,1,3,-1,-1,0,-3,2],
    [1,1,0,-1,-3,1,0,1,3,-2],
    [1,2,3,1,3,-1,-1,0,-3,2],
    [1,1,0,-1,-3,1,0,1,3,-2],
    [1,2,3,1,3,-1,-1,0,-3,2],
    [1,1,0,-1,-3,1,0,1,3,-2],
    [1,2,3,1,3,-1,-1,0,-3,2],
    [1,-3,np.nan,-1,-3,1,0,1,3,-2],
    ]
    my_cmap2=custom_div_cmap(numcolors=21, mincol='#240caf', maxcol='#f14040', midcol='#3ff075')
    my_cmap2.set_bad((1, 1, 1, 1))
    cax = ax.imshow(data, interpolation='none', cmap=my_cmap2)
    ax.set_xticks(np.arange(-.5, len(xlabels), 1))
    ax.set_yticks(np.arange(.5, len(ylabels), 1))
    ax.set_xticklabels(np.arange(1, len(xlabels)+1, 1), horizontalalignment='left')
    ax.set_yticklabels(ylabels, verticalalignment='bottom')
    ax.yaxis.labelpad = 60
    grids = ax.get_ygridlines()
    grids[3].set_color('black')
    grids[3].set_linewidth(2)
    grids[7].set_color('black')
    grids[7].set_linewidth(2)
    grids[11].set_color('black')
    grids[11].set_linewidth(2)
    grids[15].set_color('black')
    grids[15].set_linewidth(2)
    grids[19].set_color('black')
    grids[19].set_linewidth(2)
    cbar = fig.colorbar(cax, orientation='vertical')

draw()
plt.grid(True)
plt.show()
