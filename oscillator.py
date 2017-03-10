import pylab as pl
import math as mt
t = pl.linspace(0,2*(mt.pi),100)
z = pl.sin(t)
pl.plot(t,z)
pl.xlim([0,2*mt.pi])
pl.xlabel('$x$',size = 20)
pl.ylabel('$y(x)$',size = 20)
pl.figure()
pl.plot(t,z**2,'2--')
pl.show()