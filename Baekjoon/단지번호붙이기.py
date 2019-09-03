import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = [list(sys.stdin.readline()) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
count = 0

def DFS(n,m):
    global arr_count
    visit[n][m] = 1
    arr_count += 1
    for x in range(4):
        tx, ty = n+dx[x], m+dy[x]
        if tx >= 0 and tx < N and ty >= 0 and ty < N:
            if int(visit[tx][ty]) == 0 and int(arr[tx][ty]) > 0:
                DFS(tx,ty)
result = []
for i in range(N):
    for j in range(N):
        arr_count = 0
        if int(arr[i][j]) > 0 and not visit[i][j]:
            DFS(i,j)
            count += 1
            result.append(arr_count)

result.sort()
print(count)
for t in range(count):
    print(result[t])