#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: lizujun
# @email: lizujun2008@gmail.com
# @cratetime : 2017-08-02 13:13:55
import os
import sys
from sympy import Function,symbols,Symbol,solve

def alc(total,num,rembursement):
	#total:总(贷款)额
	#num:还款期数(月)
	#rembursement：每一期还款
	pass
	#返回年利率
	return rate

def remain(total,rete,rembursement):
	#知道利率和每一期还款，计算仍欠款数
	return total*(1+rate)-rembursement


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
