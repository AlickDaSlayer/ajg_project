import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        # jumping
        self.jumping = False
        self.in_air = True
        self.falling = False 
        self.velY = 13
        self.velX = 0
        self.momentum = 5
        self.ground = False

    def move(self, val1):
        self.rect.x += val1 


    def update(self):
        self.velX = 0

        self.rect.x += self.velX
    
    def delete(self):
        self.kill()


class Wall(pygame.sprite.Sprite):
    def __init__(self, sprite, width, height, x, y):
        super().__init__()
        self.surface = pygame.Surface([width, height])
        self.image = pygame.image.load(sprite)
        self.rect = self.surface.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def move(self, val1):
        self.rect.x += val1 

    def delete(self):
        self.kill() 
    

