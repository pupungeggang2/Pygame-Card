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
    rect_player = [var.Field.position_player[0] - var.Field.camera[0] - 20, var.Field.position_player[1] - var.Field.camera[1] - 20, 40, 40]
    pygame.draw.rect(var.screen, const.Color.black, rect_player, 2)

def draw_info():
    pass