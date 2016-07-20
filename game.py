import pygame, sys
import pygame.locals as pgl
import world_init


# магическая команда инициализации модуля
pygame.init()

# создаем экран с заданным размером и меняем заголовок окна
WINDOWWIDTH = 400
WINDOWHEIGHT = 300
display = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('PyPong')

# цвет фона
background_color = pygame.Color(127, 198, 127, 0)

# инициализация мира
world = world_init.init(WINDOWWIDTH, WINDOWHEIGHT)

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
    display.fill(background_color)
    # отрисовка мира
    world.draw(display)

    # обновление экрана
    pygame.display.update()

    # пропускаем лишнее время, чтобы
    # добиться 60 фреймов в секунду
    clock.tick(60)
