import numpy as np

def r_rand(l, h):
    return l + np.random.random()*(h-l)

class Body:
    def __init__(self, pos = np.array[0,0,0], vel=np.array[0,0,0], mass=0):
        self.pos = pos
        self.vel = vel
        self.mass = mass

class NBody:
    def __init__(self, n):
        self.body = []
        for i in range(n):
            self.body.append(Body())
            
def spherical(r):
    v = np.array([0,0,0])
    theta = np.arccos(r_rand(-1, 1))
    phi = r_rand(0, 2*np.pi)
    v[0] = r * np.sin(theta) * np.cos(phi)
    v[1] = r * np.sin(theta) * np.sin(phi)
    v[2] = r * np.cos(theta)
    return v
    
            
def make_plummer(n):
    nb = NBody(n)
    for b in nb.body:
        b.mass = 1.0/n
        radius = 1.0/np.sqrt(np.random.random()**(-2.0/3.0) - 1.0)
        b.pos = spherical(radius)
        x = 0.0
        y = 0.1
        while y>x*x*(1 - x**2)**3.5:
            x = r_rand(0, 1)
            y = r_rand(0, 0.1)
        velocity = x * np.sqrt(2.0) * (1.0 + radius**2)**(-0.25)
        b.vel = spherical(velocity)
    return nb



