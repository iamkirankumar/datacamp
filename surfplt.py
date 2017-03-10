#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 03:21:36 2017

@author: Creative
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.cm as cm
from pylab import rcParams
rcParams['figure.figsize'] = 5,5
        
fig = plt.figure()
axes = fig.gca(projection='3d')

x = np.linspace(-1,1,100)
y = np.linspace(-1,1,100)

xv, yv = np.meshgrid(x,y)
z = (xv**2+yv**2)/2
    
p = axes.plot_surface(xv,yv,z,rstride=4,cstride=4,cmap=cm.RdBu,linewidth=0,antialiased=False)
fig.colorbar(p,shrink=0.5)
axes.set_xlabel('$x$',fontsize=15)
axes.set_ylabel('$y$',fontsize=15)
axes.set_zlabel('$z$',fontsize=15)

plt.tight_layout()
plt.savefig('temp.pdf')
plt.show()