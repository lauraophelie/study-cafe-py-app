import pyglet
import tkinter as tk

from screens.popup import Popup

pyglet.font.add_file("assets/fonts/PixelifySans-Regular.ttf")
pixelify_font = pyglet.font.load("Pixelify Sans").name

def display_create_popup():
    create_popup = Popup(
        popup_title="Start a study session", 
        popup_dimension="375x300", 
        background="#ffe478"
    )
    input_label = tk.Label(
        create_popup,
        text="Welcome :) Please enter your username",
        font=(pixelify_font, 15),
        bg=None,
        fg="#FFFFEB"
    )
    input_label.pack(padx=50, pady=65)

    return create_popup

def display_join_popup():
    pass