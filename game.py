import pygame, sys
import pygame.locals as pgl


# магическая команда инициализации модуля
pygame.init()

# описание объектов - задний фон и прямоугольник игрока
WINDOWWIDTH = 500 # размер окна по длине
WINDOWHEIGHT = 400 # размер окна по ширине

RECTWIDTH = round(WINDOWHEIGHT / 100 * 2) + round(WINDOWWIDTH / 100 * 1) # размер игрока по длине
RECTHEIGHT = round(WINDOWHEIGHT  / 100 * 20) # размер игрока по ширине
OFFSET = 15 # расстояние игрока от стенки

background_color = pygame.Color(127, 198, 127, 0)
#goalkeeper_rect = pygame.Rect(OFFSET + RECTWIDTH, 100, OFFSET, 60)
goalkeeper_rect = pygame.Rect(OFFSET,WINDOWHEIGHT / 2 - RECTHEIGHT,RECTWIDTH,RECTHEIGHT)
goalkeeper_color = pygame.Color(255, 255, 255, 0)

# создаем экран 400х300 и меняем заголовок окна
display = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Hello World!')

# объект для отслеживания времени
clock = pygame.time.Clock()

# нажата ли клавиша в данный момент
move_down = False
move_up = False

# скорость движения игрока
goalkeeper_speed = 10

while True:
    # перебираем все ивенты в очереди
    for event in pygame.event.get():
        # пользователь закрыл окно
        if event.type == pgl.QUIT:
            pygame.quit()
            sys.exit()
        # пользователь нажал клавишу
        elif event.type == pgl.KEYDOWN:
            if event.key == pgl.K_DOWN:
                move_down = True
            if event.key == pgl.K_UP:
                move_up = True
        # пользователь отпустил клавишу
        elif event.type == pgl.KEYUP:
            if event.key == pgl.K_DOWN:
                move_down = False
            if event.key == pgl.K_UP:
                move_up = False

    #str st = goalkeeper_rect.y
    pygame.display.set_caption(str(goalkeeper_rect.y))


    # обновление движения игрока
    if (goalkeeper_rect.y < WINDOWHEIGHT  - RECTHEIGHT):
        if move_down:
            goalkeeper_rect.y += goalkeeper_speed
    if (goalkeeper_rect.y >= 10):
        if move_up:
            goalkeeper_rect.y -= goalkeeper_speed

    # заливка фона
    display.fill(background_color)
    # отрисовка игрока
    pygame.draw.rect(display,
                     goalkeeper_color,
                     goalkeeper_rect)

    # обновление экрана
    pygame.display.update()

    # пропускаем лишнее время, чтобы
    # добиться 60 фреймов в секунду
    clock.tick(60)
