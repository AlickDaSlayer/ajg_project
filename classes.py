import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, x, y, walls):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.left_pressed = False
        self.right_pressed = False
        self.jumping = False
        self.velY = 20
        self.velX = 0
        self.momentum = 5
        self.walls = walls

    def update(self):
        self.velX = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -5
        if self.right_pressed and not self.left_pressed:
            self.velX = 5


        player_collision = pygame.sprite.spritecollide(self, self.walls, False)
        for x in player_collision:
            if self.rect.y > x.rect.y-20:
                self.rect.y = x.rect.y-20

        self.rect.x += self.velX
        self.rect.y += self.momentum


class Wall(pygame.sprite.Sprite):
    def __init__(self, sprite, width, height, x, y):
        super().__init__()
        self.surface = pygame.Surface([width, height])
        self.image = pygame.image.load(sprite)
        self.rect = self.surface.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
