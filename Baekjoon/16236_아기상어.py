from collections import deque

def bfs(x,y,b):
    global ans
    q = deque()
    flag = 0
    q.append((x,y))
    body = b
    while q:
        v,w = q.popleft()
        ans += 1
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            tx, ty = v+dx,w+dy
            if tx < 0 or tx >= N or ty < 0 or ty >= N:
                continue
            else:
                if not board[tx][ty] or board[tx][ty] >= body:
                    q.append((tx,ty))
                if board[tx][ty] < body:


    if flag:
        return ans
    else:
        return 01


N = int(input())
board = [list(map(int,input().split())) for _ in  range(N)]
ans = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            bfs(i,j,2)