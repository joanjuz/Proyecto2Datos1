import pygame
from pygame.locals import *

pygame.init()
win = pygame.display.set_mode((750, 900,))
pygame.display.set_caption("Fist Window")


walkRight = [pygame.image.load('correr_0.png'), pygame.image.load('correr_1.png'), pygame.image.load('correr_2.png'), pygame.image.load('correr_3.png'), pygame.image.load('correr_4.png'), pygame.image.load('correr_5.png'), pygame.image.load('correr_6.png'), pygame.image.load('correr_7.png'), pygame.image.load('correr_8.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


x=50
y=650
width = 60
heigth =80
vel: int = 6
run = True
Jump = False
JumpCount = 10
left = False
rigth = False
walk= False
walkCount = 0





while run:
    pygame.time.delay(100)
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x-= vel

    if keys[pygame.K_RIGHT] and x < 750- width - vel :
        x += vel
    if not (Jump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 750 - heigth - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            Jump= True
    else:
        if JumpCount >= -10:
            neg = 1
            if JumpCount < 0:
                neg = -1
            y -= (JumpCount ** 2)* 0.5 * neg
            JumpCount -= 1

        else:
            Jump = False
            JumpCount = 10

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, heigth))
    pygame.display.update()
pygame.quit()

