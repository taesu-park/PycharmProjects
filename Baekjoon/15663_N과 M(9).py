N, M = map(int,input().split())
arr = list(map(int,input().split()))
result = []
arr.sort()
visit = [False]*N
tmp = []
def back(n):
    global tmp
    if len(result) == M:
        tmp = result
        print(*result)
        return
    for i in range(n, N):
        result.append(arr[i])
        visit[i] = True
        back(i)
        result.pop()

back(0)