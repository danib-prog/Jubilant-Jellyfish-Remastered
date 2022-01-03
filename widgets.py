import os
from typing import Tuple

import pygame as pg

pg.font.init()

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")
fonts_dir = os.path.join(data_dir, "fonts")
font_path = os.path.join(fonts_dir, "Minecraftia-Regular.ttf")

font_b = pg.font.Font(font_path, 40)
font_t = pg.font.Font(font_path, 12)


def create_text(txt: str):
    widget = pg.Surface((700, 350))
    widget.fill((255, 255, 255))
    widget.set_clip(pg.Rect(2, 2, 696, 346))
    widget.fill((19, 7, 201))
    widget_r = widget.get_rect()

    text = font_t.render(txt, True, (255, 255, 255))
    textpos = text.get_rect(center=widget_r.center)

    widget.blit(text, textpos)

    sprite = pg.sprite.Sprite()
    sprite.image = widget
    sprite.rect = widget_r

    return sprite


class Button(pg.sprite.Sprite):
    def __init__(self, image: pg.Surface, rect: pg.Rect):
        super().__init__()

        self.image = image
        self.rect = rect

    def point_inside(self, coords: Tuple[int]):
        return self.rect.collidepoint(coords)


def create_button(txt: str):
    widget = pg.Surface((150, 60))
    widget.fill((255, 255, 255))
    widget.set_clip(pg.Rect(2, 2, 146, 56))
    widget.fill((19, 7, 201))
    widget_r = widget.get_rect()

    text = font_b.render(txt, True, (255, 255, 255))
    textpos = text.get_rect(center=widget_r.center)

    widget.blit(text, textpos)

    return Button(image=widget, rect=widget_r)


def align_column(surface: pg.Surface, *widgets):
    x = int((surface.get_width() / 2) // 1)
    row_h = int((surface.get_height() / (len(widgets) + 1)) // 1)

    for i, widget in enumerate(widgets):
        i += 1
        widget.rect.center = x, row_h * i
        surface.blit(widget.image, widget.rect)

    return surface
