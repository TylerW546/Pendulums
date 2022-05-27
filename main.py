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
    balls = [Ball(Vector2(SCREEN_WIDTH/2+random.randint(0, 200)-100, SCREEN_HEIGHT/2-100))]
    for i in range(1):
        balls.append(Ball(Vector2(SCREEN_WIDTH/2+random.randint(0, 20)-10, 50*i+SCREEN_HEIGHT/2-50), parent = balls[i]))

    for i in range(len(balls)-1):
        Pendulum(balls[i], balls[i+1])
    
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        screen.fill(background)

        Pendulum.drawAll(screen)
        Ball.physicsAll()

        pygame.display.update()
        
        time.sleep(.001)

if __name__ == "__main__":
    main()