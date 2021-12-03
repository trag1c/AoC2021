with open("data/binary_diagnostic.txt") as f:
    data = f.readlines()

# Part I
arr = [{} for _ in range(12)]

for line in data:
    for i, b in enumerate(line.strip()):
        arr[i][b] = arr[i].get(b, 0) + 1

gamma_rate = "".join(
    (nd := {v: k for k, v in i.items()})[max(nd.keys())] for i in arr
)

epsilon_rate = "".join("01"[i == "0"] for i in gamma_rate)

product = int(gamma_rate, 2) * int(epsilon_rate, 2)

print(product)

# Part II