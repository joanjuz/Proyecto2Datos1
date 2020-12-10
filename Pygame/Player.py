import pygame
from spritesheet import Spritesheet
from time import  sleep
#####################################################################################
W1 = Spritesheet('WalkR')
walkRight = W1.get_spritte()

W2 = Spritesheet('WalkL')
walkLeft = W2.get_spritte()

G1 = Spritesheet('GolpeL')
golpeI = G1.get_spritte()

G2 = Spritesheet('GolpeR')
golpeD = G2.get_spritte()

P1 = Spritesheet('punchL')
punchI = P1.get_spritte()

P2 = Spritesheet('punchR')
punchD = P2.get_spritte()

J1 = Spritesheet('jumpR')
jumpD = J1.get_spritte()

J2 = Spritesheet('jumpL')
jumpI = J2.get_spritte()

S1 = Spritesheet('Stand')
Stand = S1.get_spritte()

#############################################################################################
class player(object):
    def __init__(self):
        ################################
        self.image = walkRight[0]
        self.rect = self.image.get_rect()
        ###################################
        self.isJump = False
        self.isjumpcount = 0
        self.on_ground = False
        ###########################
        self.gravity, self.friction = .13, -.10
        ###############################
        self.position = pygame.math.Vector2(0,0)
        self.vel = pygame.math.Vector2(0, 0)
        #################
        self.acceleration = pygame.math.Vector2(0, self.gravity)
        ################
        self.standing = True
        self.left = False
        self.right = False
        self.walkCount = 0
        self.scount = 0
        ###############################
        self.hit = False
        ###############################
        self.hitbox = (self.position.x + 17, self.position.y + 11, 29, 52)
        ###############################
        self.punch = False
        self.punchCount = 0
        self.golpe = False
        self.golpeCount = 0
        ###############################

        ###############################
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.FACING_LEFT = False

        ################
        self.pow = False
        self.shield = False
        self.jumpow = False
        self.powpunch = False
        self.useshield = False
        self.usejump = False
        self.catch = None


    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), self.rect, 2)
        if self.isjumpcount + 1 >= 100:
            self.isjumpcount = 0
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if self.punchCount + 1 >= 42:
            self.punchCount = 0
            self.standing = True
            self.rect = self.image.get_rect()
            self.punch = False

        if self.golpeCount + 1 >= 36:
            self.golpeCount = 0
            self.golpe = False
        if self.scount + 1 == 30:
            self.scount = 0

        if not (self.standing):
            if self.isJump:
                if self.left:
                    win.blit(jumpI[self.isjumpcount // 10], (self.position.x, self.position.y))
                    self.isjumpcount += 1
                    self.rect.w = 40
                elif self.right:
                    win.blit(jumpD[self.isjumpcount // 10], (self.position.x, self.position.y))
                    self.isjumpcount += 1
                    self.rect.w = 40
            elif self.golpe:
                if self.left:
                    win.blit(punchI[self.golpeCount // 6], (self.position.x, self.position.y))
                    self.golpeCount += 1

                if self.right:
                    win.blit(punchD[self.golpeCount // 6], (self.position.x, self.position.y))
                    self.golpeCount += 1

            elif self.punch:
                if self.left:
                    win.blit(golpeI[self.punchCount // 6], (self.position.x, self.position.y))
                    self.punchCount += 1

                    pygame.draw.rect(win, (255, 0, 0), self.rect, 2)

                if self.right:
                    win.blit(golpeD[self.punchCount // 6], (self.position.x, self.position.y))
                    self.punchCount += 1
                    pygame.draw.rect(win, (255, 0, 0), self.rect, 2)

            elif self.left:
                win.blit(walkLeft[self.walkCount // 6], (self.position.x, self.position.y))
                self.walkCount += 1
                self.rect.w = 40
                pygame.draw.rect(win, (255, 0, 0), self.rect, 2)
            elif self.right:
                win.blit(walkRight[self.walkCount // 6], (self.position.x, self.position.y))
                self.walkCount += 1
                self.rect.w = 40
                pygame.draw.rect(win, (255, 0, 0), self.rect, 2)
        else:
            if self.isJump:
                if self.left:
                    win.blit(jumpI[self.isjumpcount // 10], (self.position.x, self.position.y))
                    self.isjumpcount += 1
                else:
                    win.blit(jumpD[self.isjumpcount // 10], (self.position.x, self.position.y))
                    self.isjumpcount += 1
            elif self.golpe:
                if self.left:
                    win.blit(punchI[self.golpeCount // 6], (self.position.x, self.position.y))
                    self.golpeCount += 1
                else:
                    win.blit(punchD[self.golpeCount // 6], (self.position.x, self.position.y))
                    self.golpeCount += 1
            elif self.punch:
                if self.left:
                    win.blit(golpeI[self.punchCount // 6], (self.position.x, self.position.y))
                    self.punchCount += 1
                    self.hitbox = (self.position.x - 10, self.position.y + 45, 31, 20)
                    pygame.draw.rect(win, (255, 0, 0), self.rect, 2)

                else:
                    win.blit(golpeD[self.punchCount // 6], (self.position.x, self.position.y))
                    self.punchCount += 1
                    self.hitbox = (self.position.x + 70, self.position.y + 45, 31, 20)
                    pygame.draw.rect(win, (255, 0, 0), self.rect, 2)

            else:
                win.blit(Stand[self.scount // 6], (self.position.x, self.position.y))
                self.scount += 1
                self.rect.w = 40
                pygame.draw.rect(win, (255, 0, 0), self.rect, 2)

    def update(self,dt,players,platform,powers):
        self.horizontal_movement(dt)
        self.checkCollisionsx(players)
        self.checkCollisionspx(platform)
        self.vertical_movement(dt)
        self.checkCollisionsy(players)
        self.checkCollisionspy(platform)
        self.checkCollisionspowers(powers)

    def horizontal_movement(self,dt):
        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x -= .5
        elif self.RIGHT_KEY:
            self.acceleration.x += .5
        self.acceleration.x += self.vel.x * self.friction
        self.vel.x += self.acceleration.x * dt
        self.limit_velocity(15)
        self.position.x += self.vel.x * dt + (self.acceleration.x * .5)*(dt * dt)
        if not self.punch:
            self.rect.x = self.position.x + 20
        elif self.punch:
            if self.right:
                self.rect.x = self.position.x + 75
            else:
                self.rect.x = self.position.x - 20


    def vertical_movement(self,dt):
        self.vel.y +=  self.acceleration.y * dt
        if self.vel.y > 7: self.vel.y = 7
        self.position.y += self.vel.y * dt + (self.acceleration.y * .5) *(dt * dt)
        if not self.punch:
            self.rect.bottom = self.position.y + 150
        else:
            self.rect.y = self.position.y + 100
    def limit_velocity(self,max_vel):
        min(-max_vel,max(self.vel.x,max_vel))
        if abs(self.vel.x) < .01: self.vel.x = 0

    def jump(self):
        if self.on_ground or self.usejump:
            self.isJump = True
            self.vel.y -= 8
            self.on_ground = False
            self.usejump = False
    def get_hits(self,players):
        hits = []
        for player in players:
            if self.rect.colliderect(player):
                hits.append(player)
        return hits
    def checkCollisionsx(self,players):
        collisions = self.get_hits(players)
        for player in collisions:
            if not self.punch and not player.punch:
                if self.vel.x > 0:
                    self.position.x = player.rect.left - self.rect.w - 20
                    self.rect.x = self.position.x + 20
                    if player.standing == True:
                        player.vel.x += 0.25
                elif self.vel.x < 0:
                    self.position.x = player.rect.right - 20
                    self.rect.x = self.position.x + 20
                    if player.standing == True:
                        player.vel.x -= 0.25
            else:
                if self.punch:
                    if not player.useshield:
                        if self.right:
                            player.right = False
                            player.left = True
                            player.golpe = True
                            player.vel.x += 40
                        else:
                            player.left = False
                            player.right = True
                            player.golpe = True
                            player.vel.x -= 40
                    else:
                        self.punch = False
                        player.useshield = False



    def checkCollisionsy(self,players):
        self.on_ground = False
        self.rect.bottom += 2
        collisions = self.get_hits(players)
        for player in collisions:
            if not self.punch and not player.punch:
                if self.vel.y > 0:
                    self.on_ground = True
                    self.isJump = False
                    self.vel.y = 0
                    self.position.y = player.rect.top - 150
                    self.rect.bottom = self.position.y + 150
                elif self.vel.y < 0:
                    self.vel.y = 0
                    self.position.y = player.rect.bottom + self.rect.h
                    self.rect.bottom = self.position.y
            else:
                if self.punch:
                    if not player.useshield:
                        if self.right:
                            player.right = False
                            player.left = True
                            player.golpe = True
                            player.vel.y -= 6
                        else:
                            player.left = False
                            player.right = True
                            player.golpe = True
                            player.vel.y -= 6
                    else:
                        self.punch = False
                        player.useshield = False


    def checkCollisionspx(self,platform):
        collisions = self.get_hits(platform)
        for plat in collisions:
            if self.vel.x > 0:
                self.position.x = plat.rect.left - self.rect.w - 20
                self.rect.x = self.position.x + 20
            elif self.vel.x < 0:
                self.position.x = plat.rect.right - 20
                self.rect.x = self.position.x + 20
    def checkCollisionspy(self,platform):
        self.on_ground = False
        self.rect.bottom += 1
        collisions = self.get_hits(platform)
        for plat in collisions:
            if self.vel.y > 0:
                self.on_ground = True
                self.isJump = False
                self.vel.y = 0
                self.position.y = plat.rect.top - 150
                self.rect.bottom = self.position.y + 150
            elif self.vel.y < 0:
                self.vel.y = 0
                self.position.y = plat.rect.bottom + self.rect.h
                self.rect.bottom = self.position.y
    def checkCollisionspowers(self,pows):
        collisions = self.get_hits(pows)
        if not self.pow:
            for power in collisions:
                if power.power == "shield":
                    self.pow = True
                    self.shield = True
                    self.powpunch = False
                    self.jumpow = False
                    power.drop = True
                    self.catch = power
                elif power.power == "jump":
                    self.pow = True
                    self.shield = False
                    self.powpunch = False
                    self.jumpow = True
                    power.drop = True
                    self.catch = power
                elif power.power == "punch":
                    self.pow = True
                    self.shield = False
                    self.powpunch = True
                    self.jumpow = False
                    power.drop = True
                    self.catch = power
