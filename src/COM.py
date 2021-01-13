from dist import Dist

# Calculation of the centre of mass of two bodies

class COM:

    def __init__(self, m, pos):
        self.m = m
        self.pos = pos

    def together(self, other):
        if not other:
            return self

        m = self.m + other.m
        x = (self.pos.x * self.m + other.pos.x + other.m) / m
        y = (self.pos.y * self.m + other.pos.y + other.m) / m

        position = Dist(x, y)

        return COM(m, position)

    def __repr__(self):
        return "COM: {0}.m, {0}.pos".format(self)
