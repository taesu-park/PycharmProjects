from collections import deque

N, M = map(int,input().split())
r,c,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dx, dy = [0,-1,0,1],[-1,0,1,0]

def bfs(x,y,d):
    Q = deque()
    Q.append((x,y))
    while Q:
        v, w = Q.popleft()
        for a in range(4):
            tx, ty = v+dx[(a+d)%4], w+dy[(a+d)%4]
            if board[tx][ty] == 0:
                Q.append((tx, ty))
                

bfs(r,c,d)