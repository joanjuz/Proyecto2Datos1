import pygame
import random
from spritesheet import  Spritesheet
class powers(object):
    def __init__(self,power,x,y):
        self.power = power
        self.get = Spritesheet(self.power)
        self.image = self.get.get_spritte()[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = pygame.math.Vector2(0,0)
        self.acceleration = pygame.math.Vector2(0,.1)
        self.on_ground = False
        self.col = False
        self.drop = False

    def draw(self,win):
        if not self.col and not self.drop:
            win.blit(self.image,(self.rect.x,self.rect.y))
        elif self.col or self.drop:
            self.rect.x=random.randint(100,1700)
            self.rect.y = 40
            self.col = False



    def update(self,dt,plat):
        self.checkCollisionspy(plat)
    def checkCollisionspy(self,platform):
        if not self.on_ground:
            self.rect.bottom += 4
        if self.rect.y >= 1000:
            self.col = True

    def get_hits(self,players):
        hits = []
        for player in players:
            if self.rect.colliderect(player):
                hits.append(player)
        return hits