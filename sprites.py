import os

import pygame as pg

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")
image_dir = os.path.join(data_dir, "images")
image = os.path.join(image_dir, "target.png")
surface = pg.image.load(image)

print(surface.get_at((8, 8)))
