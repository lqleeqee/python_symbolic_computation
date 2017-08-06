#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-06 21:59:01
from __future__ import division
from sympy import *
x,y,z = symbols('x,y,z')
k,m,n = symbols('k,m,n',integer=True)
f,g,h = map(Function,'fgh')

# Derivative表示导函数的类，第一个参数是需要进行求导的数学函数，
# 第二个参数是求导的自变量。Derivative得到的是一个导函数，不进行求导运算。
# 如果需要计算出导函数，可以调用doit()方法
t = Derivative(sin(x),x)
print(t)#Derivative(sin(x), x)
t = t.doit()
print(t)#cos(x)
#也可以使用diff()函数或表达式的diff()方法来计算导函数
t = diff(sin(2*x),x)
print(t)#2*cos(2*x)
t = sin(2*x).diff(x)
print(t)#2*cos(2*x)

#使用Derivative对象可以自定义数学函数的导函数
t = Derivative(f(x),x)
print(t)#Derivative(f(x), x)
#由于不知道自定义函数求导法则，因此使用diff方法也不会进行具体计算。
t = f(x).diff(x)
print(t)#Derivative(f(x), x)

#Derivative添加更多符号可以表示高阶导数
t = Derivative(f(x),x,x,x)
print(t)#Derivative(f(x), x, x, x)
t = Derivative(f(x),x,3)
print(t)#Derivative(f(x), x, x, x)

#也可以表示多个变量的导函数
t = Derivative(f(x,y),x,2,y,3)
print(t)#Derivative(f(x, y), x, x, y, y, y)

# diff()和Derivative相同。
# 对sin(x,y),x求两次导，对y求三次导
t = diff(sin(x*y),x,2,y,3)
print(t)#x*(x**2*y**2*cos(x*y) + 6*x*y*sin(x*y) - 6*cos(x*y))

