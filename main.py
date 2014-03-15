import math, random, sys, pygame # Built-in modules.
from pygame.locals import *

class Display(object):
    def __init__(self):
        self.window_size = (1200, 800)
        self.left        = 1
        self.displays    = []
        self.fps         = 30
        self.start_pygame()

    def start_pygame(self):
        # Initiate pygame and set up dependencies.
        self.surface = pygame.display.set_mode(self.window_size)
        pygame.display.init()
        pygame.font.init()
        self.fps_clock = pygame.time.Clock()

class Cursor(object):
    def __init__(self):
        self.update  = True
        #self.surface = pygame.line.

        ################ LEFT OFF

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y)

    def set_up(self):
        self.rect = self.surface.get_rect()

    def update(self):
        self.blit(self.surface, self.rect)

class Control(object):
    def __init__(self):
        self.on = True
        self.main_loop()
        
    def main_loop(self):
        while self.on == True:
            self.events()
            self.update()
        
        while self.on == False:
            pygame.quit()
            sys.exit()

    def update(self):
        pygame.display.update()
        DISPLAY.fps_clock.tick(DISPLAY.fps)

    def events(self):
        for event in pygame.event.get():
            
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                self.on = False 
                
            elif event.type == pygame.MOUSEMOTION:
                print("x")
                
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == DISPLAY.left:
                print("x")

            elif event.type == KEYUP:
                if event.key == K_q:
                    print("Q")

def main():
    global DISPLAY, CONTROL
    DISPLAY = Display()
    CONTROL = Control()

if __name__ == "__main__":
    main()
    

