#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 00:52:36 2017

@author: Creative
"""

import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 5,3
#figure of size is 5 inches and 3 inches

x = np.linspace(-1,1,10)
y = x**2
y1 = x**3
plt.plot(x,y,label = r'$y=x^2$')
plt.plot(x,y1, lw = 3, color = 'g', label = r'$y=x^3$')

plt.axhline(0,color='k')
plt.axvline(0,color='g')

plt.xlim(-1,1)
plt.ylim(-1,1)

plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)

plt.legend(loc=4)
plt.savefig('2dplot.pdf')
plt.show()