import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, sprite_image, position_x, position_y, callback, sprite_name=""):
        super().__init__()
        self.image = sprite_image
        self.rect = self.image.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y
        self.name = sprite_name
        self.callback = callback

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.callback()

