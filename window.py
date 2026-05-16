import pygame
from game_objects.background import Map

pygame.init()

window = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Study café")

sprite_img_path = "assets/sprites/"
window_map_path = "assets/map/"

sprites = [
    pygame.image.load(f"{sprite_img_path}wall-tile.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}woodtile-sprite.png").convert_alpha()
]
window_map = Map(f"{window_map_path}menu_map.csv", sprites, tile_size=32)

run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    window_map.render(window)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()