#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-09 22:35:31
from __future__ import division
import sympy
from sympy.plotting import plot
from sympy import *
x,y,z = symbols('x,y,z')
k,m,n = symbols('k,m,n',integer=True)
f,g,h = map(Function,'fgh')

import os
os.environ['PYGLET_SHADOW_WINDOW']="0"

p = plot(x/2)
print(type(p))
print(p)

print(p[0])
print(type(p[0]))
print(p)


p.append(plot(x**2)[0])
p.append(plot(log(x))[0])
print(p)

p.append(plot(sin(x),cos(x))[0])
print(p[3])

#p.append(plot(cos(2**x),"mode=polar")[0])
p_1 = plot(cos(2*x))
p._label_axes = True
p.save("sympy_plot2d.png")

