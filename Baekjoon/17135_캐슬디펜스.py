from collections import deque

N, M, D = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0
print(board)

def bfs(pick,D):
    global ans
    enemy = set()
    Q = deque()
    for i in range(3):
        Q.append((N, pick[i]))

    while Q:
        for x in range(N):
            cnt = 0
            Q = deque()
            for i in range(3):
                Q.append((N, pick[i]))
            q = len(Q)
            for i in range(q):
                a = 0
                v, w = Q.popleft()

                for c in range(D):
                    if a:
                        break
                    for dx, dy in [(0, -1-c), (-1-c,0), (0, 1+c)]:
                        tx, ty = v+dx, w+dy
                        if tx < 0 or tx >= N-x or ty < 0 or ty >= N-x:
                            continue
                        if board[tx][ty] == 1:
                            enemy.add((tx,ty))
                            a = 1
                            print(enemy)
                            break
                        else:
                            Q.append((tx,ty))
            for x,y in enemy:
                cnt += 1
                board[x][y] = 0
        ans = max(ans, cnt)
def back(k,s, pick):
    if k == 3:
        bfs(pick,D)
        return
    else:
        for i in range(s, M):
            back(k+1, i+1, pick+[i])
back(0,0,[])
print(ans)