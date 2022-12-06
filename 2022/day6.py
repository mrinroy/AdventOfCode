
def find_window(in_file, window):
    with open(in_file) as file:
        line = file.readline()
        char_pos = [-1]*26 # since only lowercase chars
        pos_dict = {}
        start = 0
        for end, c in enumerate(line):
            ix = ord(c) - ord('a')
            if char_pos[ix] != -1:
                start = max(start,char_pos[ix] + 1)
            char_pos[ix] = end
            if end - start == window - 1:
                return end + 1
            
        return -1

if __name__ == '__main__':
    print("part1: ",find_window("input.txt", 4))
    print("part2: ",find_window("input.txt", 14))
