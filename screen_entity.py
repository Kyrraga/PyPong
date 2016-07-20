import pygame
from ecs_pattern import Entity, Component, System


class ScreenEntity(Entity):
    def __init__(self, width, height, color):
        Entity.__init__(self)
        self.add_component(ScreenLimitsComponent(width, height))
        self.add_component(ColorComponent(color))

class ColorComponent(Component):
    def __init__(self, color):
        self.color = color
        
class ScreenLimitsComponent(Component):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class DrawScreenSystem(System):
    def draw(self, entities, display):
        for entity in entities:
            screen = entity.get_component(ScreenLimitsComponent)
            color = entity.get_component(ColorComponent)
            if screen and color:
                pygame.display.update()
                #display = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                display.fill(color)