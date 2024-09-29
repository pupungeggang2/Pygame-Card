import pygame
import asset, UI, data, var, const
import funcphysics, funcdraw, funcfield, funcsave

def loop():
    if var.menu == False:
        if var.state == '':
            funcfield.field_tick()

    display()

def display():
    var.screen.fill(const.Color.white)

    funcdraw.draw_field()

    if var.state == 'save':
        funcdraw.draw_save()

    if var.state == 'adventure_confirm_start' or var.state == 'adventure_confirm_end':
        funcdraw.draw_adventure_confirm()

    if var.state == 'info':
        funcdraw.draw_info()

    if var.menu == True:
        funcdraw.draw_menu_field()

    var.screen.blit(asset.Font.main_32.render(var.Field.place, False, const.Color.black), UI.Field.text_place)
    var.screen.blit(asset.Image.Button.menu, UI.Field.button_menu[:2])
    var.screen.blit(asset.Font.main_32.render('[E] Interact [I] Info', False, const.Color.black), UI.Field.text_tip)
    var.screen.blit(asset.Image.Button.info, UI.Field.button_info[:2])
    
    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.menu == False:
            if funcphysics.point_inside_rect_array(x, y, UI.Field.button_menu):
                var.menu = True

            if var.state == '':
                if funcphysics.point_inside_rect_array(x, y, UI.Field.button_info):
                    var.state = 'info'

            elif var.state == 'info':
                if funcphysics.point_inside_rect_array(x, y, UI.Field.Info.button_close):
                    var.state = ''

            if var.state == 'adventure_confirm_start':
                if funcphysics.point_inside_rect_array(x, y, UI.Field.Confirm.button_yes):
                    var.state = ''
                    var.Adventure.adventure = True
                    var.Field.place = var.Field.destination_place
                    funcfield.load_field(var.Field.place)
                    var.Field.position_player = var.Field.destination_position

                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Confirm.button_no):
                    var.state = ''

            elif var.state == 'adventure_confirm_end':
                if funcphysics.point_inside_rect_array(x, y, UI.Field.Confirm.button_yes):
                    var.state = ''
                    var.Adventure.adventure = False
                    var.Field.place = var.Field.destination_place
                    funcfield.load_field(var.Field.place)
                    var.Field.position_player = var.Field.destination_position

                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Confirm.button_no):
                    var.state = ''

            elif var.state == 'save':
                if funcphysics.point_inside_rect_array(x, y, UI.Field.Save.button_yes):
                    var.state = ''
                    funcsave.save_data()

                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Save.button_no):
                    var.state = ''

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

            if key == pygame.K_i:
                var.state = 'info'

        elif var.state == 'info':
            if key == pygame.K_i:
                var.state = ''

def key_up(key):
    pass