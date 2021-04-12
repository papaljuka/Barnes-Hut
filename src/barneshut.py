from node import Node
from body import Body
from dist import Dist
from time import sleep
from vector import Vector
import numpy as np
from constants import *
import pygame
from pygame.locals import *
import os.path
from os import path


class Simulation:

    def __init__(self):
        self.width =
        self.height =
        size = (self.width, self.height)
        background_colour = (0, 0, 0)
        self.numofp = constants.numofp

        root = Node(size, 0, 0)
        system = self.generatesystem()

        for body in system:
            root.addBody(body)

        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Simulation')


        esc = False
        while not esc:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esc = True

                #navigating with arrowkeys
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_LEFT:
                        pass
                    if event.type == pygame.K_RIGHT:
                        pass
                    if event.type == pygame.K_UP:
                        pass
                    if event.type == pygame.K_DOWN:
                        pass

                #zooming with the mouse wheel
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #forward roll
                    if event.button == 4:
                        glTranslatef(0.0, 0.0, 1)
                    #backwards roll
                    if event.button == 5:
                        glTranslatef(0.0, 0.0, -1)


        pygame.display.flip()

        #changes due to gravity

    def generateSystem(self):
        w = self.width
        h = self.height
        system = np.array()
        if path.exists("system.txt"):
            for i in range(len(constants.m)):
                mass = constants.m[i]
                position = (constants.x[i], constants.y[i])
                velocity = (constants.vx[i], constants.vy[i])
                # size?
                
                #
                system.append(Body(mass, position, velocity, size))
        else:
            for i in range(self.numofp):
                x = random.randint(0, w)
                y = random.randint(0, h)
                pos = Dist(x, y)
                vx = random.random()
                vy = random.random()
                velocity = (vx, vy)
                mass = random.random() * constants.cons_m
                system.append(Body(mass, position, velocity, size))
            return system

    def drawSimulation(self, screen, rootNode):
        screen.fill(background_colour)
        rootNode.pydraw(pygame.draw, screen)
        pygame.display.update()


if __name__ == "__main__": Simulation()
