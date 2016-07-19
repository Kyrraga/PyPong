import pygame, sys
import pygame.locals as pgl
from goalkeeper import Goalkeeper


# магическая команда инициализации модуля
pygame.init()

# создаем экран 400х300 и меняем заголовок окна
WIDTH = 400
HEIGHT = 300
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

# цвет фона
background_color = pygame.Color(127, 198, 127, 0)

# объекты игроков
goalkeeper1 = Goalkeeper(10, 10, 0, HEIGHT,
                         color=pygame.Color(255, 64, 64, 0))
goalkeeper2 = Goalkeeper(WIDTH - 40, 10, 0, HEIGHT,
                         color=pygame.Color(64, 64, 255, 0),
                         key_up=pgl.K_w,
                         key_down=pgl.K_s)

# объект для отслеживания времени
clock = pygame.time.Clock()

while True:
    # перебираем все ивенты в очереди
    for event in pygame.event.get():
        # пользователь закрыл окно
        if event.type == pgl.QUIT:
            pygame.quit()
#           sys.exit()  # не нужно в интерактивном режиме

    # обновление движения игрока
    goalkeeper1.update()
    goalkeeper2.update()

    # заливка фона
    display.fill(background_color)
    # отрисовка игрока
    goalkeeper1.draw(display)
    goalkeeper2.draw(display)

    # обновление экрана
    pygame.display.update()

    # пропускаем лишнее время, чтобы
    # добиться 60 фреймов в секунду
    clock.tick(60)
