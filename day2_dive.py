with open("data/dive.txt") as f:
    instructions = f.readlines()

# Part I
horizontal = 0
depth = 0

for i in instructions:
    cmd, num = i.split()
    num = int(num)
    if cmd == "forward":
        horizontal += num
    elif cmd == "down":
        depth += num
    elif cmd == "up":
        depth -= num

print(horizontal * depth)

# Part II
horizontal = 0
depth = 0
aim = 0

for i in instructions:
    cmd, num = i.split()
    num = int(num)
    if cmd == "down":
        aim += num
    elif cmd == "up":
        aim -= num
    elif cmd == "forward":
        horizontal += num
        depth += aim * num

print(horizontal * depth)