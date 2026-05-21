import pygame

from game_objects.background import Map
from game_objects.sprite import Sprite

sprite_img_path = "assets/menu_sprites/"
window_map_path = "assets/map/"
ui_sprites_path = "assets/ui/"

def load_menu_screen():
    menu_map = init_menu_map()
    ui_elements = init_ui_elements()

    return menu_map, ui_elements

def init_ui_elements():
    ui_objects_sprites = pygame.sprite.Group()

    logo_app = pygame.image.load(f"{ui_sprites_path}study-cafe-logo.png").convert_alpha()
    start_button = pygame.image.load(f"{ui_sprites_path}start_button.png").convert_alpha()
    join_button = pygame.image.load(f"{ui_sprites_path}join_button.png").convert_alpha()
    exit_button = pygame.image.load(f"{ui_sprites_path}exit_button.png").convert_alpha()

    logo = Sprite(logo_app, 230, 70, test_callback, "logo")
    start = Sprite(start_button, 225, 115, test_callback, "start_session", )
    join = Sprite(join_button, 225, 150, test_callback, "join_session", )
    exiting = Sprite(exit_button, 255, 195, test_callback, "exit")

    ui_objects_sprites.add(logo, start, join, exiting)

    return ui_objects_sprites

def test_callback():
    print(f"testing the buttons")

def init_menu_map():
    menu_map = f"{window_map_path}menu_map.csv"
    sprites = init_menu_sprites()

    return Map(
        csv_file=menu_map,
        tile_images=sprites,
        tile_size=64
    )

def init_menu_sprites():
    return [
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