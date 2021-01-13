import numpy as np

class Point():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y

    def distx(self, other):
        return np.abs(self.x - other.x)

    def disty(self, other):
        return np.abs(self.y - other.y)

    def dist(self, other):
        x = distx(self, other)
        y = disty(self, other)
        return np.sqrt(x**2 + y**2)
