import pygame
import asset, UI, data, var, const
import funcphysics, funcdraw, funcfield

def loop():
    if var.menu == False:
        if var.state == '':
            funcfield.field_tick()

    display()

def display():
    var.screen.fill(const.Color.white)

    funcdraw.draw_field()

    if var.state == 'adventure_confirm_start' or var.state == 'adventure_confirm_end':
        funcdraw.draw_adventure_confirm()

    if var.menu == True:
        funcdraw.draw_menu_field()

    var.screen.blit(asset.Font.main_32.render(var.Field.place, False, const.Color.black), UI.Field.text_place)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.button_menu, 2)
    var.screen.blit(asset.Font.main_32.render('[E] Interact [I] Info', False, const.Color.black), UI.Field.text_tip)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.button_info, 2)
    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.menu == False:
            if funcphysics.point_inside_rect_array(x, y, UI.Field.button_menu):
                var.menu = True

        elif var.menu == True:
            if funcphysics.point_inside_rect_array(x, y, UI.Field.Menu.button_resume):
                var.menu = False

            elif funcphysics.point_inside_rect_array(x, y, UI.Field.Menu.button_exit):
                var.menu = False
                var.scene = 'title'
                var.state = ''

def key_down(key):
    if var.menu == False:
        if var.state == '':
            if key == pygame.K_e:
                funcfield.interact()

def key_up(key):
    pass