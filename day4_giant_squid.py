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
        return score * picks[0]

# Data parsing
picks = [*map(int, data[0].split(","))]

boards = []
newboard = []
for line in data[1:]:
    if line == "\n":
        boards.append(newboard)
        newboard = []
    else:
        newboard.append(line.strip())

boards = [Bingo(board) for board in boards]

while picks:
    for board in boards:
        board.put(picks[0])
        if board.is_bingo:
            print(board.score)
            exit()
    picks.pop(0)