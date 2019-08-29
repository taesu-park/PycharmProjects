import sys
sys.stdin = open('input2.txt','r')

T = int(input())
for t in range(1, T+1):
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    Smax = a = b = 0
    for i in range(N):
        for j in range(N):
            S = arr[i][j]
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                while x >= 0 and x < N and y >= 0 and y < N:
                    S += arr[x][y]
                    x = x + dx[k]
                    y = y + dy[k]
                if Smax <= S:
                    Smax = S
                    a = i
                    b = j
    print(a, b, Smax)