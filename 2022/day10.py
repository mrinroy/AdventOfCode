def simulate(input_file):
    cycle = val = 1

    with open(input_file) as file:
        cycle_val = {}
        for line in file:
            line.rstrip()
            cycle_val[cycle] = val
            command = line.split()
            if command[0] == "noop":
                cycle += 1
            else:
                cycle += 2
                val += int(command[1])
    return cycle_val

def part_1(cycle_val, checks):
    ans = 0
    for check in checks:
        # if check is not there check - 1 has to be there
        ans += check * cycle_val.get(check, cycle_val.get(check - 1))
    return ans

def get_pixel(pos, cycle_val):
    i, j = pos
    ix = i*40 + j + 1
    sprite_start = cycle_val.get(ix, cycle_val.get(ix-1)) - 1
    if sprite_start <= j <= sprite_start + 2:
        return '#'
    return ' ' # space renders better readability that '.'

def part_2(cycle_val):
    grid = [['' for _ in range(40)] for _ in range(6)]
    for i in range(6):
        for j in range(40):
            grid[i][j] = get_pixel((i,j), cycle_val)
    return grid

if __name__ == "__main__":
    checks = [20, 60, 100, 140, 180, 220]

    cycle_val = simulate("input.txt")
    
    print(f"Part 1: {part_1(cycle_val, checks)}")

    grid = part_2(cycle_val)
    for row in grid:
        print ("".join(row))



