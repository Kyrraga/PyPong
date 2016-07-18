import pygame, sys
import pygame.locals as pgl


pygame.init()

display_surface = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

background_color = pygame.Color(127, 198, 127, 0)
goalkeeper_rect = pygame.Rect(30, 100, 20, 60)
goalkeeper_color = pygame.Color(255, 255, 255, 0)

clock = pygame.time.Clock()

move_down = False
move_up = False
goalkeeper_speed = 10

while True:
    for event in pygame.event.get():
        if event.type == pgl.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pgl.KEYDOWN:
            if event.key == pgl.K_DOWN:
                move_down = True
            if event.key == pgl.K_UP:
                move_up = True
        elif event.type == pgl.KEYUP:
            if event.key == pgl.K_DOWN:
                move_down = False
            if event.key == pgl.K_UP:
                move_up = False

    if move_down:
        goalkeeper_rect.y += goalkeeper_speed
    if move_up:
        goalkeeper_rect.y -= goalkeeper_speed

    display_surface.fill(background_color)
    pygame.draw.rect(display_surface,
                     goalkeeper_color,
                     goalkeeper_rect)

    pygame.display.update()

    clock.tick(60)
