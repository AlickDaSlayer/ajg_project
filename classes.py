from cgitb import grey
import pygame
import math

wall_group = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, x, y, group):
        super().__init__(group)
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # jumping
        self.jumping = [0, 0] # y value of jumping
        self.is_jumping = False
        self.falling = [0, 0] # - self.falling[1] => speed of falling
        self.is_falling = False
        self.vel = [0, 0]
        self.acc = [0, 0.5]
        self.step = [4, 0]
        self.gravity_acc = [0, 0]
        self.jump_dec = [0, 0]
        self.can_doublejump = False
        self.space_pressed = False
        # wall sliding
        self.left_sliding = False
        self.right_sliding = False

    def delete(self):
        self.kill()

    def gravity(self):
        # Gravitational acceleration is by default 0
        self.gravity_acc = [0, 0]
        # If the speed of falling doesn't exceed 10 and the player isn't in the process of jumping upwards
        if self.falling[1] <= 10 and self.jumping[1] >= 0 and self.is_falling and self.left_sliding is False or self.right_sliding is False:
            # Sets the acceleration to a value
            self.gravity_acc = [0, 0.5]
        if self.is_falling and self.can_doublejump is False:
            # Increases the speed of falling when in air
            self.falling[1] += self.gravity_acc[1]
            self.move("down")

        while self.left_sliding is True or self.right_sliding is True:
            self.gravity_acc = [0, 0.1]

    
    def jump(self):
        
        if self.can_doublejump is True:
            self.jumping[1] = -8
            self.can_doublejump = False

        # Deceleration on the upward jumping speed is by default 0
        self.jump_dec = [0, 0]
        # If the player is jumping and the player is going upwards
        if self.is_jumping and self.jumping[1] <= 0 and self.can_doublejump is False:
            # A value is assigned to deceleration
            self.jump_dec = [0, 0.1]   # Value which pulls the player downs as soon as it starts jumping

        if self.falling[1] >= 0 and self.can_doublejump is False: # If the player is falling
            self.is_falling = True
            # Makes the player fall(calling the gravity function) if the jumping deceleration
            # is making the player to go down
        if self.is_jumping is False: # If the player is not jumping
            self.is_falling = False
            self.is_jumping = True
            self.space_pressed = False

        self.jumping[1] += self.jump_dec[1]

    def move(self, direction):
        
        # Movement
        if direction == 'left':
            self.rect.left -= self.step[0]
        if direction == 'right':
            self.rect.right += self.step[0]
        if direction == 'up':
            self.rect.top += self.jumping[1]
        if direction == 'down':
            self.rect.bottom += self.falling[1]

        walls_hit = pygame.sprite.spritecollide(self, wall_group, False)
        for wall in walls_hit:
            if self.rect.colliderect(wall):
                if direction == "left":
                    self.rect.left = wall.rect.right
                    self.left_sliding = True
                else:
                    self.left_sliding = False
                if direction == "right":
                    self.rect.right = wall.rect.left
                    self.right_sliding = True
                else:
                    self.right_sliding = False 
                if direction == "up":
                    self.rect.top = wall.rect.bottom
                    self.jumping[1] = 0
                    self.is_jumping = True
                if direction == "down":
                    self.rect.bottom = wall.rect.top
                    self.is_falling = False
                    self.falling[1] = 0
                    self.jumping[1] = -6.5




    def update(self):
        # Move the player if relevant key press detected.
        keys = pygame.key.get_pressed()
        # Player 
        if keys[pygame.K_a]:
            self.move("left")
            self.is_jumping = True
        if keys[pygame.K_d]:
            self.move("right")
            self.is_jumping = True
        if keys[pygame.K_SPACE] and self.can_doublejump is False:
            self.jump()
            self.move("up")
            self.space_pressed = True
        else:
            # If the player no longer presses on the key, sets the jumping speed to 0
            self.jumping[1] = 0  

        self.gravity()
        self.jump()
    


class Wall(pygame.sprite.Sprite):
    def __init__(self, sprite, width, height, x, y, group):
        super().__init__(group)
        self.surface = pygame.Surface([width, height])
        self.image = pygame.image.load(sprite)
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y

    def delete(self):
        self.kill() 

class Fog(pygame.sprite.Sprite):
    def __init__(self, sprite, width, height, x, y, group):
        super().__init__(group)
        self.surface = pygame.Surface([width, height])
        self.image = pygame.image.load(sprite)
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += 1
    
    def delete(self):
        self.kill()


    

