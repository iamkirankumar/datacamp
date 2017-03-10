#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 02:26:25 2017

@author: Creative
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.cm as cm
from pylab import rcParams
rcParams['figure.figsize'] = 5,3

#vector plot 
x = np.linspace(-1,1,10)
y = np.linspace(-1,1,10)

xv,yv = np.meshgrid(x,y)
#meshgrid is 2d grid : (xv,yv) provides the coordinates as the points
#in a mesh of Nx*Ny grid

plt.figure()
plt.quiver(xv,yv,-xv**1,-yv**1)
#quiver = arrow : at the points (xv,yv) make 
#vector of (-xv,-xy)
plt.axes().set_aspect('equal')
"""
plt.xlabel(r'$x$', fontsize=20)
plt.ylabel(r'$y$', fontsize=20)
plt.xticks(np.linspace(-1, 1, 5, endpoint=True))
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

plt.tight_layout()
plt.savefig('vectorplt.png')"""
plt.show()