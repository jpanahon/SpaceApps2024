import itertools;
import math;
import pygame;

class Star(object):

    def __init__(self, x, y, bright):
        self.x = x;
        self.y = y;
        self.bright = bright;
    
    def draw(self, g):
        imglen = self.bright * 2 + 1;
        descent = 240 // self.bright;
        img = pygame.Surface((imglen, imglen));
        for y, x in itertools.product(range(0, imglen), range(0, imglen)):
            intensity = 255 - int(math.hypot(y - self.bright, x - self.bright)) * descent;
            intensity = max(0, intensity);
            img.set_at((x, y), (intensity, intensity, intensity, 255));
        g.blit(img, (self.x - self.bright, self.y - self.bright));
    
    def __setitem__(self, ind, val):
        if (0 <= ind and ind < 2):
            if (type(value) is int):
                if (ind == 0):
                    self.x = val;
                else:
                    self.y = val;
            raise TypeError("val must be an integer");
        raise IndexError("index must be zero or 1");

    def __getitem__(self, ind):
        if (0 <= ind and ind < 2):
            return self.x if ind == 0 else self.y;
        raise IndexError("index must be zero or 1");

    def coord_tuple(self):
        return(self.x, self.y);

# e is a pair of stars
def draw_edge(g, e):
    pygame.draw.line(g, pygame.Color("white"), e[0].coord_tuple(), e[1].coord_tuple(), 1);