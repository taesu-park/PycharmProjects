from collections import deque
import pprint
def bfs(x,y,k):
    global ans
    Q = deque()
    Q.append((x,y,k))
    dist[0][0][0] = 1
    while Q:
        v, w, z = Q.popleft()
        # pprint.pprint(dist)
        if v == N-1 and w == M-1:
            return dist[v][w][z]
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            tx, ty = v+dx, w+dy
            if tx < 0 or tx >= N or ty < 0 or ty >= M:
                continue
            if dist[tx][ty][z]:
                continue
            if board[tx][ty] == '0':
                dist[tx][ty][z] = dist[v][w][z] + 1
                Q.append((tx,ty,z))
            if board[tx][ty] == '1' and z == 0:
                dist[tx][ty][1] = dist[v][w][z] + 1
                Q.append((tx,ty,1))
    return -1

N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]
dist = [[[0, 0] for _ in range(M)] for _ in range(N)]
print(bfs(0,0,0))
