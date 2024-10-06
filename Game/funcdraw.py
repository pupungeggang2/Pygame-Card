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
    var.screen.blit(asset.Image.background[const.place_background[var.Field.place]], [-var.Field.camera[0], -var.Field.camera[1]])

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
    var.screen.blit(asset.Image.player[var.Field.player_facing], rect_player)

def draw_info():
    pygame.draw.rect(var.screen, const.Color.white, UI.Field.Info.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.rect, 2)
    var.screen.blit(asset.Image.Button.close, UI.Field.Info.button_close)

    var.screen.blit(asset.Image.Tab.profile, UI.Field.Info.tab_profile)
    var.screen.blit(asset.Image.Tab.deck, UI.Field.Info.tab_deck)
    var.screen.blit(asset.Image.Tab.card, UI.Field.Info.tab_card)
    var.screen.blit(asset.Image.Tab.crystal, UI.Field.Info.tab_crystal)
    var.screen.blit(asset.Image.Tab.equipment, UI.Field.Info.tab_equipment)
    var.screen.blit(asset.Image.Tab.item, UI.Field.Info.tab_item)
    var.screen.blit(asset.Image.Tab.place, UI.Field.Info.tab_place)
    var.screen.blit(asset.Image.Tab.progress, UI.Field.Info.tab_progress)

    if var.tab_field == 'profile':
        pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.Profile.profile_image, 2)
        pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.Profile.icon_gold, 2)
        var.screen.blit(asset.Font.main_32.render(f'{var.Player.gold}', False, const.Color.black), UI.Field.Info.Profile.text_gold)

    elif var.tab_field == 'card':
        for i in range(2):
            for j in range(5):
                index = 10 * var.card_display_page + i * 5 + j
                if index < len(var.card_display_list):
                    draw_card(data.card[var.card_display_list[index]], [UI.Field.Info.Card.item_start[0] + UI.Field.Info.Card.item_interval[0] * j, UI.Field.Info.Card.item_start[1] + UI.Field.Info.Card.item_interval[1] * i])

                    try:
                        if var.Player.card_discovered[var.card_display_list[index]] == 'false':
                            draw_unknown_big([UI.Field.Info.Card.item_start[0] + UI.Field.Info.Card.item_interval[0] * j, UI.Field.Info.Card.item_start[1] + UI.Field.Info.Card.item_interval[1] * i])
                    except:
                        pass
                    
        var.screen.blit(asset.Image.Button.prev, UI.Field.Info.button_prev)
        var.screen.blit(asset.Font.main_32.render(f'{var.card_display_page + 1}/{len(var.card_display_list) // 8 + 1}', False, const.Color.black), UI.Field.Info.text_page)
        var.screen.blit(asset.Image.Button.next, UI.Field.Info.button_next)

    elif var.tab_field == 'crystal':
        for i in range(2):
            for j in range(5):
                index = 10 * var.crystal_display_page + i * 5 + j
                if index < len(var.crystal_display_list):
                    draw_crystal(data.crystal[var.crystal_display_list[index]], [UI.Field.Info.Crystal.item_start[0] + UI.Field.Info.Crystal.item_interval[0] * j, UI.Field.Info.Crystal.item_start[1] + UI.Field.Info.Crystal.item_interval[1] * i])
                
                    try:
                        if var.Player.crystal_discovered[var.crystal_display_list[index]] == 'false':
                            draw_unknown_big([UI.Field.Info.Crystal.item_start[0] + UI.Field.Info.Crystal.item_interval[0] * j, UI.Field.Info.Crystal.item_start[1] + UI.Field.Info.Crystal.item_interval[1] * i])
                    except:
                        pass

        var.screen.blit(asset.Image.Button.prev, UI.Field.Info.button_prev)
        var.screen.blit(asset.Font.main_32.render(f'{var.crystal_display_page + 1}/{len(var.crystal_display_list) // 10 + 1}', False, const.Color.black), UI.Field.Info.text_page)
        var.screen.blit(asset.Image.Button.next, UI.Field.Info.button_next)

    elif var.tab_field == 'equipment':
        for i in range(6):
            for j in range(7):
                index = 42 * var.equipment_display_page + i * 7 + j
                if index < len(var.equipment_display_list):
                    draw_equipment(data.equipment[var.equipment_display_list[index]], [UI.Field.Info.Equipment.item_start[0] + UI.Field.Info.Equipment.item_interval[0] * j, UI.Field.Info.Equipment.item_start[1] + UI.Field.Info.Equipment.item_interval[1] * i])

                    try:
                        if var.Player.equipment_discovered[var.equipment_display_list[index]] == 'false':
                            draw_unknown_small([UI.Field.Info.Equipment.item_start[0] + UI.Field.Info.Equipment.item_interval[0] * j, UI.Field.Info.Equipment.item_start[1] + UI.Field.Info.Equipment.item_interval[1] * i])
                    except:
                        pass

        var.screen.blit(asset.Image.Button.prev, UI.Field.Info.button_prev)
        var.screen.blit(asset.Font.main_32.render(f'{var.equipment_display_page + 1}/{len(var.equipment_display_list) // 42 + 1}', False, const.Color.black), UI.Field.Info.text_page)
        var.screen.blit(asset.Image.Button.next, UI.Field.Info.button_next)

        pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.Equipment.description_box, 2)

        if var.equipment_display_selected != -1:
            index = 42 * var.equipment_display_page + var.equipment_display_selected

            if index < len(var.equipment_display_list):
                try:
                    equipment_id = var.equipment_display_list[index]
                    if var.Player.equipment_discovered[equipment_id] == 'true':
                        description = data.description['equipment'][equipment_id]

                        for i in range(len(description)):
                            var.screen.blit(asset.Font.main_16.render(description[i], False, const.Color.black), UI.Field.Info.Equipment.description_text[i])
                except:
                    pass

    elif var.tab_field == 'item':
        for i in range(6):
            for j in range(7):
                index = 42 * var.item_display_page + i * 7 + j
                if index < len(var.item_display_list):
                    draw_item(data.item[var.item_display_list[index]], [UI.Field.Info.Item.item_start[0] + UI.Field.Info.Item.item_interval[0] * j, UI.Field.Info.Item.item_start[1] + UI.Field.Info.Item.item_interval[1] * i])

                    try:
                        if var.Player.item_discovered[var.item_display_list[index]] == 'false':
                            draw_unknown_small([UI.Field.Info.Item.item_start[0] + UI.Field.Info.Item.item_interval[0] * j, UI.Field.Info.Item.item_start[1] + UI.Field.Info.Item.item_interval[1] * i])
                    except:
                        pass

        var.screen.blit(asset.Image.Button.prev, UI.Field.Info.button_prev)
        var.screen.blit(asset.Font.main_32.render(f'{var.item_display_page + 1}/{len(var.item_display_list) // 42 + 1}', False, const.Color.black), UI.Field.Info.text_page)
        var.screen.blit(asset.Image.Button.next, UI.Field.Info.button_next)

        pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.Item.description_box, 2)

        if var.item_display_selected != -1:
            index = 42 * var.item_display_page + var.item_display_selected

            if index < len(var.item_display_list):
                try:
                    item_id = var.item_display_list[index]
                    if var.Player.item_discovered[item_id] == 'true':
                        description = data.description['item'][item_id]

                        for i in range(len(description)):
                            var.screen.blit(asset.Font.main_16.render(description[i], False, const.Color.black), UI.Field.Info.Item.description_text[i])
                except:
                    pass

    elif var.tab_field == 'place':
        temp_surface = pygame.Surface((UI.Field.Info.Place.rect[2], UI.Field.Info.Place.rect[3]))
        temp_surface.fill(const.Color.white)
        pygame.draw.rect(temp_surface, const.Color.black, UI.Field.Info.Place.rect, 2)

        for place in const.place_display:
            if data.field[place]['village'] == False:
                pygame.draw.rect(temp_surface, const.Color.black, const.place_display[place], 2)
            else:
                pygame.draw.rect(temp_surface, const.Color.blue, const.place_display[place], 4)

        pygame.draw.rect(temp_surface, const.Color.green, const.place_display[var.Field.place], 4)
        var.screen.blit(temp_surface, UI.Field.Info.Place.position)

    elif var.tab_field == 'progress':
        pass

