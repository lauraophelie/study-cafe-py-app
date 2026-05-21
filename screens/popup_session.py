import pyglet
import tkinter as tk

from screens.popup import Popup
from PIL import Image, ImageTk

pyglet.font.add_file("assets/fonts/PixelifySans-Regular.ttf")
pixelify_font = pyglet.font.load("Pixelify Sans").name

JOIN_BACKGROUND_COLOR = "#FFE478"
BORDER_COLOR = "#272736"
LIGHT_BG_COLOR = "#C2C2D1"
BACKGROUND_COLOR = "#FFFFEB"

FONT_PIXEL = (pixelify_font, 10)

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
    label_image.pack(pady=(40, 20))

    text_input = create_input_text(create_popup, BACKGROUND_COLOR)
    text_input.pack(ipady=2)

    text_placeholder = "Enter your username here"
    add_input_placeholder(text_input, text_placeholder)

    border_frame = tk.Frame(create_popup, bg=BORDER_COLOR)
    border_frame.pack(pady=(20, 0), padx=(10, 0))

    action_button = create_action_button(border_frame, "Create session", "#FFB697")
    action_button.pack(ipady=2)

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

def create_input_text(popup, bg_color):
    return tk.Entry(
        popup,
        bg=bg_color,
        fg=BORDER_COLOR,
        insertbackground=BORDER_COLOR,
        font=FONT_PIXEL,
        width=20,
        relief="flat",
        bd=1,
        highlightthickness=3,
        highlightbackground=BORDER_COLOR,
        highlightcolor=BORDER_COLOR
    )

def create_action_button(frame, text, bg_color):
    return tk.Button(
        frame,
        bg=bg_color,
        text=text,
        font=FONT_PIXEL,
        fg=BORDER_COLOR,
        relief="solid",
        bd=1.5,
        width=15
    )

def add_input_placeholder(input_entry, placeholder):
    input_entry.insert(0, placeholder)
    input_entry.config(fg=LIGHT_BG_COLOR)

    def on_focus_in(event):
        if input_entry.get() == placeholder:
            input_entry.delete(0, tk.END)
            input_entry.config(fg=BORDER_COLOR)

    def on_focus_out(event):
        if input_entry.get() == "":
            input_entry.insert(0, placeholder)
            input_entry.config(fg=LIGHT_BG_COLOR)

    input_entry.bind("<FocusIn>", on_focus_in)
    input_entry.bind("<FocusOut>", on_focus_out)