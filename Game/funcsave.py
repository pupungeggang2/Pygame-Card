import ast
import asset, UI, data, var, const

def save_data():
    f = open('Save/save.txt', 'w')
    f.write(str(
        {
            'place' : var.Field.place,
            'card_discovered' : str(var.Player.equipment_discovered),
            'crystal_discovered' : str(var.Player.crystal_discovered),
            'equipment_discovered' : str(var.Player.equipment_discovered),
            'item_discovered' : str(var.Player.item_discovered),
            'gold' : var.Player.gold,
            'progress' : {}
        }
    ))
    f.close()

def load_data():
    f = open('Save/save.txt', 'r')
    temp_save = ast.literal_eval(f.read())
    var.Field.place = temp_save['place']
    var.Player.card_discovered = temp_save['card_discovered']
    var.Player.crystal_discovered = temp_save['crystal_discovered']
    var.Player.equipment_discovered = temp_save['equipment_discovered']
    var.Player.item_discovered = temp_save['item_discovered']
    var.Player.gold = temp_save['gold']
    f.close()

def erase_data():
    f = open('Save/save.txt', 'w')
    f.write(str(const.empty_save))
    f.close()
    f = open('Save/save.txt', 'r')
    var.save = ast.literal_eval(f.read())
    f.close()
