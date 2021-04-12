import constants
import numpy as np
import scipy.integrate as integrate

class Force:

    def __init__(self, m):
        self.Forcex = 0
        self.Forcey = 0
        self.m = m

    def add(self, other):
        return Force(self.Forcex + other.Forcex, self.Forcey + other.Forcey)

    @staticmethod
    def applyForce_body(self, other):
        F = other.m * accelleration(self, m, pos, epsilon)

    @staticmethod
    def applyForce_COM(self, other):
        F =  other.m * accelleration(self, m, COM.pos, epsilon)
