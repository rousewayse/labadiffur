#!/bin/env python3
import matplotlib.pyplot as plt




def f(x, y):
    return x
#(x0, y0) --- Cauchy, f = y' --- function, iters --- number of iterations, h - is step
def RungeKutt(x0, y0, f, iters, h):
    x = [x0]
    y = [y0]
    for i in range(0, iters):
        k1 = f(x[-1], y[-1])
        k2 = f(x[-1] + h/2, y[-1] + h/2*k1)
        k3 = f(x[-1] + h/2, y[-1] + h/2*k2)
        k4  =f(x[-1] + h, y[-1] + h*k3)
        x.append(x[-1] + h)
        y.append( y[-1] +  h/6*(k1+2*k2+2*k3 + k4))
    return (x, y)
x, y = RungeKutt(-0.5,0,f,100,0.01)

plt.plot(x,y, "-", label="runge");
plt.legend()
plt.show()
