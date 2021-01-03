from COM import COM
from force import Force
import constants

class Node:

    def __init__(self, size, x, y, z):
        self.width = size[0]
        self.height = size[1]
        self.depth = size[2]
        self.x = x
        self.y = y
        self.z = z
        self.subNodes = {"0": None, "1": None, "2": None, "3": None,
                        "4": None, "5": None, "6": None, "7": None}
        sefl.body = None
        self.com = None
        self.theta = constants.theta

    def addbody(self, newbody):
        if self.isempty():
            self.body = newbody
            self.com = newbody.getcom()
            return

        if self.subNodes["1"] is None:
            self.populate()

        if self.body is not None:
            self.com = None

        self.addbodytosubnode(self.body)
        self.addbodytosubnode(newbody)

        self.body = None

    def populate(self):
        subW = self.width/2
        subH = self.height/2
        subD = self.depth/2
        subSize = (subW; subH, subD)
        x = self.x
        y = self.y
        z = self.z
        self.subNodes["0"] = Node(subSize, x, y, z)
        self.subNodes["1"] = Node(subSize, x + subW, y, z)
        self.subNodes["2"] = Node(subSize, x, y + subH, z)
        self.subNodes["3"] = Node(subSize, x, y, z + subD)
        self.subNodes["4"] = Node(subSize, x + subW, y + subH, z)
        self.subNodes["5"] = Node(subSize, x, y + subH, z + subD)
        self.subNodes["6"] = Node(subSize, x + subW, y, z + subD)
        self.subNodes["7"] = Node(subSize, x + subW, y + subH, z + subD)

    def addbodytosubnode(self, body):
        if body is None:
            return

        for node in self.subNodes(values):
            if node.boundsAround(body):
                node.addbody(body)
                com = node.COM
                self.COM = com.together(self.COM)
                return
        print("Node out of bounds")

    def boundsAroun(self, body):
        pos = body.pos
        return (pos.x >= self.x and pos.y = self.y and pos.z = self.z
                and pos.x < self.x + self.width
                and pos.y < self.z + self.height
                and pos.z < self.z + self.depth)

    def applyGravity(self, body):
        if self.body is body or self.isempty():
            return
        elif self.isExternal():
            Force.applyForce_body(body, self.body)
        elif self.isFar(body):
            Force.applyForce_COM(body, self.body)
        else:
            for node in self.subNodes.values():
                node.applyGravity(body)

    def isFar(self, particle):
        d = self.COM.pos.dist(body.pos)
        return (self.width / d < self.theta
                and self.depth / d < self.theta)

    def isInternal(self):
        return self.body is None and self.subNodes["1"] is not None

    def isExternal(self):
        return self.subNodes["1"] is None and self.body is not None

    def pydraw(self):
        pass

    def __repr__(self):
        return 'NODE: (x: {0}.x, y:{0}.y, z: {0}.z), (w: {0}.width, h: {0}.height, d: {0}.depth), body: {0}.body, nodes: {0}.nodes'.format(self)
