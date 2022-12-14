import functools


def parse_packet(packet):
    # add splitters
    packet = packet.replace("[","[,")
    packet = packet.replace("]",",]")
    stack = []
    for c in packet.split(","):
        
        if not c:
            # duplicate splitter
            continue

        if c != ']':
            stack.append(c)
        else:
            lst = []
            popped = stack.pop()
            while popped != '[':
                lst.append(popped)
                popped = stack.pop()
            stack.append(lst[::-1])
    return stack.pop()

def get_packets(in_file):
    with open(in_file) as file:
        lines = file.read()
        pairs = lines.split("\n\n")
        packets = []
        for pair in pairs:
            left, right = pair.split("\n")
            parsed_left, parsed_right = parse_packet(left), parse_packet(right)
            packets.append((parsed_left, parsed_right))
    return packets

def compare_lists(left, right):
    for i,l_val in enumerate(left):
        if i == len(right):
            # Right exhausted
            return 1
        r_val = right[i]
        if type(r_val) == type(l_val):
            # both are lists
            if type(r_val) == list:
                is_ok = compare_lists(l_val, r_val)
                if is_ok == 0:
                    continue
                return is_ok
                
            else:
                # both are numbers
                if int(r_val) == int(l_val):
                    continue
                return -1 if int(l_val) < int(r_val) else 1
        else:
            # one is a list other isnt
            if type(r_val) == list:
                l_val = [l_val]
            else:
                r_val = [r_val]
            is_ok = compare_lists(l_val, r_val)
            if is_ok == 0:
                continue
            return is_ok
    return 0 if len(left) == len(right) else -1


if __name__ == "__main__":
    
    packet_pairs = get_packets("input.txt")
    ans = 0
    for i,(left, right) in enumerate(packet_pairs):
        if compare_lists(left, right) == -1:
            ans += (i+1)
    print (f"Part 1: {ans}")

    # part 2
    divider_packets = [[['2']], [['6']]]
    packets = []
    for pair in packet_pairs:
        packets.append(pair[0])
        packets.append(pair[1])
    packets.extend(divider_packets)
    packets.sort(key=functools.cmp_to_key(compare_lists))
    # list can not be searched
    hashable_packets = list(map(tuple, packets))
    pos_1 = hashable_packets.index(tuple(divider_packets[0])) + 1
    pos_2 = hashable_packets.index(tuple(divider_packets[1])) + 1

    print(f"Part 2: {pos_1 * pos_2}")
    



