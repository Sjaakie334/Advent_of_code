from utils.my_utils import get_grid_from_txt, get_txt_lines, get_txt_whole
from itertools import product

# Prep
data = get_txt_lines(7, example=False)
data = [(int(x.split(': ')[0]), x.split(': ')[1].strip().split(' ')) for x in data]
# print(data)

operators = ['+', '*']
operators_part_2 = ['+', '*', '||']

def generate_outcomes(values, operators):
    values = [int(x) for x in values]

    outcomes = set()

    for op_combi in product(operators, repeat=len(values)-1):
        expression = values[0]
        for i, op in enumerate(op_combi):
            if op == '+':
                expression += values[i+1]
            elif op == '*':
                expression *= values[i+1]
            elif op == '||':
                expression = int(str(expression) + str(values[i+1]))

        outcomes.add(expression)
    return outcomes 

# print(generate_outcomes(data[0][1]))
# print(generate_outcomes(data[1][1]))


"""
    Part 1
        quite a fun problem, especially since I could solve it within 10 minutes.
        better than another problem *cough* *cough* day 6 part 2 *cough* *cough*
"""
def part_1():
    correct_calibrations = []
    for test, values in data:
        outcomes = generate_outcomes(values, operators)
        if test in outcomes:
            correct_calibrations.append(test)
    return sum(correct_calibrations)

print('Part 1:', part_1())

"""
    Part 2
        Easy enough to solve by tweaking the generate_outcomes function
        at first the operators were hardcoded in the functions, but with part 2 i made them into parameters
        this way i could use the function for both parts
"""
def part_2():
    correct_calibrations = []
    for test, values in data:
        outcomes = generate_outcomes(values, operators_part_2)
        if test in outcomes:
            correct_calibrations.append(test)
    return sum(correct_calibrations)

print('Part 2:', part_2())