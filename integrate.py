#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-07 20:57:33
from __future__ import division
from sympy import *
x,y,z = symbols('x,y,z')
k,m,n = symbols('k,m,n',integer=True)
f,g,h = map(Function,'fgh')

# integrate() 可以计算定积分和不定积分
# integrate(f,x) 计算不定积分
# integrate(f,(x,a,b)) 计算不定积分

# 如果要计算多重积分，则将积分的变量依次列出
# integrate(f,x,y)
# integrate(f,(x,a,b),(y,c,d))

# 和Derivative 对象表示微分表达式类似，Integral对象表示积分表达式，

e = Integral(x*sin(x),x)
print(e)#Integral(x*sin(x), x)
t = e.doit()
print(t)#-x*cos(x) + sin(x)

#有些积分表达式无法通过符号化简，这时可以调用 evalf() 方法或者调用求职函数 N() 对其进行数值运算。
e = Integral(sin(x)/x,(x,0,1))
print(e)#Integral(sin(x)/x, (x, 0, 1))
print(e.doit())#Si(1)

print(e.evalf())#0.946083070367183
print(N(e))#0.946083070367183
print(N(e,100))#指定精度
#0.9460830703671830149413533138231796578123379547381117904714547735666870365407979180887021330817407112

t = N(Integral(sin(x)/x,(x,0,oo)))
print(t) #-0.e+0
#oo表示无穷大
#没有计算出正确结果pi/2。
t = N(Integral(sin(x)/x,(x,0,10000)))
print(t) #0.e+0
t = N(Integral(sin(x)/x,(x,0,1000)))
print(t) #1.57023312196877

#as_sum()方法可以将定积分准换为近似求和公式，它将积分面积区域分割为n个小矩形的面积之和。
t = Integral(sin(x),(x,0,1)).as_sum(5)
print(t)#sin(1/10)/5 + sin(3/10)/5 + sin(1/2)/5 + sin(7/10)/5 + sin(9/10)/5