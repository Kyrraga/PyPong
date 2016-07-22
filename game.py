import pygame, sys
from pygame.locals import *
import pygame.locals as pgl
import world_init


# магическая команда инициализации модуля
pygame.init()

BLACK = (0, 0, 0, 0)
WHITE = (255, 255, 255, 0)

BOXSIZE = 40 # size of box height & width in pixels
GAPSIZE = 10 # size of gap between boxes in pixels


# создаем экран с заданным размером и меняем заголовок окна
WINDOWWIDTH = 400
WINDOWHEIGHT = 300
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('PyPong')

# цвет фона
background_color = pygame.Color(127, 198, 127, 0)

# инициализация мира
world = world_init.init(WINDOWWIDTH, WINDOWHEIGHT)

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
            mouseClicked = False
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                elif event.type == MOUSEMOTION:
                    mousex, mousey = event.pos
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    mouseClicked = True
            
            if mousex > WINDOWWIDTH/2 and mousey > WINDOWHEIGHT/2:
                pygame.display.set_caption('PyPong1')
            
 
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
 
#gm = GameMenu(screen)
#gm.run()

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
    screen.fill(background_color)
    # отрисовка мира
    world.draw(screen)

    # обновление экрана
    pygame.display.update()

    # пропускаем лишнее время, чтобы
    # добиться 60 фреймов в секунду
    clock.tick(60)
