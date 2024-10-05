import pygame
from pygame.locals import *
 
class App:
    def __init__(self):
        self.running = True
        self.display_surf = None
 
    def on_init(self):
        pygame.init()
        self.screen_info = pygame.display.Info()
        self.size = self.width, self.height = self.screen_info.current_w, self.screen_info.current_h - 45
        self.display_surf = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        self.running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self.running = False
 
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()
            
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()