N, M = map(int,input().split())
arr = list(map(int,input().split()))
visit = [False]*N
result = []
arr.sort()
def back(n):
    global result, visit
    if len(result) == M:
        print(*result)
        return
    for i in range(N):
        if not visit[i]:
            result.append(arr[i])
            visit[i] = True
            back(i+1)
            result.pop()
            visit[i] = False

back(0)
