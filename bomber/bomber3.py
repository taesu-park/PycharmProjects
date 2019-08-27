import sys
sys.stdin = open('input3.txt','r')


T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    Smax = a = b = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            S = 0
            for x in range(r, r+M):
                for y in range(c, c+M):
                    S += arr[x][y]
            for i in range(r+1, r+M-1):
                for j in range(c+1, c+M-1):
                    S -= arr[i][j]
            if S >= Smax:
                Smax = S
                a, b = r, c
    print(Smax, a, b)