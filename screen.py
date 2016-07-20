import pygame
#import pygame.locals as pgl


class Screen:
    def __init__(self,
                 width = 0, height = 0,
                 color = pygame.Color(255, 255, 255, 0),
                 name = 'NaN'):
        #self.rect = pygame.Rect(x, y, width, height)
        self.screen = pygame.display.set_mode((width, height))
        self.color = color
        self.name = name
        #pygame.self.screen.set_caption(name)
        #self.speed = speed  # per frame
        #self.TOP = min_y
        #self.BOTTOM = max_y
        #self.key_up = key_up
        #self.key_down = key_down

    def update(self):
        self.screen.fill(self.color)
        #pygame.self.screen.update()
        #keys = pygame.key.get_pressed()
        #if keys[self.key_down]:
        #    self.rect.y += self.speed
        #if keys[self.key_up]:
        #    self.rect.y -= self.speed

        #if self.rect.top < self.TOP:
        #    self.rect.top = self.TOP
        #if self.rect.bottom > self.BOTTOM:
        #    self.rect.bottom = self.BOTTOM

    def draw(self, display):
        pygame.display.update()
        #pygame.draw.rect(display, self.color, self.rect)
