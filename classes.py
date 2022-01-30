import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # jumping
        self.jumping = [0, 0]
        self.is_jumping = False
        self.falling = [0, 0]
        self.is_falling = False
        self.vel = [0, 0]
        self.acc = [0, 0]

    def gravity(self):
        pass

    def move(self, val1):
        self.rect.x += val1

    def collided(self, sprite):
        self.rect.colliderect(sprite)


    def update(self):
        pass
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_a]:
        #     player.move(-2)
        #     for all in wall_group:
        #         all.rect.x += 2

        # if keys[pygame.K_d]:
        #     player.move(2)
        #     for what in wall_group:
        #         what.rect.x -= 2
    
    def delete(self):
        self.kill()


class Wall(pygame.sprite.Sprite):
    def __init__(self, sprite, width, height, x, y):
        super().__init__()
        self.surface = pygame.Surface([width, height])
        self.image = pygame.image.load(sprite)
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def move(self, val1):
        self.rect.x += val1 

    def delete(self):
        self.kill() 
    

