import pygame

class Student(pygame.sprite.Sprite):
    def __init__(self, x, y, collision_sprites, speed=4):
        super().__init__()
        self.speed = speed

        self.images = {
            "down": pygame.image.load("assets/sprites/mini-chair-sprite.png").convert_alpha(),
            "up": pygame.image.load("assets/sprites/mini-chair-sprite.png").convert_alpha(),
            "left": pygame.image.load("assets/sprites/mini-chair-sprite.png").convert_alpha(),
            "right": pygame.image.load("assets/sprites/mini-chair-sprite.png").convert_alpha()
        }
        self.direction = "down"
        self.image = self.images[self.direction]
        self.rect = self.rect = self.image.get_rect(topleft=(x, y))
        self.collision_sprites = collision_sprites
        
    def update(self, events=None):
        keys = pygame.key.get_pressed()
        moving = False

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.check_collision():
                self.rect.x += self.speed

            self.direction = "left"
            moving = True

        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.check_collision():
                self.rect.x -= self.speed

            self.direction = "right"
            moving = True

        elif keys[pygame.K_UP]:
            self.rect.y -= self.speed
            if self.check_collision():
                self.rect.y += self.speed

            self.direction = "up"
            moving = True

        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            if self.check_collision():
                self.rect.y -= self.speed

            self.direction = "down"
            moving = True
        self.image = self.images[self.direction]

    def check_collision(self):
        for sprite in self.collision_sprites:
            if self.rect.colliderect(sprite.rect):
                return True
        return False