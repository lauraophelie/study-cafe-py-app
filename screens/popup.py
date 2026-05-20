import tkinter as tk

class Popup(tk.Tk):
    def __init__(self, popup_title, popup_dimension, background="#ffffff"):
        super().__init__()
        self.geometry = popup_dimension
        self.title = popup_title
        self.configure(bg=background)