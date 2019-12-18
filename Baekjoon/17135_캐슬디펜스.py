from collections import deque

N, M, D = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0
print(board)

def bfs(pick,D):
    global ans
    cnt = 0
    Q = deque()
    for i in range(3):
        Q.append((pick[i],N))
    q = len(Q)
    print(Q)
    for x in range(N):
        for i in range(q):
            v, w = Q[i][0], Q[i][1]-x
            print(v, w)
            for dx, dy in [(-1, 0), (0, -1), (0, 1)]:
                tx, ty = v+dx, w+dy
                if tx < 0 or tx >= N-x or ty < 0 or ty >= N-x:
                    continue
                if board[tx][ty] == 1 and (abs(v-tx)+abs(w-ty)) <= D:
                    board[tx][ty] = 0
                    cnt += 1
            D += 1
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