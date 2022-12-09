def _get_next_point(head, tail):
    move = min(1, abs(head - tail))
    if head < tail:
        move = -1 * move
    return tail + move

def _get_tail(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail
    if max(abs(head_x - tail_x), abs(head_y - tail_y)) == 2:
        # need to move
        tail_x, tail_y = _get_next_point(head_x, tail_x), _get_next_point(head_y,tail_y)
    return (tail_x, tail_y)
    

def part_1(input):
    head, tail = ((0,0),(0,0))
    points_visited = set([tail])
    delta = {'R': (0,1), 'D': (1,0), 'L': (0,-1), 'U':(-1,0)}

    with open(input) as file:
        for line in file:
            direction, count = line.split()
            count = int(count.rstrip())
            x,y = delta[direction]
            for _ in range(count):
                head = (head[0] + x, head[1] + y)
                tail = _get_tail(head, tail)
                points_visited.add(tail)
    
    return len(points_visited)

def part_2(input):
    points = [(0,0)] * 10
    points_visited = set([(0,0)])
    delta = {'R': (0,1), 'D': (1,0), 'L': (0,-1), 'U':(-1,0)}

    with open(input) as file:
        for line in file:
            direction, count = line.split()
            count = int(count.rstrip())
            x,y = delta[direction]
            for _ in range(count):
                points[0] = (points[0][0] + x, points[0][1] + y)
                for i in range(1,10):
                    points[i] = _get_tail(points[i-1], points[i])
                points_visited.add(points[9])
    
    return len(points_visited)

if __name__ == "__main__":
    in_file = "input.txt"
    print(f" Part 1: {part_1(in_file)}")
    print(f" Part 2: {part_2(in_file)}")
