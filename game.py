import pygame, sys
import pygame.locals as pgl
from goalkeeper import Goalkeeper


# магическая команда инициализации модуля
pygame.init()

BLACK = (0, 0, 0, 0)
WHITE = (255, 255, 255, 0)

WINDOWWIDTH = 400 # размер окна по длине
WINDOWHEIGHT = 300 # размер окна по ширине

RECTWIDTH = round(WINDOWHEIGHT / 100 * 2) + round(WINDOWWIDTH / 100 * 1) # размер игрока по длине
RECTHEIGHT = round(WINDOWHEIGHT  / 100 * 20) # размер игрока по ширине
OFFSET = 15 # расстояние игрока от стенки

# создаем экран 400х300 и меняем заголовок окна
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pong')

# цвет фона
background_color = BLACK

# объект игрока
goalkeeper = Goalkeeper(x = OFFSET, y = (WINDOWHEIGHT - RECTHEIGHT) / 2, min_y = 0, speed = 5,
                       max_y = WINDOWHEIGHT,width = RECTWIDTH,height = RECTHEIGHT, color =WHITE)

# объект для отслеживания времени
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

class GameMenu():
    def __init__(self, screen, bg_color=(0,0,0)):
 
        self.screen = screen
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
 
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
 
            # Redraw the background
            self.screen.fill(self.bg_color)
            largeText = pygame.font.Font('freesansbold.ttf',15)
            TextSurf, TextRect = text_objects("PONG", largeText)
            TextRect.center = ((WINDOWWIDTH/2),(WINDOWHEIGHT/2))
            screen.blit(TextSurf, TextRect)
            pygame.display.flip()
 
#if __name__ == "__main__":
    # Creating the screen
    #screen = pygame.display.set_mode((640, 480), 0, 32)
    #pygame.display.set_caption('Game Menu')
gm = GameMenu(screen)
gm.run()

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
    screen.fill(background_color)
    # отрисовка игрока
    goalkeeper.draw(screen)

    # обновление экрана
    pygame.display.update()

    # пропускаем лишнее время, чтобы
    # добиться 60 фреймов в секунду
    clock.tick(60)
