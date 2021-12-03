with open("data/solar_sweep.txt") as file:
    data = [*map(int, file.readlines())]

# Part I
increments = sum(line > data[i] for i, line in enumerate(data[1:]))
print(increments)

# Part II
sums = [sum(data[i:i + 3]) for i in range(len(data) - 2)]
increments = sum(line > sums[i] for i, line in enumerate(sums[1:]))
print(increments)