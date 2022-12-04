

score = 0
with open("input.txt") as file:

    for line in file:
        line = line.rstrip()

        comp_1 = set(line[:len(line)//2])
        comp_2 = set(line[len(line)//2:])
        common = list(comp_1.intersection(comp_2))[0]
        priority = ord(common) - ord('a') if common.islower() else ord(common) - ord('A') + 26
        score += priority + 1
print(score)


score = 0
counter = 1
with open("input.txt") as file:
    for line in file:
        line = line.rstrip()
        if counter % 3 == 1:
            badge = set(line)
        else:
            badge = badge.intersection(set(line))
        
        if counter % 3 == 0:
            common = list(badge)[0]
            priority = (ord(common) - ord('a') if common.islower() else ord(common) - ord('A') + 26) + 1
            score += priority
            
        counter += 1
        

print(score)


