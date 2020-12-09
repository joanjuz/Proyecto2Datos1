import pygame, csv , os

class platform(object):
    def __init__(self,image,x,y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y

    def draw(self,surface):
        surface.blit(self.image,(self.rect.x,self.rect.y))

