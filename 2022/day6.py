
def find_window(stream, window):
    char_pos = [-1]*26 # since only lowercase chars
    start = 0
    for end, c in enumerate(stream):
        ix = ord(c) - ord('a')
        if char_pos[ix] != -1:
            start = max(start,char_pos[ix] + 1)
        char_pos[ix] = end
        if end - start == window - 1:
            return end + 1
        
    return -1

if __name__ == '__main__':
    with open("input.txt") as file:
        line = file.readline()
    print("part1: ",find_window(line, 4))
    print("part2: ",find_window(line, 14))
