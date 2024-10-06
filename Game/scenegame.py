import pygame
import asset, UI, data, var, const
import funcphysics, funcdraw, funcfield, funcgame

def loop():
    if var.menu == False:
        if var.state == '':
            funcgame.mouse_card_handle()
    display()

def display():
    var.screen.fill(const.Color.white)

    funcdraw.draw_game_field()
    funcdraw.draw_game_lower()

    if var.state == 'start' or var.state == 'start_confirm':
        funcdraw.draw_game_start()

    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.menu == False:
            if var.state == '':
                if var.state_game_click == '':
                    for i in range(len(var.Game.hand_card)):
                        if funcphysics.point_inside_rect_array(x, y, UI.Game.Lower.hand_card_mouse[i]):
                            var.state_game_click = 'card'
                            var.Game.selected_card = i

                    if funcphysics.point_inside_rect_array(x, y, UI.Game.Lower.button_turn_end):
                        funcgame.turn_end()
                        funcgame.turn_start()

                elif var.state_game_click == 'card':
                    if funcphysics.point_inside_rect_array(x, y, UI.Game.Lower.hand_card[var.Game.selected_card]):
                        funcgame.handle_effect_card(var.Game.hand_card[var.Game.selected_card])

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
                    funcgame.turn_start_first()
                    funcgame.turn_start()
                    var.state = ''

def mouse_move(x, y):
    var.mouse[0] = x
    var.mouse[1] = y

def key_down(key):
    pass

def key_up(key):
    pass