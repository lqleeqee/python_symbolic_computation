#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-03 11:26:22

from __future__ import division
from sympy import *
x,y,z = symbols('x,y,z')
k,m,n = symbols('k,m,n',integer=True)
f,g,h = map(Function,'fgh')

def print_expression(e,level=0):
	space = "    "*level
	if isinstance(e,(Symbol,Number)):
		print(space+str(e))
		return
	if len(e.args)>0:
		print(space+e.func.__name__)
		for arg in e.args:
			print_expression(arg,level+1)
	else:
		print(space+e.func.__name__)

if __name__ == '__main__':
	print_expression(sqrt(x**2+y**2))

	f = Function('f')
	t = f(x,y)
	print(t+t**2)