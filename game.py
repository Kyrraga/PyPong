import pygame, sys
from pygame.locals import *
import pygame.locals as pgl
import world_init
import menu

# магическая команда инициализации модуля
pygame.init()

# цвет фона
background_color = pygame.Color(127, 198, 127, 0)
BLACK = (0, 0, 0, 0)
WHITE = (255, 255, 255, 0)

# создаем экран с заданным размером и меняем заголовок окна
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('PyPong')

# инициализация мира

world = world_init.init(WINDOWWIDTH, WINDOWHEIGHT)
world_menu = menu.init(WINDOWWIDTH, WINDOWHEIGHT)

# объект для отслеживания времени
clock = pygame.time.Clock()
 
scenes = {'Main': world_menu,
          'Battle': world} #etc

scene = scenes['Main']


while True:
    # перебираем все ивенты в очереди
    for event in pygame.event.get():
        # пользователь закрыл окно
        print(event.type)
        print(scene)
        if event.type == pgl.QUIT:
            pygame.quit()
        if event.type == 5:
            scene = scenes['Battle']
            
    
    # обновление мира
    scene.update()

    # заливка фона
    screen.fill(background_color)
    # отрисовка мира
    scene.draw(screen)

    # обновление экрана
    pygame.display.update()

    # пропускаем лишнее время, чтобы
    # добиться 60 фреймов в секунду
    clock.tick(60)
