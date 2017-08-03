#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-03 10:19:56
from __future__ import division
from sympy import *
x,y,z = symbols('x,y,z')
k,m,n = symbols('k,m,n',integer=True)
f,g,h = map(Function,'fgh')


print('volume of sphere')
x,y,r = symbols('x,y,r')
r = Symbol('r',positive=True)
#切片法，先求出每个圆‘片’的面积。再对直径积分
circle_area = 2*integrate(sqrt(r*r - x*x),(x,-r,r))
print('cirele area :{0}'.format(circle_area))
#对切片的圆面积中的半径r进行替换，r=(R**2-X**2),X为圆心离球心的距离。
circle_area = circle_area.subs(r,sqrt(r*r-x*x))
#对X进行积分，积分区间为直径[-R,R]
print('volum of sphere:{0}'.format(integrate(circle_area,(x,-r,r))))