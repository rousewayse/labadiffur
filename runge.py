#!/bin/env python3
import matplotlib.pyplot as plt
from math import exp



def f(t, x, y):
    p1 = 1
    p2 = -0.01
    return (exp(y) - 1 + p2*(exp(x)-1)/(p2 + exp(2*x))*exp(y), p1*(1 - exp(x)) - p1*p2*(exp(x)-1)/(p2 + exp(2*x))*exp(x))
#(x0, y0) --- Cauchy, f = y' --- function, iters --- number of iterations, h - is step
def RungeKutt(t0, x0, y0, f, iters, h):
    res = [[x0, y0]]

    t = t0
    for i in range(0, iters):
        k1 = f(t, res[-1][0], res[-1][1])
        k2 = f(t + h/2, res[-1][0] + h/2*k1[0], res[-1][1] + h/2*k1[1])
        k3 = f(t+ h/2, res[-1][0]+ h/2*k2[0] , res[-1][1] + h/2*k2[1])
        k4  =f(t + h, res[-1][0]+ h*k3[0], res[-1][1] + h*k3[1])
        t += h
        
        x = res[-1][0] +  h/6*(k1[0]+2*k2[0]+2*k3[0] + k4[0])
        y = res[-1][1] +  h/6*(k1[1]+2*k2[1]+2*k3[1] + k4[1])
        res.append([x, y])
    return res
data = RungeKutt(0,0.5,0.55,f,50000,0.01)
plt.scatter([i[0] for i in data ],[i[1] for i in data], label="runge", s=0.3);
plt.legend()
plt.show()
