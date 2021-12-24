import json
import os
from typing import Any, Dict, List, Tuple

import pygame as pg
from blessed import Terminal
from pygame.pixelcopy import surface_to_array

import physics2
import sprites
from sprites import Box, Platform, Player, Target, ThinkingBox

PLAYER_W = 4
PLAYER_H = 3
BOX_W = 4
BOX_H = 2
TARGET_W = 2
TARGET_H = 2
PLATFORM_H = 1
THINKINGBOX_W = 8
THINKINGBOX_H = 3


class Map:
    def __init__(self, terminal: Terminal):
        self.terminal = terminal
        self.player = None
        self.player_rect: physics2.Object
        self.thinking_box = None
        self.boxes = []
        self.boxes_rect: List[physics2.Object] = []
        self.targets = []
        self.platforms = []
        self.space = physics2.Space(100, 30, gravity=20, upscale=100)
        self.time_left = 0  # you should always use the ceil() of this variable to get the integer number of seconds left


    def create_level2(self):
        self.player = Player(35, 4, self.terminal)
        player_rect = self.space.add_object(35, 4, PLAYER_W, PLAYER_H, type="player")
        self.player_rect = player_rect

        self.thinking_box = ThinkingBox(20, 4, self.terminal)
        self.space.add_object(20, 4, THINKINGBOX_W, THINKINGBOX_H, type="thinkingbox")

        box1 = Box(6, 5, self.terminal)
        box1_rect = self.space.add_object(6, 5, BOX_W, BOX_H, type="box")
        self.boxes_rect.append(box1_rect)
        self.boxes.append(box1)

        box2 = Box(47, 12, self.terminal)
        box2_rect = self.space.add_object(47, 12, BOX_W, BOX_H, type="box")
        self.boxes_rect.append(box2_rect)
        self.boxes.append(box2)
        box3 = Box(55, 12, self.terminal)
        box3_rect = self.space.add_object(55, 12, BOX_W, BOX_H, type="box")
        self.boxes_rect.append(box3_rect)
        self.boxes.append(box3)


        border1 = Platform(0, 29, 100, True, self.terminal)
        self.space.add_object(0, 29, 100, PLATFORM_H, type="platform")
        self.platforms.append(border1)
        
        platform1 = Platform(0, 7, 40, True, self.terminal)
        self.space.add_object(0, 7, 40, PLATFORM_H, type="platform")
        self.platforms.append(platform1)

        platform2 = Platform(0, 26, 40, True, self.terminal)
        self.space.add_object(0, 26, 40, PLATFORM_H, type="platform")
        self.platforms.append(platform2)

        platform3 = Platform(44, 14, 30, True, self.terminal)
        self.space.add_object(44, 14, 30, PLATFORM_H, type="platform")
        self.platforms.append(platform3)

        target1 = Target(36, 27, self.terminal)
        self.space.add_object(36, 27, TARGET_W, TARGET_H, type="target")
        self.targets.append(target1)
        target1 = Target(90, 27, self.terminal)
        self.space.add_object(90, 27, TARGET_W, TARGET_H, type="target")
        self.targets.append(target1)
        target1 = Target(0, 24, self.terminal)
        self.space.add_object(0, 24, TARGET_W, TARGET_H, type="target")
        self.targets.append(target1)

        self.time_left = 120

    def create_level3(self):
        self.player = Player(25, 4, self.terminal)
        player_rect = self.space.add_object(25, 4, PLAYER_W, PLAYER_H, type="player")
        self.player_rect = player_rect

        self.thinking_box = ThinkingBox(15, 4, self.terminal)
        self.space.add_object(15, 4, THINKINGBOX_W, THINKINGBOX_H, type="thinkingbox")
        
        border1 = Platform(0, 29, 100, True, self.terminal)
        self.space.add_object(0, 29, 100, PLATFORM_H, type="platform")
        self.platforms.append(border1)

        platform1 = Platform(0, 7, 40, True, self.terminal)
        self.space.add_object(0, 7, 40, PLATFORM_H, type="platform")
        self.platforms.append(platform1)

        platform2 = Platform(44, 10, 40, True, self.terminal)
        self.space.add_object(44, 10, 40, PLATFORM_H, type="platform")
        self.platforms.append(platform2)

        platform3 = Platform(0, 16, 40, True, self.terminal)
        self.space.add_object(0, 16, 40, PLATFORM_H, type="platform")
        self.platforms.append(platform3)

        platform4 = Platform(0, 24, 40, True, self.terminal)
        self.space.add_object(0, 24, 40, PLATFORM_H, type="platform")
        self.platforms.append(platform4)

        platform5 = Platform(44, 24, 40, True, self.terminal)
        self.space.add_object(44, 24, 40, PLATFORM_H, type="platform")
        self.platforms.append(platform5)

        box1 = Box(35, 5, self.terminal)
        box1_rect = self.space.add_object(35, 5, BOX_W, BOX_H, type="box")
        self.boxes_rect.append(box1_rect)
        self.boxes.append(box1)

        box2 = Box(50, 8, self.terminal)
        box2_rect = self.space.add_object(50, 8, BOX_W, BOX_H, type="box")
        self.boxes_rect.append(box2_rect)
        self.boxes.append(box2)
        box3 = Box(60, 8, self.terminal)
        box3_rect = self.space.add_object(60, 8, BOX_W, BOX_H, type="box")
        self.boxes_rect.append(box3_rect)
        self.boxes.append(box3)

        box4 = Box(20, 14, self.terminal)
        box4_rect = self.space.add_object(20, 14, BOX_W, BOX_H, type="box")
        self.boxes_rect.append(box4_rect)
        self.boxes.append(box4)

        target1 = Target(0, 27, self.terminal)
        self.space.add_object(0, 27, TARGET_W, TARGET_H, type="target")
        self.targets.append(target1)
        target2 = Target(0, 25, self.terminal)
        self.space.add_object(0, 25, TARGET_W, TARGET_H, type="target")
        self.targets.append(target2)
        target3 = Target(0, 22, self.terminal)
        self.space.add_object(0, 22, TARGET_W, TARGET_H, type="target")
        self.targets.append(target3)
        target4 = Target(90, 27, self.terminal)
        self.space.add_object(90, 27, TARGET_W, TARGET_H, type="target")
        self.targets.append(target4)

        self.time_left = 120

    def delete(self):
        print(self.terminal.home + self.terminal.on_midnightblue + self.terminal.clear(), flush=True)

    def sync_coords(self):
        self.player.x, self.player.y = self.player_rect.get_position()
        for i, box in enumerate(self.boxes):
            box.x, box.y = self.boxes_rect[i].get_position()

    def draw(self):
        string = ""
        string += self.thinking_box.draw()
        for target in self.targets:
            string += target.draw()
        string += self.player.draw()
        for platform in self.platforms:
            string += platform.draw()
        for box in self.boxes:
            string += box.draw()
        print(string, flush=True)

    def clear_level(self):
        self.player = 0
        self.player_rect = None
        self.targets = []
        self.thinking_box = None
        self.boxes = []
        self.boxes_rect = []
        self.platforms = []
        self.space.reset()


