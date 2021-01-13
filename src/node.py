from COM import COM
from force import Force
import constants

class Node():

    def __init__(self, size, x0, y0, body):
        self.width = size[0]
        self.height = size[1]
        self.x0 = x0
        self.y0 = y0
        self.body = body
        self.subNodes = {"0": None, "1": None, "2": None, "3": None}
        self.com = None

    def addBody(self, newBody):
        if self.isEmpty():
            self.body = newBody
            self.com = newBody.getCOM()
            return

        if self.subNodes["1"] is None:
            self.populate()

        if self.body is not None:
            self.com = None

        self.addBodyToSubnode(self.body)
        self.addBodyToSubnode(newBody)

        self.body = None

    def populate(self):
        subW = self.width/2
        subH = self.height/2
        subSize = (subW; subH)
        x = self.x
        y = self.y
        self.subNodes["nw"] = Node(subSize, x, y)
        self.subNodes["ne"] = Node(subSize, x + subW, y)
        self.subNodes["sw"] = Node(subSize, x, y + subH)
        self.subNodes["se"] = Node(subSize, x + subW, y + subH)


    def addBodyToSubnode(self, body):
        if body is None:
            return

        for node in self.subNodes.values():
            if node.boundsAround(body):
                node.addBody(body)
                com = node.COM
                self.COM = com.together(self.COM)
                return
        print("Node out of bounds")

    def boundsAround(self, body):
        pos = body.pos
        return (pos.x >= self.x and pos.y = self.y
                and pos.x < self.x + self.width
                and pos.y < self.z + self.height)

    def applyGravity(self, body):
        if self.body == body or self.isEmpty():
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
        return self.body == None and self.subNodes["0"] != None

    def isExternal(self):
        return self.subNodes["0"] == None and self.body != None

    def isEmpty(self):
        return self.subNodes["0"] == None and self.body == None

    def pydraw(self, pd, screen):
        if (self.drawGrid):
            pd.rect(screen, self.borderColour,
                    (self.x, self.y, self.width, self.height), 1)
        if self.body == None:
            for node in self.subNodes.values():
                if node != None:
                    node.pydraw(pd, screen)
        else:
            self.body.pydraw(pd, screen)

        M = self.COM.mass
        if self.width > 1:
            font = pygame.font.SysFont('helvetica', 20 + (int)(30 * self.width / constants.CANVAS_WIDTH))
            textsurface = font.render(str(mass), False, (255,255,255))
            screen.blit(textsurface, (self.x + (self.width * 0.5) - 50, self.y + (self.height*0.5) - 50))

    def __repr__(self):
        return 'NODE: (x: {0}.x, y:{0}.y, z: {0}.z), (w: {0}.width, h: {0}.height, d: {0}.depth), body: {0}.body, nodes: {0}.nodes'.format(self)
