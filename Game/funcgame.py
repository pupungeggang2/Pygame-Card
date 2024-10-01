import pygame, ast
import random
import asset, UI, data, var, const

def game_init():
    build_deck()
    var.Game.start_hand_change = [False, False, False]

def turn_start_first():
    for i in range(3):
        draw_card_from_deck()

def turn_start():
    draw_card_from_deck()

    for i in range(var.Game.crystal_max):
        draw_crystal_from_deck()

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
            var.Game.hand_card.append(var.Game.deck_card.pop())

def draw_crystal_from_deck():
    if len(var.Game.deck_crystal) > 0:
        if len(var.Game.hand_crystal) < 16:
            var.Game.hand_crystal.append(var.Game.deck_crystal.pop())