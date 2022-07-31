import matplotlib.pyplot as plt
import plummer_model_alt as plum
from mpl_toolkits import mplot3d

sc = plum.make_plummer(1000, 1e30, 1e16)
sc.write_diagnostics()

x = []
y = []
z = []

for i in sc.body:
    x.append(i.pos[0])
    y.append(i.pos[1])
    z.append(i.pos[2])
    
fig = plt.figure(dpi=600)
ax = plt.axes(projection='3d')
ax.axes.set_xlim3d(left=-1e17, right=1e17) 
ax.axes.set_ylim3d(bottom=-1e17, top=1e17) 
ax.axes.set_zlim3d(bottom=-1e17, top=1e17)
ax.scatter3D(x,y,z)

