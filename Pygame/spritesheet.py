import pygame

class Spritesheet:
    def __init__(self,filename):
        self.filename = filename

    def get_spritte(self):
        if self.filename == "WalkR":
            return [pygame.image.load('Recursos/Caminar/caminarD1.png'), pygame.image.load('Recursos/Caminar/caminarD2.png'),
             pygame.image.load('Recursos/Caminar/caminarD3.png'), pygame.image.load('Recursos/Caminar/caminarD4.png')]
        elif self.filename == "WalkL":
            return [ pygame.image.load('Recursos/Caminar/caminarI1.png'), pygame.image.load('Recursos/Caminar/caminarI2.png'),
             pygame.image.load('Recursos/Caminar/caminarI3.png'), pygame.image.load('Recursos/Caminar/caminarI4.png')]
        elif self.filename == "GolpeL":
            return [pygame.image.load('Recursos/Punch/PunchI1.png'),pygame.image.load('Recursos/Punch/PunchI2.png'),pygame.image.load('Recursos/Punch/PunchI3.png'),
          pygame.image.load('Recursos/Punch/PunchI4.png'),pygame.image.load('Recursos/Punch/PunchI5.png'),pygame.image.load('Recursos/Punch/PunchI6.png'),
          pygame.image.load('Recursos/Punch/PunchI7.png')]
        elif self.filename == "GolpeR":
            return [pygame.image.load('Recursos/Punch/PunchD1.png'),pygame.image.load('Recursos/Punch/PunchD2.png'),pygame.image.load('Recursos/Punch/PunchD3.png'),
          pygame.image.load('Recursos/Punch/PunchD4.png'),pygame.image.load('Recursos/Punch/PunchD5.png'),pygame.image.load('Recursos/Punch/PunchD6.png'),
          pygame.image.load('Recursos/Punch/PunchD7.png')]
        elif self.filename == "punchL":
            return [pygame.image.load('Recursos/Golpe/golpeI1.png'),pygame.image.load('Recursos/Golpe/golpeI2.png'),pygame.image.load('Recursos/Golpe/golpeI3.png'),
          pygame.image.load('Recursos/Golpe/golpeI4.png'),pygame.image.load('Recursos/Golpe/golpeI5.png'),pygame.image.load('Recursos/Golpe/golpeI6.png')]

        elif self.filename == "punchR":
            return  [pygame.image.load('Recursos/Golpe/golpeD1.png'),pygame.image.load('Recursos/Golpe/golpeD2.png'),pygame.image.load('Recursos/Golpe/golpeD3.png'),
          pygame.image.load('Recursos/Golpe/golpeD4.png'),pygame.image.load('Recursos/Golpe/golpeD5.png'),pygame.image.load('Recursos/Golpe/golpeD6.png')]

        elif self.filename == "jumpR":
            return [pygame.image.load('Recursos/Salto/SaltoD1.png'),pygame.image.load('Recursos/Salto/SaltoD2.png'),pygame.image.load('Recursos/Salto/SaltoD3.png'),
          pygame.image.load('Recursos/Salto/SaltoD4.png'),pygame.image.load('Recursos/Salto/SaltoD5.png'),pygame.image.load('Recursos/Salto/SaltoD6.png'),pygame.image.load('Recursos/Salto/SaltoD7.png'),
          pygame.image.load('Recursos/Salto/SaltoD8.png'),pygame.image.load('Recursos/Salto/SaltoD9.png'),pygame.image.load('Recursos/Salto/SaltoD10.png')]

        elif self.filename == "jumpL":
            return  [pygame.image.load('Recursos/Salto/SaltoI1.png'),pygame.image.load('Recursos/Salto/SaltoI2.png'),pygame.image.load('Recursos/Salto/SaltoI3.png'),
          pygame.image.load('Recursos/Salto/SaltoI4.png'),pygame.image.load('Recursos/Salto/SaltoI5.png'),pygame.image.load('Recursos/Salto/SaltoI6.png'),pygame.image.load('Recursos/Salto/SaltoI7.png'),
          pygame.image.load('Recursos/Salto/SaltoI8.png'),pygame.image.load('Recursos/Salto/SaltoI9.png'),pygame.image.load('Recursos/Salto/SaltoI10.png')]

        elif self.filename == "Stand":
            return [pygame.image.load('Recursos/Stand/standD1.png'),pygame.image.load('Recursos/Stand/standD2.png'),pygame.image.load('Recursos/Stand/standD3.png'), pygame.image.load('Recursos/Stand/standD4.png'),
                    pygame.image.load('Recursos/Stand/standD5.png')]

        elif self.filename == "platform":
            return [pygame.image.load('Recursos/Plataforma/piso.png')]
        elif self.filename == "platform1":
            return [pygame.image.load('Recursos/Plataforma/plataforma1.png'), pygame.image.load('Recursos/Plataforma/plataforma2.png')]
        elif self.filename =="shield":
            return[pygame.image.load('Recursos/heart.png')]
        elif self.filename == "jump":
            return[pygame.image.load('Recursos/potion.png')]
        elif self.filename == "punch":
            return [pygame.image.load("Recursos/punch.png")]