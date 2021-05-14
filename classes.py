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
        self.momentum = 7
        self.walls = walls
        self.scroll = [0, 0]

    def update(self):
        self.velX = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -5
        if self.right_pressed and not self.left_pressed:
            self.velX = 5

        player_collision = pygame.sprite.spritecollide(self, self.walls, False)
        for x in player_collision:
            if self.rect.bottom > x.rect.top:
                self.rect.bottom = x.rect.top

        self.rect.x += self.velX
        # Background scrolling
        self.rect.x -= self.scroll[0]
        self.rect.y -= self.scroll[1]


class Wall(pygame.sprite.Sprite):
    def __init__(self, sprite, width, height, x, y, scroll_x, scroll_y):
        super().__init__()
        self.surface = pygame.Surface([width, height])
        self.image = pygame.image.load(sprite)
        self.rect = self.surface.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.scroll_x = scroll_x
        self.scroll_y = scroll_y

    def update(self):
        self.rect.x -= self.scroll_x
        self.rect.y -= self.scroll_y
