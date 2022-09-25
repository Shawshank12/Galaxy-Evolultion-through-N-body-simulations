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
#init_vel *= 1e3 #initial guess, gives weird energy
init_vel *= 10**(7.5)/np.sqrt(1.4)
init_m *= 2e40

speeds = [np.linalg.norm(x) for x in init_vel]
radii = [np.linalg.norm(x) for x in init_pos]

plt.title("Radial distribution of particles")
plt.ylabel("Counts")
plt.xlabel("Radius (m)")
counts1, bins1 = np.histogram(radii, bins=50)
plt.stairs(counts1, bins1)
f = plt.figure()
plt.title("Velocity distribution of particles")
plt.ylabel("Counts")
plt.xlabel("Velocity (m/s)")
counts2, bins2 = np.histogram(speeds, bins=50)
plt.stairs(counts2, bins2)

x_init = [i[0] for i in init_pos]
y_init = [i[1] for i in init_pos]
z_init = [i[2] for i in init_pos]

k = 0
p = 0
for i in range(len(init_vel)):
    k += 0.5 * init_m[i] * np.linalg.norm(init_vel[i])**2
BIG_G = 6.67e-11
for i in range(len(init_pos)):
    for j in range(i+1, len(init_pos)):
        if i != j:
            dist = np.linalg.norm(init_pos[i] - init_pos[j]) + 0.0001
            p += (-1 * BIG_G * init_m[i] * init_m[j])/dist

print(sum(init_m))
print(k)
print(p)

f2 = plt.figure(dpi=600)
ax = plt.axes(projection='3d')
plot_scale = 2e22
ax.set_xlim(left=-1*plot_scale, right=plot_scale) 
ax.set_ylim(bottom=-1*plot_scale, top=plot_scale) 
ax.set_zlim(bottom=-1*plot_scale, top=plot_scale)
ax.scatter3D(x_init, y_init, z_init, s=0.2)