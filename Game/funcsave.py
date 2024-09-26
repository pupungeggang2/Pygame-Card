import ast
import asset, UI, data, var, const

def save_data():
    f = open('Save/save.txt', 'w')
    f.write(str(var.save))
    f.close()

def load_data():
    f = open('Save/save.txt', 'r')
    var.save = ast.literal_eval(f.read())
    f.close()

def erase_data():
    f = open('Save/save.txt', 'w')
    f.write(str(const.empty_save))
    f.close()
    f = open('Save/save.txt', 'r')
    var.save = ast.literal_eval(f.read())
    f.close()
