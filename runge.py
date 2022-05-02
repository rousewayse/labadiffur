#!/bin/env python3
import matplotlib.pyplot as plt




def f(t, x, y):
    return (t, t**2)
#(x0, y0) --- Cauchy, f = y' --- function, iters --- number of iterations, h - is step
def RungeKutt(t0, x0, y0, f, iters, h):
    x = [x0]
    y = [y0]
    t = t0
    for i in range(0, iters):
        k1 = f(t, x[-1], y[-1])
        k2 = f(t + h/2, x[-1] + h/2*k1[0], y[-1] + h/2*k1[1])
        k3 = f(t+ h/2, x[-1]+ h/2*k2[0] , y[-1] + h/2*k2[1])
        k4  =f(t + h, x[-1]+ h*k3[0], y[-1] + h*k3[1])
        t += h
        x.append(x[-1] +  h/6*(k1[0]+2*k2[0]+2*k3[0] + k4[0]))
        y.append(y[-1] +  h/6*(k1[1]+2*k2[1]+2*k3[1] + k4[1]))
    return (x, y)
x, y = RungeKutt(-0.5,0,0,f,100,0.01)

plt.plot(x,y, ".", label="runge");
plt.legend()
plt.show()
