from Ball import Ball
from Path import Path
from Vector2 import Vector2
import pygame
import math
import random

class PendulumConnection():
    def __init__(self, ball1, ball2, lineColor = (200,0,0)):
        self.ball1 = ball1
        self.ball2 = ball2
        self.lineColor = lineColor
    
    def draw(self, screen):
        pygame.draw.lines(screen, self.lineColor, False, [(self.ball1.position.x, self.ball1.position.y), (self.ball2.position.x, self.ball2.position.y)])
        self.ball1.draw(screen)
        self.ball2.draw(screen)

            
class Pendulum():
    pendulums = []
    
    def __init__(self, initial_point, angles, lengths):
        assert len(angles) == len(lengths), "The length of list angles and list lengths must be the same for a pendulum object"
        Pendulum.pendulums.append(self)
        
        
        self.ball_list = [Ball(Vector2(initial_point.x, initial_point.y))]
        
        
        last_point = initial_point
        for i in range(len(angles)):
            last_point = last_point.add(Vector2(math.cos(math.radians(angles[i]))*lengths[i], math.sin(math.radians(angles[i]))*lengths[i]))
            self.ball_list.append(Ball(Vector2(last_point.x, last_point.y), parent = self.ball_list[i]))
        
        self.ball_list[-1].path_object = Path(color=[random.randrange(255) for i in range(3)])
        
        self.connections = []
        for i in range(len(self.ball_list)-1):
            self.connections.append(PendulumConnection(self.ball_list[i], self.ball_list[i+1]))
    
    def draw(self, screen):
        for connection in self.connections:
            connection.draw(screen)
    
    @staticmethod
    def drawAll(screen):
        for p in Pendulum.pendulums:
            p.draw(screen)