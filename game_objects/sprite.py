import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, sprite_image, position_x, position_y, sprite_name=""):
        super().__init__()
        self.image = sprite_image
        self.rect = self.image.get_rect()

        self.rect.x = position_x
        self.rect.y = position_y
        self.name = sprite_name

    def update(self):
        pass

