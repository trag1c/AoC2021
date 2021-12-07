with open("data/the_treachery_of_whales.txt") as f:
    data = sorted([*map(int, f.read().split(","))])

center = data[len(data) // 2]

print(sum(abs(x - center) for x in data))

# Part II

center = (sum(data) / len(data)).__floor__()

print(
    sum(
        (a := abs(x - center)) * (a + 1) // 2
        for x in data
    )
)