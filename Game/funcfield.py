import pygame, ast
import random
import asset, UI, data, const, var
import funcphysics

def field_init():
    var.Field.place = var.save['place']
    load_field(var.Field.place)

def load_field(place):
    var.Field.field = ast.literal_eval(str(data.field[place]))

    if var.Field.field['village'] == False:
        var.Field.field['event'] = []
        temp_event_spawn = ast.literal_eval(str(var.Field.field['event_spawn']))

        for i in range(3):
            temp_position = temp_event_spawn.pop(random.randint(0, len(temp_event_spawn) - 1))
            var.Field.field['event'].append({'type' : 'monster', 'position' : temp_position})

        temp_position = temp_event_spawn.pop(random.randint(0, len(temp_event_spawn) - 1))
        temp_type = random.choice(['shop', 'mystery'])
        var.Field.field['event'].append({'type' : temp_type, 'position' : temp_position})

def field_tick():
    move_player()
    collision_check()

def move_player():
    temp_position = [var.Field.position_player[0], var.Field.position_player[1]]

    if var.keyboard['left'] == True:
        temp_position[0] += -320 / var.FPS
    if var.keyboard['right'] == True:
        temp_position[0] += 320 / var.FPS
    if var.keyboard['up'] == True:
        temp_position[1] += -320 / var.FPS
    if var.keyboard['down'] == True:
        temp_position[1] += 320 / var.FPS

    var.Field.position_player[0] = temp_position[0]
    var.Field.position_player[1] = temp_position[1]

    temp_camera = [var.Field.position_player[0] - 640, var.Field.position_player[1] - 360]

    var.Field.camera[0] = temp_camera[0]
    var.Field.camera[1] = temp_camera[1]

def collision_check():
    for i in range(len(var.Field.field['event'])):
        temp_event = var.Field.field['event'][i]
        if funcphysics.point_inside_rect_array(var.Field.position_player[0], var.Field.position_player[1], temp_event['position']):
            if temp_event['type'] == 'monster':
                var.Field.field['event'].pop(i)
                var.scene = 'game'
                var.state = ''
                break

def interact():
    for i in range(len(var.Field.field['connection'])):
        temp_connection = var.Field.field['connection'][i]
        rect_connection = var.Field.field['connection'][i][0]
        if funcphysics.point_inside_rect_array(var.Field.position_player[0], var.Field.position_player[1], rect_connection):
            var.Field.destination_place = temp_connection[1]
            var.Field.destination_position = temp_connection[2]

            if var.Adventure.adventure == True and data.field[var.Field.destination_place]['village'] == True:
                var.state = 'adventure_confirm_end'

            elif var.Adventure.adventure == False and data.field[var.Field.destination_place]['village'] == False:
                var.state = 'adventure_confirm_start'

            else:
                var.Field.place = var.Field.destination_place
                load_field(var.Field.place)
                var.Field.position_player = var.Field.destination_position

    for i in range(len(var.Field.field['thing'])):
        thing = var.Field.field['thing'][i]

        if funcphysics.point_inside_rect_array(var.Field.position_player[0], var.Field.position_player[1], thing[0]):
            var.state = 'save'