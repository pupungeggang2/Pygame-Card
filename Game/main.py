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
    f = open('Data/deck.txt', 'r')
    data.deck = ast.literal_eval(f.read())
    f.close()
    f = open('Data/card.txt', 'r')
    data.card = ast.literal_eval(f.read())
    f.close()
    f = open('Data/crystal.txt', 'r')
    data.crystal = ast.literal_eval(f.read())
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
    f = open('Data/description.txt', 'r')
    data.description = ast.literal_eval(f.read())
    f.close()

    var.card_display_list = []

    for card in data.card:
        var.card_display_list.append(card)

    var.crystal_display_list = []

    for crystal in data.crystal:
        var.crystal_display_list.append(crystal)

    var.equipment_display_list = []

    for equipment in data.equipment:
        var.equipment_display_list.append(equipment)

    var.item_display_list = []

    for item in data.item:
        var.item_display_list.append(item)

def load_asset():
    try:
        asset.Font.main_32 = pygame.font.Font('Font/neodgm.ttf', 32)
        asset.Font.main_16 = pygame.font.Font('Font/neodgm.ttf', 16)

    except:
        asset.Font.main_32 = pygame.font.SysFont(None, 32)
        asset.Font.main_16 = pygame.font.SysFont(None, 16)

    asset.Image.connection = pygame.image.load('Image/Connection.png')
    asset.Image.monster = pygame.image.load('Image/Monster.png')
    asset.Image.mystery = pygame.image.load('Image/Mystery.png')
    asset.Image.field_shop = pygame.image.load('Image/FieldShop.png')
    asset.Image.save = pygame.image.load('Image/Save.png')
    asset.Image.unknown_big = pygame.image.load('Image/UnknownBig.png')
    asset.Image.unknown_small = pygame.image.load('Image/UnknownSmall.png')
    asset.Image.temp_80 = pygame.image.load('Image/TempImage80.png')
    asset.Image.temp_40 = pygame.image.load('Image/TempImage40.png')

    for card in data.card:
        try:
            asset.Image.card[card] = pygame.image.load(f'Image/Card{str(card).zfill(3)}.png')
        except:
            asset.Image.card[card] = pygame.image.load('Image/TempImage80.png')

    for crystal in data.crystal:
        try:
            asset.Image.crystal[crystal] = pygame.image.load(f'Image/Crystal{str(crystal).zfill(3)}.png')
        except:
            asset.Image.crystal[crystal] = pygame.image.load('Image/TempImage40.png')

    for equipment in data.equipment:
        try:
            asset.Image.equipment[equipment] = pygame.image.load(f'Image/Equipment${str(equipment).zfill(3)}.png')
        except:
            asset.Image.equipment[equipment] = pygame.image.load('Image/TempImage80.png')

    for item in data.item:
        try:
            asset.Image.item[item] = pygame.image.load(f'Image/Item${str(item).zfill(3)}.png')
        except:
            asset.Image.item[item] = pygame.image.load('Image/TempImage80.png')

    asset.Image.player['left'] = pygame.image.load('Image/PlayerLeft.png')
    asset.Image.player['right'] = pygame.image.load('Image/PlayerRight.png')
    asset.Image.player['up'] = pygame.image.load('Image/PlayerUp.png')
    asset.Image.player['down'] = pygame.image.load('Image/PlayerDown.png')

    asset.Image.background['grass'] = pygame.image.load('Image/Grass.png')
    asset.Image.background['snow'] = pygame.image.load('Image/Snow.png')

    asset.Image.Button.menu = pygame.image.load('Image/Button/ButtonMenu.png')
    asset.Image.Button.info = pygame.image.load('Image/Button/ButtonInfo.png')
    asset.Image.Button.close = pygame.image.load('Image/Button/ButtonClose.png')
    asset.Image.Button.prev = pygame.image.load('Image/Button/ButtonPrev.png')
    asset.Image.Button.next = pygame.image.load('Image/Button/ButtonNext.png')

    asset.Image.Tab.profile = pygame.image.load('Image/Tab/TabProfile.png')
    asset.Image.Tab.deck = pygame.image.load('Image/Tab/TabDeck.png')
    asset.Image.Tab.card = pygame.image.load('Image/Tab/TabCard.png')
    asset.Image.Tab.crystal = pygame.image.load('Image/Tab/TabCrystal.png')
    asset.Image.Tab.equipment = pygame.image.load('Image/Tab/TabEquipment.png')
    asset.Image.Tab.item = pygame.image.load('Image/Tab/TabItem.png')
    asset.Image.Tab.place = pygame.image.load('Image/Tab/TabPlace.png')
    asset.Image.Tab.progress = pygame.image.load('Image/Tab/TabProgress.png')

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

        if event.type == pygame.MOUSEMOTION:
            if var.scene == 'game':
                mouse = pygame.mouse.get_pos()
                x = mouse[0]
                y = mouse[1]
                scenegame.mouse_move(x, y)

        if event.type == pygame.KEYDOWN:
            key = event.key

            if key == pygame.K_LEFT or key == pygame.K_a:
                var.keyboard['left'] = True
            if key == pygame.K_RIGHT or key == pygame.K_d:
                var.keyboard['right'] = True
            if key == pygame.K_UP or key == pygame.K_w:
                var.keyboard['up'] = True
            if key == pygame.K_DOWN or key == pygame.K_s:
                var.keyboard['down'] = True

            if var.scene == 'title':
                scenetitle.key_down(key)

            elif var.scene == 'field':
                scenefield.key_down(key)

            elif var.scene == 'game':
                scenegame.key_down(key)

        if event.type == pygame.KEYUP:
            key = event.key

            if key == pygame.K_LEFT or key == pygame.K_a:
                var.keyboard['left'] = False
            if key == pygame.K_RIGHT or key == pygame.K_d:
                var.keyboard['right'] = False
            if key == pygame.K_UP or key == pygame.K_w:
                var.keyboard['up'] = False
            if key == pygame.K_DOWN or key == pygame.K_s:
                var.keyboard['down'] = False

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