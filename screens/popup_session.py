import tkinter as tk

from screens.popup import Popup

POP_UP_DIMENSION = "400x300"

def display_create_popup():
    create_popup = Popup(
        popup_title="Start a study session", 
        popup_dimension="375x300", 
        background="#ffe478"
    )
    return create_popup

def display_join_popup():
    pass