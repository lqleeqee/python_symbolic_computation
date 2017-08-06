#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-06 21:48:13
from __future__ import division
from sympy import *
x,y,z = symbols('x,y,z')
k,m,n = symbols('k,m,n',integer=True)
f,g,h = map(Function,'fgh')

a,b,c=symbols('a,b,c')
t = solve(a*x**2+b*x+c,x)
print(t)#[(-b + sqrt(-4*a*c + b**2))/(2*a), -(b + sqrt(-4*a*c + b**2))/(2*a)]

t = solve((x**2+x*y+1,y**2+x*y+2),x,y)
print(t)#[(-sqrt(3)*I/3, -2*sqrt(3)*I/3), (sqrt(3)*I/3, 2*sqrt(3)*I/3)]

# 在sympy中，表达式可以直接表示值为0的方程。也可以使用Eq()创建方程。
# solve()可以对方程进行符号求解，第一个参数是方程(组)的表达式，其后的参数为要求解的未知变量的符号。