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

print(f"Gamma rate: {gamma_rate} ({int(gamma_rate, 2)})")
print(f"Epsilon rate: {epsilon_rate} ({int(epsilon_rate, 2)})")
print(f"Product: {product}")

# Part II
to_delete = []
for i in range(12):
    nd = {v: k for k, v in arr[i].items()}
    mostpop = nd[max(nd.keys())]
    for line in data:
        if line[i] != mostpop:
            to_delete.append(line)

o2 = [i for i in data if i not in to_delete][0].strip()

to_delete = []
for i in range(12):
    nd = {v: k for k, v in arr[i].items()}
    leastpop = nd[min(nd.keys())]
    for line in data:
        if line[i] != leastpop:
            to_delete.append(line)

co2 = [i for i in data if i not in to_delete]

print(f"O2: {o2} ({int(o2, 2)})")
print(f"CO2: {co2}")#" ({int(co2, 2)})")