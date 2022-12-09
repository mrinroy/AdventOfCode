def get_grid(in_file):
    grid = []
    with open(in_file) as file:
        for line in file:
            line = line.rstrip()
            grid.append(list(map(int,line)))
    return grid


def find_visible(grid):
    visibility_grid = [[False for _ in range(len(grid[row]))] for row in range(len(grid))]
    for i in range(len(grid)):
        visibility_grid[i][0] = visibility_grid[i][-1] = True
    for j in range(len(grid[0])):
        visibility_grid[0][j] = visibility_grid[-1][j] = True
    
    def update_visibility(grid, visibility_grid, right_bottom = False):
        row_generator = range(1,len(grid)-1) if not right_bottom else range(len(grid)-2, 0, -1)
        col_generator = range(1,len(grid[0])) if not right_bottom else range(len(grid[0])-2, 0, -1)
        prev = -1 if right_bottom else 1
        max_grid = [[v for v in row] for row in grid]
        for i in row_generator:
            row_max = grid[i][0] if not right_bottom else grid[i][-1]
            for j in col_generator:
                visibility_grid[i][j] = visibility_grid[i][j] or grid[i][j] > min(max_grid[i - prev][j], row_max)
                max_grid[i][j] = max(max_grid[i-prev][j], grid[i][j])
                row_max = max(row_max, grid[i][j])
    
    update_visibility(grid, visibility_grid)
    update_visibility(grid, visibility_grid, True)

    return visibility_grid

def get_scenic_scores(grid):

    def _get_score(visible_stack, row, col):
        height = grid[row][col]
        while visible_stack[-1][0] > 0 and visible_stack[-1][0] < len(grid)-1\
            and visible_stack[-1][1] > 0 and visible_stack[-1][1] < len(grid[0]) - 1:
            i,j = visible_stack[-1]
            if height > grid[i][j]:
                visible_stack.pop()
            else:
                break
        score = max(abs(visible_stack[-1][0] - row), abs(visible_stack[-1][1] - col))
        visible_stack.append((row,col))
        return score
        
    
    score_grid = [[1 for _ in range(len(grid[row]))] for row in range(len(grid))]
    for i in range(len(grid)):
        score_grid[i][0] = score_grid[i][-1] = 0
    for j in range(len(grid[0])):
        score_grid[0][j] = score_grid[-1][j] = 0
    
    
    

    # populate score and distance from bottom right
    #MONOTONIC STACKS
    col_stacks = [[(len(grid)-1, j)] for j in range(len(grid[0]))]
    for row in range(len(grid) - 2, -1, -1):
        row_stack = [(row,len(grid[row])-1)]
        for col in range(len(grid[row]) - 2, 0, -1):
            row_dist = _get_score(row_stack, row, col)
            col_dist = _get_score(col_stacks[col], row, col)
            #print(f"\t ({row},{col}) -> row: {row_dist}, col: {col_dist}")
            score_grid[row][col] *= (row_dist * col_dist)
    
    # populate score and distance from top left
    col_stacks = [[(0, j)] for j in range(len(grid[0]))]
    for row in range(1, len(grid)):
        row_stack = [(row,0)]
        for col in range(1, len(grid[row]) - 1):
            row_dist = _get_score(row_stack, row, col)
            col_dist = _get_score(col_stacks[col], row, col)
            # print(f"\t ({row},{col}) -> row: {row_dist}, col: {col_dist}")
            score_grid[row][col] *= (row_dist * col_dist)
    
    return score_grid
    

if __name__ == "__main__":
    grid = get_grid("input.txt")
    visibility_grid = find_visible(grid)
    count_visible = sum(sum(visibility_grid,[]))
    print(f"Visible trees: {count_visible}")

    scenic_scores = get_scenic_scores(grid)
    max_score = max(map(max,scenic_scores))
    print(f"max scenic score: {max_score}")

    


        
    
