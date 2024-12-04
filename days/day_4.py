from utils.my_utils import get_grid_from_txt, get_txt_lines, get_txt_whole
from collections import defaultdict

# matrix = get_grid_from_txt(4, example=True)
# print(matrix)

"""
    Part 1
        I'm not going to beat around the bush. I could not figure out how to iterate 2d arrays and look in all directions, 
        so i searched on the internet and this code using imaginary units looked the most understandable for me.
"""
def part_1(example = False):
    letters = defaultdict(str)
    Xs = []
    imaginary = 0+1j
    for j, l in enumerate(get_txt_lines(4, example)):
        for i,c in enumerate(l.strip()):
            letters[i+j*imaginary] = c
            if c == 'X':
                Xs.append(i+j*imaginary)

    count = 0
    for x in Xs:
        for d in [+1,-1,+1j,-1j,+1+1j,-1+1j,+1-1j,-1-1j]: # move 3 steps in all 8 possible directions
            if "".join([letters[x+k*d] for k in range(1,4)]) == "MAS":
                count+=1
    return count

"""
    Part 2
        This part im using code from part 1 and change it so it looks for x patterns of "MAS"
"""
def part_2(use_example = False):
    letters = defaultdict(str)
    As = []
    imaginary = 0+1j
    for j, l in enumerate(get_txt_lines(4, use_example)):
        for i,c in enumerate(l.strip()):
            letters[i+j*imaginary] = c
            if c == 'A': 
                As.append(i+j*imaginary)

    count = 0
    for a in As:
        c = [letters[a+p] for p in [-1+1j,+1+1j,+1-1j,-1-1j]]
        if ''.join(c) in ['MMSS', 'SSMM', 'MSSM', 'SMMS']:
            # print(c)
            count += 1
    return count


print('Part 1:', part_1())
print('Part 2:', part_2())