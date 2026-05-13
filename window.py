import pygame
from background import Map 

pygame.init()

window = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Study café")

sprite_path = "assets/sprites/"
sprites = [
    pygame.image.load(f"{sprite_path}wall-tile.png").convert_alpha(),
    pygame.image.load(f"{sprite_path}woodtile-sprite.png").convert_alpha()
]
window_map = Map("map.csv", sprites, tile_size=32)

run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    window_map.render(window)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()