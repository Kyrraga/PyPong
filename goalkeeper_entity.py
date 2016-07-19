import pygame
from ecs_pattern import Entity, Component, System


class GoalkeeperEntity(Entity):
    def __init__(self, rect, color, key_up, key_down, speed, min_y, max_y):
        Entity.__init__(self)
        self.add_component(RectComponent(rect))
        self.add_component(ColorComponent(color))
        self.add_component(UpDownComponent(key_up, key_down, speed))
        self.add_component(VerticalLimitsComponent(min_y, max_y))


class RectComponent(Component):
    def __init__(self, rect):
        self.rect = rect


class ColorComponent(Component):
    def __init__(self, color):
        self.color = color


class UpDownComponent(Component):
    def __init__(self, key_up, key_down, speed):
        self.key_up = key_up
        self.key_down = key_down
        self.speed = speed


class VerticalLimitsComponent(Component):
    def __init__(self, min_y, max_y):
        self.min_y = min_y
        self.max_y = max_y


class DrawRectangleSystem(System):
    def draw(self, entities, display):
        for entity in entities:
            rect = entity.get_component(RectComponent)
            color = entity.get_component(ColorComponent)
            if rect and color:
                pygame.draw.rect(display, color.color, rect.rect)


class UpDownSystem(System):
    def update(self, entities):
        keys = pygame.key.get_pressed()
        for entity in entities:
            rect = entity.get_component(RectComponent)
            movement = entity.get_component(UpDownComponent)
            if rect and movement:
                if keys[movement.key_up]:
                    rect.rect.y -= movement.speed
                if keys[movement.key_down]:
                    rect.rect.y += movement.speed


class VecticalLimitsSystem(System):
    def update(self, entities):
        for entity in entities:
            rect = entity.get_component(RectComponent)
            limits = entity.get_component(VerticalLimitsComponent)
            if rect and limits:
                if rect.rect.top < limits.min_y:
                    rect.rect.top = limits.min_y
                if rect.rect.bottom > limits.max_y:
                    rect.rect.bottom = limits.max_y
