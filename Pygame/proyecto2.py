import pygame


# Colors
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

#functions of instructions

#functions of instructions
def Instructions():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    Back_Ground_IMG = pygame.image.load("Recursos/fondoins.png")

    running = False
    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = True
        screen.blit(Back_Ground_IMG, (0, 0))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 400+200 > mouse[0] > 400 and 600+50 > mouse[1] > 600:
            pygame.draw.rect(screen, GREY, (400, 600, 200, 50))
            if click[0] == 1:
                running = True
                main_menu()
        else:
            Back_button = pygame.draw.rect(screen, WHITE, (400, 600, 200, 50))
            
      
        
        #General_Info = Instructions.render("General information:", True, WHITE)
        #screen.blit(General_Info, (25, 150))
        #General_Info1 = Instructions.render("-Coins will appear randomly in the screen, click them to add the amount to your reserve.", True, WHITE)
        #screen.blit(General_Info1, (25, 175))
        #General_Info2 = Instructions.render("-At the right side of the screen you will see your username, the amount of money and game time.", True, WHITE)
        #screen.blit(General_Info2, (25, 200))
        #General_Info3 = Instructions.render("-To add Rooks click on one of them to select it and then click in one of the squares to place it.", True, WHITE)
        #screen.blit(General_Info3, (25, 225))
        #General_Info4 = Instructions.render("-There are 4 types of Rooks you can chose from: sand, rock, fire and water.", True, WHITE)
        #screen.blit(General_Info4, (25, 250))
        #General_Info5 = Instructions.render("-There are 4 Avatars: Archer, Shield, Lumberjack, Cannibal. They will spawn at the buttom.", True, WHITE)
        #screen.blit(General_Info5, (25, 275))
        #General_Info6 = Instructions.render("-This game has three levels, each level is 30% more difficult.", True, WHITE)
        #screen.blit(General_Info6, (25, 300))
        #General_Info7 = Instructions.render("-If you win the game, your name and time will be saved in a document.", True, WHITE)
        #screen.blit(General_Info7, (25, 325))
        #General_Info8 = Instructions.render("-Your name will be placed in the score board if you make it in the top 10.", True, WHITE)
        #screen.blit(General_Info8, (25, 350))
                   
        BackFont = pygame.font.Font("freesansbold.ttf", 55)
        Back = BackFont.render("Back", True, BLACK)
        screen.blit(Back, (435, 600))
        pygame.display.update()
        
#functions of credits
def Credits():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    Back_Ground_IMG = pygame.image.load("Recursos/fondo4.png")
    running = False
    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = True
        screen.blit(Back_Ground_IMG,(0, 0))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if 400+200 > mouse[0] > 400 and 600+50 > mouse[1] > 600:
            pygame.draw.rect(screen, GREY, (400, 600, 200, 50))
            if click[0] == 1:
                running = True
                main_menu()
        else:
            Back_button = pygame.draw.rect(screen, WHITE, (400, 600, 200, 50))
        titleFont =pygame.font.Font("freesansbold.ttf", 55)
        Back = titleFont.render("Back", True, BLACK)
        screen.blit(Back, (435, 600))
        Title = titleFont.render("Credits", True, WHITE)
        screen.blit(Title, (400, 50))
        Creators_Names = titleFont.render("1. Felipe Vargas...", True, WHITE)
        screen.blit(Creators_Names, (50, 150))
        Version = titleFont.render("2. Version 1.0", True, WHITE)
        screen.blit(Version, (50, 250))
        Country= titleFont.render("3. Costa Rica", True, WHITE)
        screen.blit(Country, (50, 350))
        University= titleFont.render("4. Tecnologico de Costa Rica", True, WHITE)
        screen.blit(University, (50, 450))
        pygame.display.update()
        
