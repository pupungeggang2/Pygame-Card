import pygame
import asset, UI, data, var, const
import funcphysics, funcdraw, funcfield

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    if var.state == 'start':
        funcdraw.draw_game_start()

    pygame.display.flip()

def mouse_up(x, y, button):
    pass

def key_down(key):
    pass

def key_up(key):
    pass