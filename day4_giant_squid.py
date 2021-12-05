with open("data/giant_squid.txt") as f:
    data = f.readlines()

class Bingo:
    def __init__(self, rows: list[str]):
        self.rows = [[*map(int, row.split())] for row in rows]
        self.picked = [[0] * 5 for _ in range(5)]
    
    def put(self, number: int):
        for i, row in enumerate(self.rows):
            if number in row:
                self.picked[i][row.index(number)] = 1
    
    @property
    def is_bingo(self) -> bool:
        return (
            any(all(row) for row in self.picked)
            or any(all(col) for col in zip(*self.picked))
        )
    
    @property
    def score(self) -> int:
        score = 0
        for i, row in enumerate(self.rows):
            for j, number in enumerate(row):
                if self.picked[i][j] == 0:
                    score += number
        return score * first

# Data parsing
picks = [*map(int, data[0].split(","))]

boards = []
newboard = []
for line in data[2:]:
    if line == "\n":
        boards.append(newboard)
        newboard = []
    else:
        newboard.append(line.strip())

# Part I
boards = [Bingo(board) for board in boards]
p1_picks = picks[:]
while p1_picks:
    first = p1_picks.pop(0)
    for board in boards:
        board.put(first)
        if board.is_bingo:
            print(board.score)
            p1_picks = []
            break

# Part II
p2_picks = picks[:]
to_delete = []
while p2_picks and boards:
    first = p2_picks.pop(0)
    for board in boards:
        board.put(first)
        if board.is_bingo:
            to_delete.append(board)
    for i in to_delete:
        boards.remove(i)
    to_delete = []

print(board.score)