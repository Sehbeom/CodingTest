# 2022.08.23
# 백준 / 9663번 블랙잭

# def putQueens(x, y, board):
#     # diag = {'lt': True, 'lb': True, 'rb': True, 'rt': True}
#     diag = ['lt', 'lb', 'rb', 'rt']

#     for i in range(N):
#         board[y][i] = False
#         board[i][x] = False

#     while diag:


def putQueens(pos, board):

    for b in board:
        if b % N == pos % N:
            board[b] = False

        if b//N == pos//N:
            board[b] = False

        if b % (N+1) == pos % (N+1):
            board[b] = False

        if b % (N-1) == pos % (N-1):
            board[b] = False


N = int(input())
# board = [[True]*N for i in range(N)]
board = {i: True for i in range(N*N)}

visited = {i: [] for i in range(N*N)}

putQueens(0, board)
for i in range(N*N):
    print(board[i], end=" ")
    if i % N == (N-1):
        print("\n")

# for i in range(N):
#     for j in range(N):
