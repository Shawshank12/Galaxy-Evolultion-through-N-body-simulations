import numpy as np

class Body:
    def __init__(self, pos = np.array([0.0,0.0,0.0]), vel=np.array([0.0,0.0,0.0]), mass=0.0):
        self.pos = pos
        self.vel = vel
        self.mass = mass

class NBody:
    def __init__(self, n):
        self.body = []
        for i in range(n):
            self.body.append(Body())
            
def ret_sph(r):
    v = np.array([0.0,0.0,0.0])
    theta = np.arccos(np.random.uniform(-1, 1))
    phi = np.random.uniform(0, 2*np.pi)
    v[0] = r * np.sin(theta) * np.cos(phi)
    v[1] = r * np.sin(theta) * np.sin(phi)
    v[2] = r * np.cos(theta)
    return v
    
            
def make_plummer(n):
    nb = NBody(n)
    for b in nb.body:
        b.mass = 1.0/n
        radius = 1.0/np.sqrt((np.random.random())**(-2.0/3.0) - 1.0)
        b.pos = ret_sph(radius)
        x = 0.0
        y = 0.1
        while y>(x**2)*((1 - x**2)**3.5):
            x = np.random.uniform(0, 1)
            y = np.random.uniform(0, 0.1)
        velocity = x * np.sqrt(2.0) * (1.0 + radius**2)**(-0.25)
        b.vel = ret_sph(velocity)
    return nb

test = make_plummer(4)


