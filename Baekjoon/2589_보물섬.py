from collections import deque
import sys
def BFS(x, y):
    global S
    cnt = -1
    visit = [[0] * W for _ in range(L)]
    Q = deque()
    Q.append((x, y))
    visit[x][y] = 1
    while Q:
        q = len(Q)
        cnt += 1
        for _ in range(q):
            x, y = Q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tx, ty = x + dx, y + dy
                if 0 <= tx < L and 0 <= ty < W and not visit[tx][ty] and board[tx][ty] == 'L':
                    visit[tx][ty] = 1
                    Q.append((tx, ty))
    return cnt

L, W = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(L)]
S = 0

for i in range(L):
    for j in range(W):
        if board[i][j] == 'L':
            m=BFS(i,j)
            if m > S:
                S = m
print(S)