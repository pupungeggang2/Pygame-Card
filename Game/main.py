import pygame, sys, ast
import asset, UI, data, var, const
import scenetitle, scenefield, scenegame

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.resolution)
    pygame.display.set_caption('Card Game')
    var.clock = pygame.time.Clock()

    load_data()
    load_asset()
    load_save()

def load_data():
    f = open('Data/card.txt', 'r')
    data.card = ast.literal_eval(f.read())
    f.close()

    f = open('Data/equipment.txt', 'r')
    data.equipment = ast.literal_eval(f.read())
    f.close()

    f = open('Data/field.txt', 'r')
    data.field = ast.literal_eval(f.read())
    f.close()

    f = open('Data/item.txt', 'r')
    data.item = ast.literal_eval(f.read())
    f.close()

    f = open('Data/monster.txt', 'r')
    data.monster = ast.literal_eval(f.read())
    f.close()

def load_asset():
    try:
        asset.Font.main_32 = pygame.font.Font('Font/neodgm.ttf', 32)

    except:
        asset.Font.main_32 = pygame.font.SysFont(None, 32)

def load_save():
    try:
        f = open('Save/save.txt', 'r')
        var.save = ast.literal_eval(f.read())
        f.close()

    except:
        f = open('Save/save.txt', 'w')
        f.write(str(const.empty_save))
        f.close()
        f = open('Save/save.txt', 'r')
        var.save = ast.literal_eval(f.read())
        f.close()

def main():
    while True:
        var.clock.tick(var.FPS)
        handle_input()
        handle_scene()

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            x = mouse[0]
            y = mouse[1]
            button = event.button

            if var.scene == 'title':
                scenetitle.mouse_up(x, y, button)

            elif var.scene == 'field':
                scenefield.mouse_up(x, y, button)

            elif var.scene == 'game':
                scenegame.mouse_up(x, y, button)

        if event.type == pygame.KEYDOWN:
            key = event.key

            if var.scene == 'title':
                scenetitle.key_down(key)

            elif var.scene == 'field':
                scenefield.key_down(key)

            elif var.scene == 'game':
                scenegame.key_down(key)

        if event.type == pygame.KEYUP:
            key = event.key

            if var.scene == 'title':
                scenetitle.key_up(key)

            elif var.scene == 'field':
                scenefield.key_up(key)

            elif var.scene == 'game':
                scenegame.key_up(key)

def handle_scene():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'field':
        scenefield.loop()

    elif var.scene == 'game':
        scenegame.loop()

init()
main()