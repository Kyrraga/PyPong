# -*- coding: utf-8 -*-
import pygame
from ecs_pattern import Component, System


class ButtonComponent(Component):
    def __init__(self, button):
        self.button = button



class ColorComponent(Component):
    def __init__(self, color):
        self.color = color
    
class EventComponent(Component):
    def __init__(self, event):
        self.event = event

class DrawButtonSystem(System):
    def draw(self, entities, display):
        for entity in entities:
            button = entity[ButtonComponent]
            color = entity[ColorComponent]
            if button and color:
                pygame.draw.rect(display, color.color, button.button)
                
class HighLightSystem(System):
    def draw(self, entities, display):
        pos = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        for entity in entities:
            button = entity[ButtonComponent]
            color = entity[ColorComponent]
            if button and color:
                if (pos[0] > button.button.left and pos[0] < button.button.right) and (pos[1] > button.button.top and pos[1] < button.button.bottom):
                    if press == (1,0,0):
                        pygame.draw.rect(display, (0,255,255), button.button)
                    else:
                        pygame.draw.rect(display, (0,0,0), button.button)
                else:
                    pygame.draw.rect(display, (255,255,255), button.button)

class HighLightPressSystem(System):
    def draw(self, entities, display):
        keys = pygame.mouse.get_pressed()
        for entity in entities:
            button = entity[ButtonComponent]
            color = entity[ColorComponent]
            if button and color:
                if keys == (1,0,0):
                    pygame.draw.rect(display, (255,0,0), button.button)
                else:
                    pygame.draw.rect(display, (0,0,255), button.button)