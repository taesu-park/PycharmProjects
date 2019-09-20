N, M = map(int,input().split())
result = []
def back(n):
    if len(result) == M:
        print(*result)
        return
    for i in range(n, N+1):
        result.append(i)
        back(i)
        result.pop()
back(1)