n, m = map(int, input().split())
board = [[0 for j in range(n)] for i in range(n)]
count = 0
qxy = []
move = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
for i in range(m):
    xy = list(map(int, input().split()))
    xy[0] -= 1
    xy[1] -= 1
    qxy.append(xy)

for i in range(len(qxy)):
    for xy in move:
        for j in range(0, n+1, 1):
            if (0 <= qxy[i][0] + xy[0]*j < n) and (0 <= qxy[i][1] + xy[1]*j < n):
                board[qxy[i][0] + xy[0]*j][qxy[i][1] + xy[1]*j] = -1

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] != -1:
            count += 1
