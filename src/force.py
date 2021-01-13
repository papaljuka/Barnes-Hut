import constants
import numpy as np
import scipy.integrate as integrate

class Force:

    def __init__(self):
        self.Forcex = 0
        self.Forcey = 0

    def add(self, other):
        return Force(self.Forcex + other.Forcex, self.Forcey + other.Forcey)

    @staticmethod
    def applyForce_body(p1, p2):
        pass

    @staticmethod
    def applyForce_COM(p1, com):
        pass
