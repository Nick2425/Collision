import pygame, os, math
tick = 0.01
objects = []
collisionCount = 0

class Thing():    
    def __init__(self, mass = float, vi = pygame.math.Vector2(), position = pygame.math.Vector2(), w = 1, h = 1, color = (255,255,255)):
        objects.append(self)
        self.mass = mass
        self.v = pygame.math.Vector2(vi, 0) 
        self.pos = position
        self.size = pygame.math.Vector2(w, h)
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)
        self.hitbox = [self.pos.x, self.pos.x + self.size.x, self.pos.y, self.pos.y + self.size.y]
        self.color = color
        self.center = pygame.math.Vector2(0,0)
    def move(self):
        self.center.x = self.pos.x + 0.5*self.size.x
        self.center.y = self.pos.y + 0.5*self.size.y
        self.pos.x += self.v.x*0.01
        self.hitbox = [self.pos.x, self.pos.x + self.size.x, self.pos.y, self.pos.y + self.size.y]
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect, 1)
        pygame.draw.circle(pygame.display.get_surface(), (255,0,0), (self.pos.x, self.pos.y), 10)
        self.collide()

    def collide(self):
        for x in objects:
            if self != x:
                print("!")
                if overlap(self, x):
                    print("collision")
                    # m1v1^2 + m2v2^2 = m1v3^2 + m2v4^2
                    # m1v1 + m2v2 = m1v3 + m1v4    
                    self.v =  (self.v*(self.mass/x.mass - 1) + 2*x.v)/(self.mass/x.mass + 1)
                    self.pos += self.v*0.1


def overlap(a, b):
    if a.center.x > b.hitbox[0] and a.center.x < b.hitbox[1]:
        if a.center.y > b.hitbox[2] and a.center.y < b.hitbox[3]:
            return True