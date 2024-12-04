
path_prefix = './input/'
example_suffix = '_example.txt'
real_suffix = '_real.txt'

def get_txt_whole(day, example=False):
    path = path_prefix + str(day) + (example_suffix if example else real_suffix)
    with open(path, 'r') as f:
        return f.read()

def get_txt_lines(day, example=False):    
    path = path_prefix + str(day) + (example_suffix if example else real_suffix)
    with open(path, 'r') as f:
        return f.readlines()
    
def get_grid_from_txt(day, example=False):
    return [list(line.strip()) for line in get_txt_lines(day, example)]