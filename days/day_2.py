
matrix = []
filename_e = './input/2_example.txt'    # example data
filename_r = './input/2_real.txt'       # real data

with open(filename_r, 'r') as f:
    for lines in f:
        matrix.append([int(x) for x in lines.split(' ')])

# print(matrix)

def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False

# check for each row if the difference is in the allowed differences
def part_1(data):
    safe_count = sum([is_safe(row) for row in data])
    print(safe_count)

part_1(matrix)

def part_2(data):
    safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
    print(safe_count)

part_2(matrix)
