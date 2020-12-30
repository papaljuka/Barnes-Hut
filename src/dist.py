import numpy as np

class Dist:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distx(self, other):
        return np.abs(self.x - other.x)

    def disty(self, other):
        return np.abs(self.y - other.y)
    
    def distz(self, other):
        return np.abs(self.z - other.z)

    def dist(self, other):
        x = distx(self, other)
        y = disty(self, other)
        z = distz(self, other)
        return np.sqrt(x**2 + y**2 + z**2)


