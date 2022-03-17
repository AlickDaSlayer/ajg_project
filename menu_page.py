import pygame
import sys
from main import *

screen = pygame.display.set_mode((800,480))

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
GREY = (70, 67, 74)
WHITE = (255, 255, 255)
LILAC = (169, 126, 230)
PURPLE = (105, 39, 196)
DARKBLUE = (22, 57, 110)

font1 = pygame.font.SysFont(None, 150)
font2 = pygame.font.SysFont(None, 100)
font3 = pygame.font.SysFont(None, 160)

def draw_text(text, font, colour, x, y):
    text_obj = font.render(text, 1, colour)
    text_rect = text_obj.get_rect()
    text_rect_x = x
    text_rect_y = y
    text_image = screen.blit(text_obj, (text_rect_x, text_rect_y))


def menu():
    while True:
        screen.fill(DARKBLUE)
        draw_text("Main Menu", font3, GREY, 131, 95)
        draw_text("Main Menu", font3, WHITE, 125, 100)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 300, 200, 75)
        button_shadow = pygame.Rect(305, 295, 200, 75)
        pygame.draw.rect(screen, GREY, button_shadow)
        pygame.draw.rect(screen, PURPLE, button_1)
        draw_text("Start", font2, WHITE, 318, 307)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mx, my)):
            if click:
                main()

        pygame.display.update()
        clock.tick(60)
