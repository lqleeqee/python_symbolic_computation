#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-02 20:06:57

from __future__ import division
from sympy import *
x,y,z = symbols('x,y,z')
k,m,n = symbols('k,m,n',integer=True)
f,g,h = map(Function,'fgh')

print('E**(I*pi)+1={0}'.format(E**(I*pi)+1))
print('expand(E**(I*x))={0}'.format(expand(E**(I*x))))
print('expand(E**(I*x),complex=True)={0}'.format(expand(E**(I*x),complex=True)))
x=Symbol('x',real=True)
print('expand(E**(I*x),complex=True)={0}'.format(expand(E**(I*x),complex=True)))

tmp = series(exp(I*x),x,0,10)
print('taylor expansion of exp(I*x)={0}'.format(tmp))

print('real part of exp(I*x)={0}'.format(re(tmp)))
print('taylor expansion of cos(x)={0}'.format(series(cos(x),x,0,10)))



print('imaginary part of exp(I*x)={0}'.format(im(tmp)))
print('taylor expansion of sin(x)={0}'.format(series(sin(x),x,0,10)))


print('integrate(x*sin(x),x)={0}'.format(integrate(x*sin(x),x)))
print('integrate(x*sin(x),(x,0,2*pi))={0}'.format(integrate(x*sin(x),(x,0,2*pi))))

#--------------------------------------------#
print('volume of sphere')
x,y,r = symbols('x,y,r')
r = Symbol('r',positive=True)
circle_area = 2*integrate(sqrt(r*r - x*x),(x,-r,r))
print('cirele area :{0}'.format(circle_area))
circle_area = circle_area.subs(r,sqrt(r*r-x*x))
print('volum of sphere:{0}'.format(integrate(circle_area,(x,-r,r))))