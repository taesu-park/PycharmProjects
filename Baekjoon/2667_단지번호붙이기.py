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