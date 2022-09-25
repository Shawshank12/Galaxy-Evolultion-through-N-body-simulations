# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:58:05 2022

@author: Shashank
"""

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
import time
from matplotlib.animation import FuncAnimation

begin = time.time()

def c2p(arr):
    radius = np.sqrt(arr[0]**2 + arr[1]**2)
    angle = np.arctan2(arr[1], arr[0])
    return radius, angle

BIG_G = 6.67e-11

n = 750
r = []
theta = []
asteroids = []
sun = bh.cel_obj(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.989e30)
jupiter = bh.cel_obj(778.570e9, 0.0, 0.0, 0.0, 13e3, 0.0, 1898.19e24)
for i in range(n):
    if i == 0:
        asteroids.append(sun)
        asteroids.append(jupiter)
    mass = 1e2 + np.random.random()*2e5
    c = 2*np.pi*np.random.random()
    b = 229e9 + np.random.random()*(777e9 - 229e9)
    p = 0
    if len(asteroids)>1:
        for i in range(len(asteroids)):
            dist = np.linalg.norm(np.array([b*np.cos(c), b*np.sin(c), 0]) - asteroids[i].pos)
            p += (-1 * BIG_G * mass * asteroids[i].m)/dist
    v_b = np.sqrt(-1*p/mass)
    r.append(b)
    theta.append(c) 
    obj = bh.cel_obj(b*np.cos(c), b*np.sin(c), 0, -1*v_b*np.sin(c), v_b*np.cos(c), 0, mass)
    asteroids.append(obj)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.scatter(theta, r, s=0.8)
ax.set_rmax(1e12)
ax.set_rlabel_position(-22.5)
ax.grid(True)

t_0 = 0
t = t_0
dt = 86400
t_end = 86400 * 365 * 0.2
t_array = np.arange(t_0, t_end, dt)
BIG_G = 6.67e-11

positions = np.array([x.pos for x in asteroids])
velocities = np.array([x.vel for x in asteroids])
masses = np.array([x.m for x in asteroids])

fig2, ax2 = plt.subplots(subplot_kw={'projection': 'polar'})
ax2.set_rmax(1e12)
ax2.set_rlabel_position(-22.5)
ax2.grid(True)
ke = []
pe = []
e = []
e_scale = 1e15
r_total = []
theta_total = []
k = 1

while t<t_end:
    en = 0
    p = 0
    a_g = np.zeros_like(asteroids)
    for i in range(len(asteroids)):
        en += 0.5 * asteroids[i].m * np.linalg.norm(asteroids[i].vel)**2
    for i in range(len(asteroids)):
        for j in range(i+1, len(asteroids)):
            if i != j:
                dist = np.linalg.norm(asteroids[i].pos - asteroids[j].pos) + 0.0001
                a_g[i] += (asteroids[i].pos - asteroids[j].pos)*(-1 * BIG_G *  asteroids[j].m)/dist**3
                p += (-1 * BIG_G * asteroids[i].m * asteroids[j].m)/dist
    for m1_id in range(len(asteroids)):                 
        asteroids[m1_id].vel += a_g[m1_id] * dt
        velocities[m1_id] = asteroids[m1_id].vel
    for e_id in range(len(asteroids)):
        asteroids[e_id].pos += asteroids[e_id].vel * dt
        positions[e_id] = asteroids[e_id].pos
    ke.append(en/e_scale)
    pe.append(p/e_scale)
    e.append((en+p)/e_scale)
    r_p = []
    theta_p = []
    for i in range(len(asteroids)):
        ra, th = c2p(asteroids[i].pos)
        r_p.append(ra)
        theta_p.append(th)
    r_total.append(r_p)
    theta_total.append(theta_p)
    #print("Step {} done".format(k))
    k += 1
    t += dt

def update_func(i):
    ax2.cla()
    ax2.scatter(theta_total[i], r_total[i], s=0.5)
    print("Frame {} rendered".format(i))

#animation = FuncAnimation(fig2, update_func, interval = 50, save_count=70)
#animation.save("asteroid_belt.gif", dpi=600)

fig6 = plt.figure()
plt.xlabel("Time (s)")
plt.ylabel("Energy (J)")
plt.plot(t_array, ke)
plt.plot(t_array, pe)
plt.plot(t_array, e)
fig3 = plt.figure()
plt.xlabel("Time (s)")
plt.ylabel("Kinetic Energy (J)")
plt.plot(t_array, ke)
fig4 = plt.figure()
plt.xlabel("Time (s)")
plt.ylabel("Potential Energy (J)")
plt.plot(t_array, pe)
fig5 = plt.figure()
plt.xlabel("Time (s)")
plt.ylabel("Total Energy (J)")
plt.plot(t_array, e)

print(ke[0],pe[0],e[0])
print(ke[-1],pe[-1],e[-1])

end = time.time()
print(end - begin)