import numpy as np
import constants
from vector import Vector
from dist import Dist
# Definition of a body

class Body():

    def __init__(self, m, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        #self.m = m[i] for i in range(len(m))

#   E = E_k + E_pot
    def energy(self):
        pass

#   p_1 + p_2 = p_12
    def momentum(self, other):
        pass

    def angular_momentum(self, other):
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

    def __repr__(self):
        return "Body: ({0}.x, {0}.y, {0}.z), mass= {0}.m".format(self)
