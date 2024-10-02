screen = None
resolution = [1280, 720]
FPS = 60
clock = None

save = {}

scene = 'title'
state = ''
menu = False

tab_field = ''
tab_adventure = ''

card_display_list = []
card_display_page = 0

keyboard = {
    'left' : False, 'right' : False, 'up' : False, 'down' : False
}

class Field():
    camera = [0, 0]
    position_player = [640, 640]
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
    basic_deck = {
        'card' : [1, 1, 1, 2, 2, 2, 3, 3, 3],
        'crystal' : [1, 1, 1, 1, 1, 1, 1, 1]
    }
    selected_deck = 0
    card = []
    equipment = []
    item = []

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