from Vector2 import Vector2
import pygame
import math
import random

g = 100

def thetaFromPoints(p1, p2):
    x_diff = p2.x-p1.x
    y_diff = p2.y-p1.y

    if x_diff == 0:
        if y_diff > 0:
            return math.pi/2
        else:
            return math.pi*3/2
    elif y_diff == 0:
        if x_diff > 0:
            return 0
        else:
            return math.pi/2
    else:
        if x_diff > 0:
            return (math.atan(y_diff/x_diff) + math.pi*2) % (math.pi*2)
        else:
            return (math.atan(y_diff/x_diff) + math.pi*3) % (math.pi*2)

class Ball():
    balls = []

    def __init__(self, initial_point, mass=10, color=(0,0,200), parent=None):
        self.initial_point = initial_point
        self.position = initial_point
        self.velocity = Vector2()
        self.mass = mass
        self.color = color
        self.parent = parent

        self.theta_to_parent = 0
        self.global_theta = 0

        self.angular_momentum = math.pi/1024 * random.randint(0,1000)/1000 * [1,-1][random.randint(0,1)]

        if self.parent:
            self.distance_to_parent = math.dist((self.position.x, self.position.y), (parent.position.x, parent.position.y))
            self.global_theta = thetaFromPoints(self.parent.position, self.position)
            self.theta_to_parent = self.global_theta - self.parent.global_theta

        Ball.balls.append(self)
    
    def physics(self):
        self.global_theta = thetaFromPoints(self.parent.position, self.position)
        self.theta_to_parent = self.global_theta - self.parent.global_theta
        


        self.position.x += self.velocity.x
        self.position.y += self.velocity.y


    @staticmethod
    def physicsAll():
        for ball in Ball.balls:
            if ball.parent:
                ball.physics()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), 5)

