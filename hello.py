import pygame, sys

pygame.init()

LINE_BOARD_COLOR = (23,145,135)
LINE_GROSSOR = 15

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("TIC TAC TOE Game")
screen.fill((28,170,156))
pygame.draw.line(screen, LINE_BOARD_COLOR, (0,200), (600,200), LINE_GROSSOR)
pygame.draw.line(screen, LINE_BOARD_COLOR, (0,400), (600,400), LINE_GROSSOR)

pygame.draw.line(screen, LINE_BOARD_COLOR, (200,0), (200,600), LINE_GROSSOR)
pygame.draw.line(screen, LINE_BOARD_COLOR, (400,0), (400,600), LINE_GROSSOR)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()