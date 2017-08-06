#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-06 23:23:15
from __future__ import division
from sympy import *
x,y,z = symbols('x,y,z')
k,m,n = symbols('k,m,n',integer=True)
f,g,h = map(Function,'fgh')

f = Function('f')
# dsolve()可以对微分方程进行符号求解，
# 第一个参数是一个带未知函数的表达式
# 第二个参数是需要求解的未知函数
t = dsolve(Derivative(f(x),x)-f(x),f(x))
print(t)#Eq(f(x), C1*exp(x))

x = symbols('x',real=True)
eq_0 = dsolve(f(x).diff(x)+f(x)**2+f(x),f(x))
print(eq_0)#Eq(f(x), -C1/(C1 - exp(x)))

# hint参数指定微分方程的解法。默认为default，由sympy自动挑选解法。
# "best",让 dsolve()尝试所有的解法，并返回最简单的解。
eq_1 = dsolve(f(x).diff(x)+f(x)**2+f(x),f(x),hint="best")
print(eq_1)#Eq(f(x), 1/(C1*exp(x) - 1))


#eq_0,eq_1是表示等式的Equality对象，等号左右两边的表达式可以通过lhs和rhs属性获取。
print(eq_0.func) #<class 'sympy.core.relational.Equality'>
print(eq_0.lhs) #f(x)
print(eq_0.rhs) #-C1/(C1 - exp(x))

print(eq_1.func) #<class 'sympy.core.relational.Equality'>
print(eq_1.lhs) #f(x)
print(eq_1.rhs) #-C1/(C1 - exp(x))


#为了验证eq_0,eq_1两个等式是完全等价的，只需将 eq_1带入eq_0中进行简化即可。
t = simplify(eq_0.lhs.subs(f(x),eq_1.rhs))
print(t)

print(eq_1 == eq_0) #True