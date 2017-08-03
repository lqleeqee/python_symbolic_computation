#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-02 13:13:55
import os
import sys
from sympy import Function,symbols,Symbol,solve

#摊余法计算贷款年利率
#贷款五万，24个月等额本息每月2400元。
#计算年利率
def sys_cla(A,r,X):
	#A,r,X = symbols('A,r,X')
	return A*(1+r)-X

def iteration(A,r,X,n):
	#
	for i in range(n):
		A = sys_cla(A,r,X)
	return A

if __name__ == '__main__':
	A,r,X = symbols('A,r,X')
	S = iteration(A,r,X,24).subs([(X,2400.0),(A,50000.0)])
	resu = solve(S)
	resu = [i for i in resu if not ("I" in str(i)) and not ("-" in str(i))]
	rate = resu[0]
	print(rate*12.0)
