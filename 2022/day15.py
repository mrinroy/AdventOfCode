from collections import defaultdict, deque


def parse(in_file):
    to_replace = set([
        "Sensor at ",
        "x=",
        "y=",
        " closest beacon is at "
    ])
    sernsor_nearest_beacon = {}
    with open(in_file) as file:
        for line in file:
            line = line.rstrip()
            for key in to_replace:
                line = line.replace(key, "")
            sensor, beacon = line.split(':')
            sensor_x, sensor_y = map(int, sensor.split(','))
            beacon_x, beacon_y = map(int, beacon.split(','))
            sernsor_nearest_beacon[(sensor_x, sensor_y)] = (beacon_x, beacon_y)
    return sernsor_nearest_beacon




def affected_points_in_axis(sensor, beacon, y_axis, affected_set):
    start_x, end_x = affected_range_in_axis(sensor, beacon, y_axis)
    for x in range(start_x, end_x + 1):
        affected_set.add((x,y_axis))

def affected_range_in_axis(sensor, beacon, y_point):
    dist = abs(sensor[0] - beacon[0]) + abs (sensor[1] - beacon[1])
    axis_diff = abs(y_point - sensor[1])
    if axis_diff > dist:
        # won't be affected
        return (-1,-1)
    return ((sensor[0] - (dist - axis_diff), sensor[0] + (dist - axis_diff)))
    

def block_points(sensor, beacon, y_dict, limit, candidates):
    dist = abs(sensor[0] - beacon[0]) + abs (sensor[1] - beacon[1])
    for y in range(sensor[1] - dist, sensor[1] + dist + 1):
        if y < 0 or y > limit:
            continue
        if y_dict[y].no_point_left():
            continue
        block_range = affected_range_in_axis(sensor, beacon, y) 
        y_dict[y].block(block_range)
        if y_dict[y].no_point_left() and y in candidates:
            del candidates[y]
        check, val = y_dict[y].single_point_left()
        if check:
            candidates[y] = val
        
def part_1(sensor_beacon, y_axis):
    affected_set = set()
    axis_sensor, axis_beacon = set(), set()
    for sensor, beacon in sensor_beacon.items():
        if sensor[1] == y_axis:
            axis_sensor.add(sensor)
        if beacon[1] == y_axis:
            axis_beacon.add(beacon)
        affected_points_in_axis(sensor, beacon, y_axis, affected_set)
    # remove the existing sensors and beacons
    affected_set.difference_update(axis_sensor)
    affected_set.difference_update(axis_beacon)
    
    print(f" Part 1 : {len(affected_set)}")

def part_2(sensor_beacon, limit):

    class Y_Axis:
        def __init__(self):
            self.open_blocks = [(0,limit)]
        
        def no_point_left(self):
            return len(self.open_blocks) == 0
        
        def single_point_left(self):
            if len(self.open_blocks) == 1 and self.open_blocks[0][1] - self.open_blocks[0][0] == 0:
                return True, self.open_blocks[0][0]
            return False,(-1,-1)
        
        def block(self, interval):
            res = []
            i = 0
            while i < len(self.open_blocks) and self.open_blocks[i][1] < interval[0]:
                res.append(self.open_blocks[i])
                i += 1
            # may be bisect above
            if i < len(self.open_blocks) and self.open_blocks[i][0] < interval[0]:
                res.append((self.open_blocks[i][0], interval[0] - 1))
            while i < len(self.open_blocks) and interval[1] >= self.open_blocks[i][1]:
                i += 1
            if i < len(self.open_blocks):
                res.append((max(interval[1] + 1, self.open_blocks[i][0]), self.open_blocks[i][1])) 
            res.extend(self.open_blocks[i+1:])

            self.open_blocks = res
    
    y_dict = defaultdict(Y_Axis)

    candidates = {}

    for sensor, beacon in sensor_beacon.items():
        block_points(sensor, beacon, y_dict, limit, candidates)
    
    assert 1, len(candidates)

    for y,x in candidates.items():
        print(f"Part 2: {x * 4000000 + y}")

if __name__ == "__main__":
    sensor_beacon = parse("input.txt")

    part_1(sensor_beacon, 2000000)

    part_2(sensor_beacon, 4000000)
    

    

