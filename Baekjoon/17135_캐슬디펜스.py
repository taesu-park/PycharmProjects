from collections import deque

N, M, D = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0
print(board)


def bfs(pick,D):
    global ans
    visit = [[0]*M for _ in range(N)]
    enemy = []
    for i in range(3):
        archer = (N, pick[i])
        Q = deque()
        Q.append(archer)
        while Q:
            x, y = Q.popleft()
            for dx, dy in [(0,-1),(-1,0),(0,1)]:
                tx, ty = x+dx, y+dy
                if 0 > tx or tx >= N or 0 > ty or ty >= M:
                    continue
                if board[tx][ty] == 1 and (abs(x-tx)+abs(y-ty))<= D and not visit[tx][ty]:
                    enemy.append((tx,ty))
                elif board[tx][ty] == 0 and not visit[tx][ty]:
                    Q.append((tx,ty))
                visit[tx][ty] = 1
        print(enemy, archer)
def back(k,s, pick):
    if k == 3:

        bfs(pick,D)
        print('------')
        return
    else:
        for i in range(s, M):
            back(k+1, i+1, pick+[i])
back(0,0,[])
print(ans)
