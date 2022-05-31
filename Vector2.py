import math

class Vector2():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getMagnitude(self):
        return math.dist((0,0), (self.x, self.y))

    def scalarMultiply(self, mult):
        return Vector2(self.x*mult, self.y*mult)

    def add(self, other):
        return Vector2(self.x+other.x, self.y+other.y)

    def subtract(self, other):
        return Vector2(self.x-other.x, self.y-other.y)

    def dotProduct(self, other):
        return self.x*other.x+self.y*other.y

    def decomposeTo(self, other):
        dot_prod = self.dotProduct(other)

        v_p = other.scalarMultiply(dot_prod/other.getMagnitude()/other.getMagnitude())
        v_o = self.subtract(v_p)

        return v_p, v_o

