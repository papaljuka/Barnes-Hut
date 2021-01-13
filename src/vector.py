import numpy as np

class Vector:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def magnitude(self):
        return np.sqrt(self.x * self.x + self.y * self.y)

    def __repr__(self):
        return "Vektor({0}.x, {0}.y)".format(self)
