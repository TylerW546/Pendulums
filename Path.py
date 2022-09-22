import pygame
import random

class Path():
    """A Path is a colorful trail that eventually decays when it gets too long"""
    paths = []
    
    def __init__(self, color=[random.randrange(255) for i in range(3)]):
        self.points = []
        self.color = color
        
        Path.paths.append(self)
        
    def addPoint(self, point):
        """Adds a new point to the path"""
        self.points.append(point)
    
    def update(self):
        """Deletes the oldest point when the path has too many points"""
        if len(self.points) > 50:
            self.points = self.points[1:]

    def draw(self, screen):
        """Draws lines between each of the points of the path"""
        for i in range(len(self.points)-1):
            factor = i/(len(self.points)-1)
            pygame.draw.lines(screen, (self.color[0]*factor, self.color[1]*factor, self.color[2]*factor), False, [(self.points[i].x, self.points[i].y), (self.points[i+1].x, self.points[i+1].y)], 2)
            
    @staticmethod
    def drawAll(screen):
        """Draws all the paths stored in the class level list of paths"""
        for p in Path.paths:
            p.draw(screen)