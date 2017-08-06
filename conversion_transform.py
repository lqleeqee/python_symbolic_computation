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

#因式分解
t = factor(sin(cancel((x**2-1)/(x+1)))) #sin(x - 1)
print(t)
#因式分解
t = factor(sin(factor((x**2-1)/(x+1)))) #sin(x - 1)
print(t)

t = cancel((f(x)**2-1)/(f(x)+1)) #f(x) - 1
print(t)

t = factor((f(x)**2-1)/(f(x)+1)) #f(x) - 1
print(t)

#trigsimp()对表达式中的三角函数进行简化
#sin(2*x) + 1
t = trigsimp(sin(x)**2+2*sin(x)*cos(x)+cos(x)**2)
print(t)
#f(sin(2*x) + 1),默认对嵌套的表达式进行简化
t = trigsimp(f(sin(x)**2+2*sin(x)*cos(x)+cos(x)**2))
print(t)
#deep属性不影响，皆对嵌套的表达式进行简化
t = trigsimp(f(sin(x)**2+2*sin(x)*cos(x)+cos(x)**2),deep=True)
print(t)


#expand_trig()对三角函数的表达式进行简化
#(2*cos(x)**2 - 1)*sin(y) + 2*sin(x)*cos(x)*cos(y)
t =expand_trig(sin(2*x+y))
print(t)


#expand()对表达式进行展开
#默认
#mul=True,展开乘法
#log=True 展开对数函数参数中的乘积和幂运算
#multinomial = True 展开加法式的整数次幂
#power_base =True 展开幂函数的底数乘积
#power_exp = True 展开幂函数的指数和
#可以将默认为True的标志参数设置为False，强制不展开对应的表达式
#默认
# complex=False 不展开复数的实部和虚部
# func = False 对一些特殊函数不进行展开
# trig=False 默认不展开三角函数
#expand_trig(),expand_log(),expand_mul(),expand_complex(),expand_func()等函数则是通过设置相应的标志，对expend()进行封装。

t = expand(x*(y+z)) #默认mul=True,展开乘法，x*y + x*z
print(t)

x,y = symbols('x,y',positive=True)
#log=True 展开对数函数参数中的乘积和幂运算
t = expand(log(x*y**2)) #log(x) + 2*log(y)
print(t)

#multinomial = True 展开加法式的整数次幂
t=expand((x+y)**3) #x**3 + 3*x**2*y + 3*x*y**2 + y**3
print(t)

#power_base =True 展开幂函数的底数乘积
t = expand((x*y)**z) #x**z*y**z
print(t)

#power_exp = True 展开幂函数的指数和
t = expand(x**(z+y)) #x**y*x**z
print(t)

x,y,z = symbols('x,y,z',positive=True)
#通过设置mul=False,对乘法不进行展开。
t = expand(x*log(y*z),mul=False) #x*(log(y) + log(z))
print(t)

x,y=symbols('x,y',complex=True)
# complex=False 默认不展开复数的实部和虚部
t = expand(x*y,complex=True)
print(t) #re(x)*re(y) + I*re(x)*im(y) + I*re(y)*im(x) - im(x)*im(y)

# func = False 默认对一些特殊函数不进行展开
t=expand(gamma(1+x),func=True)
print(t) #x*gamma(x)


# trig=False 默认不展开三角函数
t=expand(sin(x+y),trig=True)
print(t)#sin(x)*cos(y) + sin(y)*cos(x)

#factor()可对多项式表达式进行因式分解
t = factor(15*x**2+2*y-3*x-10*x*y)
print(t) #(3*x - 2*y)*(5*x - 1)

t = expand((x+y)**20)
print(t)
t = factor(expand((x+y)**20))
print(t) #(x+y)**20


#collect()收集表达式中指定符号的有理数指数次幂的系数。
a,b=symbols('a,b')
eq = (1+a*x)**3+(1+b*x)**2
eq1=expand(eq)
print(eq1)#a**3*x**3 + 3*a**2*x**2 + 3*a*x + b**2*x**2 + 2*b*x + 2
t=collect(eq1,x)
print(t)#a**3*x**3 + x**2*(3*a**2 + b**2) + x*(3*a + 2*b) + 2
#默认情况下，collect()返回的是一个整理之后的表达式。如果想得到x的各次幂的系数，
#可以设置evaluate参数为False，返回一个以x的幂为键，系数为值的字典。
t = collect(eq1,x,evaluate=False)
print(t)#{x**3: a**3, x**2: 3*a**2 + b**2, x: 3*a + 2*b, 1: 2}
#collect()也可用于收集表达式的各次幂的系数
t = collect(a*sin(2*x)+b*sin(2*x),sin(2*x))
print(t)#(a + b)*sin(2*x)

