import tkinter as tk

def create_stroked_text(
    canvas, 
    x, y, 
    text, 
    stroke_color, 
    fill_color, 
    text_font, 
    stroke_width=2, 
    anchor="ne"
):
    for dx in (-stroke_width, 0, stroke_width):
        for dy in (-stroke_width, 0, stroke_width):
            if dx != 0 or dy != 0:
                canvas.create_text(
                    x + dx,
                    y + dy,
                    text=text,
                    font=text_font,
                    fill=stroke_color,
                    anchor=anchor
                )
    canvas.create_text(
        x, y, 
        text=text, 
        font=text_font, 
        fill=fill_color,
        anchor=anchor
    )

    