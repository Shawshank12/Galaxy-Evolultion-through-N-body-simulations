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

t_0 = 0
t = t_0
dt = 86400
t_end = 86400 * 365 * 0.3
t_array = np.arange(t_0, t_end, dt)
BIG_G = 6.67e-11

positions = np.array([x.pos for x in asteroids])
velocities = np.array([x.vel for x in asteroids])
masses = np.array([x.m for x in asteroids])

x_pos = [[],[],[],[]]
y_pos = [[],[],[],[]]
z_pos = [[],[],[],[]]

while t<t_end:
    a_g = bh.GravAccel(positions, masses)
    for m1_id in range(len(asteroids)):                 
        asteroids[m1_id].vel += a_g[m1_id] * dt
        velocities[m1_id] = asteroids[m1_id].vel
    for e_id in range(len(asteroids)):
        asteroids[e_id].pos += asteroids[e_id].vel * dt
        positions[e_id] = asteroids[e_id].pos
    for i in range(1, 5):
        x_pos[i-1].append(asteroids[i].pos[0])
        y_pos[i-1].append(asteroids[i].pos[1])
        z_pos[i-1].append(asteroids[i].pos[2])
    t += dt

fig = plt.figure(dpi=600)
ax = plt.axes(projection='3d')
ax.axes.set_xlim3d(left=-8e11, right=8e11) 
ax.axes.set_ylim3d(bottom=-8e11, top=8e11) 
ax.axes.set_zlim3d(bottom=-1, top=1)
for j in range(4):    
    ax.plot3D(x_pos[j], y_pos[j], z_pos[j])