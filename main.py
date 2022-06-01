from Vector2 import Vector2
from Ball import Ball
from Pendulum import Pendulum
from Path import Path

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
    
    
    length = 2
    #Pendulum(Vector2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2-100), [random.randint(0,359) for i in range(length)], [50 for i in range(length)])
    
    length = 5
    for x in range(100, 400, 50):
        Pendulum(Vector2(x,SCREEN_HEIGHT/2-100), [90 for i in range(length)], [50 for i in range(length)])
    
    show_pends = True
    delay = 0
    max_delay = 10
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            Ball.processEvent(event)
            
            if event.type == pygame.MOUSEBUTTONDOWN and delay == 0:
                show_pends = not(show_pends)
                delay = max_delay
        
        if delay > 0:
            delay -= 1
        
        screen.fill(background)

        Ball.pathAll()
        Path.drawAll(screen)
        
        if show_pends:
            Pendulum.drawAll(screen)
        Ball.physicsAll()
        
        
        

        pygame.display.update()
        
        time.sleep(.001)

if __name__ == "__main__":
    main()