def draw_info_adventure():
    pygame.draw.rect(var.screen, const.Color.white, UI.Field.Info_Adventure.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info_Adventure.rect, 2)
    var.screen.blit(asset.Image.Button.close, UI.Field.Info_Adventure.button_close)

    var.screen.blit(asset.Image.Tab.profile, UI.Field.Info_Adventure.tab_profile)
    var.screen.blit(asset.Image.Tab.deck, UI.Field.Info_Adventure.tab_deck)
    var.screen.blit(asset.Image.Tab.crystal, UI.Field.Info_Adventure.tab_crystal)
    var.screen.blit(asset.Image.Tab.place, UI.Field.Info_Adventure.tab_place)

    if var.tab_adventure == 'profile':
        pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.Profile.profile_image, 2)
        pygame.draw.rect(var.screen, const.Color.black, UI.Field.Info.Profile.icon_gold, 2)
        var.screen.blit(asset.Font.main_32.render(f'{var.Player.gold}', False, const.Color.black), UI.Field.Info.Profile.text_gold)

    elif var.tab_adventure == 'deck':
        for i in range(2):
            for j in range(5):
                index = 10 * var.deck_card_display_page + i * 5 + j
                if index < len(var.Adventure.deck_card):
                    draw_card(var.Adventure.deck_card[index], [UI.Field.Info_Adventure.Deck.item_start[0] + UI.Field.Info_Adventure.Deck.item_interval[0] * j, UI.Field.Info_Adventure.Deck.item_start[1] + UI.Field.Info_Adventure.Deck.item_interval[1] * i])

        var.screen.blit(asset.Image.Button.prev, UI.Field.Info_Adventure.button_prev)
        var.screen.blit(asset.Font.main_32.render(f'{var.card_display_page + 1}/{len(var.Adventure.deck_card) // 10 + 1}', False, const.Color.black), UI.Field.Info_Adventure.text_page)
        var.screen.blit(asset.Image.Button.next, UI.Field.Info_Adventure.button_next)

    elif var.tab_adventure == 'crystal':
        for i in range(2):
            for j in range(5):
                index = 10 * var.crystal_display_page + i * 5 + j
                if index < len(var.Adventure.deck_crystal):
                    draw_crystal(var.Adventure.deck_crystal[index], [UI.Field.Info_Adventure.Deck.item_start[0] + UI.Field.Info_Adventure.Deck.item_interval[0] * j, UI.Field.Info_Adventure.Deck.item_start[1] + UI.Field.Info_Adventure.Deck.item_interval[1] * i])

        var.screen.blit(asset.Image.Button.prev, UI.Field.Info_Adventure.button_prev)
        var.screen.blit(asset.Font.main_32.render(f'{var.crystal_display_page + 1}/{len(var.Adventure.deck_crystal) // 10 + 1}', False, const.Color.black), UI.Field.Info_Adventure.text_page)
        var.screen.blit(asset.Image.Button.next, UI.Field.Info_Adventure.button_next)

    elif var.tab_adventure == 'place':
        temp_surface = pygame.Surface((UI.Field.Info_Adventure.Place.rect[2], UI.Field.Info_Adventure.Place.rect[3]))
        temp_surface.fill(const.Color.white)
        pygame.draw.rect(temp_surface, const.Color.black, UI.Field.Info_Adventure.Place.rect, 2)

        for place in const.place_display:
            if data.field[place]['village'] == False:
                pygame.draw.rect(temp_surface, const.Color.black, const.place_display[place], 2)
            else:
                pygame.draw.rect(temp_surface, const.Color.blue, const.place_display[place], 4)

        pygame.draw.rect(temp_surface, const.Color.green, const.place_display[var.Field.place], 4)
        var.screen.blit(temp_surface, UI.Field.Info_Adventure.Place.position)

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

