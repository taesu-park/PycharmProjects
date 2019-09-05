import sys
N, M = map(int, sys.stdin.readline().split())
used = [0]*(N+1)
ans = []

def backtrack(start):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(1, N+1):
        if not used[i]:
            used[i] = 1
            ans.append(i)
            backtrack(i)
            ans.pop()
            used[i] = 0

backtrack(1)