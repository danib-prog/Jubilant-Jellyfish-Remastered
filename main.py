# from math import ceil
# from os import system

# import blessed.keyboard
# from blessed import Terminal
# from pygame.time import Clock, wait

# from maps import Map

import pygame as pg

import maps
import physics2

#terminal = Terminal()
fps = 120
def run_game():
    pg.init()
    clock = pg.time.Clock()
    level_i = 1
    while level_i < 3:
        scale = 2 # TODO: make this responsive to graphics settings
        level = maps.load_level(level_i, scale)
        groups = level[0]
        area = level[1]
        time_left = level[2]

        screen = pg.display.set_mode(tuple([c*scale for c in area])) #, pg.SCALED)
        space = physics2.Space(*area, 400, scale)
        space.reset() # WTF moments here because when space is newly initiated (the previous space has explicitly been deleted) it already has objects in it

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

            keys_pressed = pg.key.get_pressed() # sequence of booleans

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
            # TODO: winner winner chicken dinner

        else:
            level_i = 1
            # TODO: try again or quit

        del space

def run_tutorial():
    val = terminal.inkey(timeout=1 / fps)
    while val != 'q':
        val = terminal.inkey(timeout=1/fps)
        tutorial = terminal.move_xy(40, 5) +  terminal.lightcyan(terminal.on_darkslategray4('TUTORIAL'))
        info1 = terminal.move_xy(20, 10) +  terminal.lightcyan(terminal.on_darkslategray('The purpose of the game is to push the boxes until all targets have a box inside. Make sure to finish it in time. If you want to think about the level, enter the gray thinking box and the timer will stop.'))
        info2 = terminal.move_xy(20, 17) +  terminal.lightcyan(terminal.on_darkslategray('MOVEMENT: use A and D or left and right arrow keys to move. Use W and up arrow to jump and S and down arrow to cancel the jump'))
        exit = terminal.move_xy(20, 20) + terminal.lightcyan(terminal.on_darkslategray('Press q to exit. You can use q to quit the main game and the menu too.'))
        print(tutorial + info2 + info1 + exit, flush=True)


def menu():
    with terminal.cbreak(), terminal.hidden_cursor(), terminal.fullscreen():
        val: blessed.keyboard.Keystroke = terminal.inkey(timeout=1/fps)
        print(terminal.home + terminal.lightcyan_on_darkslategray + terminal.clear)
        index = 1
        while val != 'q':
            val = terminal.inkey(timeout=1/fps)
            if val.name == "KEY_UP":
                index -= 1
            if val.name == "KEY_DOWN":
                index += 1
            if index < 1:
                index = 3
            if index > 3:
                index = 1
            if val.name == "KEY_ENTER":
                if index == 1:
                    run_game()
                    print(terminal.home + terminal.lightcyan_on_darkslategray + terminal.clear)
                if index == 2:
                    print(terminal.home + terminal.lightcyan_on_darkslategray + terminal.clear)
                    run_tutorial()
                    print(terminal.home + terminal.lightcyan_on_darkslategray + terminal.clear)
                if index == 3:
                    break

            menu = terminal.move_xy(20 , 7) + terminal.lightcyan(terminal.on_darkslategray('MENU'))
            start = terminal.move_xy(20 , 10) + terminal.lightcyan(terminal.on_darkslategray('START GAME'))
            tutorial = terminal.move_xy(20, 11) +  terminal.lightcyan(terminal.on_darkslategray('TUTORIAL'))
            exit = terminal.move_xy(20, 13) + terminal.lightcyan(terminal.on_darkslategray('EXIT'))
            if index == 1:
                start = terminal.move_xy(20 , 10) + terminal.lightcyan(terminal.on_darkslategray4('START GAME'))
            if index == 2:
                tutorial = terminal.move_xy(20, 11) +  terminal.lightcyan(terminal.on_darkslategray4('TUTORIAL'))
            if index == 3:
                exit = terminal.move_xy(20, 13) +  terminal.lightcyan(terminal.on_darkslategray4('EXIT'))
            print(start + menu + tutorial + exit, flush=True)


def main():
    system("resize -s 30 100 | 2> /dev/null")
    menu()


#system("clear")
#main()
#system("clear")


run_game()
