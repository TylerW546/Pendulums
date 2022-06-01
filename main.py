from Vector2 import Vector2
from Ball import Ball
from Pendulum import Pendulum

import math
import random
import time

import pygame
from pygame.locals import *

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
settingsColor = (100,100,200)

white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
blue = (0, 0, 255)
background = black

pygame.font.init()
defaultFont = pygame.font.SysFont('Times New Roman', 20)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    chains = 4
    balls = [[Ball(Vector2(SCREEN_WIDTH/2-125 + 50*i, SCREEN_HEIGHT/2-100))] for i in range(chains)]
    for i in range(chains):
        for j in range(random.randint(4,10)):
            balls[i].append(Ball(Vector2(SCREEN_WIDTH/2-125 + 50*i + 5 + 5*j, SCREEN_HEIGHT/2-75+25*j), parent=balls[i][j]))

        for j in range(len(balls[i])-1):
            Pendulum(balls[i][j], balls[i][j+1])
    
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #Ball.processEvent(event)
            
        screen.fill(background)

        Pendulum.drawAll(screen)
        Ball.physicsAll()

        pygame.display.update()
        
        time.sleep(.001)

if __name__ == "__main__":
    main()