N, M = map(int,input().split())
arr = list(map(int,input().split()))
result = []
arr.sort()
def back(n):
    if len(result) == M:
        print(*result)
        return
    for i in range(n, N):
        result.append(arr[i])
        back(i+1)
        result.pop()
back(0)
