#3
t=symbol('t')
st=5*t**2+2*t+8
t1=symbol('t1')
delta_t=symbol('delta_t')
st1=st.subs({t:t1})
st1_delta(st.subs({t:t1+delta_t}))
Limit(((st1_delta-st1)/delta_t),delta_t,0)




#2
u=symbol('u')
t=symbol('t')
g=symbol('g')
theta=symbol('theta')

from sympy import solve,sin
solve(u*sin(theta)-g*t,t)
#output  [u*sin(theta)/g]

x=symbol('x')
from sympy import Limit,s

l=Limit(1/x,x,S,dir='-')
l.doit()





#1
from sympy import symbol
theta=symbol('theta')

import math
math.sin(theta)

import sympy
sympy.sin(theta)+sympy.sin(theta)

2*sin(theta)
