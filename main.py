import pygame
from pygame.locals import *
import sys
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

display = (700, 500)                                # Set screen width,height
screen = pygame.display.set_mode(display)           # Create window
pygame.display.set_caption("Project")               # Title
pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left_pressed = False
        self.right_pressed = False
        self.y_momentum = 0
        self.velX = 0
        self.bounce = 0

    # def set_speed(self, val):
    #     self.speed = val

    def update(self):
        self.velX = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -5
        if self.right_pressed and not self.left_pressed:
            self.velX = 5

        self.rect.x += self.velX
        self.rect.y += self.y_momentum


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

        if player.rect.y > 480:
            player.y_momentum = -player.y_momentum
            player.bounce += 1
        else:
            player.y_momentum += 0.2

        if player.bounce == 3:
            player.y_momentum = player.y_momentum

        all_sprite_group.update()
        screen.fill(WHITE)
        all_sprite_group.draw(screen)

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
    pygame.quit()

