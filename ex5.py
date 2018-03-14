import numpy as np
import scipy.optimize as opt

def fun(x):
    return (x**2+x*3-7)

def bysec(a,b,t):
	if( fun(a)*fun(b)>0. ):
		print('Error: f(a) and f(b) should have opposite signs! Stopping.')
	else:
		while(0.5*(b-a)>t):
			c=0.5*(a+b)
			if( fun(a)*fun(c)<0.):
				b=c
			else:
				a=c
		x=0.5*(b+a)
	return x

bysec_root=bysec(0.,5.,0.001)
brentq_root=opt.brentq(fun,0.,5.)
bisect_root=opt.bisect(fun,0.,5.)
newton_root=opt.newton(fun, 0.)

bysec_time=%timeit -o bysec(0.,5.,0.001)

brentq_time=%timeit -o opt.brentq(fun,0.,5.)

bisect_time=%timeit -o opt.bisect(fun,0.,5.)

newton_time=%timeit -o opt.newton(fun, 0.)




