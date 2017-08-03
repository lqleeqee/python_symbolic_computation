#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-03 11:12:38
from __future__ import division
from sympy import *
x,y,z = symbols('x,y,z')
k,m,n = symbols('k,m,n',integer=True)
f,g,h = map(Function,'fgh')

#浮点数:1.6666...
t = 1/2 +2/3
print(t)

#SymPy的数值对象:7/6
t = S(1)/2+2/S(3)
#SymPy提供了一个S对象用于转换Python数值类型为SymPy数值类型
print(t)

#Rational对象，------有理数，会自动进行约分处理
t = Rational(3,9) #1/3
print(t)

#N()函数用于查看浮点数的实际数值。实数用real对象表示，和标准的浮点数类似，但是它的精度（有效数字）
#可以通过参数指定，浮点数和real对象内部都使用二进制方式表示数值，因此没法精确表示十进制中的精确小数。
t = N(0.1,60)
print(t)
t = N(1000.1,60)
print(t)