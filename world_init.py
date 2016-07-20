# -*- coding: utf-8 -*-
import pygame
import pygame.locals as pgl
from ecs_pattern import World, Entity
from goalkeeper_entity import RectComponent
from goalkeeper_entity import ColorComponent
from goalkeeper_entity import UpDownComponent
from goalkeeper_entity import VerticalLimitsComponent
from goalkeeper_entity import DrawRectangleSystem
from goalkeeper_entity import UpDownSystem
from goalkeeper_entity import VecticalLimitsSystem


def init(WINDOWWIDTH, WINDOWHEIGHT):
    world = World()

    width = 5.0 * WINDOWWIDTH / 100
    height = 20.0 * WINDOWHEIGHT / 100
    offset = 10

    rect1 = pygame.Rect(0, 0, width, height)
    rect1.centery = WINDOWHEIGHT / 2
    rect1.left = offset

    rect2 = rect1.copy()
    rect2.right = WINDOWWIDTH - offset

    goalkeeper1 = Entity()
    goalkeeper1 += RectComponent(rect1)
    goalkeeper1 += ColorComponent(pygame.Color(255, 64, 64, 0))
    goalkeeper1 += UpDownComponent(pgl.K_w, pgl.K_s, 10)
    goalkeeper1 += VerticalLimitsComponent(0, WINDOWHEIGHT)

    goalkeeper2 = Entity()
    goalkeeper2 += RectComponent(rect2)
    goalkeeper2 += ColorComponent(pygame.Color(64, 64, 255, 0))
    goalkeeper2 += UpDownComponent(pgl.K_UP, pgl.K_DOWN, 10)
    goalkeeper2 += VerticalLimitsComponent(0, WINDOWHEIGHT)

    world += goalkeeper1
    world += goalkeeper2
    world += DrawRectangleSystem()
    world += UpDownSystem()
    world += VecticalLimitsSystem()

    return world
