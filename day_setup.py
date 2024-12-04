DAY_NUMBER = 5

# Create input files
f= open(f'input/{DAY_NUMBER}_example.txt', 'w')
f= open(f'input/{DAY_NUMBER}_real.txt', 'w')

# Create day.py file with starting code
f= open(f'days/day{DAY_NUMBER}.py', 'w')
f.write("""from utils.my_utils import get_grid_from_txt, get_txt_lines, get_txt_whole

data = get_txt_whole(4, example=True)
print(data)

def part_1():
    return""")