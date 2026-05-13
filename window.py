import pygame
from background import Map
from sprite import Sprite 

pygame.init()

window = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Study café")

sprite_path = "assets/sprites/"
sprites = [
    pygame.image.load(f"{sprite_path}wall-tile.png").convert_alpha(),
    pygame.image.load(f"{sprite_path}woodtile-sprite.png").convert_alpha()
]
window_map = Map("map.csv", sprites, tile_size=32)

all_objects_sprites = pygame.sprite.Group()

book_shelf_sprite = pygame.image.load(f"{sprite_path}book-shelf.png").convert_alpha()
clock_sprite = pygame.image.load(f"{sprite_path}clock-sprite.png").convert_alpha()
couch_sprite = pygame.image.load(f"{sprite_path}couch-blue.png").convert_alpha()
plant_sprite = pygame.image.load(f"{sprite_path}plant.png").convert_alpha()

chair_sprite = pygame.image.load(f"{sprite_path}chair-attempt.png").convert_alpha()
table_sprite = pygame.image.load(f"{sprite_path}table.png").convert_alpha()

couch = Sprite(couch_sprite, 136, 62, "couch")
plant = Sprite(plant_sprite, 224, 75, "plant")
book_shelf = Sprite(book_shelf_sprite, 240, 43, "book_shelf")
clock = Sprite(clock_sprite, 320, 11, "clock")

all_objects_sprites.add(couch, plant, book_shelf, clock)

run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    window_map.render(window)
    all_objects_sprites.draw(window)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()