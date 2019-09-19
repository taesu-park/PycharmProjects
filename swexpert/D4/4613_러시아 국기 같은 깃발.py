T = int(input())
dy = 1

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(M):