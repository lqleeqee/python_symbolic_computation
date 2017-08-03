#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-03 09:47:01
from __future__ import division
from sympy import *
x,y,z = symbols('x,y,z')
k,m,n = symbols('k,m,n',integer=True)
f,g,h = map(Function,'fgh')

#验证欧拉公式e**(i*pi)+1=0
#打印欧拉公式：E**(I*pi)+1=0
print('E**(I*pi)+1={0}'.format(E**(I*pi)+1))
#展开欧拉公式（没有成功）
#expand(E**(I*x))=exp(I*x)
print('expand(E**(I*x))={0}'.format(expand(E**(I*x))))

#当expand的complex参数为True时，欧拉公式被展开为实数和虚数两个部分
#expand(E**(I*x),complex=True)=I*exp(-im(x))*sin(re(x)) + exp(-im(x))*cos(re(x))
print('expand(E**(I*x),complex=True)={0}'.format(expand(E**(I*x),complex=True)))

#重新定义x为实数
x=Symbol('x',real=True)
#expand(E**(I*x),complex=True)=I*sin(x) + cos(x)
print('expand(E**(I*x),complex=True)={0}'.format(expand(E**(I*x),complex=True)))

#对e**（i*x）泰勒展开
#taylor expansion of exp(I*x)
#=1 + I*x - x**2/2 - I*x**3/6 + x**4/24 + I*x**5/120 - x**6/720 - I*x**7/5040 + x**8/40320 + I*x**9/362880 + O(x**10)
tmp = series(exp(I*x),x,0,10)
print('taylor expansion of exp(I*x)={0}'.format(tmp))

#取e**(i*x)泰勒展开的实部
#real part of exp(I*x)=x**8/40320 - x**6/720 + x**4/24 - x**2/2 + re(O(x**10)) + 1
print('real part of exp(I*x)={0}'.format(re(tmp)))

#对cos(x)泰勒展开
#taylor expansion of cos(x)=1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320 + O(x**10)
print('taylor expansion of cos(x)={0}'.format(series(cos(x),x,0,10)))

#取e**(i*x)泰勒展开的虚部
#imaginary part of exp(I*x)=x**9/362880 - x**7/5040 + x**5/120 - x**3/6 + x + im(O(x**10))
print('imaginary part of exp(I*x)={0}'.format(im(tmp)))
#对sin(x)泰勒展开
#taylor expansion of sin(x)=x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880 + O(x**10)
print('taylor expansion of sin(x)={0}'.format(series(sin(x),x,0,10)))

co = series(cos(x),x,0,10)
rea = re(tmp)-re(O(x**10))+O(x**10)
print('real:re(series(exp(I*x),x,0,10))=series(cos(x),x,0,10))?\n{0}'.format(co==rea))

si = series(sin(x),x,0,10)
img = im(tmp)-im(O(x**10))+O(x**10)
print('imag:im(series(exp(I*x),x,0,10))=series(sin(x),x,0,10))?\n{0}'.format(si==img))