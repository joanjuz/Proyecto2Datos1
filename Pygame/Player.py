import pygame
walkRight = [pygame.image.load('Recursos/Sprittes correr/R1.png'), pygame.image.load('Recursos/Sprittes correr/R2.png'), pygame.image.load('Recursos/Sprittes correr/R3.png'),
             pygame.image.load('Recursos/Sprittes correr/R4.png'), pygame.image.load('Recursos/Sprittes correr/R5.png'), pygame.image.load('Recursos/Sprittes correr/R6.png'),
             pygame.image.load('Recursos/Sprittes correr/R7.png'), pygame.image.load('Recursos/Sprittes correr/R8.png'),pygame.image.load("Recursos/Sprittes correr/R9.png")]
walkLeft = [pygame.image.load('Recursos/Sprittes correr/L1.png'), pygame.image.load('Recursos/Sprittes correr/L2.png'), pygame.image.load('Recursos/Sprittes correr/L3.png'),
             pygame.image.load('Recursos/Sprittes correr/L4.png'), pygame.image.load('Recursos/Sprittes correr/L5.png'), pygame.image.load('Recursos/Sprittes correr/L6.png'),
             pygame.image.load('Recursos/Sprittes correr/L7.png'), pygame.image.load('Recursos/Sprittes correr/L8.png'), pygame.image.load("Recursos/Sprittes correr/L9.png")]

golpeI = [pygame.image.load('Recursos/Sprittes golpear/L1.png'),pygame.image.load('Recursos/Sprittes golpear/L2.png'),pygame.image.load('Recursos/Sprittes golpear/L3.png'),
          pygame.image.load('Recursos/Sprittes golpear/L4.png'),pygame.image.load('Recursos/Sprittes golpear/L5.png'),pygame.image.load('Recursos/Sprittes golpear/L6.png'),
          pygame.image.load('Recursos/Sprittes golpear/L7.png')]
golpeD = [pygame.image.load('Recursos/Sprittes golpear/R1.png'),pygame.image.load('Recursos/Sprittes golpear/R2.png'),pygame.image.load('Recursos/Sprittes golpear/R3.png'),
          pygame.image.load('Recursos/Sprittes golpear/R4.png'),pygame.image.load('Recursos/Sprittes golpear/R5.png'),pygame.image.load('Recursos/Sprittes golpear/R6.png'),
          pygame.image.load('Recursos/Sprittes golpear/R7.png')]




class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.hit = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.punch = False
        self.punchCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.punchCount + 1 >= 21:
            self.punchCount = 0
            self.punch = False

        if not (self.standing):
            if self.punch:
                if self.left:
                    win.blit(golpeI[self.punchCount // 3], (self.x, self.y))
                    self.punchCount += 1
                    self.hitbox = (self.x + 17, self.y + 2, 31, 120)
                if self.right:
                    win.blit(golpeD[self.punchCount // 3], (self.x, self.y))
                    self.punchCount += 1
                    self.hitbox = (self.x + 17, self.y + 2, 31, 120)
            elif self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 17, self.y + 2, 31, 120)
                pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 50, self.y + 2, 31, 120)
                pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        else:
            if self.punch:
                if self.left:
                    win.blit(golpeI[self.punchCount // 3], (self.x, self.y))
                    self.punchCount += 1
                    self.hitbox = (self.x + 17, self.y + 2, 31, 120)
                if self.right:
                    win.blit(golpeD[self.punchCount // 3], (self.x, self.y))
                    self.punchCount += 1
                    self.hitbox = (self.x + 17, self.y + 2, 31, 120)
            elif self.right:
                win.blit(walkRight[0], (self.x, self.y))
                self.hitbox = (self.x + 50, self.y + 2, 31, 120)
                pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            else:
                win.blit(walkLeft[0], (self.x, self.y))
                self.hitbox = (self.x + 17, self.y + 2, 31, 120)
                pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)