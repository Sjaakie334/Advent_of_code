import re

f_example = './input/3_example.txt'
f_real = './input/3_real.txt'

# Pattern to match is 'mul('+<number containing 1-3 digits>+','+<number containing 1-3 digits>+')'
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

lines = []

# with open(f_real, 'r') as f:
#     for line in f:
#         lines.append(line)


"""
    Part 1:
        Never thought that the first thing i would use would be regex.
        Shout out to RegExr cheatsheet. I made my pattern using this.
"""
def part_1(data):
    results = []
    for line in data:
        matches = re.findall(pattern, line)
        results.append(sum([ int(x)*int(y) for x, y in matches ]))
    print('part 1: ', sum(results))

"""
    Part 2
        Not gonna lie, this part is a bit of a pain.
        Since the way of part 1 will not really work here. We are approaching this
        differently: 
            - To begin, we will read the file as a whole. 
            - And use regex to first filter out everything between
                shouldn't and 'do()' or end of line.
            - Then we can use the method of part 1 to get the answer.
            - First we will rework part 1 so that we can use it in part 2.
"""
input = open(f_real, 'r').read()

def part_1_reworked(text):
    matches = re.findall(pattern, text)
    return sum([ int(x)*int(y) for x, y in matches ])

def part_2(text):
    # Remove all text between 'don't()' and ('do()' or end of line) as per the specs
    text = re.sub(r"don't\(\).*?(?:$|do\(\))", '', text, flags=re.DOTALL)
    print('part 2: ', part_1_reworked(text))

# part_1(lines)
print('Part 1 (reworked):', part_1_reworked(input))
part_2(input)