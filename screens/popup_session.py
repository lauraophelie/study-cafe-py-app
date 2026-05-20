import pyglet
import tkinter as tk

from screens.popup import Popup
from PIL import Image, ImageTk

pyglet.font.add_file("assets/fonts/PixelifySans-Regular.ttf")
pixelify_font = pyglet.font.load("Pixelify Sans").name

JOIN_BACKGROUND_COLOR = "#FFE478"

def display_create_popup():
    create_popup = Popup(
        popup_title="Start a study session", 
        popup_dimension="375x300", 
        background=JOIN_BACKGROUND_COLOR
    )
    input_title = Image.open("assets/ui/join_input_title.png")
    create_popup.images["title"] = ImageTk.PhotoImage(input_title)

    label_image = tk.Label(
        create_popup,
        image=create_popup.images["title"],
        bg=JOIN_BACKGROUND_COLOR
    )
    label_image.pack(padx=50, pady=65)

    text_placeholder = "Enter your username here"
    text_input = tk.Entry(
        create_popup,
        bg="#FFFFEB",
        font=(pixelify_font, 10),
        width=20
    )
    text_input.insert(0, text_placeholder)
    text_input.pack(ipady=2)

    return create_popup

def display_join_popup():
    pass

def create_canvas_popup_title(popup_root):
    canvas = tk.Canvas(
        popup_root, 
        width=50, 
        height=30, 
        bg="#272736", 
        highlightthickness=0
    )
    canvas.pack()
    
    return canvas