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
    ylabels = [ '0th second','' ,'' ,'' ,'10th second','','','','20th second','','','','30th second','','','','40th second','','','','160th second','','','']
    data = [
    [0,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],
    [0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
    [-5,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],
 [3,0,0,0,0,0,0,0,0,0],
[3,0,0,0,0,0,0,0,0,0],
[3,0,0,0,0,0,0,0,0,0],
[np.nan,0,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],
 [3,0,0,0,0,0,0,0,0,0],
[3,0,0,0,0,0,0,0,0,0],
[3,0,0,0,0,0,0,0,0,0],


[np.nan,-5,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],
 [3,3,0,0,0,0,0,0,0,0],
[3,3,0,0,0,0,0,0,0,0],
[3,3,0,0,0,0,0,0,0,0],



[np.nan,np.nan,0,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],
 [3,3,0,0,0,0,0,0,0,0],
[3,3,0,0,0,0,0,0,0,0],
[3,3,0,0,0,0,0,0,0,0],


[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,-5],
 [3,3,3,3,3,3,3,3,3,3],
 [3,3,3,3,3,3,3,3,3,3],
 [3,3,3,3,3,3,3,3,3,3],
    ]

    texts = [
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,1,3,3,3,3,3]
    ]
    my_cmap2=custom_div_cmap(numcolors=21, mincol='#240caf', maxcol='#f14040', midcol='#3ff075')
    my_cmap2.set_bad((1, 1, 1, 1))
    cax = ax.imshow(data, interpolation='none', cmap=my_cmap2)
    ax.set_xticks(np.arange(-.5, len(xlabels), 1))
    ax.set_yticks(np.arange(.5, len(ylabels), 1))
    ax.set_xticklabels(np.arange(1, len(xlabels)+1, 1), horizontalalignment='left')
    ax.set_yticklabels(ylabels, verticalalignment='bottom')
    ax.yaxis.labelpad = 60
    for i in range(len(ylabels)):
        for j in range(len(xlabels)):
            text = ax.text(j, i, texts[i][j],
                       ha="center", va="center", color="k", size="smaller")
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
