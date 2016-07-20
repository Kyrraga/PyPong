# -*- coding: utf-8 -*-
import pygame
from ecs_pattern import Component, System


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
            rect = entity[RectComponent]
            color = entity[ColorComponent]
            if rect and color:
                pygame.draw.rect(display, color.color, rect.rect)


class UpDownSystem(System):
    def update(self, entities):
        keys = pygame.key.get_pressed()
        for entity in entities:
            rect = entity[RectComponent]
            movement = entity[UpDownComponent]
            if rect and movement:
                if keys[movement.key_up]:
                    rect.rect.y -= movement.speed
                if keys[movement.key_down]:
                    rect.rect.y += movement.speed


class VecticalLimitsSystem(System):
    def update(self, entities):
        for entity in entities:
            rect = entity[RectComponent]
            limits = entity[VerticalLimitsComponent]
            if rect and limits:
                if rect.rect.top < limits.min_y:
                    rect.rect.top = limits.min_y
                if rect.rect.bottom > limits.max_y:
                    rect.rect.bottom = limits.max_y
