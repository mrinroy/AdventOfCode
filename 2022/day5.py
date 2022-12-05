in_file = "input.txt"

def build_stacks(in_file):
    list_read = []
    meta_lines = 0
    with open(in_file) as file:
        for line in file:
            line = line.replace('\n','')
            meta_lines += 1
            if line:
                i = 0
                if line.lstrip()[0] == "[":
                    list_read.append([])
                    
                    line_split = line.split(' ')
                    while i < len(line_split):
                        if line_split[i]:
                            list_read[-1].append(line_split[i])
                            i += 1
                        else:
                            list_read[-1].append(' ')
                            i += 4
                else:
                    # must be stack names
                    stack_count = len(line.split())

            else:
                break

    
    stacks = [[] for _ in range(stack_count)]
    list_read.reverse()
    for crates in list_read:
        for stack_ix,crate in zip(range(stack_count), crates):
            if crate != ' ':
                stacks[stack_ix].append(crate[1])

    return meta_lines, stacks

# Uptil here could easily have been done manually and the input then can just start from the move instructions
# :'(

def move_one_at_a_time(src, dest, count):
    for _ in range(count):
        dest.append(src.pop())

def move_together(src, dest, count):
    dest.extend(src[-count:])
    for _ in range(count):
        src.pop()

def part_1(in_file):
    meta_lines, stacks = build_stacks(in_file)
    cur_line = 0
    with open(in_file) as file:
        for line in file:
            cur_line += 1
            if cur_line <= meta_lines:
                continue

            line = line.rstrip()
            to_remove = ["move", "from", "to"]
            for w in to_remove:
                line = line.replace(w, "")
            (count, src, dest) = map(int,line.split())
            move_one_at_a_time(stacks[src-1], stacks[dest-1], count)

    print(''.join([crates[-1] for crates in stacks]))

def part_2(in_file):
    meta_lines, stacks = build_stacks(in_file)
    cur_line = 0
    with open(in_file) as file:
        for line in file:
            cur_line += 1
            if cur_line <= meta_lines:
                continue

            line = line.rstrip()
            to_remove = ["move", "from", "to"]
            for w in to_remove:
                line = line.replace(w, "")
            (count, src, dest) = map(int,line.split())
            move_together(stacks[src-1], stacks[dest-1], count)

    print(''.join([crates[-1] for crates in stacks]))

part_1("input.txt")
part_2("input.txt")





