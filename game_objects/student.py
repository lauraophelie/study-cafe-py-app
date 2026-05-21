import pygame

class Student(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, speed=4):
        super().__init__()

        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        
    def update(self, events=None):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed