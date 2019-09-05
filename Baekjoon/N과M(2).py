N, M = map(int,input().split())
ans = []


def backtrack(k, n):
    if k == M:
        print(*ans)
        return

    for i in range(n, N+1):
        ans.append(i)
        backtrack(k+1, i+1)
        ans.pop()
backtrack(0, 1)