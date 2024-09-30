import pygame
import asset, UI, data, var, const
import funcphysics, funcdraw, funcfield, funcgame

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    if var.state == 'start' or var.state == 'start_confirm':
        funcdraw.draw_game_start()

    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.menu == False:
            if var.state == '':
                pass
            elif var.state == 'start':
                for i in range(3):
                    if funcphysics.point_inside_rect_array(x, y, UI.Game.Start.button_select[i]):
                        if var.Game.start_hand_change[i] == False:
                            var.Game.start_hand_change[i] = True
                        else:
                            var.Game.start_hand_change[i] = False

                if funcphysics.point_inside_rect_array(x, y, UI.Game.Start.button_start):
                    funcgame.start_card_change()
                    var.state = 'start_confirm'

            elif var.state == 'start_confirm':
                if funcphysics.point_inside_rect_array(x, y, UI.Game.Start.button_start):
                    var.state = ''

def key_down(key):
    pass

def key_up(key):
    pass