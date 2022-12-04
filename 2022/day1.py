import heapq


INPUT_FILE = "input.txt"

elves = []

cur = 0
with open(INPUT_FILE) as file:
    for line in file:
        line = line.rstrip()
        if not line:
            heapq.heappush(elves, -cur)
            cur = 0
        else:
            cur += int(line)
    heapq.heappush(elves, -cur)

print (-elves[0])

ans = 0
for _ in range(3):
    ans += (-heapq.heappop(elves))
print(ans)
