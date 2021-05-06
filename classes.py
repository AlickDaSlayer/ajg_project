import pygame

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
        self.jumping = False
        self.y_momentum = 0
        self.velX = 0
        self.bounce = 0


    def update(self):
        self.velX = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -5
        if self.right_pressed and not self.left_pressed:
            self.velX = 5

        self.rect.x += self.velX
        self.rect.y += self.y_momentum