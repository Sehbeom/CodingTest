board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
for b in board:
    print(b)
cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
print(cols)
