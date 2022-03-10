from ast import Delete
from cmath import rect
from queue import Empty
import pygame
from pygame.locals import *
import sys
import random
import math
from classes import *
from maps import *
from menu import *


BLACK = (0, 0, 0)
GREY = (70, 67, 74)
WHITE = (255, 255, 255)
LILAC = (169, 126, 230)
PURPLE = (105, 39, 196)
DARKBLUE = (22, 57, 110)

pygame.init()

def draw_timer(screen, x, y, output):
    font = pygame.font.Font(None, 36) #Choose the font for the text
    text = font.render(output, 1, WHITE) #Create the text
    screen.blit(text, (x, y)) #Draw the text on the screen

font1 = pygame.font.SysFont(None, 150)
font2 = pygame.font.SysFont(None, 100)
font3 = pygame.font.SysFont(None, 160)


display = (800, 480)                                # Set screen width,height
screen = pygame.display.set_mode(display)           # Create window
pygame.display.set_caption("Project")               # Title

all_sprite_group = pygame.sprite.Group()

frame_rate = 60

clock = pygame.time.Clock()

player = Player(PURPLE, 16, 16, (display[0]/2), (display[1]/2))
player_group = pygame.sprite.pygame.sprite.GroupSingle(player)
all_sprite_group.add(player)


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

def main():

    frame_count = 0

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        ## - Logic for game timer 
        total_seconds = frame_count // frame_rate
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

        all_sprite_group.update()
        screen.fill(DARKBLUE)
        all_sprite_group.draw(screen)

        # - Timer drawn on screen
        draw_timer(screen, 350, 20, output_string)

        frame_count += 1    # - Frame count increases every iteration of the game loop
        
        clock.tick(frame_rate)

        pygame.display.flip()


if __name__ == "__main__":
    menu()
    pygame.quit()
    sys.exit()

