import itertools;
import pygame
from pygame.locals import *

from skymap import *;
 
class App:
    def __init__(self):
        self.running = True
        self.display_surf = None
        self.stararr = list();
        self.edgearr = list();
 
    def on_init(self):
        pygame.init()
        self.screen_info = pygame.display.Info()
        self.size = self.width, self.height = self.screen_info.current_w, self.screen_info.current_h - 45
        self.display_surf = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        self.running = True
        return True;
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        pass

    def on_render(self):
        # test code
        stars = list();
        for y, x in itertools.product(range(0, 3), range(0, 3)):
            s = Star(x * 200 + 300, y * 200 + 300, y * 3 + x + 2)
            stars.append(s);
            s.draw(self.display_surf);
        for m, n in itertools.product(stars, stars):
            if(not m is n):
                draw_edge(self.display_surf, (m, n));
        # test code end
        for st in self.stararr:
            st.draw(self.display_surf);
        for e in self.edgearr:
            draw_edge(self.display_surf, e);
        pygame.display.flip();

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if not self.on_init():
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