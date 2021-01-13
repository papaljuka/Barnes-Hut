import numpy as np
from constants import *
from vector import Vector
from dist import Dist
# Definition of a body

class Body():

    def __init__(self, m=constants.cons_m, pos, v = Vector(), size=, i):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.m = m
        self.pos = pos
        self.v = v
        self.a = Vector()

    def accelleration(self, m, pos, epsilon):
        x = pos[:, 0, 1]
        y = pos[:, 1, 2]
        dx = x.T - x
        dy = y.T - y
        r3_inv = (dx**2 + dy**2 + epsilon**2)** (-1.5)
        ax = constants.G * (dx * r3_inv) @ mass
        ay = constants.G * (dy * r3_inv) @ mass
        a = np.hstack((ax, ay))
        return a

#   a = (ax, ay, az) gravitacijski!
#   Leap-Frog integration: kick + drift + kick
    def move(self, dt, ax, ay):
		vx += ax * 0.5 * dt
        vy += ay * 0.5 * dt
        x += vx * dt
        y += vy * dt
		acc = accelleration(self, m, x, y, G, epsilon)
		vx += ax * 0.5 * dt
		vy += ay * 0.5 * dt
		t += dt

		EKin, EPot  = energy(self, m, G, vx, vy, x, y)

#   E = E_k + E_pot
    def energy(self, m, G, v, pos):
        Ekin = 0.5 * np.sum(np.sum( m * v **2))
        x = pos[:, 0, 1]
        y = pos[:, 1, 2]
        dx = x.T - x
        dy = y.T - y
        r_inv = np.sqrt(dx**2 + dy**2)
        r_inv[r_inv > 0] = 1.0 / r_inv[r_inv > 0]
        EPot = constants.G * np.sum(np.sum(np.triu(-(m*m.T)*r_inv,1))
        return (EKin, EPot)

#   assuming that when two bodies collide they merge, we can look at the CMS velocity
    def collision(self, other):
        self.vx = (self.m * vx + other.m * other.vx) / (self.m + other.m)
        self.vy = (self.m * vy + other.m * other.vy) / (self.m + other.m)
        self.m += other.m

    def pydraw(self, pd, plane):
        pass

    def __repr__(self):
        return "Body: ({0}.x, {0}.y), mass= {0}.m".format(self)
