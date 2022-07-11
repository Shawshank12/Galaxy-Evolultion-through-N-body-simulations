# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 20:58:58 2022

@author: Shashank
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('/path/to/application/app/folder')

n = 1000
r = []
theta = []
for i in range(n):
    a = np.random.random()
    b = 229e9 + a*(777e9 - 229e9)
    r.append(b)
for i in range(n):
    a = 2*np.pi*np.random.random()
    theta.append(a)


fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.scatter(theta, r)
ax.set_rmax(1e12)
ax.set_rlabel_position(-22.5)
ax.grid(True)