# from math import ceil
# from os import system

# import blessed.keyboard
# from blessed import Terminal
# from pygame.time import Clock, wait

# from maps import Map

import pygame as pg

import maps
import physics2
import widgets

#terminal = Terminal()
fps = 120


def run_game():
    pg.mouse.set_visible(False)
    clock = pg.time.Clock()
    level_i = 1
    while level_i < 3:
        scale = 2  # TODO: make this responsive to graphics settings
        level = maps.load_level(level_i, scale)
        groups = level[0]
        area = level[1]
        time_left = level[2]

        screen = pg.display.set_mode(tuple([c*scale for c in area]), pg.SCALED)
        space = physics2.Space(*area, 400, scale)
        # space.reset()  # Interesting moments here because when space is newly initiated (the previous space has explicitly been deleted) it already has objects in it

        allsprites = pg.sprite.RenderPlain()
        for type in groups:
            for sprite in groups[type]:
                space.add_object(sprite.rect, type=type)
                sprite.image.convert()
                sprite.add(allsprites)

        player_sprite = groups["player"].sprites()[0]
        player_rect = player_sprite.rect
        thinking_spriteg = groups["thinkingbox"]
        thinking_spriteg.add(player_sprite)

        background = pg.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 153, 255))

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pg.display.flip()

        while space.targets_engaged < len(space.targets) and time_left > 0:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return

            keys_pressed = pg.key.get_pressed()  # sequence of booleans

            if keys_pressed[pg.K_UP]:
                space.move_player(player_rect, "up")
            if keys_pressed[pg.K_DOWN]:
                space.move_player(player_rect, "down")
            if keys_pressed[pg.K_LEFT] == keys_pressed[pg.K_RIGHT]:
                space.move_player(player_rect, "stop_hor")
            elif keys_pressed[pg.K_LEFT]:
                space.move_player(player_rect, "left")
            else:
                space.move_player(player_rect, "right")

            if not space.player_in_thinkingbox:
                screen.blit(background, (0, 0))
                allsprites.draw(screen)

                time_left -= 1 / fps

            else:
                bg_black = pg.Surface(screen.get_size())
                bg_black = bg_black.convert()
                bg_black.fill((0, 0, 0))
                screen.blit(bg_black, (0, 0))

                thinking_spriteg.draw(screen)

            font = pg.font.Font(None, 32)
            mins, secs = divmod(time_left, 60)
            mins = int(mins // 1)
            secs = int(secs // 1)
            text = font.render(f"{mins}:{secs}", True, (255, 255, 255))
            textpos = text.get_rect(centerx=screen.get_width() / 2, y=20)
            screen.blit(text, textpos)

            pg.display.flip()

            space.step(fps)
            clock.tick(fps)

        if space.targets_engaged == len(space.targets):
            level_i += 1

            banner = widgets.create_banner("Well done! Next level incoming!")
            widgets.align_column(screen, banner)
            pg.display.flip()

            wait_time = 3000
            pg.time.wait(wait_time)

        else:
            level_i = 1
            banner = widgets.create_banner("Time's up! Try again from the beginning!")
            widgets.align_column(screen, banner)
            pg.display.flip()

            wait_time = 3000
            pg.time.wait(wait_time)

        del space

    return


def run_help():
    screen = pg.display.set_mode((800, 480), pg.SCALED)
    screen.fill((0, 153, 255))
    pg.mouse.set_visible(True)

    help_widget = widgets.create_text(
        ["You must move a jellyfish in the map to push some boxes into their places. Your time is limited ",
         "though! You can see how much time is left to complete the level on the top-mid of the screen. ",
         "If you need time to think about how you can solve the current level, just enter the grey thinking-",
         "box, and the timer will stop. Keep in mind, that jellyfishes need a calm place to think, so there ",
         "is dark and quiet inside the box: You cannot see the level when you're inside."])

    widgets.align_column(screen, help_widget)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return

        pg.display.flip()


def menu():
    def init():
        screen = pg.display.set_mode((800, 480), pg.SCALED)
        screen.fill((0, 153, 255))
        pg.mouse.set_visible(True)

        start_button = widgets.create_button("Start")
        help_button = widgets.create_button("Help")

        widgets.align_column(screen, start_button, help_button)

        return start_button, help_button

    start_button, help_button = init()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        mouse_pressed = pg.mouse.get_pressed()[0]
        if mouse_pressed:
            mouse_pos = pg.mouse.get_pos()
            if start_button.point_inside(mouse_pos):
                run_game()
                start_button, help_button = init()
            if help_button.point_inside(mouse_pos):
                run_help()
                start_button, help_button = init()

        pg.display.flip()


# system("clear")
# main()
# system("clear")


if __name__ == '__main__':
    pg.init()
    menu()
