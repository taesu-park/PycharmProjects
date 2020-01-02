from collections import deque

def bfs(x,y,k):
    global ans
    Q = deque()
    Q.append((x,y))
    cnt = 1
    while Q:
        cnt += 1
        v, w = Q.popleft()
        if v == N and w == M:
            ans = min(ans,cnt)
            break
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            tx, ty = v+dx, w+dy
            if tx < 0 or tx >= N or ty < 0 or ty >= M:
                continue
            if board[tx][ty] == 0 and not visit[[tx][ty]] and not destroy[tx][ty]:
                Q.append((tx,ty))
                visit[tx][ty] = 1
            if k and board[tx][ty] == 1 and not visit[tx][ty] and not destroy[tx][ty]:
                Q.append((tx,ty))
                visit[tx][ty] = 1
                destroy[tx][ty] = 1
                k -= 1


N, M = map(int,input().split())
board = list(map(int,input().split()) for _ in range(N))
visit = [[0]*M for _ in range(N)]
destroy = [[0]*M for _ in range(N)]
ans = 0
bfs(0,0,1)
print(ans) if ans else print(-1)