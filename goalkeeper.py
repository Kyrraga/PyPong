import pygame
import pygame.locals as pgl


class Goalkeeper:
    def __init__(self, x, y, top, bottom):
        self.rect = pygame.Rect(x, y, 20, 60)
        self.color = pygame.Color(255, 255, 255, 0)
        self.speed = 10  # per frame
        self.TOP = top
        self.BOTTOM = bottom

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pgl.K_DOWN]:
            self.rect.y += self.speed
        if keys[pgl.K_UP]:
            self.rect.y -= self.speed

        if self.rect.top < self.TOP:
            self.rect.top = self.TOP
        if self.rect.bottom > self.BOTTOM:
            self.rect.bottom = self.BOTTOM

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.rect)
