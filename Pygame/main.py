import pygame
from Player import  player
from spritesheet import Spritesheet
from platform import platform
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

P1 = Spritesheet("platform")
Platform1 = P1.get_spritte()

P2 = Spritesheet("platform1")
Platform2 = P2.get_spritte()

score = 0
TARGET_FPS = 60

def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (350, 10))
    piso.draw(win)
    plataform1.draw(win)
    platform2.draw(win)
    player2.draw(win)
    player1.draw(win)
    pygame.display.update()


# mainloop
font = pygame.font.SysFont('comicsans', 30, True)
player1 = player()
player1.position.x = 500
player1.position.y = 700
player2 = player()
player2.position.x = 600
player2.position.y = 700

piso = platform(Platform1[0],450,860)
plataform1 = platform(Platform2[0],1400,650)
platform2 = platform(Platform2[1],200,650)

run = True
while run:
    dt = clock.tick(60) * .001 * TARGET_FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1.LEFT_KEY = True
                player1.left = True
                player1.right = False
                player1.standing = False
                player1.punch = False
            elif event.key == pygame.K_d:
                player1.RIGHT_KEY = True
                player1.left = False
                player1.right = True
                player1.standing = False
                player1.punch = False
            elif event.key == pygame.K_w:
                player1.jump()
            elif event.key == pygame.K_j:
                player2.LEFT_KEY = True
                player2.left = True
                player2.right = False
                player2.standing = False
                player2.punch = False
            elif event.key == pygame.K_l:
                player2.RIGHT_KEY = True
                player2.left = False
                player2.right = True
                player2.standing = False
                player2.punch = False
            elif event.key == pygame.K_i:
                player2.jump()
            elif event.key == pygame.K_s:
                player1.punchCount = 0
                player1.punch = True
                player1.standing = False
            elif event.key == pygame.K_k:
                player2.punchCount = 0
                player2.punch = True
                player2.standing = False
        ############################################
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player1.LEFT_KEY = False
                player1.right = False
                player1.standing = True
            elif event.key == pygame.K_d:
                player1.RIGHT_KEY = False
                player1.LEFT_KEY = False
                player1.left = False
                player1.standing = True
            elif event.key == pygame.K_w:
                if player1.isJump:
                    player1.vel.y *= .25
                    player1.isJump = False
            if event.key == pygame.K_j:
                player2.LEFT_KEY = False
                player2.right = False
                player2.standing = True
            elif event.key == pygame.K_l:
                player2.RIGHT_KEY = False
                player2.left = False
                player2.standing = True
            elif event.key == pygame.K_i:
                if player2.isJump:
                    player2.vel.y *= .25
                    player2.isJump = False

    player2.update(dt,[player1],[piso,platform2,plataform1])
    player1.update(dt,[player2],[piso,platform2,plataform1])
    redrawGameWindow()

pygame.quit()
