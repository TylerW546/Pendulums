from Ball import Ball
import pygame

class Pendulum():
    pendulums = []

    def __init__(self, ball1, ball2, lineColor = (200,0,0)):
        self.ball1 = ball1
        self.ball2 = ball2
        self.lineColor = lineColor
        Pendulum.pendulums.append(self)
    
    def draw(self, screen):
        pygame.draw.lines(screen, self.lineColor, False, [(self.ball1.position.x, self.ball1.position.y), (self.ball2.position.x, self.ball2.position.y)])
        self.ball1.draw(screen)
        self.ball2.draw(screen)
        
    @staticmethod
    def drawAll(screen):
        for p in Pendulum.pendulums:
            p.draw(screen)