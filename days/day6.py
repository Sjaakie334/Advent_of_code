from utils.my_utils import get_grid_from_txt, get_txt_lines, get_txt_whole

data = get_grid_from_txt(6, example=True)
# print(data)

up = '^'
down = 'v'
left = '<'
right = '>'
hazard = '#'
visited = 'X'

outer_row = len(data) - 1
outer_col = len(data[0]) - 1

# print(data.)

def find_guard(grid):
    for row in grid:
        for cell in row:
            if cell == up:
                return (grid.index(row), row.index(cell)), up
            elif cell == down:
                return (grid.index(row), row.index(cell)), down
            elif cell == left:
                return (grid.index(row), row.index(cell)), left
            elif cell == right:
                return (grid.index(row), row.index(cell)), right

    return 'none found'

print(find_guard(data))

def count_distinct_visited(grid):
    visited_locations = []
    for row in grid:
        for cell in row:
            if cell == visited:
                visited_locations.append(cell)
    return len(visited_locations) + 2 # +2 since the check is before taking a step and count the guards current position

def check_win(grid, row, col, direction):
    if direction == up and row == 1:
        return (True, count_distinct_visited(grid))
    elif direction == down and row == outer_row -1:
        return (True, count_distinct_visited(grid))
    elif direction == left and col == 1:
        return (True, count_distinct_visited(grid))
    elif direction == right and col == outer_col - 1:
        return (True, count_distinct_visited(grid))
    else:
        return (False, 0)
        

def walk_guard(grid):
    g_pos, direction = find_guard(grid)
    # print((g_pos[0], g_pos[1]), direction)
    
    # print(grid, g_pos[0], g_pos[1], direction)
    win_check, locations = check_win(grid, g_pos[0], g_pos[1], direction)
    if win_check:
        return locations

    if direction == up:
        grid[g_pos[0]][g_pos[1]] = visited
        if grid[g_pos[0] - 2][g_pos[1]] == hazard:
            direction = right
        grid[g_pos[0] - 1][g_pos[1]] = direction
    elif direction == down:
        grid[g_pos[0]][g_pos[1]] = visited
        if grid[g_pos[0] + 2][g_pos[1]] == hazard:
            direction = left
        grid[g_pos[0] + 1][g_pos[1]] = direction
    elif direction == left:
        grid[g_pos[0]][g_pos[1]] = visited
        if grid[g_pos[0]][g_pos[1] - 2] == hazard:
            direction = up
        grid[g_pos[0]][g_pos[1] - 1] = direction
    elif direction == right:
        grid[g_pos[0]][g_pos[1]] = visited
        if grid[g_pos[0]][g_pos[1] + 2] == hazard:
            direction = down
        grid[g_pos[0]][g_pos[1] + 1] = direction

    return grid

def part_1():
    temp_grid = data
    while True:
        temp_grid = walk_guard(temp_grid)
        if type(temp_grid) == int:
            return temp_grid

print('part 1:', part_1())

def part_2():

        
    with open('./input/6_real.txt', 'r') as f:
        input_grid = f.read().split('\n')
    UP, LEFT, DOWN, RIGHT = 1, 2, 3, 4
    rows = len(input_grid)
    cols = len(input_grid[0])
    obstacles = set()
    guard_start = (0,0,UP)
    for i, r in enumerate(input_grid):
        for j, c in enumerate(r):
            if c == '#':
                obstacles.add((i,j))
            elif c == '^':
                guard_start = (i, j, UP)

    total = 0
    for r in range(rows):
        for c in range(cols):
            if (r,c) in obstacles:
                continue

            obstacles.add((r,c))
            visited_states = {guard_start}
            guard = guard_start
            while True:
                if guard[2] == UP:
                    if (guard[0] - 1, guard[1]) in obstacles:
                        guard = (guard[0], guard[1], RIGHT)
                    else:
                        guard = (guard[0] - 1, guard[1], guard[2])
                elif guard[2] == RIGHT:
                    if (guard[0], guard[1] + 1) in obstacles:
                        guard = (guard[0], guard[1], DOWN)
                    else:
                        guard = (guard[0], guard[1] + 1, guard[2])
                elif guard[2] == DOWN:
                    if (guard[0] + 1, guard[1]) in obstacles:
                        guard = (guard[0], guard[1], LEFT)
                    else:
                        guard = (guard[0] + 1, guard[1], guard[2])
                else:
                    if (guard[0], guard[1] - 1) in obstacles:
                        guard = (guard[0], guard[1], UP)
                    else:
                        guard = (guard[0], guard[1] - 1, guard[2])

                if guard[0] < 0 or guard[0] >= rows or guard[1] < 0 \
                    or guard[1] >= cols:
                    obstacles.remove((r,c))
                    break
                elif guard in visited_states:
                    total += 1
                    obstacles.remove((r,c))
                    break
                else:
                    visited_states.add(guard)
    print('part 2:', total)

part_2()