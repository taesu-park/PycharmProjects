L, C = map(int,input().split())
arr = list(input().split())
visit = [False for _ in range(L+1)]
arr.sort()
print(arr)
ans = []
def DFS(n):
    S = []
    S.append(n)
    visit[n] = True
    for i in range(len(arr)):
        if not visit[i] and len(S) < 4:
            DFS(i)
    if len(S) == 4:
        ans += S
        S = []
DFS(arr[0])
print(visit)