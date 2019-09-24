T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    result = []
    tmp = []
    def back(n):
        global result, tmp
        if len(tmp) == N:
            result.append(tmp)
            return
        for i in range(1, N+1):
            tmp.append(i)
            back(i+1)
            tmp.pop()
    back(1)
    print(result)
