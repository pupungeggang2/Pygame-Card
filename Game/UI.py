class Title():
    text_title = [8, 4]
    button_start = [160, 160, 960, 80]
    text_start = [168, 184]
    button_erase = [160, 240, 960, 80]
    text_erase = [168, 264]

class Field():
    button_menu = [1220, 20, 40, 40]
    button_info = [1220, 660, 40, 40]
    text_place = [8, 24]
    text_tip = [8, 664]

    class Info():
        rect = [80, 80, 1120, 560]
        button_close = [1160, 80, 40, 40]
        tab_profile = [80, 80, 80, 80]
        tab_card = [160, 80, 80, 80]
        tab_deck = [240, 80, 80, 80]
        tab_equipment = [320, 80, 80, 80]
        tab_item = [400, 80, 80, 80]
        tab_map = [480, 80, 80, 80]
        tab_progress = [560, 80, 80, 80]

    class Menu():
        rect = [320, 240, 640, 240]
        text_pause = [328, 264]
        button_resume = [320, 320, 640, 80]
        text_resume = [328, 344]
        button_exit = [320, 400, 640, 80]
        text_exit = [328, 424]

    class Confirm():
        rect = [320, 240, 640, 240]
        text_title = [328, 264]
        button_yes = [400, 320, 160, 80]
        text_yes = [408, 344]
        button_no = [720, 320, 160, 80]
        text_no = [728, 344]

    class Save():
        rect = [320, 240, 640, 240]
        text_title = [328, 264]
        button_yes = [400, 320, 160, 80]
        text_yes = [408, 344]
        button_no = [720, 320, 160, 80]
        text_no = [728, 344]

class Game():
    class Start():
        rect = [80, 80, 1120, 560]
        text_title = [88, 88]
        button_select = [
            [160, 160, 160, 240], [560, 160, 160, 240], [960, 160, 160, 240]
        ]
        button_start = [560, 480, 160, 80]
        text_start = [568, 504]