def load_object(topleft: Tuple[int], scale: int, type: str, width: int = 16):

    #possible types: "player", "box", "thinkingbox", "target", "platform"

    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "data")
    image_dir = os.path.join(data_dir, "images")

    if type != "platform":
        image = os.path.join(image_dir, f"{type}.png")
        surface = pg.image.load(image)
    else:
        PLATFORM_H = 16
        PLATFORM_MIN_W = 16
        #the sides of a platform are each 8 pixels wide in basic scale

        surface = pg.Surface((width, PLATFORM_H))

        pl_left_img = os.path.join(image_dir, "platform_left.png")
        pl_left_img = pg.image.load(pl_left_img)
        surface.blit(pl_left_img, (0, 0))

        if width > PLATFORM_MIN_W:
            pl_mid_img =  os.path.join(image_dir, "platform_mid.png")
            pl_mid_img = pg.image.load(pl_mid_img)
            surface.blit(pl_mid_img, (8, 0))

        pl_right_img = os.path.join(image_dir, "platform_right.png")
        pl_right_img = pg.image.load(pl_right_img)
        topleft_x = width - 8
        surface.blit(pl_right_img, (topleft_x, 0))

    size = surface.get_size()
    size = size[0] * scale, size[1] * scale
    surface = pg.transform.scale(image, size)

    surface = surface.convert()
    surface.set_colorkey(pg.Color(0, 0, 0, 0), pg.RLEACCEL)

    rect = surface.get_rect()

    sprite = pg.sprite.Sprite()
    sprite.image = surface
    sprite.rect = rect

    return sprite


def load_level(level: int, scale:int=1):
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "data")
    levels_dir = os.path.join(data_dir, "levels")
    level_path = os.path.join(levels_dir, f"level{level}.json")

    level_raw = json.loads(level_path)

    players = pg.sprite.RenderPlain()
    boxes = pg.sprite.RenderPlain()
    thinking_boxes = pg.sprite.RenderPlain()
    platforms = pg.sprite.RenderPlain()
    targets = pg.sprite.RenderPlain()

    def fetch_and_scale_topleft(coords: Dict[Any]):
        x = coords["x"] * scale
        y = coords["y"] * scale

        return x, y

    for player in level_raw["players"]:
        topleft = fetch_and_scale_topleft(player)
        player_sprite = load_object(topleft, scale, type="player")
        player_sprite.add(players)

    for box in level_raw["boxes"]:
        topleft = fetch_and_scale_topleft(box)
        box_sprite = load_object(topleft, scale, type="box")
        box_sprite.add(boxes)

    for thinking_box in level_raw["thinking_boxes"]:
        topleft = fetch_and_scale_topleft(thinking_box)
        thinking_box_sprite = load_object(topleft, scale, type="thinkingbox")
        thinking_box_sprite.add(thinking_boxes)

    for target in level_raw["targets"]:
        topleft = fetch_and_scale_topleft(target)
        target_sprite = load_object(topleft, scale, type="target")
        target_sprite.add(targets)

    for platform in level_raw["platforms"]:
        topleft = fetch_and_scale_topleft(platform)
        width = platform["w"] * scale
        platform_sprite = load_object(topleft, scale, type="platform", width=width)
        platform_sprite.add(platforms)


