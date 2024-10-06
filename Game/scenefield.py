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

    if var.state == 'info_adventure':
        funcdraw.draw_info_adventure()

    if var.menu == True:
        funcdraw.draw_menu_field()

    pygame.draw.rect(var.screen, const.Color.white, UI.Field.box_place)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.box_place, 2)
    var.screen.blit(asset.Font.main_32.render(var.Field.place, False, const.Color.black), UI.Field.text_place)
    var.screen.blit(asset.Image.Button.menu, UI.Field.button_menu[:2])
    pygame.draw.rect(var.screen, const.Color.white, UI.Field.box_tip)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.box_tip, 2)
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
                    if var.Adventure.adventure == False:
                        var.state = 'info'
                        var.tab_field = 'profile'
                    else:
                        var.state = 'info_adventure'
                        var.tab_adventure = 'profile'

            elif var.state == 'info':
                if funcphysics.point_inside_rect_array(x, y, UI.Field.Info.button_close):
                    var.state = ''

                if funcphysics.point_inside_rect_array(x, y, UI.Field.Info.tab_profile):
                    var.tab_field = 'profile'
                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Info.tab_deck):
                    var.tab_field = 'deck'
                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Info.tab_card):
                    var.tab_field = 'card'
                    var.card_display_page = 0
                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Info.tab_crystal):
                    var.tab_field = 'crystal'
                    var.crystal_display_page = 0
                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Info.tab_equipment):
                    var.tab_field = 'equipment'
                    var.equipment_display_page = 0
                    var.equipment_display_selected = -1
                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Info.tab_item):
                    var.tab_field = 'item'
                    var.item_display_page = 0
                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Info.tab_place):
                    var.tab_field = 'place'
                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Info.tab_progress):
                    var.tab_field = 'progress'

                if var.tab_field == 'card':
                    if funcphysics.point_inside_rect_array(x, y, UI.Field.Info.button_next):
                        if var.card_display_page < len(var.card_display_list) // 10:
                            var.card_display_page += 1
                    elif funcphysics.point_inside_rect_array(x, y, UI.Field.Info.button_prev):
                        if var.card_display_page > 0:
                            var.card_display_page -= 1

                elif var.tab_field == 'crystal':
                    if funcphysics.point_inside_rect_array(x, y, UI.Field.Info.button_next):
                        if var.crystal_display_page < len(var.crystal_display_list) // 10:
                            var.crystal_display_page += 1
                    elif funcphysics.point_inside_rect_array(x, y, UI.Field.Info.button_prev):
                        if var.crystal_display_page > 0:
                            var.crystal_display_page -= 1

                elif var.tab_field == 'equipment':
                    if funcphysics.point_inside_rect_array(x, y, UI.Field.Info.button_next):
                        if var.equipment_display_page < len(var.equipment_display_list) // 42:
                            var.equipment_display_page += 1
                    elif funcphysics.point_inside_rect_array(x, y, UI.Field.Info.button_prev):
                        if var.equipment_display_page > 0:
                            var.equipment_display_page -= 1

                    for i in range(6):
                        for j in range(7):
                            if funcphysics.point_inside_rect(x, y, UI.Field.Info.Equipment.item_start[0] + UI.Field.Info.Equipment.item_interval[0] * j, UI.Field.Info.Equipment.item_start[1] + UI.Field.Info.Equipment.item_interval[1] * i, UI.Field.Info.Equipment.item_size[0], UI.Field.Info.Equipment.item_size[1]):
                                var.equipment_display_selected = i * 7 + j

            elif var.state == 'info_adventure':
                if funcphysics.point_inside_rect_array(x, y, UI.Field.Info_Adventure.button_close):
                    var.state = ''

                if funcphysics.point_inside_rect_array(x, y, UI.Field.Info_Adventure.tab_profile):
                    var.tab_adventure = 'profile'
                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Info_Adventure.tab_deck):
                    var.tab_adventure = 'deck'
                    var.deck_card_display_page = 0
                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Info_Adventure.tab_crystal):
                    var.tab_adventure = 'crystal'
                    var.crystal_display_page = 0
                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Info_Adventure.tab_place):
                    var.tab_adventure = 'place'

            elif var.state == 'adventure_confirm_start':
                if funcphysics.point_inside_rect_array(x, y, UI.Field.Confirm.button_yes):
                    var.state = ''
                    funcfield.adventure_init()

                elif funcphysics.point_inside_rect_array(x, y, UI.Field.Confirm.button_no):
                    var.state = ''

            elif var.state == 'adventure_confirm_end':
                if funcphysics.point_inside_rect_array(x, y, UI.Field.Confirm.button_yes):
                    var.state = ''
                    funcfield.adventure_end()

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
                if var.Adventure.adventure == False:
                        var.state = 'info'
                        var.tab_field = 'profile'
                else:
                    var.state = 'info_adventure'
                    var.tab_adventure = 'profile'

        elif var.state == 'info':
            if key == pygame.K_i:
                var.state = ''

        elif var.state == 'info_adventure':
            if key == pygame.K_i:
                var.state = ''

        elif var.state == 'adventure_confirm_start':
            if key == pygame.K_y:
                var.state = ''
                funcfield.adventure_init()

            elif key == pygame.K_n:
                var.state = ''
                funcfield.adventure_end()

        elif var.state == 'adventure_confirm_end':
            if key == pygame.K_y:
                var.state = ''
                funcfield.adventure_init()

            elif key == pygame.K_n:
                var.state = ''
                funcfield.adventure_end()

def key_up(key):
    pass