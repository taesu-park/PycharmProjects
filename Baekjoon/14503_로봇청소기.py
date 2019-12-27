from collections import deque
N, M = map(int,input().split())
r,c,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
clean = [[0]*M for _ in range(N)]
dx, dy = [0,1,0,-1],[-1,0,1,0]
cnt = 1

def bfs(x,y,z):
    global cnt
    Q = deque()
    Q.append((x,y,z))
    while Q:
        v, w, d = Q.popleft()
        clean[v][w] = 1
        # pprint.pprint(board)
        # pprint.pprint(clean)
        for i in range(4):
            tx, ty, td = dx[((4-d)+i)%4]+v, dy[((4-d)+i)%4]+w, (d+(3-i))%4
            if tx < 0 or tx >= N or ty < 0 or ty >= M:
                continue
            if board[tx][ty] != 1 and not clean[tx][ty]:
                Q.append((tx,ty,td))
                cnt += 1
                break
        else:
            if d == 0:
                tx, ty, td = v+1, w, d
            if d == 1:
                tx, ty, td = v, w-1, d
            if d == 2:
                tx, ty, td = v-1, w, d
            if d == 3:
                tx, ty, td = v, w+1, d
            if board[tx][ty] != 1:
                Q.append((tx,ty,td))
            else:
                break

bfs(r,c,d)
print(cnt)