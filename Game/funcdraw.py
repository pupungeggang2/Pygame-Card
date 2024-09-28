import pygame
import asset, UI, data, var, const

def draw_menu_field():
    pygame.draw.rect(var.screen, const.Color.white, UI.Field.Menu.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Menu.rect, 2)
    var.screen.blit(asset.Font.main_32.render('Paused', False, const.Color.black), UI.Field.Menu.text_pause)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Menu.button_resume, 2)
    var.screen.blit(asset.Font.main_32.render('Resume', False, const.Color.black), UI.Field.Menu.text_resume)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Menu.button_exit, 2)
    var.screen.blit(asset.Font.main_32.render('Exit to title', False, const.Color.black), UI.Field.Menu.text_exit)

def draw_menu_game():
    pass

def draw_field():
    for i in range(len(var.Field.field['connection'])):
        position_connection = [var.Field.field['connection'][i][0][0] - var.Field.camera[0], var.Field.field['connection'][i][0][1] - var.Field.camera[1]]
        var.screen.blit(asset.Image.connection, position_connection)

    for i in range(len(var.Field.field['event'])):
        event_type = var.Field.field['event'][i]['type']
        position_event = [var.Field.field['event'][i]['position'][0] - var.Field.camera[0], var.Field.field['event'][i]['position'][1] - var.Field.camera[1]]
        
        if event_type == 'monster':
            var.screen.blit(asset.Image.monster, position_event)

        elif event_type == 'mystery':
            var.screen.blit(asset.Image.mystery, position_event)

        elif event_type == 'shop':
            var.screen.blit(asset.Image.field_shop, position_event)

    for i in range(len(var.Field.field['thing'])):
        thing = var.Field.field['thing'][i]
        position_thing = [thing[0][0] - var.Field.camera[0], thing[0][1] - var.Field.camera[1]]

        if thing[1] == 'save':
            var.screen.blit(asset.Image.save, position_thing)

    rect_player = [var.Field.position_player[0] - var.Field.camera[0] - 20, var.Field.position_player[1] - var.Field.camera[1] - 20, 40, 40]
    pygame.draw.rect(var.screen, const.Color.black, rect_player, 2)

def draw_adventure_confirm():
    pygame.draw.rect(var.screen, const.Color.white, UI.Field.Confirm.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Confirm.rect, 2)

    if var.state == 'adventure_confirm_start':
        var.screen.blit(asset.Font.main_32.render('Start Adventure?', False, const.Color.black), UI.Field.Confirm.text_title)

    elif var.state == 'adventure_confirm_end':
        var.screen.blit(asset.Font.main_32.render('End Adventure?', False, const.Color.black), UI.Field.Confirm.text_title)

    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Confirm.button_yes, 2)
    var.screen.blit(asset.Font.main_32.render('Yes', False, const.Color.black), UI.Field.Confirm.text_yes)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Confirm.button_no, 2)
    var.screen.blit(asset.Font.main_32.render('No', False, const.Color.black), UI.Field.Confirm.text_no)

def draw_save():
    pygame.draw.rect(var.screen, const.Color.white, UI.Field.Save.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Save.rect, 2)

    var.screen.blit(asset.Font.main_32.render('Save Data?', False, const.Color.black), UI.Field.Save.text_title)

    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Save.button_yes, 2)
    var.screen.blit(asset.Font.main_32.render('Yes', False, const.Color.black), UI.Field.Save.text_yes)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Save.button_no, 2)
    var.screen.blit(asset.Font.main_32.render('No', False, const.Color.black), UI.Field.Save.text_no)

def draw_info():
    pass