N, M = map(int,input().split())
ans = []
def backtrack(k):
    if k == M:
        print(*ans)
        return
    for i in range(1, N+1):
        ans.append(i)
        backtrack(k+1)
        ans.pop()
backtrack(0)