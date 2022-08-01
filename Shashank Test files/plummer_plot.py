import matplotlib.pyplot as plt
import plummer_model as plum
from mpl_toolkits import mplot3d

sc = plum.make_plummer(1000)
print(sc.energy_vals())

x = []
y = []
z = []

for i in sc.body:
    x.append(i.pos[0])
    y.append(i.pos[1])
    z.append(i.pos[2])
    
fig = plt.figure(dpi=600)
ax = plt.axes(projection='3d')
a = 2
ax.axes.set_xlim3d(left=-1*a, right=a) 
ax.axes.set_ylim3d(bottom=-1*a, top=a) 
ax.axes.set_zlim3d(bottom=-1*a, top=a)
ax.scatter3D(x,y,z)

