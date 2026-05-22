import pygame

from game_objects.background import Map
from game_objects.sprite import Sprite
from game_objects.student import Student
from utils.registre import load_latest_session

sprite_img_path = "assets/sprites/"
game_window_map = "assets/map/room_map.csv"

def load_study_room():
    sprites = init_background_sprites()
    room_map = init_room_map(sprites, game_window_map)
    game_objects_sprites, collisions_sprites = init_game_objects_sprites()

    session = load_latest_session()
    if session:
        student = Student(
            x = session["position_x"],
            y = session["position_y"],
            collision_sprites=collisions_sprites,
            speed=3
        )
        game_objects_sprites.add(student)

    return room_map, game_objects_sprites, collisions_sprites

def init_background_sprites(length=13):
    sprites = []
    for i in range(0, length):
        image = pygame.image.load(f"{sprite_img_path + str(i)}.png").convert_alpha()
        sprites.append(image)

    return sprites

def init_room_map(sprites, map_file_path):
    return Map(
        csv_file=map_file_path, 
        tile_images=sprites, 
        tile_size=32
    )

def simple_callback():
    print(f"this is a sprite")

def init_game_objects_sprites():
    all_objects_sprites = pygame.sprite.Group()
    collisions_sprites = pygame.sprite.Group()

    book_shelf_sprite = pygame.image.load(f"{sprite_img_path}book-shelf.png").convert_alpha()
    clock_sprite = pygame.image.load(f"{sprite_img_path}clock-sprite.png").convert_alpha()
    couch_sprite = pygame.image.load(f"{sprite_img_path}couch-blue.png").convert_alpha()
    plant_sprite = pygame.image.load(f"{sprite_img_path}plant.png").convert_alpha()
    cafe_window_sprite = pygame.image.load(f"{sprite_img_path}cafe-window-sprite.png").convert_alpha()
    counter_sprite = pygame.image.load(f"{sprite_img_path}counter-serve-sprite.png").convert_alpha()
    small_chair = pygame.image.load(f"{sprite_img_path}mini-chair-sprite.png").convert_alpha()

    couch = Sprite(couch_sprite, 122, 48, simple_callback, "couch")
    book_shelf = Sprite(book_shelf_sprite, 176, 42, simple_callback, "book_shelf")
    plant = Sprite(plant_sprite, 224, 74, simple_callback, "plant")
    clock = Sprite(clock_sprite, 253, 42, simple_callback, "clock")
    cafe_window = Sprite(cafe_window_sprite, 352, 32, simple_callback, "cafe_window")
    counter = Sprite(counter_sprite, 432, 80, simple_callback, "counter")

    all_objects_sprites.add(couch, plant, book_shelf, clock, cafe_window, counter)
    collisions_sprites.add(couch, plant, book_shelf, clock, cafe_window, counter)

    mini_chair_pos_y = 144
    mini_chair_pos_x = 448

    for i in range(0, 3):
        mini_chair = Sprite(small_chair, mini_chair_pos_x, mini_chair_pos_y, simple_callback, f"mini-chair-{i}")
        mini_chair_pos_x += 52
        all_objects_sprites.add(mini_chair)
        collisions_sprites.add(mini_chair)

    return all_objects_sprites, collisions_sprites