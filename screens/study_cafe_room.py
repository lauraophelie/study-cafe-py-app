import pygame

from game_objects.background import Map

sprite_img_path = "assets/sprite/"
game_window_map = "assets/map/room_map.csv"

def init_background_sprites():
    sprites = [
        pygame.image.load(f"").convert_alpha()
    ]
    return sprites

def init_room_map(sprites, map_file_path):
    return Map(map_file_path, sprites, tile_size=32)
