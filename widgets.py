import os

import pygame as pg

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")
fonts_dir = os.path.join(data_dir, "fonts")
font_path = os.path.join(fonts_dir, "Minecraftia-Regular.ttf")

font = pg.font.Font(font_path, 40)

def create_button(txt: str):
    widget = pg.Surface((150, 60), color=(255, 255, 255))
    widget.set_clip(pg.Rect(2, 2, 146, 56))
    widget.fill((19, 7, 201))
    widget_r = widget.get_rect()

    text = font.render(txt, True, (255, 255, 255))
    textpos = text.get_rect(center=widget_r.center)

    widget.blit(text, textpos)

    return pg.sprite.Sprite(image=widget, rect=widget_r)

def align_column(surface: pg.Surface, *widgets):
    x = int((surface.get_width() / 2) // 1)
    row_h = int((surface.get_height() / (len(widgets) + 1)) // 1)

    for i, widget in enumerate(widgets):
        i += 1
        widget.rect.center = x, row_h * i
        surface.blit(widget.image, widget.rect)

    return surface
