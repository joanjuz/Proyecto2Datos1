import json
import os

import pygame
from Player import  player
from spritesheet import Spritesheet
from platform import platform
from Powers import powers
import random
pygame.init()
from Trees import tree

timer = 0
pygame.time.set_timer(pygame.USEREVENT,1000)
def game():
    global timer
    win = pygame.display.set_mode((1900, 1000))

    pygame.display.set_caption("First Game")
    # char = pygame.image.load('standing.png')

    clock = pygame.time.Clock()
    bg = pygame.image.load('Recursos/Backgroung/bg.png')
    board = pygame.image.load('Recursos/Board.png')
    label1 = pygame.font.SysFont('arial',28).render("Player1:", 1,(0,255,0))
    label2 = pygame.font.SysFont('arial',28).render("Player2:", 1,(0,255,0))
    label3 = pygame.font.SysFont('arial',28).render("Vidas:", 1,(0,255,0))
    label4 = pygame.font.SysFont('arial',28).render("Vidas:", 1,(0,255,0))
    label8 = pygame.font.SysFont('arial',28).render("Time: ",1,(0,255,0))
    labelwin = pygame.font.SysFont('arial',100).render("PLAYER 1 is the WINNER!",1,(0,0,0))
    labelwin1 = pygame.font.SysFont('arial',100).render("PLAYER 2 is the WINNER!",1,(0,0,0))


    counter = 120

    #Inicializar control
    joysticks = []
    for i in range(pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
    for joystick in joysticks:
        joystick.init()
    with open(os.path.join("ps4_keys.json"),'r+') as file:
        button_keys = json.load(file)

    #analog keys
    analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1}

    # bulletSound = pygame.mixer.Sound('bullet.wav')
    # hitSound = pygame.mixer.Sound('hit.wav')

    # music = pygame.mixer.music.load('music.mp3')
    # pygame.mixer.music.play(-1)

    P1 = Spritesheet("platform")
    Platform1 = P1.get_spritte()

    P2 = Spritesheet("platform1")
    Platform2 = P2.get_spritte()

    TARGET_FPS = 60
    def redrawGameWindow():
        win.blit(bg, (0, 0))
        win.blit(board, (1500, 0))
        win.blit(label1,(1530,140))
        win.blit(label2,(1530,550))
        win.blit(label3,(1530,180))
        win.blit(label4,(1530,630))
        win.blit(label5,(1630,180))
        win.blit(label6,(1630,630))

        win.blit(label8,(1530,40))
        win.blit(label7,(1600,40))

        win.blit(labelwin,(3,700))


        piso.draw(win)
        plataform1.draw(win)
        platform2.draw(win)
        pow1.draw(win)
        pow2.draw(win)
        pow3.draw(win)
        player2.draw(win)
        player1.draw(win)
        AVL.draw(win)

        pygame.display.update()


    # mainloop
    font = pygame.font.SysFont('comicsans', 30, True)
    player1 = player()
    player1.position.x = 500
    player1.position.y = 700
    player1.rect.y = player1.position.y
    player2 = player()
    player2.position.x = 600
    player2.position.y = 700


    pow1 = powers(random.choice(["shield"]), random.randint(100, 1500), 40)
    pow2 = powers(random.choice(["jump"]), random.randint(100, 1500), 40)
    pow3 = powers(random.choice(["punch"]), random.randint(100, 1500), 40)

    AVL = tree("AVL",random.randint(100,1500),40)


    piso = platform(Platform1[0],250,860)
    plataform1 = platform(Platform2[0],1200,650)
    platform2 = platform(Platform2[1],100,650)

    run = True
    while run:
        dt = clock.tick(60) * .001 * TARGET_FPS

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                counter  -= 1
                timer = str(counter).rjust(3) if counter > 0 else quit()
            else:
                clock.tick(60)
            if event.type == pygame.QUIT:
                run = False
            label5 = pygame.font.SysFont('arial', 28).render(str(player1.vidas), 1, (0, 255, 0))
            label6 = pygame.font.SysFont('arial', 28).render(str(player2.vidas), 1, (0, 255, 0))
            label7 = pygame.font.SysFont('arial', 28).render(str(timer), 1, (0, 255, 0))
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == button_keys['left_arrow']:
                    player1.LEFT_KEY = True
                    player1.left = True
                    player1.right = False
                    player1.standing = False
                    player1.punch = False
                if event.button == button_keys['right_arrow']:
                    player1.RIGHT_KEY = True
                    player1.left = False
                    player1.right = True
                    player1.standing = False
                    player1.punch = False
                if event.button == button_keys['up_arrow']:
                    player1.jump()
                if event.button ==  button_keys['square']:
                    if player1.pow:
                        if player1.powpunch:
                            player1.punchCount = 0
                            player1.punch = True
                            player1.standing = False
                            player1.pow = False
                        elif player1.jumpow:
                            player1.usejump = True
                            player1.jump()
                            player1.pow = False
                        elif player1.shield:
                            player1.useshield = True
                            player1.pow = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:#or event.button == button_keys['x']
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
                    if player1.pow:
                        if player1.powpunch:
                            player1.punchCount = 0
                            player1.punch = True
                            player1.standing = False
                            player1.pow = False
                        elif player1.jumpow:
                            player1.usejump = True
                            player1.jump()
                            player1.pow = False
                        elif player1.shield:
                            player1.useshield = True
                            player1.pow = False
                elif event.key == pygame.K_k:
                    if player2.pow:
                        if player2.powpunch:
                            player2.punchCount = 0
                            player2.punch = True
                            player2.standing = False
                            player2.pow = False
                        elif player2.jumpow:
                            player2.usejump = True
                            player2.jump()
                            player2.pow = False
                        elif player2.shield:
                            player2.useshield = True
                            player2.pow = False
            ############################################
            if event.type == pygame.JOYBUTTONUP:
                if event.button == button_keys['left_arrow']:
                    player1.LEFT_KEY = False
                    player1.right = False
                    player1.standing = True
                if event.button == button_keys['right_arrow']:
                    player1.RIGHT_KEY = False
                    player1.LEFT_KEY = False
                    player1.left = False
                    player1.standing = True
                if event.button == button_keys['up_arrow']:
                    if player1.isJump:
                        player1.vel.y *= .25
                        player1.isJump = False
                if event.button ==  button_keys['square']:
                    if player1.catch != None:
                        player1.catch.drop = False
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
                elif event.key == pygame.K_s:
                    if player1.catch != None:
                        player1.catch.drop = False
                elif event.key == pygame.K_k:
                    if player2.catch !=None:
                        player2.catch.drop = False
        AVL.update(dt,[piso,platform2,plataform1])
        pow1.update(dt,[piso,platform2,plataform1])
        pow2.update(dt, [piso, platform2, plataform1])
        pow3.update(dt, [piso, platform2, plataform1])
        player2.update(dt,[player1],[piso,platform2,plataform1],[pow1,pow2,pow3],[[AVL],"AVL"])
        player1.update(dt,[player2],[piso,platform2,plataform1],[pow1,pow2,pow3],[[AVL],"AVL"])
        redrawGameWindow()

