import sys
sys.stdin = open('input5.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    S = 0
    for _ in range(M):
        a, b = map(int,input().split())
        for r in range(N):
            for c in range(N):
                for k in range(N):
                    S += arr[a][k] + arr[k][b]
                    arr[a][k] = arr[k][b] = 0
    print(S)