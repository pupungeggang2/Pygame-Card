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
        tab_place = [480, 80, 80, 80]
        tab_progress = [560, 80, 80, 80]
        button_prev = [920, 560, 40, 40]
        text_page = [964, 564]
        button_next = [1080, 560, 80, 80]
        description_rect = []

        class Profile():
            pass

        class Card():
            item_start = [80, 160]
            item_size = [160, 240]
            item_interval = [160, 240]
            
        class Deck():
            item_start = [80, 160]
            item_size = [160, 240]
            item_interval = [160, 240]

        class Equipment():
            pass

        class Item():
            pass

        class Place():
            pass

        class Progress():
            pass

    class Info_Adventure():
        rect = [80, 80, 1120, 560]
        button_close = [1160, 80, 40, 40]

        tab_profile = [80, 80, 80, 80]
        tab_deck = [160, 80, 80, 80]
        button_prev = [920, 560, 40, 40]
        text_page = [964, 564]
        button_next = [1080, 560, 80, 80]

        class Profile():
            pass

        class Deck():
            item_start = [80, 160]
            item_size = [160, 240]
            item_interval = [160, 240]

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

    class Field():
        unit = [
            [580, 40, 120, 80],
            [280, 120, 120, 80], [400, 120, 120, 80], [520, 120, 120, 80], [640, 120, 120, 80], [760, 120, 120, 80], [880, 120, 120, 80],
            [280, 200, 120, 80], [400, 200, 120, 80], [520, 200, 120, 80], [640, 200, 120, 80], [760, 200, 120, 80], [880, 200, 120, 80],
            [580, 280, 120, 80]
        ]

    class Lower():
        hand_card = [
            [80, 480, 160, 240], [160, 480, 160, 240], [240, 480, 160, 240], [320, 480, 160, 240],
            [400, 480, 160, 240], [480, 480, 160, 240], [560, 480, 160, 240], [640, 480, 160, 240]
        ]

        crystal = [
            [960, 480, 40, 40], [1000, 480, 40, 40], [1040, 480, 40, 40], [1080, 480, 40, 40],
            [960, 520, 40, 40], [1000, 520, 40, 40], [1040, 520, 40, 40], [1080, 520, 40, 40],
            [960, 560, 40, 40], [1000, 560, 40, 40], [1040, 560, 40, 40], [1080, 560, 40, 40],
        ]
        button_turn_end = [1160, 480, 80, 40]
        text_turn_end = [1168, 484]

class Card():
    rect = [0, 0, 160, 240]
    crystal = [[0, 0], [40, 0], [80, 0], [120, 0]]
    text_crystal = [[16, 4], [46, 4], [96, 4], [136, 4]]
    image_card = [40, 40, 80, 80]
    text_name = [4, 122]
    text_attack = [24, 204]
    text_life = [124, 204]

class Equipment():
    rect = [0, 0, 160, 240]