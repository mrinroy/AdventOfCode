
def find_window(in_file, window):
    with open(in_file) as file:
        line = file.readline()
        pos_dict = {}
        start = 0
        for end, c in enumerate(line):
            if c in pos_dict:
                start = max(start,pos_dict[c] + 1)
            pos_dict[c] = end
            if end - start == window - 1:
                return end + 1
            
        return -1

if __name__ == '__main__':
    print("part1: ",find_window("input.txt", 4))
    print("part2: ",find_window("input.txt", 14))
