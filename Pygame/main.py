import pygame

pygame.init()

win = pygame.display.set_mode((1900, 1000))

pygame.display.set_caption("First Game")

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
bg = pygame.image.load('Recursos/Backgroung/bg.png')
#char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

#bulletSound = pygame.mixer.Sound('bullet.wav')
#hitSound = pygame.mixer.Sound('hit.wav')

#music = pygame.mixer.music.load('music.mp3')
#pygame.mixer.music.play(-1)

score = 0


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
                win.blit(golpeI[self.punchCount // 3], (self.x, self.y))
                self.punchCount += 1
                self.hitbox = (self.x + 17, self.y + 2, 31, 120)
            if self.left:
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
                win.blit(golpeI[self.punchCount // 3], (self.x, self.y))
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





class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (350, 10))
    player1.draw(win)
    player2.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# mainloop
font = pygame.font.SysFont('comicsans', 30, True)
player1 = player(300, 700, 100, 150)
player2 = player(700, 700, 100, 150)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)
    if player1.hitbox[1] < player2.hitbox[1] + player2.hitbox[3] and player1.hitbox[1] + player1.hitbox[3] > player2.hitbox[1]:
        if player1.hitbox[0] + player1.hitbox[2] > player2.hitbox[0] and player1.hitbox[0] < player2.hitbox[0] + player2.hitbox[2]:
            player1.hit = True
            if player1.right == True:
                if player2.right == True:
                    player1.x -= player1.vel
                    player2.x += player2.vel
                else:
                    player2.x += player2.vel

            else:
                if player2.right == False:
                    player1.x += player1.vel
                    player2.x -= player2.vel
                else:
                    player2.x -= player2.vel
        else:
            player1.hit = False
    else:
        player1.hit = False
    if player2.hitbox[1] < player1.hitbox[1] + player1.hitbox[3] and player2.hitbox[1] + player2.hitbox[3] > player1.hitbox[1]:
        if player2.hitbox[0] + player2.hitbox[2] > player1.hitbox[0] and player2.hitbox[0] < player1.hitbox[0] + player1.hitbox[2]:
            player2.hit = True
            if player2.right == True:
                if player1.right == True:
                    player2.x += player2.vel
                    player1.x -= player1.vel
                player1.x += player1.vel
            else:
                if player1.right == False:
                    player2.x -= player2.vel
                    player1.x += player1.vel
                else:
                    player1.x -= player1.vel
        else:
            player2.hit = False
    else:
        player2.hit = False

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < player2.hitbox[1] + player2.hitbox[3] and bullet.y + bullet.radius > player2.hitbox[1]:
            if bullet.x + bullet.radius > player2.hitbox[0] and bullet.x - bullet.radius < player2.hitbox[0] + \
                    player2.hitbox[2]:
                #hitSound.play()
                player2.hit = True
                bullets.pop(bullets.index(bullet))

        if bullet.x < 1550 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_s]:
        print("punch")
        player1.punch = True
        player1.right = False
        player1.standing = False
        player1.left = False


    if keys[pygame.K_a] and player1.x > player1.vel:
        player1.x -= player1.vel
        player1.left = True
        player1.right = False
        player1.standing = False
        player1.punch = False
    elif keys[pygame.K_d] and player1.x < 1550 - player1.width - player1.vel:
        player1.x += player1.vel
        player1.right = True
        player1.left = False
        player1.standing = False
        player1.punch = False

    else:
        player1.standing = True
        player1.walkCount = 0

    if not (player1.isJump):
        if keys[pygame.K_w]:
            player1.isJump = True
            player1.right = False
            player1.left = False
            player1.punch = False
            player1.walkCount = 0
    else:
        if player1.jumpCount >= -10:
            neg = 1
            if player1.jumpCount < 0:
                neg = -1
            player1.y -= (player1.jumpCount ** 2) * 0.5 * neg
            player1.jumpCount -= 1
        else:
            player1.isJump = False
            player1.jumpCount = 10
    if keys[pygame.K_j] and player2.x > player2.vel:
        player2.x -= player2.vel
        player2.left = True
        player2.right = False
        player2.standing = False
    elif keys[pygame.K_l] and player2.x < 1550 - player2.width - player2.vel:
        player2.x += player2.vel
        player2.right = True
        player2.left = False
        player2.standing = False
    else:
        player2.standing = True
        player2.walkCount = 0

    if not (player2.isJump):
        if keys[pygame.K_i]:
            player2.isJump = True
            player2.right = False
            player2.left = False
            player2.walkCount = 0
    else:
        if player2.jumpCount >= -10:
            neg = 1
            if player2.jumpCount < 0:
                neg = -1
            player2.y -= (player2.jumpCount ** 2) * 0.5 * neg
            player2.jumpCount -= 1
        else:
            player2.isJump = False
            player2.jumpCount = 10
    redrawGameWindow()

pygame.quit()
