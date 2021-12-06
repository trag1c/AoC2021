with open("data/lanternfish.txt") as f:
    data = f.read()

lanternfish = {}
for i in map(int, data.split(",")):
    if i not in lanternfish:
        lanternfish[i] = 0
    lanternfish[i] += 1

for _ in range(256):
    nl = {}
    to_add = 0
    for k in range(9):
        if k in lanternfish:
            v = lanternfish[k]
            if not k:
                nl[8] = v
                to_add = v
            else:
                nl[k - 1] = v
    nl[6] = nl.get(6, 0) + to_add
    lanternfish = nl.copy()

print(sum(lanternfish.values()))