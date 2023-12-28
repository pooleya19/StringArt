# Imports
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap
import numpy as np

def PreviewImage(image, figsize=(3,3), cmap=None, plot=True, plotCB=True):
    colors = np.array([[0.5, 0.5, 0.5, 1],
                       [1, 1, 1, 1],
                       [0, 0, 0, 1]])
    colormap = ListedColormap(colors)

    if cmap is None:
        cmap=colormap

    prevInt = plt.isinteractive()
    plt.ioff()
    plt.figure(figsize=figsize)
    plt.imshow(image, cmap=cmap, extent=[-1, 1, -1, 1])
    if plotCB:
        plt.colorbar()
    plt.axis('off')
    if prevInt:
        plt.ion()

    if plot:
        plt.show()
    else:
        gcf = plt.gcf()
        return gcf