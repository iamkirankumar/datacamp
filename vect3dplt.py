#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 03:01:40 2017

@author: Creative
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.cm as cm

plt.gca(projection='3d') #gcd = get current axis

x = np.linspace(-10,10,10)
y = np.linspace(-10,10,10)
z = np.linspace(-10,10,10)

xv,yv,zv = np.meshgrid(x,y,z)
# meshgrid is a 3d arrow here : (xv,yv,zv) = coordinates

plt.quiver(xv,yv,zv,-xv,-yv,-zv)
plt.savefig('vect3dfig.pdf')
plt.show()