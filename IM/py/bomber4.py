import sys
sys.stdin = open('input4.txt','r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    S = 0

    for _ in range(M):
        a, b, c = map(int,input().split())

        v = a + c
        w = b + c
        if v >= N:
            v = N
        if w >= N:
            w = N
        for x in range(a, v):
            for y in range(b, w):
                print(arr[x][y], end=' ')
                S += arr[x][y]
                # arr[x][y] = 0
    print(S)
