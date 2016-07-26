# -*- coding: utf-8 -*-
import pygame
import pygame.locals as pgl
from ecs_pattern import World, Entity

from button import ButtonComponent
from button import ColorComponent
from button import DrawButtonSystem
from button import HighLightSystem


def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def init(WINDOWWIDTH, WINDOWHEIGHT):
    world = World()

    width = 5.0 * WINDOWWIDTH / 100
    height = 20.0 * WINDOWHEIGHT / 100
    
    rect3 = pygame.Rect(0, 0, height, width)
    rect3.centery = WINDOWHEIGHT / 2
    rect3.left = WINDOWWIDTH / 2 - height/2
    
    button1 = Entity()
    button1 += ButtonComponent(rect3)
    button1 += ColorComponent(pygame.Color(255, 64, 255, 0))
    
    world += button1
    world += DrawButtonSystem()
    world += HighLightSystem()

    return world
