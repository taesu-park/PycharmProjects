### DFS

N = int(input())
visit = [[False] * (N) for _ in range(N)]
arr = [list(input()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr_count = total_count = 0
result = []


def DFS(n, m):
    global arr_count

    for x in range(4):
        tx = n + dx[x]
        ty = m + dy[x]
        if tx >= 0 and tx < N and ty >= 0 and ty < N and arr[tx][ty] == '1' and not visit[tx][ty]:
            visit[tx][ty] = True
            DFS(tx, ty)
            arr_count += 1


for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visit[i][j]:
            arr_count = 1
            visit[i][j] = True
            DFS(i, j)
            result.append(arr_count)
            total_count += 1
result.sort()
print(total_count)
for a in result:
    print(a)

### BFS
from collections import deque

def bfs(x,y):
    global cnt, ans
    visit[x][y] = 1
    Q = deque()
    Q.append((x,y))
    while Q:
        v,w = Q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            tx, ty = v + dx, w + dy
            if tx < 0 or tx >= N or ty < 0 or ty >= N:
                continue
            if not visit[tx][ty] and int(board[tx][ty])==1:
                visit[tx][ty] = 1
                Q.append((tx,ty))
        cnt += 1
    return cnt
N = int(input())
board = [list(input()) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
ans = 0
result = []

for i in range(N):
    for j in range(N):
        if int(board[i][j]) == 1 and not visit[i][j]:
            cnt = 0
            result.append(bfs(i,j))
            ans += 1
print(ans)
result.sort()
for a in range(len(result)):
    print(result[a])