#!/bin/env python3
import re
import math
import tabulate
import pandas as pd
import threading 
import matplotlib.pyplot as plt 
import math
import numpy as np
def fetchCoord(coord, data):
    #print(coord)
    return  [a[coord] for a in data]


def getZs(N=4, coord = 0):
    zs = []
    da  = fetchCoord(coord, measurement)
    for i in range(0, len(da)-N+1):
        zs.append(list(map(float,  da[i:i+N])))
    return zs

def dist(z1, z2):
    tmp = 0;
    for i in range(0, len(z1)):
        tmp += (z1[i] - z2[i])**2
    return math.sqrt(tmp)

def Tetta(z1, z2, eps=0.01):
    tmp = eps - dist(z1, z2)
    if tmp < 0:
        return 0
    else:
        return 1

def C(eps, zs):
    tmp = 0;
    for i in range(0, len(zs)):
        for k in range (0, len(zs)):
            tmp += Tetta(zs[i], zs[k], eps)
    tmp = tmp/(len(zs)**2)
    return tmp

def Dc(eps, zs):
    return math.log(C(eps, zs))/math.log(eps)
#garbage in fact, not used
freq = float(100.00)
duration = float(5.14)
sensity = float(50)
channels = int(16)


file = open("data2/files1/99060004.ASC", 'r')
measurement = []
for line in file:
    measurement.append((list(filter(lambda a: a!='' , re.split("\s+\n*", line)))))

tau = int(2)
tmp = []
for i in range(0, len(measurement)-1, tau):
   tmp.append(measurement[i])
measurement = tmp;
print(measurement)
def printData(data):
    for i in data:
        for k in i:
            print(str(k) + " ", end='')
        print()

Nstart = 4
Nstop = 10
'''
def func(res, coord):
    #res[coord] = [ln(C(0.01, getZs(N=i, coord=coord))) for i in range (Nstart, Nstop)]
    res[coord] = [Dc(0.01, getZs(N=i, coord=coord)) for i in range (Nstart, Nstop)]
data = [[]] * 16
threads = [threading.Thread(target=func, args=(data, i)) for i in range(0, 16)]

for i in threads:
    i.start()

for i in threads:
    i.join()
'''

def get_eps(zi):
    mins = []
    for i in zi:
        mins.append(min([dist(i, j) for j in list(filter(lambda z: z != i ,zi)) ]))
    return min(mins)
        
zs = getZs(4, 0)
print(get_eps(zs[ :len(zs)//3 ]))
print(get_eps(zs[ :2*len(zs)//3 ]))
print(get_eps(zs))



coord = 0
deps = 0.1
x_plot = [ 0.3 +  i*deps for i in range(0, 20)]
y_plots= []
for i in range (Nstart, Nstop):
    zs = getZs(i, coord)
    x_plot = sorted([ get_eps(zs[:len(zs)//2]), get_eps(zs)])
    print(x_plot)
    y_plots.append([math.log(C(eps , zs)) for eps in x_plot])
    print(y_plots[-1])
    print([math.log(x) for x in x_plot])
    A = np.vstack ([[math.log(x) for x in x_plot], np.ones(len(x_plot))]).T
    m,c = np.linalg.lstsq(A, y_plots[-1], rcond=None)[0]
    plt.plot([math.log(x) for x in x_plot], m*np.array([math.log(x) for x in x_plot]) + c, "-.", label=f"Dc = {m} for dim zs =  {i}, ")
    plt.plot([math.log(x) for x in x_plot], y_plots[-1], "-", label=f"dim Zs =  {i}")
plt.legend()
plt.show()


"""
#data = [[Dc(0.01, getZs(N=i, coord=k)) for i in range(Nstart,Nstop)] for k in  range(0,16)]
x_plot = [i for i in range(Nstart, Nstop)]
y_plots = []
for i in range(0, 16):
    y_plots.append(data[i])
    plt.plot(x_plot, y_plots[-1], "-", label=f"?????????? {i}")

#x_plot = [i for i in range(Nstart,Nstop )]
#y_plot = data[3]
#plt.plot(x_plot, y_plot, "-", label="da")
plt.legend()
plt.show()

out = open("output.html", 'w')
out.write(f"tau = {tau}")
out.write(pd.DataFrame(data, index=[f"?????????? {i}" for i in range(0, 16 )]  , columns= [f"dim zi={i}" for i in range (Nstart,Nstop)]).to_html())
"""
