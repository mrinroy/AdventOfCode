def parse(in_file: str, blocked: set):
    max_y = 0
    with open(in_file) as file:
        for line in file:
            line = line.rstrip()
            points = line.split(" -> ")
            for i in range(1, len(points)):
                prev_x, prev_y = map(int,points[i-1].split(","))
                x, y = map(int, points[i].split(","))
                max_y = max(max_y, y)
                if x < prev_x:
                    x, prev_x = prev_x, x
                for p_x in range(prev_x, x + 1):
                    blocked.add((p_x, y))
                if y < prev_y:
                    y, prev_y = prev_y, y
                for p_y in range(prev_y, y+1):
                    blocked.add((x, p_y))
    return max_y


def place_sand(stack: list, max_y: int, blocked: set, floor):
    # stacks helps in jumping to last placed sand
    x,y = stack[-1]
    # go to bottom
    if (x, y+1) not in blocked and y + 1 < floor:
        # this will preserve the orig as this is going to be wiped off
        stack.append((x,y))
        while (x,y+1) not in blocked and y < floor-1:
            y += 1
            stack.pop()
            stack.append((x,y))

    if y >= max_y:
        print(f"Found the hole")
        return True
    
    if (x,y) == (500,-1):
        print("reached source")
        return True
    
    if not (x-1,y+1) in blocked and y + 1 < floor :
        stack.append((x-1,y+1))
        return place_sand(stack, max_y, blocked, floor)
    if not (x+1,y+1) in blocked and y + 1 < floor:
        stack.append((x+1, y+1))
        return place_sand(stack, max_y, blocked, floor)
    if ((x,y+1) in blocked and (x-1,y+1) in blocked and (x+1,y+1) in blocked) or y + 1 == floor:
        # sand will be placed here
        blocked.add((x,y))
        stack.pop()
        return False
    

def get_count_to_leak(start: tuple, max_y: int, blocked: set, floor: int):
    stack = [start]
    count = 0
    while not place_sand(stack, max_y, blocked, floor):
        count += 1
    return count

if __name__ == "__main__":
    blocked = set()
    max_y = parse("input.txt", blocked)
    count_to_hole = get_count_to_leak((500,-1), max_y, blocked, max_y + 2)
    print(f"Part 1: {count_to_hole}")

    # already filled by part 1
    # increase the max_y so that sand reaches floor
    remaining_to_source = get_count_to_leak((500,-1), max_y+5, blocked, max_y + 2)
    print(f"Part 2: {count_to_hole + remaining_to_source}")







