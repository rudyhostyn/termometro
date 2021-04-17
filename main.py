import pygame, sys
from pygame.locals import *

class mainApp():
    termometro = None
    entrada = None
    selector = None
            
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((628, 402))
        #self.__background = pygame.image.load("images/campoFutbol.jpg")
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((244, 236, 203))
    
    def __on_close(self):
        pygame.quit()
        sys.exit()
    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__on_close()
        
        
            pygame.display.flip()
        
        
if __name__ =="__main__":
    pygame.font.init()
    app = mainApp()
    app.start()