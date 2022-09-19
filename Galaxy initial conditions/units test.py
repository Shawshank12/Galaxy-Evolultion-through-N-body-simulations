# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 09:19:27 2022

@author: Shashank
"""

import numpy as np
import matplotlib.pyplot as plt

init_pos = np.loadtxt("galaxy_coords.txt")
init_vel = np.loadtxt("galaxy_vels.txt")
init_m = np.loadtxt("galaxy_masses.txt")

init_pos *= 3.0856e19
init_vel *= 1e3
init_m *= 2e40

x_init = [i[0] for i in init_pos]
y_init = [i[1] for i in init_pos]
z_init = [i[2] for i in init_pos]

print(init_vel)

f = plt.figure(dpi=600)
ax = plt.axes(projection='3d')
plot_scale = 2e22
ax.set_xlim(left=-1*plot_scale, right=plot_scale) 
ax.set_ylim(bottom=-1*plot_scale, top=plot_scale) 
ax.set_zlim(bottom=-1*plot_scale, top=plot_scale)
ax.scatter3D(x_init, y_init, z_init, s=0.2)
