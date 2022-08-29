import sys
sys.path.append('D:\KSP 3.0\Galaxy-Evolution-through-N-body-simulations\Solar_System_using_Barnes_Hut')
import matplotlib.pyplot as plt
import numpy as np
import plummer_model as plum
from mpl_toolkits import mplot3d
import barnes_hut
import time

begin = time.time() 

sc = plum.make_plummer(200)
print(sc.energy_vals())

positions = np.array([x.pos for x in sc.body])
velocities = np.array([x.vel for x in sc.body])
masses = np.array([x.mass for x in sc.body])

t_0 = 0
t = t_0
div = 1
dt = 86400/div
t_end = 86400 * 365 * 10
t_array = np.arange(t_0, t_end, dt)

fig = plt.figure(dpi=600)
ax = plt.axes(projection='3d')
plot_scale = 2
ax.axes.set_xlim3d(left=-1*plot_scale, right=plot_scale) 
ax.axes.set_ylim3d(bottom=-1*plot_scale, top=plot_scale) 
ax.axes.set_zlim3d(bottom=-1*plot_scale, top=plot_scale)
j = 0

ke = []
pe = []
e = []

while t<t_end:
    a_g = barnes_hut.GravAccel(positions, masses, G=1)
    for m1_id in range(len(sc.body)):                 
        sc.body[m1_id].vel += a_g[m1_id] * dt
        velocities[m1_id] = sc.body[m1_id].vel
    for e_id in range(len(sc.body)):
        sc.body[e_id].pos += sc.body[e_id].vel * dt
        positions[e_id] = sc.body[e_id].pos
    
    k, p, tot = sc.energy_vals()
    ke.append(k)
    pe.append(p)
    e.append(tot)
    
    x = []
    y = []
    z = []

    for i in sc.body:
        x.append(i.pos[0])
        y.append(i.pos[1])
        z.append(i.pos[2])
        
    ax.cla()  
    ax.scatter3D(x,y,z)
    fig.savefig('D:\KSP 3.0\Plots\plummer_plot_{}.png'.format(j), dpi=600)
    j += 1
    t += dt

fig2 = plt.figure()
plt.plot(t_array, ke)
plt.plot(t_array, pe)
plt.plot(t_array, e)
fig3 = plt.figure()
plt.plot(t_array, ke)
fig4 = plt.figure()
plt.plot(t_array, pe)
fig5 = plt.figure()
plt.plot(t_array, e)

end = time.time()
print(end - begin)