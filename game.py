import pygame, sys
import pygame.locals as pgl
from goalkeeper import Goalkeeper


# магическая команда инициализации модуля
pygame.init()

WINDOWWIDTH = 400 # размер окна по длине
WINDOWHEIGHT = 300 # размер окна по ширине

RECTWIDTH = round(WINDOWHEIGHT / 100 * 2) + round(WINDOWWIDTH / 100 * 1) # размер игрока по длине
RECTHEIGHT = round(WINDOWHEIGHT  / 100 * 20) # размер игрока по ширине
OFFSET = 15 # расстояние игрока от стенки

# создаем экран 400х300 и меняем заголовок окна
display = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pong')

# цвет фона
background_color = pygame.Color(127, 198, 127, 0)

# объект игрока
goalkeeper = Goalkeeper(OFFSET, (WINDOWHEIGHT - RECTHEIGHT) / 2, RECTWIDTH, RECTHEIGHT,  0, WINDOWHEIGHT)

# объект для отслеживания времени
clock = pygame.time.Clock()

while True:
    # перебираем все ивенты в очереди
    for event in pygame.event.get():
        # пользователь закрыл окно
        if event.type == pgl.QUIT:
            pygame.quit()
            sys.exit()

    # обновление движения игрока
    goalkeeper.update()

    # заливка фона
    display.fill(background_color)
    # отрисовка игрока
    goalkeeper.draw(display)

    # обновление экрана
    pygame.display.update()

    # пропускаем лишнее время, чтобы
    # добиться 60 фреймов в секунду
    clock.tick(60)