# Game

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

        if var.Game.field[i] != None:
            draw_unit(var.Game.field[i], UI.Game.Field.unit[i][:2])

def draw_game_lower():
    for i in range(len(var.Game.hand_card)):
        draw_card(var.Game.hand_card[i], [UI.Game.Lower.hand_card[i][0], UI.Game.Lower.hand_card[i][1]])

    if var.state_game_click == '':
        if var.Game.hand_card_mouse != -1:
            draw_card(var.Game.hand_card[var.Game.hand_card_mouse], [UI.Game.Lower.hand_card[var.Game.hand_card_mouse][0], UI.Game.Lower.hand_card[var.Game.hand_card_mouse][1]])
    elif var.state_game_click == 'card':
        draw_card(var.Game.hand_card[var.Game.selected_card], [UI.Game.Lower.hand_card[var.Game.selected_card][0], UI.Game.Lower.hand_card[var.Game.selected_card][1]])

    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Lower.description_box, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Lower.crystal_box, 2)

    for i in range(len(var.Game.hand_crystal)):
        var.screen.blit(asset.Image.crystal[var.Game.hand_crystal[i]['id']], UI.Game.Lower.crystal[i])

    for i in range(6):
        pygame.draw.rect(var.screen, const.Color.black, UI.Game.Lower.equipment[i], 2)

    for i in range(2):
        pygame.draw.rect(var.screen, const.Color.black, UI.Game.Lower.item[i], 2)

    pygame.draw.rect(var.screen, const.Color.black, UI.Game.Lower.button_turn_end, 2)
    var.screen.blit(asset.Font.main_32.render('Turn End', False, const.Color.black), UI.Game.Lower.text_turn_end)

