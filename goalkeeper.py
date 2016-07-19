import pygame
import pygame.locals as pgl


class Goalkeeper:
    def __init__(self,
                 x=0, y=0,
                 min_y=float('-inf'),
                 max_y=float('inf'),
                 key_up=pgl.K_UP,
                 key_down=pgl.K_DOWN):
        self.rect = pygame.Rect(x, y, 20, 60)
        self.color = pygame.Color(255, 255, 255, 0)
        self.speed = 10  # per frame
        self.TOP = min_y
        self.BOTTOM = max_y

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.key_up]:
            self.rect.y += self.speed
        if keys[self.key_down]:
            self.rect.y -= self.speed

        if self.rect.top < self.TOP:
            self.rect.top = self.TOP
        if self.rect.bottom > self.BOTTOM:
            self.rect.bottom = self.BOTTOM

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.rect)
