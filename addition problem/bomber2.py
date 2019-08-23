import sys
sys.stdin = open('input2.txt','r')

T = int(input())
for t in range(1, T+1):
            # x = 행, y = 열
    dx = [-1, -1, 1, 1] # 좌상단, 우상단, 좌하단, 우하단
    dy = [-1, 1, -1, 1]
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    maxS = a = b = 0
    for r in range(N):
        for c in range(N):
            # 네방향에 대해서 자료를 읽는다.
            S = arr[r][c]
            for i in range(4):
                x, y = r + dx[i], c+ dy[i]
                while x >= 0 and x < N and y >= 0 and y < N:
                    S += arr[x][y]
                    x, y = x + dx[i] , y + dy[i]
            if S >= maxS:
                maxS = S
                a = r
                b = c
    print(maxS, a, b)