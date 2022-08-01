# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 00:06:43 2022

@author: Shashank
"""
import sys
sys.path.append('D:\KSP 3.0\Galaxy-Evolution-through-N-body-simulations\Solar_System_using_Barnes_Hut')
import matplotlib.pyplot as plt
import numpy as np
import plummer_model_alt as plum
from mpl_toolkits import mplot3d
import barnes_hut
import time

begin = time.time()

scale = 1e10

sc = plum.make_plummer(200, 1e20, scale)
sc.write_diagnostics()

positions = np.array([x.pos for x in sc.body])
velocities = np.array([x.vel for x in sc.body])
masses = np.array([x.mass for x in sc.body])

t_0 = 0
t = t_0
div = 0.1
dt = 86400/div
t_end = 86400 * 365 * 5
t_array = np.arange(t_0, t_end, dt)

fig = plt.figure(dpi=600)
ax = plt.axes(projection='3d')
ax.axes.set_xlim3d(left=-1*scale, right=scale) 
ax.axes.set_ylim3d(bottom=-1*scale, top=scale) 
ax.axes.set_zlim3d(bottom=-1*scale, top=scale)
j = 0

while t<t_end:
    a_g = barnes_hut.GravAccel(positions, masses)
    for m1_id in range(len(sc.body)):                 
        sc.body[m1_id].vel += a_g[m1_id] * dt
        velocities[m1_id] = sc.body[m1_id].vel
    for e_id in range(len(sc.body)):
        sc.body[e_id].pos += sc.body[e_id].vel * dt
        positions[e_id] = sc.body[e_id].pos
    
    x = []
    y = []
    z = []

    for i in sc.body:
        x.append(i.pos[0])
        y.append(i.pos[1])
        z.append(i.pos[2])
        
    ax.scatter3D(x,y,z)
    fig.savefig('D:\KSP 3.0\Plots\plummer_plot_{}.png'.format(j), dpi=600)
    ax.cla()
    j += 1
    t += dt

end = time.time()
print(end - begin)