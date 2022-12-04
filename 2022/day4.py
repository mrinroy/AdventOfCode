
def is_contained(pair_1, pair_2):
    range_1, range_2 = map(int, pair_1.split('-')), map(int, pair_2.split('-'))
    return range_1[0] <= range_2[0] and range_2[1] <= range_1[1] \
        or range_2[0] <= range_1[0] and range_1[1] <= range_2[1]

def overlap(pair_1, pair_2):
    range_1, range_2 = map(int, pair_1.split('-')), map(int, pair_2.split('-'))
    return range_1[0] <= range_2[0] <= range_1[1] or range_2[0] <= range_1[0] <= range_2[1]


def part1(in_file):
    ans = 0
    with open(in_file) as file:
        for line in file:
            line = line.rstrip()
            left_range, right_range = line.split(',')
            if is_contained(left_range, right_range):
                ans += 1
    return ans

def part2(in_file):
    ans = 0
    with open(in_file) as file:
        for line in file:
            line = line.rstrip()
            left_range, right_range = line.split(',')
            if overlap(left_range, right_range):
                ans += 1
    return ans

if __name__ == "__main__":
    print(part1("input.txt"))

    print(part2("input.txt"))
