from Point import Point
import pygame
import math

class Ball():
    balls = []

    def __init__(self, initial_point, mass=10, color=(0,0,200), parent=None):
        self.initial_point = initial_point
        self.position = initial_point
        self.mass = mass
        self.color = color
        self.parent = parent

        if self.parent:
            self.distance_to_parent = math.dist((self.position.x, self.position.y), (parent.position.x, parent.position.y))

        Ball.balls.append(self)
    
    @staticmethod
    def physics():
        for ball in Ball.balls:
            if ball.parent:
                ball.position.y += 1

                mag_mult = ball.distance_to_parent/math.dist((ball.position.x, ball.position.y), (ball.parent.position.x, ball.parent.position.y))

                ball.position.x = ball.parent.position.x + (ball.parent.position.x - ball.position.x) * mag_mult
                ball.position.y = ball.parent.position.y + (ball.parent.position.y - ball.position.y) * mag_mult

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), 5)

