#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 09:02:55 2017

@author: Creative
"""

import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 5,5


plt.figure()
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)

xv,yv =  np.meshgrid(x,y)
z = -np.log(np.sqrt((xv**2+yv**2)))  

cuvers = plt.contour(xv,yv,z,6)
plt.colorbar() #it show barside in which color is mentioned
plt.xlabel('$x$',fontsize=20)
plt.ylabel('$y$',fontsize=20)
plt.axes().set_aspect('equal')
plt.tight_layout()
plt.savefig('concentrc.pdf')
plt.show()