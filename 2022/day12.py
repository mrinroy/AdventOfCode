from collections import deque


def parse(in_file):
    grid = []
    with open(in_file) as file:
        for i,line in enumerate(file):
            line = line.rstrip()
            grid.append([])
            for j, val in enumerate(line):
                if val == 'S':
                    src = (i,j)
                    grid[-1].append('a')
                elif val == 'E':
                    dest = (i,j)
                    grid[-1].append('z')
                else:
                    grid[-1].append(val)
    return grid, src, dest

def _bfs(grid, src, dst, to_min = False):
    # for part 2 just go in reverse
    visited = set()
    steps = 0
    if to_min:
        src = dst
    dir = -1 if to_min else 1
    queue = deque([(src)])
    while queue:
        for _ in range(len(queue)):
            i,j = queue.popleft()
            if (i,j) in visited:
                continue
            if (not to_min and (i,j) == dst) or (to_min and grid[i][j] == 'a'):
                return steps
            for x,y in [(-1,0),(0,1),(1,0),(0,-1)]:
                new_i, new_j = i + x, j + y
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[i]):
                    if (ord(grid[new_i][new_j]) - ord(grid[i][j])) * dir <= 1:
                        queue.append((new_i, new_j))
            visited.add((i,j))
        steps += 1
    return -1

if __name__ == "__main__":
    grid, src, dst = parse("input.txt")
    print(_bfs(grid, src, dst))

    print(_bfs(grid,src, dst, to_min= True))
            
