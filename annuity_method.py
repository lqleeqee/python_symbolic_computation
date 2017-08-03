#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-02 14:49:18

import os,sys
from sympy import Function,symbols,Symbol,solve,simplify,expand,ratsimp


#年金法计算贷款的年利率
#贷款五万，24个月等额本息每月2400元。
#计算年利率
def polynomial(a,p,n):
	return a*(1+p)**(-(n+1))

def iteration(a,p,n,F):
	step_0 = polynomial(a,p,0)
	for i in range(n):
		step = polynomial(a,p,i)
		step_0 += step
	step_0 -= polynomial(a,p,0)
	return step_0 - F

if __name__ == '__main__':
	a,p,n,F = symbols('a,p,n,F')
	S = iteration(a,p,24,F).subs([(a,2400.0),(F,50000.0)])
	# print(simplify(S))
	# print(expand(S))
	# print(ratsimp(S))
	#p = Symbol('p',positive=True)
	resu = solve(S,p)
	print(resu)
	resu = [i for i in resu if not ("I" in str(i)) and not ("-" in str(i))]
	rate = resu[0]
	print(rate*12.0)