import sympy as sp
import numpy as np

x = sp.symbols('x')
a = sp.symbols('a')
n = sp.symbols('n')
f = sp.symbols('f')
f= 3*x**2+4**2
def Taylor_formula (f, x, a, n):
    for i in range (1,n):
        z = sp.diff(f,x,i)
        z= z.subs(x,a)
        b = (x-a)**i
        c = np.math.factorial(i)
        out = (z*b)/c
        out += out
    return(out)
y = Taylor_formula (f, x, 1, 3)

taylor_eval = sp.lambdify(x,y, "numpy")

print(taylor_eval(x))

import matplotlib.pyplot as plt
m = np.linspace(0.0, 1.0, 100)
plt.plot(m, taylor_eval(x), "l")
plt.xlabel('Rise')
plt.ylabel('Run')
plt.show()

#sin(6,x,3,0) return x-(x)**3/3!
