from node import Node
from body import Body
from dist import Dist
from time import sleep
from vector import Vector
import numpy as np
import constants

class Simulation:

    def __init__(self):
        self.width =
        self.height =
        self.depth =
        size = (self.width, self.height, self.depth)

        root = Node(size, 0, 0, 0)
#        system = self.generatesystem()
        for body in system:
            root.addbody(body)

        # initialize GUI: pygame?

        #changes due to gravity

    def generatesystem(self):
        pass


if __name__ == "__main__":Simulation
