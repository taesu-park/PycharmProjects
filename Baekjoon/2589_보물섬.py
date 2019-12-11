# from collections import deque
#
# def BFS(x, y):
#     global S
#     cnt = -1
#     visit = [[0] * W for _ in range(L)]
#     Q = deque()
#     Q.append((x, y))
#     visit[x][y] = 1
#     while Q:
#         q = len(Q)
#         cnt += 1
#         for _ in range(q):
#             x, y = Q.popleft()
#             for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                 tx, ty = x + dx, y + dy
#                 if 0 <= tx < L and 0 <= ty < W and not visit[tx][ty] and board[tx][ty] == 'L':
#                     visit[tx][ty] = 1
#                     Q.append((tx, ty))
#     return cnt
#
# L, W = map(int,input().split())
# board = [list(input()) for _ in range(L)]
# S = 0
#
# for i in range(L):
#     for j in range(W):
#         if board[i][j] == 'L':
#             m=BFS(i,j)
#             if m > S:
#                 S = m
# print(S)

from collections import deque

L, W = map(int,input().split())
board = list(list(input()) for _ in range(L))
ans = 0

def bfs(x, y):
    cnt = 0
    visit = [[0] * W for _ in range(L)]
    visit[x][y] = 1
    Q = deque()
    Q.append((x, y))
    while Q:
        q = len(Q)
        for _ in range(q):
            v, w = Q.popleft()
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                tx, ty = v+dx, w+dy
                if tx < 0 or tx >= L or ty < 0 or ty >= W:
                    continue
                if board[tx][ty] == 'L' and not visit[tx][ty]:
                    visit[tx][ty] = 1
                    Q.append((tx, ty))
        cnt += 1
    return cnt
for i in range(L):
    for j in range(W):
        if board[i][j] == 'L':
            c = bfs(i, j)
            if c > ans:
                ans = c
print(ans-1)