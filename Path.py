import pygame
import random

class Path():
    paths = []
    
    def __init__(self, color=[random.randrange(255) for i in range(3)]):
        self.points = []
        self.color = color
        
        Path.paths.append(self)
        
    def addPoint(self, point):
        self.points.append(point)
    
    def update(self):
        if len(self.points) > 50:
            self.points = self.points[1:]

    def draw(self, screen):
        for i in range(len(self.points)-1):
            factor = i/(len(self.points)-1)
            pygame.draw.lines(screen, (self.color[0]*factor, self.color[1]*factor, self.color[2]*factor), False, [(self.points[i].x, self.points[i].y), (self.points[i+1].x, self.points[i+1].y)], 2)
            
    @staticmethod
    def drawAll(screen):
        for p in Path.paths:
            p.draw(screen)