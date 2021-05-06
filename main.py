import pygame
from pygame.locals import *
import sys
import random
import math
from classes import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

display = (800, 480)                                # Set screen width,height
screen = pygame.display.set_mode(display)           # Create window
pygame.display.set_caption("Project")               # Title
pygame.init()

all_sprite_group = pygame.sprite.Group()

player = Player(BLUE, 20, 20, 200, screen.get_height()-20)
all_sprite_group.add(player)

clock = pygame.time.Clock()


def main():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.left_pressed = True
                if event.key == pygame.K_d:
                    player.right_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.left_pressed = False
                if event.key == pygame.K_d:
                    player.right_pressed = False

        # if player.rect.y > 480:
        #     player.y_momentum = -player.y_momentum
        #     player.bounce += 1
        # else:
        #     player.y_momentum += 0.2

        all_sprite_group.update()
        screen.fill(WHITE)
        all_sprite_group.draw(screen)

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
    pygame.quit()

