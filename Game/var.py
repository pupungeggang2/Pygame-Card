screen = None
resolution = [1280, 720]
FPS = 60
clock = None

save = {}

scene = 'title'
state = ''
state_game_click = ''
menu = False

tab_field = ''
tab_adventure = ''

card_display_list = []
card_display_page = 0
deck_card_display_page = 0
crystal_display_list = []
crystal_display_page = 0
equipment_display_list = []
equipment_display_page = 0
equipment_display_selected = -1
item_display_list = []
item_display_page = 0
item_display_selected = -1

keyboard = {
    'left' : False, 'right' : False, 'up' : False, 'down' : False
}

class Field():
    camera = [0, 0]
    position_player = [640, 640]
    player_facing = 'down'
    place = 'HomeTown'
    field = {}
    destination_place = ''
    destination_position = [0, 0]

class Adventure():
    adventure = False
    element = []
    deck_card = [

    ]
    deck_crystal = [

    ]

class Player():
    gold = 0
    
    basic_deck = {
        'card' : [1, 1, 1, 2, 2, 2, 3, 3, 3],
        'crystal' : [1, 1, 1, 1, 1, 1, 1, 1]
    }
    selected_deck = 0
    card_discovered = {}
    crystal_discovered = {}
    equipment_discovered = {}
    item_discovered = {}

class Game():
    turn = 0
    turn_who = 0

    power = 0
    energy = 0
    crystal_max = 1

    start_hand_change = [False, False, False]
    deck_card = []
    deck_crystal = []
    hand_card = []
    hand_crystal = []

    field = []

    selected_thing = {}