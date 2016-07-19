import pygame, sys
import pygame.locals as pgl
from goalkeeper import Goalkeeper


# магическая команда инициализации модуля
pygame.init()

# создаем экран 400х300 и меняем заголовок окна
display = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

# цвет фона
background_color = pygame.Color(127, 198, 127, 0)

# объект игрока
goalkeeper = Goalkeeper(10, 10, 0, 300)

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
