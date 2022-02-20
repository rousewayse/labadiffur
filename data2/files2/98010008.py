#!/bin/env python3
import re
import math
import tabulate
import pandas as pd
freq = float(100.00)
duration = float(5.14)
sensity = float(50)
channels = int(16)

file = open("98010008.ASC", 'r')
measurement = []
for line in file:
    measurement.append((list(filter(lambda a: a!='' , re.split("\s+\n*", line)))))

def fetchCoord(coord, data):
    print(coord)
    return  [a[coord] for a in data]


def getZs(N=4, coord = 0):
    zs = []
    da  = fetchCoord(coord, measurement)
    for i in range(0, len(da)-N+1):
        zs.append(list(map(float,  da[i:i+N])))
    return zs

def Tetta(z1, z2, eps=0.01):
    def dist(z1, z2):
        tmp = 0;
        for i in range(0, len(z1)):
            tmp += (z1[i] - z2[i])**2
        return math.sqrt(tmp)
    tmp = eps - dist(z1, z2)
    if tmp < 0:
        return 0
    else:
        return 1

def C(eps, zs):
    tmp = 0;
    for i in range(0, len(zs)):
        for k in range (0, len(zs)):
            tmp += Tetta(zs[i], zs[k])
    tmp = tmp/(len(zs)**2)
    return tmp

def Dc(eps, zs):
    return math.log(C(eps, zs))/math.log(eps)

Nstart = 4
Nstop = 20

data = [[Dc(0.01, getZs(N=i, coord=k)) for i in range(Nstart,Nstop)] for k in  range(0,16)]
print(pd.DataFrame(data, index=[f"Канал {i}" for i in range(0, 16 )]  , columns= [f"dim zi={i}" for i in range (Nstart,Nstop)]).to_html())
