import pygame
from ecs_pattern import Entity, Component, System


class GoalkeeperEntity(Entity):
    def __init__(self, rect, color):
        self.add_component(RectComponent(rect))
        self.add_component(ColorComponent(color))


class RectComponent(Component):
    def __init__(self, rect):
        self.rect = rect


class ColorComponent(Component):
    def __init__(self, color):
        self.color = color


class DrawRectangleSystem(System):
    def draw(self, entities, display):
        for entity in entities:
            rect = entity.get_component(RectComponent)
            color = entity.get_component(ColorComponent)
            if rect and color:
                pygame.draw.rect(display, color.color, rect.rect)
