#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:35:52 2017

@author: Creative
"""

import numpy as np
a = 1
b = 1
c = 10**(-10)

# the are regular roots
x1 = (-b+np.sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-np.sqrt(b**2-4*a*c))/(2*a)

#this are prime roots i.e (x'=1/x)
y1 = (-2*c)/(b+np.sqrt(b**2-4*a*c))
y2 = (-2*c)/(b-np.sqrt(b**2-4*a*c))

print(x1)
print(x2)
print(y1)
print(y2)