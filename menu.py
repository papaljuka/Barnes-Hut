#!/usr/bin/python

import pygame, sys
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Gravity simulator")
screen = pygame.display.set_mode((900, 900), 0, 32)

font = pygame.font.SysFont(None, 20)

def write_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():

    while True:

        screen.fill((0, 0, 0))
        write_text("MAIN MENU", font, (255, 255, 255), screen, 20, 20)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        start_button = pygame.Rect(50, 100, 200, 50)
        options_button = pygame.Rect(50, 200, 200, 50)

        if start_button.collidepoint((mouse_x, mouse_y)):
            if click:
                start_simulation()
        if options_button.collidepoint((mouse_x, mouse_y)):
            if click:
                options_menu()

        pygame.draw.rect(screen, (255, 0, 0), start_button)
        pygame.draw.rect(screen, (255, 0, 0), options_button)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        mainClock.tick(60)

def start_simulation():
    running = True
    while running:
        screen.fill((0, 0, 0))
        write_text("Simulation in progress", font, (255, 255, 255), screen, 25, 25)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
 
        pygame.display.update()
        mainClock.tick(60)

def options_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))
        write_text("Options", font, (255, 255, 255), screen, 25, 25)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
 
        pygame.display.update()
        mainClock.tick(60)

main_menu()

