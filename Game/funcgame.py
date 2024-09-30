import pygame, ast
import random
import asset, UI, data, var, const

def game_init():
    build_deck()
    var.Game.start_hand_change = [False, False, False]

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