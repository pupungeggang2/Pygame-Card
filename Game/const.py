class Color():
    black = [0, 0, 0]
    green = [0, 255, 0]
    blue = [0, 0, 255]
    white = [255, 255, 255]

empty_save = {
    'place' : 'home_town',
    'card_discovered' : {
        1 : 'true', 2 : 'true', 3 : 'true', 4 : 'false', 5 : 'false', 6 : 'false', 7 : 'false', 8 : 'false', 9 : 'false', 10 : 'false',
        11 : 'false', 12 : 'false'
    },
    'crystal_discovered' : {
        1 : 'true', 2 : 'false', 3 : 'false', 4 : 'false', 5 : 'false', 6 : 'false', 7 : 'false'
    },
    'equipment_discovered' : {
        1 : 'true', 2 : 'false', 3 : 'false', 4 : 'false', 5 : 'false', 6 : 'false'
    },
    'item_discovered' : {
        1 : 'true', 2 : 'false', 3 : 'false', 4 : 'false', 5 : 'false', 6 : 'false'
    },
    'gold' : 50,
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

place_background = {
    'home_town' : 'grass',
    'plain_1' : 'grass',
    'plain_2' : 'grass',
    'center_town' : 'grass',
    'plain_3' : 'grass',
    'plain_4' : 'grass',
    'snow_1' : 'snow'
}