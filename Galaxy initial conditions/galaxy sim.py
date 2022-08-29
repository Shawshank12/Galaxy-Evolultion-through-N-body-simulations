# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:34:36 2022

@author: Shashank
"""
import sys
sys.path.append('D:\KSP 3.0\Galaxy-Evolution-through-N-body-simulations\Solar_System_using_Barnes_Hut')
import barnes_hut as bh
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from mpl_toolkits import mplot3d
import time

begin = time.time()

init_pos = np.loadtxt("galaxy_coords.txt")
init_vel = np.loadtxt("galaxy_vels.txt")
init_m = np.loadtxt("galaxy_masses.txt")

t_0 = 0
t = t_0
div = 1
dt = 86400/div
t_end = 86400 * 365 * 10
t_array = np.arange(t_0, t_end, dt)

positions = init_pos
velocities = init_vel
masses = init_m

fig = plt.figure(dpi=600)
ax = plt.axes(projection='3d')
x = [i[0] for i in positions]
y = [i[1] for i in positions]
z = [i[2] for i in positions]
ax.scatter3D(x,y,z, s=0.2)

def update_state(positions, velocities, massses, dt):
    a_g = bh.GravAccel(positions, masses)
    for m1_id in range(len(velocities)):                 
        velocities[m1_id] += a_g[m1_id] * dt
    for e_id in range(len(positions)):
        positions[e_id] += velocities[e_id] * dt
    x = [i[0] for i in positions]
    y = [i[1] for i in positions]
    z = [i[2] for i in positions]
    ax.cla()    
    ax.scatter3D(x,y,z, s=0.2)

#animation = anim.FuncAnimation(fig, update_state, fargs = [positions, velocities, masses, dt], interval=50)

end = time.time()
print(end - begin)