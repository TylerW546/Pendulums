from pickle import TRUE
from Vector2 import Vector2
from Path import Path
import pygame
import math
import random

g = Vector2(0,.1)
friction_multiplier = 1
#friction_multiplier = 1.0005
#friction_multiplier = .9999

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

    def __init__(self, initial_point, mass=1, color=(0,0,200), parent=None, path_object=None):
        self.initial_point = initial_point
        self.position = initial_point
        self.accelleration = Vector2()
        self.velocity = Vector2()
        self.perpendicular_velocity = Vector2()
        
        self.last_move = Vector2()
        
        self.mass = mass
        self.color = color
        self.parent = parent
        
        self.a_p = Vector2()
        self.a_o = Vector2()
        
        self.path_object = path_object

        self.theta_to_parent = 0
        self.global_theta = 0

        self.angular_momentum = math.pi/1024 * random.randint(0,1000)/1000 * [1,-1][random.randint(0,1)]

        if self.parent:
            self.distance_to_parent = math.dist((self.position.x, self.position.y), (parent.position.x, parent.position.y))
            self.global_theta = thetaFromPoints(self.parent.position, self.position)
            self.theta_to_parent = self.global_theta - self.parent.global_theta

        Ball.balls.append(self)
    
    def physics(self):
        last_position = self.position.scalarMultiply(1)
        
        self.global_theta = thetaFromPoints(self.parent.position, self.position)
        self.theta_to_parent = self.global_theta - self.parent.global_theta
        
        self.vector_to_parent = self.parent.position.subtract(self.position)
        self.accelleration = self.accelleration.add(g)
        self.a_p, self.a_o = self.accelleration.decomposeTo(self.vector_to_parent)
        self.perpendicular_velocity = self.perpendicular_velocity.scalarMultiply(friction_multiplier).decomposeTo(self.vector_to_parent)[1].add(self.a_o)

        self.position.x += self.perpendicular_velocity.x + self.parent.last_move.x
        self.position.y += self.perpendicular_velocity.y + self.parent.last_move.y

        #self.velocity = self.velocity.scalarMultiply(.9)

        self.vector_to_parent = Vector2(self.parent.position.x - self.position.x, self.parent.position.y - self.position.y)
        self.position = self.parent.position.add(self.vector_to_parent.scalarMultiply(-self.distance_to_parent/self.vector_to_parent.getMagnitude()))

        self.accelleration = Vector2()
        
        self.last_move = self.position.subtract(last_position)

    def updatePath(self):
        self.path_object.addPoint(self.position)
        self.path_object.update()
    
    @staticmethod
    def physicsAll():
        for ball in Ball.balls:
            if ball.parent:
                ball.physics()
    
    @staticmethod
    def pathAll():
        for ball in Ball.balls:
            if ball.path_object:
                ball.updatePath()
    
    @staticmethod
    def processMouse():
        if pygame.mouse.get_pressed()[0] == True:
            pos = pygame.mouse.get_pos()
            for ball in Ball.balls:
                if ball.parent:
                    ball.accelleration = ball.accelleration.add(Vector2(pos[0]-ball.position.x, pos[1]-ball.position.y).scalarMultiply(-3/math.pow(math.dist((ball.position.x, ball.position.y), (pos[0],pos[1])), 2)))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), 2)
        #pygame.draw.lines(screen, (100,0,0), False, [(self.position.x, self.position.y), (self.position.x+self.perpendicular_velocity.x*300, self.position.y+self.perpendicular_velocity.y*300)])
        #pygame.draw.lines(screen, (100,0,0), False, [(self.position.x, self.position.y), (self.position.x+self.a_o.x*5000, self.position.y+self.a_o.y*5000)])
        #pygame.draw.lines(screen, (100,0,0), False, [(self.position.x, self.position.y), (self.position.x+self.a_p.x*5000, self.position.y+self.a_p.y*5000)])

