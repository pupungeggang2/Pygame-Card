class Color():
    black = [0, 0, 0]
    green = [0, 255, 0]
    blue = [0, 0, 255]
    white = [255, 255, 255]

empty_save = {
    'place' : 'home_town',
    'card' : {
        1 : {'opened' : True}, 2 : {'opened' : True}, 3 : {'opened' : True}, 4 : {'opened' : False}, 5 : {'opened' : False},
        6 : {'opened' : False},
    },
    'equipment' : [],
    'item' : [],
    'gold' : [],
    'skill_tree' : [],
    'progress' : []
}

place_display = {
    'home_town' : [40, 400, 40, 40],
    'plain_1' : [40, 360, 40, 40],
    'plain_2' : [80, 360, 40, 40],
    'center_town' : [120, 360, 40, 40],
    'plain_3' : [160, 360, 40, 40],
    'plain_4' : [200, 360, 40, 40],
    'snow_1' : [120, 320, 40, 40]
}