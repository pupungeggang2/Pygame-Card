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

def draw_info():
    pygame.draw.rect(var.screen, const.Color.white, UI.Field.Info.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.rect, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.button_close, 2)

    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.tab_profile, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.tab_card, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.tab_deck, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.tab_equipment, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.tab_item, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.tab_map, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.tab_progress, 2)

def draw_adventure_confirm():
    pygame.draw.rect(var.screen, const.Color.white, UI.Field.Confirm.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Confirm.rect, 2)

    if var.state == 'adventure_confirm_start':
        var.screen.blit(asset.Font.main_32.render('Start Adventure?', False, const.Color.black), UI.Field.Confirm.text_title)

    elif var.state == 'adventure_confirm_end':
        var.screen.blit(asset.Font.main_32.render('End Adventure?', False, const.Color.black), UI.Field.Confirm.text_title)

    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Confirm.button_yes, 2)
    var.screen.blit(asset.Font.main_32.render('Yes [Y]', False, const.Color.black), UI.Field.Confirm.text_yes)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Confirm.button_no, 2)
    var.screen.blit(asset.Font.main_32.render('No [N]', False, const.Color.black), UI.Field.Confirm.text_no)

def draw_save():
    pygame.draw.rect(var.screen, const.Color.white, UI.Field.Save.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Save.rect, 2)

    var.screen.blit(asset.Font.main_32.render('Save Data?', False, const.Color.black), UI.Field.Save.text_title)

    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Save.button_yes, 2)
    var.screen.blit(asset.Font.main_32.render('Yes [Y]', False, const.Color.black), UI.Field.Save.text_yes)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Save.button_no, 2)
    var.screen.blit(asset.Font.main_32.render('No [N]', False, const.Color.black), UI.Field.Save.text_no)

def draw_game_start():
    pygame.draw.rect(var.screen, const.Color.white, UI.Game.Start.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Start.rect, 2)

    var.screen.blit(asset.Font.main_32.render('Start', const.Color.black, False), UI.Game.Start.text_title)

    for i in range(3):
        draw_card(var.Game.deck_card[i], [UI.Game.Start.button_select[i][0], UI.Game.Start.button_select[i][1]])

        if var.state == 'start':
            if var.Game.start_hand_change[i] == True:
                pygame.draw.rect(var.screen, const.Color.green, UI.Game.Start.button_select[i], 2)
    
    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Start.button_start, 2)
    var.screen.blit(asset.Font.main_32.render('Start', const.Color.black, False), UI.Game.Start.text_start)

def draw_game_field():
    for i in range(14):
        pygame.draw.rect(var.screen, const.Color.black, UI.Game.Field.unit[i], 2)

def draw_game_lower():
    for i in range(len(var.Game.hand_card)):
        draw_card(var.Game.hand_card[i], [UI.Game.Lower.hand_card[i][0], UI.Game.Lower.hand_card[i][1]])

    for i in range(len(var.Game.hand_crystal)):
        pygame.draw.rect(var.screen, const.Color.black, UI.Game.Lower.crystal[i], 2)

## Etc

def draw_card(card, position):
    temp_rect = [position[0], position[1], UI.Card.rect[2], UI.Card.rect[3]]
    pygame.draw.rect(var.screen, const.Color.white, temp_rect)
    pygame.draw.rect(var.screen, const.Color.black, temp_rect, 2)
    temp_image = [position[0] + UI.Card.image_card[0], position[1] + UI.Card.image_card[1], UI.Card.image_card[2], UI.Card.image_card[3]]
    pygame.draw.rect(var.screen, const.Color.black, temp_image, 2)
    temp_text_name = [position[0] + UI.Card.text_name[0], position[1] + UI.Card.text_name[1]]
    var.screen.blit(asset.Font.main_16.render(f'{card['name']}', False, const.Color.black), temp_text_name)

    if card['type'] == 'unit':
        temp_text_attack = [position[0] + UI.Card.text_attack[0], position[1] + UI.Card.text_attack[1]]
        var.screen.blit(asset.Font.main_32.render(f'{card['stat'][0]}', False, const.Color.black), temp_text_attack)
        temp_text_life = [position[0] + UI.Card.text_life[0], position[1] + UI.Card.text_life[1]]
        var.screen.blit(asset.Font.main_32.render(f'{card['stat'][1]}', False, const.Color.black), temp_text_life)