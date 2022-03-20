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
from menu_page import *

pygame.init()

display = (800, 480)                                # Set screen width,height
screen = pygame.display.set_mode(display)           # Create window
pygame.display.set_caption("Project")               # Title


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2(300,100) 
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
    
    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player):
        
        self.center_target_camera(player)

        # Iterating through all the sprites in the camera group
        for sprite in self.sprites(): 
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
    
    def delete(self):
        for sprite in self.sprites():
            sprite.kill()


BLACK = (0, 0, 0)
GREY = (70, 67, 74)
WHITE = (255, 255, 255)
LILAC = (169, 126, 230)
PURPLE = (105, 39, 196)
DARKBLUE = (22, 57, 110)
GOLD = (252, 186, 3)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


def draw_timer(screen, x, y, output):
    font = pygame.font.Font(None, 30) # Choose the font for the text
    text = font.render(output, 1, WHITE) # Create the text
    screen.blit(text, (x, y)) # Draw the text on the screen
#endfunction

font1 = pygame.font.SysFont(None, 150)
font2 = pygame.font.SysFont(None, 100)
font3 = pygame.font.SysFont(None, 160)


camera_group = CameraGroup() # Initialise camera group

frame_rate = 60

clock = pygame.time.Clock()

def draw_map(map):
    x = 0
    y = 0

    for row in map:
        for col in row:
            if col == 1:
                grass_wall = Wall("assets/grass.png", 16, 16, x, y, camera_group)
                screen.blit(grass_wall.image, [grass_wall.rect.x, grass_wall.rect.y])
                #all_sprite_group.add(grass_wall)
                wall_group.add(grass_wall)
            if col == 2:
                dirt_wall = Wall("assets/dirt.png", 16, 16, x, y, camera_group)
                screen.blit(dirt_wall.image, [dirt_wall.rect.x, dirt_wall.rect.y])
                #all_sprite_group.add(dirt_wall)
                wall_group.add(dirt_wall)
            if col == 3:
                portal = Portal(GOLD, 16, 16, x, y, camera_group)
                screen.blit(portal.image, [portal.rect.x, portal.rect.y])
                portal_group.add(portal)
            if col == 4:
                trap = Traps(RED, 16, 16, x, y, camera_group)
                screen.blit(trap.image, [trap.rect.x, trap.rect.y])
                traps_group.add(trap)
            if col == 5:
                enemy = Enemy(GREEN, 16, 16, x, y, camera_group)
                screen.blit(enemy.image, [enemy.rect.x, enemy.rect.y])
            x += 16
        x = 0
        y += 16


def level1():

    player = Player(PURPLE, 16, 16, 480, 448, camera_group)
    player_group = pygame.sprite.pygame.sprite.GroupSingle(player)

    draw_map(map1)

    fog = Fog("assets/fog.png", 800, 860, -800, 0, camera_group)

    frame_count = 0

    game_end = False

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
                if event.key == pygame.K_SPACE and player.space_pressed is True: 
                    player.space_pressed = False
                    player.can_doublejump = True
                    player.jump()

        ## - Logic for game timer 
        total_seconds = frame_count // frame_rate
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

        ## - Logic for cooldown
        player.cooldown_tracker += clock.get_time()
        print(player.cooldown_tracker)

        ## - Collision with fog 
        if pygame.sprite.collide_rect(player, fog) == True:
            camera_group.delete()
            game_end = True
            done = True 
        
        ## - Collision with traps
        for trap in traps_group:
            if player.rect.colliderect(trap):
                camera_group.delete()
                game_end = True
                done = True             

        ## - Next level
        portal_hit = pygame.sprite.spritecollide(player, portal_group, False)
        for portal in portal_hit:
            if player.rect.colliderect(portal):
                camera_group.delete()
                done = True


        camera_group.update()
        screen.fill(DARKBLUE)
        camera_group.custom_draw(player)

        # - Timer drawn on screen
        draw_timer(screen, 350, 30, output_string)

        frame_count += 1    # - Frame count increases by one every iteration of the game loop
        
        clock.tick(frame_rate)

        pygame.display.flip()
    #endwhile

    if game_end is False:
        level2()

#endfunction

def level2():

    player = Player(PURPLE, 16, 16, 480, 448, camera_group)
    player_group = pygame.sprite.pygame.sprite.GroupSingle(player)

    draw_map(map2)

    fog = Fog("assets/fog.png", 800, 860, -800, 0, camera_group)

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
                if event.key == pygame.K_SPACE and player.space_pressed is True: 
                    player.space_pressed = False
                    player.can_doublejump = True
                    player.jump()
 


        ## - Logic for game timer 
        total_seconds = frame_count // frame_rate
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

        ## - Logic for fog 
        death = pygame.sprite.collide_rect(player, fog)
        if death == True:
            player.delete()
            for wall in wall_group:
                wall.delete()
            fog.delete()
            done = True 
            

        camera_group.update()
        screen.fill(DARKBLUE)
        camera_group.custom_draw(player)

        # - Timer drawn on screen
        draw_timer(screen, 350, 30, output_string)

        frame_count += 1    # - Frame count increases by one every iteration of the game loop
        
        clock.tick(frame_rate)

        pygame.display.flip()
    #endwhile
#endfunction


if __name__ == "__main__":
    menu()


