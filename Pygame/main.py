import pygame
from Player import  player
pygame.init()

win = pygame.display.set_mode((1900, 1000))

pygame.display.set_caption("First Game")
#char = pygame.image.load('standing.png')

clock = pygame.time.Clock()
bg = pygame.image.load('Recursos/Backgroung/bg.png')
#bulletSound = pygame.mixer.Sound('bullet.wav')
#hitSound = pygame.mixer.Sound('hit.wav')

#music = pygame.mixer.music.load('music.mp3')
#pygame.mixer.music.play(-1)

score = 0


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
        player1.standing = False


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
