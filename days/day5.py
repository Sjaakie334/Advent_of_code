from utils.my_utils import get_grid_from_txt, get_txt_lines, get_txt_whole
from collections import defaultdict
import functools

data = get_txt_whole(5)
# print(data)

"""
    Day 5:
        Looking on the advent of code reddit of how others solved previous days, i came across functools and cmp_to_key.
        Today i tried using it after reading some documentation. I would say it went pretty well.
"""
def day5(s, part2=False):
    p1, p2 = s.split('\n\n')
    rules = [tuple(line.split('|')) for line in p1.splitlines()]
    updates = (line.split(',') for line in p2.splitlines())

    compare = lambda a, b: -1 if (a, b) in rules else 1 if (b, a) in rules else 0

    total = 0
    for update in updates:
        new = sorted(update, key=functools.cmp_to_key(compare))
        if (new == update) ^ part2:
            total += int(new[len(new) // 2])
      
    return total

print('part 1:', day5(data))
print('part 2:', day5(data, True))