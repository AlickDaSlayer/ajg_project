import pygame
from pygame.locals import *
import sys
import random
import math
from classes import *
from maps import *


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
wall_group = pygame.sprite.Group()

clock = pygame.time.Clock()


def draw_map():
    x = 0
    y = 0

    for row in map:
        for col in row:
            if col == 1:
                grass_wall = Wall("assets/grass.png", 16, 16, x, y)
                screen.blit(grass_wall.image, [grass_wall.rect.x, grass_wall.rect.y])
                all_sprite_group.add(grass_wall)
                wall_group.add(grass_wall)
            if col == 2:
                dirt_wall = Wall("assets/dirt.png", 16, 16, x, y)
                screen.blit(dirt_wall.image, [dirt_wall.rect.x, dirt_wall.rect.y])
                all_sprite_group.add(dirt_wall)
                wall_group.add(dirt_wall)
            x += 16
        x = 0
        y += 16
draw_map()


player = Player(BLUE, 16, 16, 100, 200)
all_sprite_group.add(player)


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

        userInput = pygame.key.get_pressed()

        if player.jumping is False and userInput[pygame.K_SPACE]:
            player.jumping = True
        if player.jumping is True:
            player.rect.y -= player.velY
            player.velY -= 1
            if player.velY < -20:
                player.jumping = False
                player.velY = 20

        player_collision = pygame.sprite.spritecollideany(player, wall_group)


        all_sprite_group.update()
        screen.fill(WHITE)
        all_sprite_group.draw(screen)

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
    pygame.quit()

