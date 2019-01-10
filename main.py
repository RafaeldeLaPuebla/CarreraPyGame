import pygame
import sys

class Runner():
    

class Game():
    
    corredores = []
    
    def __init__(self):
        #Nos creamos la pantalla:
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Carrera de bichos") #Le ponemos título a la pantalla.
        self.background = pygame.image.load("images/background.png")
        #Creo un atributo:
        self.runner = pygame.image.load("images/smallball.png")
        
    #Vamos a crear la partida:
    def competir(self):
        
        x = 0
        hayGanador = False
        
        while not hayGanador:
            #comprobación de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()#estamos comprobando los eventos (que es una de las cosas que hacer obligatoriamente en PyGame.
            
            #refrescamos/renderizamos la pantalla
            self.__screen.blit(self.background, (0,0)) #Con el blit pintamos la pantalla.
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip() #Esto es 'refresca'
            
            x += 3
            if x >=250:
                hayGanador = True
        
        pygame.quit()
        sys.exit()
        
            
    

if __name__ == '__main__':
    pygame.init()
    game = Game()


