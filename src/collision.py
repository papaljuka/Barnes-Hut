import numpy as np
import constants
from vector import Vector
from dist import Dist


class Body():
    def __init__(self, m, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
#        masa
#        self.m = m[i] for i in range(len(m))

    def __repr__(self):
        pass

#   E = E_k + E_pot
    def energy(self):
        pass
    
#   p_1 + p_2 = p_12
    def momentum(self, other):
        pass
        
#   a = (ax, ay, az) gravitacijski!
#   integrator, g!
    def move(self, dt, ax, ay, az):
        pass        

#   assuming that when two bodies collide they merge, we can look at the CMS velocity 
    def collision(self, other):
        self.vx = (self.m * vx + other.m * other.vx) / (self.m + other.m)
        self.vy = (self.m * vy + other.m * other.vy) / (self.m + other.m)
        self.vz = (self.m * vz + other.m * other.vz) / (self.m + other.m)
        self.m += other.m