def menu():
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    DARK_RED = (200, 0, 0)
    BLUE = (0, 0, 255)
    DARK_BLUE = (0, 0, 200)
    WHITE = (255, 255, 255)
    GREY = (160, 160, 160)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    WIDTH = 1000
    HEIGHT = 700

    # functions of instructions

    # functions of instructions
    def Instructions():
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        Back_Ground_IMG = pygame.image.load("Recursos/Backgroung/fondoins.png")

        running = False
        while not running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = True
            screen.blit(Back_Ground_IMG, (0, 0))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 400 + 200 > mouse[0] > 400 and 600 + 50 > mouse[1] > 600:
                pygame.draw.rect(screen, GREY, (400, 600, 200, 50))
                if click[0] == 1:
                    running = True
                    main_menu()
            else:
                Back_button = pygame.draw.rect(screen, WHITE, (400, 600, 200, 50))

            # General_Info = Instructions.render("General information:", True, WHITE)
            # screen.blit(General_Info, (25, 150))
            # General_Info1 = Instructions.render("-Coins will appear randomly in the screen, click them to add the amount to your reserve.", True, WHITE)
            # screen.blit(General_Info1, (25, 175))
            # General_Info2 = Instructions.render("-At the right side of the screen you will see your username, the amount of money and game time.", True, WHITE)
            # screen.blit(General_Info2, (25, 200))
            # General_Info3 = Instructions.render("-To add Rooks click on one of them to select it and then click in one of the squares to place it.", True, WHITE)
            # screen.blit(General_Info3, (25, 225))
            # General_Info4 = Instructions.render("-There are 4 types of Rooks you can chose from: sand, rock, fire and water.", True, WHITE)
            # screen.blit(General_Info4, (25, 250))
            # General_Info5 = Instructions.render("-There are 4 Avatars: Archer, Shield, Lumberjack, Cannibal. They will spawn at the buttom.", True, WHITE)
            # screen.blit(General_Info5, (25, 275))
            # General_Info6 = Instructions.render("-This game has three levels, each level is 30% more difficult.", True, WHITE)
            # screen.blit(General_Info6, (25, 300))
            # General_Info7 = Instructions.render("-If you win the game, your name and time will be saved in a document.", True, WHITE)
            # screen.blit(General_Info7, (25, 325))
            # General_Info8 = Instructions.render("-Your name will be placed in the score board if you make it in the top 10.", True, WHITE)
            # screen.blit(General_Info8, (25, 350))

            BackFont = pygame.font.Font("freesansbold.ttf", 55)
            Back = BackFont.render("Back", True, BLACK)
            screen.blit(Back, (435, 600))
            pygame.display.update()

    # functions of credits
    def Credits():
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        Back_Ground_IMG = pygame.image.load("Recursos/Backgroung/fondocred.png")
        running = False
        while not running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = True
            screen.blit(Back_Ground_IMG, (0, 0))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 400 + 200 > mouse[0] > 400 and 600 + 50 > mouse[1] > 600:
                pygame.draw.rect(screen, GREY, (400, 600, 200, 50))
                if click[0] == 1:
                    running = True
                    main_menu()
            else:
                Back_button = pygame.draw.rect(screen, WHITE, (400, 600, 200, 50))
            titleFont = pygame.font.Font("freesansbold.ttf", 55)
            Back = titleFont.render("Back", True, BLACK)
            screen.blit(Back, (435, 600))
            Title = titleFont.render("Credits", True, WHITE)
            screen.blit(Title, (400, 50))
            Creators_Names = titleFont.render("1. Felipe Vargas, Joan Ugalde, Irene Garzona ", True, WHITE)
            screen.blit(Creators_Names, (50, 150))
            Version = titleFont.render("2. Version 1.0", True, WHITE)
            screen.blit(Version, (50, 250))
            Country = titleFont.render("3. Costa Rica", True, WHITE)
            screen.blit(Country, (50, 350))
            University = titleFont.render("4. Tecnologico de Costa Rica", True, WHITE)
            screen.blit(University, (50, 450))
            pygame.display.update()

    # functions of score board
    def Score_Board():
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        Back_Ground_IMG = pygame.image.load("Recursos/Backgroung/fondoscore.png")
        running = False
        while not running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = True
            screen.blit(Back_Ground_IMG, (0, 0))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 400 + 200 > mouse[0] > 400 and 600 + 50 > mouse[1] > 600:
                pygame.draw.rect(screen, GREY, (400, 600, 200, 50))
                if click[0] == 1:
                    running = True
                    main_menu()
            else:
                Back_button = pygame.draw.rect(screen, WHITE, (400, 600, 200, 50))
            titleFont = pygame.font.Font("freesansbold.ttf", 55)
            Back = titleFont.render("Back", True, BLACK)
            screen.blit(Back, (435, 600))
            Title = titleFont.render("profesor: Isaac", True, WHITE)
            screen.blit(Title, (400, 50))
            Creators_Names = titleFont.render("1. ", True, WHITE)
            screen.blit(Creators_Names, (50, 150))
            Version = titleFont.render("0", True, WHITE)
            screen.blit(Version, (50, 250))
            Country = titleFont.render("3", True, WHITE)
            screen.blit(Country, (50, 350))
            University = titleFont.render("4", True, WHITE)
            screen.blit(University, (50, 450))
            pygame.display.update()

    # functions of main menu
    def main_menu():
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Battle Stickman V2.0")
        Fondo_Pantalla = pygame.image.load("Recursos/fondo4.png")
        Entry = pygame.Rect(400, 130, 200, 50)
        User_Name = " "
        Active = False
        running = True
        while running:  # iteration for space of the button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Entry.collidepoint(event.pos):
                        Active = True
                if event.type == pygame.KEYDOWN:
                    if Active == True:
                        if event.key == pygame.K_BACKSPACE:
                            User_Name = User_Name[:-1]
                        else:
                            User_Name += event.unicode

            screen.blit(Fondo_Pantalla, (0, 0))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if Active:
                color = GREY
            # BR = button rectangle
            if 400 + 200 > mouse[0] > 400 and 200 + 50 > mouse[1] > 200:
                pygame.draw.rect(screen, GREY, (400, 200, 200, 50))
                if click[0] == 1:
                    return game()

            else:
                BR1 = pygame.draw.rect(screen, WHITE, (400, 200, 200, 50))
            if 400 + 200 > mouse[0] > 400 and 300 + 50 > mouse[1] > 300:
                pygame.draw.rect(screen, GREY, (400, 300, 200, 50))
                if click[0] == 1:
                    pass
                    # instrucctions()
            else:
                BR2 = pygame.draw.rect(screen, WHITE, (400, 300, 200, 50))
            if 400 + 200 > mouse[0] > 400 and 400 + 50 > mouse[1] > 400:
                pygame.draw.rect(screen, GREY, (400, 400, 200, 50))
                if click[0] == 1:
                    Instructions()
            else:
                BR3 = pygame.draw.rect(screen, WHITE, (400, 400, 200, 50))
            if 400 + 200 > mouse[0] > 400 and 500 + 50 > mouse[1] > 500:
                pygame.draw.rect(screen, GREY, (400, 500, 200, 50))
                if click[0] == 1:
                    Credits()
            else:
                BR4 = pygame.draw.rect(screen, WHITE, (400, 500, 200, 50))
            if 400 + 200 > mouse[0] > 400 and 600 + 50 > mouse[1] > 600:
                pygame.draw.rect(screen, GREY, (400, 600, 200, 50))
                if click[0] == 1:
                    Score_Board()
            else:
                BR5 = pygame.draw.rect(screen, WHITE, (400, 600, 200, 50))

            titleFont = pygame.font.Font("freesansbold.ttf", 60)
            gameTitle = titleFont.render("Battle Stickman V2.0", True, BLACK)
            screen.blit(gameTitle, (150, 50))
            textFont = pygame.font.Font("freesansbold.ttf", 30)  # font
            text1 = textFont.render("New Game", True, BLACK)  # new game text
            screen.blit(text1, (410, 210))
            text2 = textFont.render("Integrantes", True, BLACK)  # load text
            screen.blit(text2, (410, 310))
            text3 = textFont.render("Instructions", True, BLACK)  # Instructions text
            screen.blit(text3, (410, 410))
            text4 = textFont.render("Credits", True, BLACK)  # Credits text
            screen.blit(text4, (440, 510))
            text5 = textFont.render("Score Board", True, BLACK)  # Score board text
            screen.blit(text5, (410, 610))

            User_Name_display = textFont.render(User_Name, True, BLACK)
            Entry_Box = pygame.draw.rect(screen, WHITE, Entry, 2)
            screen.blit(User_Name_display, (Entry_Box.x + 10, Entry_Box.y + 10))
            Entry_Box.w = max(100, User_Name_display.get_width() + 10)

            pygame.display.update()

    main_menu()
    quit()

menu()
pygame.quit()
