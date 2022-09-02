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
div = 1/60
dt = int(86400/div)
t_end = 86400 * 365 * 5
t_array = np.arange(t_0, t_end, dt)
n_frames = int((t_end - t_0)/dt)

positions = init_pos
velocities = init_vel
masses = init_m

fig = plt.figure(dpi=600)
ax = plt.axes(projection='3d')
plot_scale = 1e18
ax.axes.set_xlim3d(left=-1*plot_scale, right=plot_scale) 
ax.axes.set_ylim3d(bottom=-1*plot_scale, top=plot_scale) 
ax.axes.set_zlim3d(bottom=-1*plot_scale, top=plot_scale)

x_t = []
y_t = []
z_t = []
j = 1

while t<t_end:
    a_g = bh.GravAccel(positions, masses, G = 44920.0)
    for m1_id in range(len(velocities)):                 
        velocities[m1_id] += a_g[m1_id] * dt
    for e_id in range(len(positions)):
        positions[e_id] += velocities[e_id] * dt
    x = [obj[0] for obj in positions]
    y = [obj[1] for obj in positions]
    z = [obj[2] for obj in positions]
    x_t.append(x)
    y_t.append(y)
    z_t.append(z)
    print("Step {} done".format(j))
    j += 1
    t += dt

def init_gif():
    x_init = [i[0] for i in init_pos]
    y_init = [i[1] for i in init_pos]
    z_init = [i[2] for i in init_pos]
    ax.scatter3D(x_init,y_init,z_init, s=0.2)
    
def update_state(i):
    ax.cla()    
    ax.scatter3D(x_t[i],y_t[i],z_t[i], s=0.2)
    print("frame {} rendered".format(i))
    
animation = anim.FuncAnimation(fig, init_func=init_gif, func=update_state, save_count=n_frames, interval=50)
animation.save("galaxy.gif", dpi=600)
end = time.time()
print(end - begin)