## Etc
def draw_equipment(equipment, position):
    temp_surface = pygame.Surface((UI.Equipment.rect[2], UI.Equipment.rect[3]))
    pygame.draw.rect(temp_surface, const.Color.white, UI.Equipment.rect)
    temp_surface.blit(asset.Image.equipment[equipment['id']], UI.Equipment.image_equipment)
    pygame.draw.rect(temp_surface, const.Color.black, UI.Equipment.rect, 2)
    var.screen.blit(temp_surface, position)

def draw_item(item, position):
    temp_surface = pygame.Surface((UI.Item.rect[2], UI.Item.rect[3]))
    pygame.draw.rect(temp_surface, const.Color.white, UI.Item.rect)
    temp_surface.blit(asset.Image.item[item['id']], UI.Item.image_item)
    pygame.draw.rect(temp_surface, const.Color.black, UI.Item.rect, 2)
    var.screen.blit(temp_surface, position)

def draw_card(card, position):
    temp_surface = pygame.Surface((UI.Card.rect[2], UI.Card.rect[3]))
    pygame.draw.rect(temp_surface, const.Color.white, UI.Card.rect)
    pygame.draw.rect(temp_surface, const.Color.black, UI.Card.rect, 2)
    temp_surface.blit(asset.Image.card[card['id']], UI.Card.image_card)
    pygame.draw.rect(temp_surface, const.Color.black, UI.Card.image_card, 2)
    temp_surface.blit(asset.Font.main_16.render(f'{card["name"]}', False, const.Color.black), UI.Card.text_name)

    for i in range(len(card['crystal'])):
        if card['crystal'][i][0] == 'any':
            temp_surface.blit(asset.Image.crystal[1], UI.Card.crystal[i])
        temp_surface.blit(asset.Font.main_32.render(f'{card["crystal"][i][1]}', False, const.Color.black), UI.Card.text_crystal[i])

    if card['type'] == 'unit':
        temp_surface.blit(asset.Font.main_32.render(f'{card["stat"][0]}', False, const.Color.black), UI.Card.text_attack)
        temp_surface.blit(asset.Font.main_32.render(f'{card["stat"][1]}', False, const.Color.black), UI.Card.text_life)

    var.screen.blit(temp_surface, position)

def draw_crystal(crystal, position):
    temp_surface = pygame.Surface((UI.Crystal.rect[2], UI.Crystal.rect[3]))
    pygame.draw.rect(temp_surface, const.Color.white, UI.Crystal.rect)
    pygame.draw.rect(temp_surface, const.Color.black, UI.Crystal.rect, 2)
    temp_surface.blit(asset.Image.crystal[crystal['id']], UI.Crystal.image_crystal)
    temp_surface.blit(asset.Font.main_16.render(f'{crystal["name"]}', False, const.Color.black), UI.Crystal.text_name)

    var.screen.blit(temp_surface, position)

def draw_unknown_big(position):
    temp_surface = pygame.Surface((160, 240))
    temp_surface.blit(asset.Image.unknown_big, [0, 0])
    pygame.draw.rect(temp_surface, const.Color.black, [0, 0, 160, 240], 2)
    var.screen.blit(temp_surface, position)

def draw_unknown_small(position):
    temp_surface = pygame.Surface((80, 80))
    temp_surface.blit(asset.Image.unknown_small, [0, 0])
    pygame.draw.rect(temp_surface, const.Color.black, [0, 0, 80, 80], 2)
    var.screen.blit(temp_surface, position)

def draw_unit(unit, position):
    temp_surface = pygame.Surface((120, 80))
    temp_surface.fill(const.Color.white)

    try:
        temp_surface.blit(asset.Image.card[unit['id']], UI.Unit.image_unit)
    except:
        temp_surface.blit(asset.Image.temp_80, UI.Unit.image_unit)

    temp_surface.blit(asset.Font.main_32.render(f'{unit["stat"][0]}', False, const.Color.black), UI.Unit.text_attack)
    temp_surface.blit(asset.Font.main_32.render(f'{unit["stat"][1]}', False, const.Color.black), UI.Unit.text_life)

    pygame.draw.rect(temp_surface, const.Color.black, UI.Unit.rect, 2)
    var.screen.blit(temp_surface, position)