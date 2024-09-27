screen = None
resolution = [1280, 720]
FPS = 60
clock = None

save = {}

scene = 'title'
state = ''
menu = False

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

class Player():
    card = []
    equipment = []
    item = []

class Game():
    turn = 0
    turn_who = 0