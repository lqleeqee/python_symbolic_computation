#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-07 22:36:36
from __future__ import division
from sympy import *
x,y,z = symbols('x,y,z')
k,m,n = symbols('k,m,n',integer=True)
f,g,h = map(Function,'fgh')

#geometry 模块可以创建表示二维几何图形的对象，如直线、三角形、圆等。并计算这些对象的各种信息


A = Point(0,0)#定义二维坐标点
B = Point(5,0)
C = Point(3,2)

t = Triangle(A,B,C)#创建三角形ABC对象

D = t.incenter #获取三角形ABC的内心
#geometry 模块只能对精确数值进行计算。
print(D)#Point2D(5*(3 + sqrt(13))/(2*sqrt(2) + sqrt(13) + 5), 10/(2*sqrt(2) + sqrt(13) + 5))

p = Circle(C,D,B)#创建圆CDB对象

i = Segment(*p.intersection(Line(A,B)))#计算圆p与直线AB的交点
j = Segment(*p.intersection(Line(A,C)))
print('i:{0}'.format(i))
print('j:{0}'.format(j))


length_i = i.length #length属性是一个精确值，非常复杂，计算开销很大。可调用evalf()查看浮点值的近似表示。
length_j = j.length
print('length of i:{0}'.format(length_i))
print('length of j:{0}'.format(length_j))

print('length of i:{0}'.format(length_i.evalf(50)))
print('length of i:{0}'.format(length_i.evalf(50)))



