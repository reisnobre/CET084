"""."""

CARDS = [0, 1, 1, 0, 1, 0]
N = len(CARDS)

BOARD = [[0 for x in range(N)] for y in range(N)]
#
#
for i in range(N):
    BOARD[i][i] = 0
#
for u in range(1, N):
    for i in range(N - u):
        j = i + u
        print(u, i, j)
        if u % 2:
            BOARD[i][j] = max([BOARD[i + 1][j] + CARDS[i], BOARD[i][j - 1] + CARDS[j]])
        else:
            BOARD[i][j] = min([BOARD[i + 1][j], BOARD[i][j - 1]])

for line in BOARD:
    print(line)
# print(BOARD)
# # M = []
# #
# # for card in CARDS:
