import pygame, sys
import pygame.locals as pgl
from goalkeeper import Goalkeeper
from screen import Screen
from ecs_pattern import World
from goalkeeper_entity import GoalkeeperEntity
from goalkeeper_entity import DrawRectangleSystem
from goalkeeper_entity import UpDownSystem
from goalkeeper_entity import VecticalLimitsSystem


# магическая команда инициализации модуля
pygame.init()

# создаем экран с заданным размером и меняем заголовок окна
WINDOWWIDTH = 400
WINDOWHEIGHT = 300
#display = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
#pygame.display.set_caption('PyPong')
screen = Screen(width = WINDOWWIDTH,
                height = WINDOWHEIGHT,
                color = pygame.Color(0, 255, 0, 0),
                name = 'PyPong')

# цвет фона
background_color = pygame.Color(127, 198, 127, 0)

# объекты игроков
width = 5.0 * WINDOWWIDTH / 100
height = 20.0 * WINDOWHEIGHT / 100
offset = 10
goalkeeper1 = Goalkeeper(x = offset,
                         y = (WINDOWHEIGHT - height)/2,
                         width=width,
                         height=height,
                         min_y=0,
                         max_y=WINDOWHEIGHT,
                         color=pygame.Color(255, 64, 64, 0))
#goalkeeper1.rect.left = offset
#goalkeeper1.rect.centery = WINDOWHEIGHT / 2
goalkeeper2 = Goalkeeper(x = WINDOWWIDTH - offset - width,
                         y = (WINDOWHEIGHT - height)/2,
                         width=width,
                         height=height,
                         min_y=0,
                         max_y=WINDOWHEIGHT,
                         color=pygame.Color(64, 64, 255, 0),
                         key_up=pgl.K_w,
                         key_down=pgl.K_s)
#goalkeeper2.rect.right = WINDOWWIDTH - offset
#oalkeeper2.rect.centery = WINDOWHEIGHT / 2


# инициализация мирв
world = World()
goalkeeper3 = GoalkeeperEntity(goalkeeper1.rect,
                               goalkeeper1.color,
                               goalkeeper1.key_up,
                               goalkeeper1.key_down,
                               goalkeeper1.speed,
                               goalkeeper1.TOP,
                               goalkeeper1.BOTTOM)
goalkeeper4 = GoalkeeperEntity(goalkeeper2.rect,
                               goalkeeper2.color,
                               goalkeeper2.key_up,
                               goalkeeper2.key_down,
                               goalkeeper2.speed,
                               goalkeeper2.TOP,
                               goalkeeper2.BOTTOM)
world.add_entity(goalkeeper3)
world.add_entity(goalkeeper4)
world.add_system(DrawRectangleSystem())
world.add_system(UpDownSystem())
world.add_system(VecticalLimitsSystem())


# объект для отслеживания времени
clock = pygame.time.Clock()

while True:
    # перебираем все ивенты в очереди
    for event in pygame.event.get():
        # пользователь закрыл окно
        if event.type == pgl.QUIT:
            pygame.quit()
#           sys.exit()  # не нужно в интерактивном режиме

    # обновление мира
    world.update()

    # заливка фона
    #display.fill(background_color)
    screen.screen.fill(background_color)
    # отрисовка мира
    world.draw(screen.screen)

    # обновление экрана
    #pygame.display.update()
    pygame.display.update()

    # пропускаем лишнее время, чтобы
    # добиться 60 фреймов в секунду
    clock.tick(60)
