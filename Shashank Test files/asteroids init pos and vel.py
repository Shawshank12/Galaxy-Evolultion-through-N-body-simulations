# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 20:58:58 2022

@author: Shashank
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('D:\KSP 3.0\Galaxy-Evolution-through-N-body-simulations\Solar_System_using_Barnes_Hut')
import barnes_hut as bh

n = 1000
r = []
theta = []
asteroids = []
for i in range(n):
    b = 229e9 + np.random.random()*(777e9 - 229e9)
    r.append(b)
    c = 2*np.pi*np.random.random()
    v_b = 1e2 + np.random.random()*(10e3 - 1e2)
    v_c = 2*np.pi*np.random.random()
    theta.append(c)
    mass = 1e2 + np.random.random()*2e10
    obj = bh.cel_obj(b*np.cos(c), b*np.sin(c), 0, v_b*np.cos(v_c), v_b*np.sin(v_c), 0, mass)
    asteroids.append(obj)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.scatter(theta, r)
ax.set_rmax(1e12)
ax.set_rlabel_position(-22.5)
ax.grid(True)