#functions of score board
def Score_Board():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    Back_Ground_IMG = pygame.image.load("Recursos/fondo4.png")
    running = False
    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = True
        screen.blit(Back_Ground_IMG,(0, 0))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if 400+200 > mouse[0] > 400 and 600+50 > mouse[1] > 600:
            pygame.draw.rect(screen, GREY, (400, 600, 200, 50))
            if click[0] == 1:
                running = True
                main_menu()
        else:
            Back_button = pygame.draw.rect(screen, WHITE, (400, 600, 200, 50))
        titleFont =pygame.font.Font("freesansbold.ttf", 55)
        Back = titleFont.render("Back", True, BLACK)
        screen.blit(Back, (435, 600))
        Title = titleFont.render("profesor: ELMAMADo", True, WHITE)
        screen.blit(Title, (400, 50))
        Creators_Names = titleFont.render("1. ", True, WHITE)
        screen.blit(Creators_Names, (50, 150))
        Version = titleFont.render("0", True, WHITE)
        screen.blit(Version, (50, 250))
        Country= titleFont.render("3", True, WHITE)
        screen.blit(Country, (50, 350))
        University= titleFont.render("4", True, WHITE)
        screen.blit(University, (50, 450))
        pygame.display.update()
        
#functions of main menu
def main_menu():
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Battle Stickman V2.0")
        Fondo_Pantalla = pygame.image.load("Recursos/fondo4.png")
        Entry = pygame.Rect(400, 130, 200, 50)
        User_Name = " "
        Active = False
        running = True
        while running: #iteration for space of the button
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
        
            screen.blit(Fondo_Pantalla, (0,0)) 
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if Active:
                color = GREY
            # BR = button rectangle
            if 400+200 > mouse[0] > 400 and 200+50 > mouse[1] > 200 :
                pygame.draw.rect(screen, GREY, (400, 200, 200, 50))
                if click[0] == 1 and User_Name != " ":
                    Play_Game(User_Name)

            else:
                BR1 = pygame.draw.rect(screen, WHITE, (400, 200, 200, 50))
            if 400+200 > mouse[0] > 400 and 300+50 > mouse[1] > 300:
                pygame.draw.rect(screen, GREY, (400, 300, 200, 50))
                if click[0] == 1:
                    running = False
                    #instrucctions()
            else:
                BR2 = pygame.draw.rect(screen, WHITE, (400, 300, 200, 50))
            if 400+200 > mouse[0] > 400 and 400+50 > mouse[1] > 400:
                pygame.draw.rect(screen, GREY, (400, 400, 200, 50))
                if click[0] == 1:
                    Instructions()
            else:
                BR3 = pygame.draw.rect(screen, WHITE, (400, 400, 200, 50))
            if 400+200 > mouse[0] > 400 and 500+50 > mouse[1] > 500:
                pygame.draw.rect(screen, GREY, (400, 500, 200, 50))
                if click[0] == 1:
                    Credits()
            else:
                BR4 = pygame.draw.rect(screen, WHITE, (400, 500, 200, 50))
            if 400+200 > mouse[0] > 400 and 600+50 > mouse[1] > 600:
                pygame.draw.rect(screen, GREY, (400, 600, 200, 50))
                if click[0] == 1:
                    Score_Board()
            else:
                BR5 = pygame.draw.rect(screen, WHITE, (400, 600, 200, 50))
                
               
            titleFont =pygame.font.Font("freesansbold.ttf", 60)
            gameTitle = titleFont.render("Battle Stickman V2.0", True, BLACK)
            screen.blit(gameTitle, (150, 50))
            textFont = pygame.font.Font("freesansbold.ttf", 30)#font
            text1 = textFont.render("New Game", True, BLACK)#new game text
            screen.blit(text1, (410, 210))
            text2 = textFont.render("Integrantes", True, BLACK)#load text
            screen.blit(text2, (410, 310))
            text3 = textFont.render("Instructions", True, BLACK)#Instructions text
            screen.blit(text3, (410, 410))
            text4 = textFont.render("Credits", True, BLACK)#Credits text
            screen.blit(text4, (440, 510))
            text5 = textFont.render("Score Board", True, BLACK)# Score board text
            screen.blit(text5, (410, 610))
            
            User_Name_display = textFont.render(User_Name, True, BLACK)
            Entry_Box = pygame.draw.rect(screen, WHITE, Entry, 2)
            screen.blit(User_Name_display, (Entry_Box.x + 10, Entry_Box.y + 10))
            Entry_Box.w = max(100, User_Name_display.get_width() + 10)
            
            pygame.display.update()

main_menu()
quit()

quit()
