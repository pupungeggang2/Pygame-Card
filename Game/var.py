screen = None
resolution = [1280, 720]
FPS = 60
clock = None

save = {}

scene = 'title'
state = ''
menu = False

class Field():
    camera = [0, 0]
    position_player = [640, 640]
    place = 'HomeTown'
    field = {}

class Adventure():
    adventure = False

class Player():
    card = []
    equipment = []
    item = []

class Game():
    turn = 0
    turn_who = 0