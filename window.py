import pygame
from game_objects.background import Map
from game_objects.sprite import Sprite

pygame.init()

window = pygame.display.set_mode((640, 384))
pygame.display.set_caption("Study café")

sprite_img_path = "assets/menu_sprites/"
window_map_path = "assets/map/"

sprites = [
    pygame.image.load(f"{sprite_img_path}walltile-sprite-dleft.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}walltile-sprite-btop.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}walltile-sprite-dright.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}walltile-sprite-bleft.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}walltile-sprite.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}walltile-sprite-bright.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}wood-wall-tile-bleft.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}wood-wall-tile.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}wood-wall-tile-bright.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}woodtile-sprite-bleft.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}woodtile-sprite.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}woodtile-sprite-bright.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}woodtile-sprite-dleft.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}woodtile-sprite-bbottom.png").convert_alpha(),
    pygame.image.load(f"{sprite_img_path}woodtile-sprite-dright.png").convert_alpha()
    
]
window_map = Map(f"{window_map_path}menu_map.csv", sprites, tile_size=64)

all_objects_sprites = pygame.sprite.Group()

ui_sprites_path = "assets/ui/"

logo_app = pygame.image.load(f"{ui_sprites_path}study-cafe-logo.png").convert_alpha()

start_button = pygame.image.load(f"{ui_sprites_path}start_button.png").convert_alpha()
join_button = pygame.image.load(f"{ui_sprites_path}join_button.png").convert_alpha()
exit_button = pygame.image.load(f"{ui_sprites_path}exit_button.png").convert_alpha()

def create_session():
    print("create study session")

def join_study_session():
    print("join study session")

logo = Sprite(logo_app, 230, 70, "logo")
start = Sprite(start_button, 225, 115, "start_session", create_session)
join = Sprite(join_button, 225, 150, "join_session", join_study_session)
exiting = Sprite(exit_button, 255, 195, "exit")

all_objects_sprites.add(logo, start, join, exiting)

run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    window_map.render(window)
    all_objects_sprites.draw(window)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()