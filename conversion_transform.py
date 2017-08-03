#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-03 15:58:22
from __future__ import division
from sympy import *
x,y,z = symbols('x,y,z')
k,m,n = symbols('k,m,n',integer=True)
f,g,h = map(Function,'fgh')

#simplify可以对数学表达式进行简化
t  = simplify((x+2)**2-(x+1)**2)
#2*x + 3
print(t)

#radsimp()对表达式的分母进行有理化
t = radsimp(1/(sqrt(5)+2*sqrt(2)))
#(-sqrt(5) + 2*sqrt(2))/3
print(t)

#(-sqrt(x)*y + x*sqrt(y))/(x*y*(x - y))
t = radsimp(1/(y*sqrt(x)+x*sqrt(y)))
print(t)

#ratsimp()对表达式中的分母进行通分
#2*y**2/(x**2 - y**2) + 1
t = ratsimp(x/(x+y)+y/(x-y))
#转为分子除以分母的形式？？？
print(t)

#fraction()返回表达式的分子与分母的元组
#(x + y, x*y)
t = fraction(ratsimp(1/x+1/y))
#fraction()不会对表达式进行通分
print(t)

#cancel()和 factor()对分式表达式的分子分母进行约分运算，去除公因式
t = cancel((x**2-1)/(x+1)) # x-1
print(t)

t = cancel(sin((x**2-1)/(x+1))) #sin(x**2/(x + 1) - 1/(x + 1))
print(t)

t = factor(sin(cancel((x**2-1)/(x+1)))) #sin(x - 1)
print(t)

t = factor(sin(factor((x**2-1)/(x+1)))) #sin(x - 1)
print(t)

t = cancel((f(x)**2-1)/(f(x)+1)) #f(x) - 1
print(t)

t = factor((f(x)**2-1)/(f(x)+1)) #f(x) - 1
print(t)

