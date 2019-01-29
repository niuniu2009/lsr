# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pylab import *

x = np.linspace(-np.pi,np.pi,256,endpoint=True)

c,s = np.cos(x),np.sin(x)

plot(x,c)
plot(x,s)

show()


