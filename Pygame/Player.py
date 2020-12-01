import pygame
walkRight = [pygame.image.load('Recursos/Caminar/caminarD1.png'), pygame.image.load('Recursos/Caminar/caminarD2.png'),
             pygame.image.load('Recursos/Caminar/caminarD3.png'), pygame.image.load('Recursos/Caminar/caminarD4.png')]
walkLeft = [ pygame.image.load('Recursos/Caminar/caminarI1.png'), pygame.image.load('Recursos/Caminar/caminarI2.png'),
             pygame.image.load('Recursos/Caminar/caminarI3.png'), pygame.image.load('Recursos/Caminar/caminarI4.png')]

golpeI = [pygame.image.load('Recursos/Punch/PunchI1.png'),pygame.image.load('Recursos/Punch/PunchI2.png'),pygame.image.load('Recursos/Punch/PunchI3.png'),
          pygame.image.load('Recursos/Punch/PunchI4.png'),pygame.image.load('Recursos/Punch/PunchI5.png'),pygame.image.load('Recursos/Punch/PunchI6.png'),
          pygame.image.load('Recursos/Punch/PunchI7.png')]
golpeD = [pygame.image.load('Recursos/Punch/PunchD1.png'),pygame.image.load('Recursos/Punch/PunchD2.png'),pygame.image.load('Recursos/Punch/PunchD3.png'),
          pygame.image.load('Recursos/Punch/PunchD4.png'),pygame.image.load('Recursos/Punch/PunchD5.png'),pygame.image.load('Recursos/Punch/PunchD6.png'),
          pygame.image.load('Recursos/Punch/PunchD7.png')]
punchI = [pygame.image.load('Recursos/Golpe/golpeI1.png'),pygame.image.load('Recursos/Golpe/golpeI2.png'),pygame.image.load('Recursos/Golpe/golpeI3.png'),
          pygame.image.load('Recursos/Golpe/golpeI4.png'),pygame.image.load('Recursos/Golpe/golpeI5.png'),pygame.image.load('Recursos/Golpe/golpeI6.png')]
punchD = [pygame.image.load('Recursos/Golpe/golpeD1.png'),pygame.image.load('Recursos/Golpe/golpeD2.png'),pygame.image.load('Recursos/Golpe/golpeD3.png'),
          pygame.image.load('Recursos/Golpe/golpeD4.png'),pygame.image.load('Recursos/Golpe/golpeD5.png'),pygame.image.load('Recursos/Golpe/golpeD6.png')]
jumpD = [pygame.image.load('Recursos/Salto/SaltoD1.png'),pygame.image.load('Recursos/Salto/SaltoD2.png'),pygame.image.load('Recursos/Salto/SaltoD3.png'),
          pygame.image.load('Recursos/Salto/SaltoD4.png'),pygame.image.load('Recursos/Salto/SaltoD5.png'),pygame.image.load('Recursos/Salto/SaltoD6.png'),pygame.image.load('Recursos/Salto/SaltoD7.png'),
          pygame.image.load('Recursos/Salto/SaltoD8.png'),pygame.image.load('Recursos/Salto/SaltoD9.png'),pygame.image.load('Recursos/Salto/SaltoD10.png')]
jumpI = [pygame.image.load('Recursos/Salto/SaltoI1.png'),pygame.image.load('Recursos/Salto/SaltoI2.png'),pygame.image.load('Recursos/Salto/SaltoI3.png'),
          pygame.image.load('Recursos/Salto/SaltoI4.png'),pygame.image.load('Recursos/Salto/SaltoI5.png'),pygame.image.load('Recursos/Salto/SaltoI6.png'),pygame.image.load('Recursos/Salto/SaltoI7.png'),
          pygame.image.load('Recursos/Salto/SaltoI8.png'),pygame.image.load('Recursos/Salto/SaltoI9.png'),pygame.image.load('Recursos/Salto/SaltoI10.png')]

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.isjumpcount = 0
        self.left = False
        self.right = False
        self.hit = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.punch = False
        self.punchCount = 0
        self.golpe = False
        self.golpeCount = 0
        self.bajada = 10

    def draw(self, win):
        if self.isjumpcount + 1 >= 30:
            self.isjumpcount = 0
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if self.punchCount + 1 >= 21:
            self.punchCount = 0
            self.punch = False
        if self.golpeCount + 1 >= 18:
            self.golpeCount = 0
            self.golpe = False

        if not (self.standing):
            if self.isJump:
                if self.left:
                    win.blit(jumpI[self.isjumpcount // 3], (self.x, self.y))
                    self.isjumpcount += 1
                elif self.right:
                    win.blit(jumpD[self.isjumpcount // 3], (self.x, self.y))
                    self.isjumpcount += 1
            elif self.golpe:
                if self.left:
                    win.blit(punchI[self.golpeCount // 3], (self.x, self.y))
                    self.golpeCount += 1

                if self.right:
                    win.blit(punchD[self.golpeCount // 3], (self.x, self.y))
                    self.golpeCount += 1

            elif self.punch:
                if self.left:
                    win.blit(golpeI[self.punchCount // 3], (self.x, self.y))
                    self.punchCount += 1
                    self.hitbox = (self.x - 10, self.y + 45, 31, 20)
                    pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

                if self.right:
                    win.blit(golpeD[self.punchCount // 3], (self.x, self.y))
                    self.punchCount += 1
                    self.hitbox = (self.x + 70, self.y + 45, 31, 20)
                    pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

            elif self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 17, self.y + 2, 31, 120)
                pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 23, self.y + 2, 31, 120)
                pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        else:
            if self.isJump:
                if self.left:
                    win.blit(jumpI[self.isjumpcount // 3], (self.x, self.y))
                    self.isjumpcount += 1
                else:
                    win.blit(jumpD[self.isjumpcount // 3], (self.x, self.y))
                    self.isjumpcount += 1
            elif self.golpe:
                if self.left:
                    win.blit(punchI[self.golpeCount // 3], (self.x, self.y))
                    self.golpeCount += 1
                else:
                    win.blit(punchD[self.golpeCount // 3], (self.x, self.y))
                    self.golpeCount += 1
            elif self.punch:
                if self.left:
                    win.blit(golpeI[self.punchCount // 3], (self.x, self.y))
                    self.punchCount += 1
                    self.hitbox = (self.x - 10, self.y + 45, 31, 20)
                    pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

                else:
                    win.blit(golpeD[self.punchCount // 3], (self.x, self.y))
                    self.punchCount += 1
                    self.hitbox = (self.x + 70, self.y + 45, 31, 20)
                    pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

            elif self.right:
                win.blit(walkRight[0], (self.x, self.y))
                self.hitbox = (self.x + 23 , self.y + 2, 31, 120)
                pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            else:
                win.blit(walkLeft[0], (self.x, self.y))
                self.hitbox = (self.x + 17, self.y + 2, 31, 120)
                pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)