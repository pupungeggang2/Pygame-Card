import pygame, ast
import random
import asset, UI, data, var, const
import funcphysics

def game_init():
    monster_list = ast.literal_eval(str(var.Field.field['monster_id']))
    var.Game.monster_id = random.choice(monster_list)

    var.Game.crystal_max = 0
    var.Game.turn = 0

    build_deck()
    var.Game.start_hand_change = [False, False, False]
    var.Game.field[0] = {
        'id' : 1000 + var.Game.monster_id, 'stat' : [0, 15], 'effect' : [] 
    }
    var.Game.field[13] = {
        'id' : 10000, 'stat' : [0, 20], 'effect' : [],
    }

def turn_start_first():
    for i in range(3):
        draw_card_from_deck()

def turn_start():
    var.Game.turn += 1

    if var.Game.crystal_max < 8:
        var.Game.crystal_max += 1

    draw_card_from_deck()

    for i in range(var.Game.crystal_max):
        draw_crystal_from_deck()

def turn_end():
    while len(var.Game.hand_crystal) > 0:
        var.Game.deck_crystal.append(var.Game.hand_crystal.pop(0))

# Manipulating hand, deck
def build_deck():
    var.Game.deck_card = []
    var.Game.deck_crystal = []

    for i in range(len(var.Adventure.deck_card)):
        var.Game.deck_card = insert_thing_random(ast.literal_eval(str(var.Adventure.deck_card[i])), var.Game.deck_card)

    for i in range(len(var.Adventure.deck_crystal)):
        var.Game.deck_crystal = insert_thing_random(ast.literal_eval(str(var.Adventure.deck_crystal[i])), var.Game.deck_crystal)

def insert_thing_random(item, arr):
    index = random.randint(0, len(arr))
    arr.insert(index, item)
    return arr

def start_card_change():
    length = len(var.Game.deck_card) - 1

    for i in range(3):
        if var.Game.start_hand_change[i] == True:
            temp = var.Game.deck_card[i]
            var.Game.deck_card[i] = var.Game.deck_card[length - i]
            var.Game.deck_card[length - i] = temp

def draw_card_from_deck():
    if len(var.Game.deck_card) > 0:
        if len(var.Game.hand_card) < 8:
            var.Game.hand_card.append(var.Game.deck_card.pop(0))

def draw_crystal_from_deck():
    if len(var.Game.deck_crystal) > 0:
        if len(var.Game.hand_crystal) < 16:
            var.Game.hand_crystal.append(var.Game.deck_crystal.pop(0))

# Card
def handle_effect_card(card):
    var.Game.hand_crystal_temp = ast.literal_eval(str(var.Game.hand_crystal))
    crystal_temp = card_crystal_unroll(card['crystal'])

    playable = False
    i = 0

    while i < len(var.Game.hand_crystal_temp):
        crystal_used = False
        for j in range(len(crystal_temp)):
            if crystal_temp[j] == 'any':
                var.Game.hand_crystal_spent.append(var.Game.hand_crystal_temp.pop(i))
                crystal_temp.pop(j)
                crystal_used = True
                break

        if len(crystal_temp) <= 0:
            playable = True
            break

        if crystal_used == False:
            i += 1

    if playable == False:
        var.state_game_click = ''
        var.Game.selected_card = -1
    else:
        var.Game.effect_queue = ast.literal_eval(str(card['effect']))
        
        while len(var.Game.effect_queue) > 0:
            if var.Game.effect_queue[0][0] == 'damage':
                if var.Game.effect_queue[0][1] == 'enemy_hero':
                    var.Game.field[0]['stat'][1] -= var.Game.effect_queue[0][2]

            var.Game.effect_queue.pop()

        if len(var.Game.effect_queue) <= 0:
            var.Game.hand_card.pop(var.Game.selected_card)
            var.Game.hand_crystal = var.Game.hand_crystal_temp

            for i in range(len(var.Game.hand_crystal_spent)):
                var.Game.deck_crystal.append(var.Game.hand_crystal_spent[i])

            var.state_game_click = ''

def card_crystal_unroll(crystal):
    result = []
    for i in range(len(crystal)):
        for j in range(crystal[i][1]):
            result.append(crystal[i][0])
    return result

# Etc
def mouse_card_handle():
    var.Game.hand_card_mouse = -1
    for i in range(len(var.Game.hand_card)):
        if funcphysics.point_inside_rect_array(var.mouse[0], var.mouse[1], UI.Game.Lower.hand_card_mouse[i]):
            var.Game.hand_card_mouse = i