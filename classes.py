from cgitb import grey
import pygame
import math

wall_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()
traps_group = pygame.sprite.Group() 
enemy_group = pygame.sprite.Group()

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
        # cooldown
        self.cooldown_tracker = 0

    def delete(self):
        self.kill()

    def gravity(self):
        # Gravitational acceleration is by default 0
        self.gravity_acc = [0, 0]
        # If the speed of falling doesn't exceed 10 and the player isn't in the process of jumping upwards
        if self.falling[1] <= 10 and self.jumping[1] >= 0 and self.is_falling:
            # Sets the acceleration to a value
            self.gravity_acc = [0, 0.5]
        if self.is_falling and self.can_doublejump is False:
            # Increases the speed of falling when in air
            self.falling[1] += self.gravity_acc[1]
            self.move("down")

    
    def jump(self):
        
        if self.can_doublejump:
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
        #print(self.jumping[1])

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

        # collision with walls and ground
        walls_hit = pygame.sprite.spritecollide(self, wall_group, False)
        for wall in walls_hit:
            if self.rect.colliderect(wall):
                if direction == "left":
                    self.rect.left = wall.rect.right
                if direction == "right":
                    self.rect.right = wall.rect.left
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
        if keys[pygame.K_LSHIFT] and keys[pygame.K_a]:
            if self.cooldown_tracker > 3000:
                self.cooldown_tracker = 0
                self.rect.x -= 150
            else:
                self.move("left")
                self.is_jumping = True
        elif keys[pygame.K_a]:
            self.move("left")
            self.is_jumping = True

        if keys[pygame.K_LSHIFT] and keys[pygame.K_d]:
            if self.cooldown_tracker > 3000:
                self.cooldown_tracker = 0
                self.rect.x += 150
            else:
                self.move("right")
                self.is_jumping = True
        elif keys[pygame.K_d]:
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

class Portal(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, x, y, group):
        super().__init__(group)
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def delete(self):
        self.kill()
    
class Traps(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, x, y, group):
        super().__init__(group)
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def delete(self):
        self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, x, y, group):
        super().__init__(group)
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.step = 4

    def move(self):
        walls_hit = pygame.sprite.spritecollide(self, wall_group, False)
        for wall in walls_hit:
            if self.rect.colliderect(wall):
                self.step = self.step * -1

    
    def update(self):
        self.rect.x += self.step

        self.move()
            

    def delete(self):
        self.kill()
