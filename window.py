import pygame
import tkinter as tk

from screens.menu_screen import load_menu_screen
from screens.study_cafe_room import load_study_room

pygame.init()

window = pygame.display.set_mode((640, 384))
pygame.display.set_caption("Let's study together")

root = tk.Tk()
root.withdraw()

menu_screen_map, menu_screen_sprites = load_menu_screen()
study_room_map, study_room_sprites = load_study_room()

run = True
clock = pygame.time.Clock()

current_screen = "menu_screen"

while run:
    root.update()
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            run = False

    if current_screen == "menu_screen":
        menu_screen_map.render(window)
        menu_screen_sprites.update(events)
        menu_screen_sprites.draw(window)

    # study_room_map.render(window)
    # study_room_sprites.update(events)
    # study_room_sprites.draw(window)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
root.destroy()