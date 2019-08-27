import sys
sys.stdin = open('input6.txt', 'r')

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int,input().split())
        S = arr[a][b]
        for i in range(4):
            a , b = a+dx[i], b+dy[i]
            while a >= 0 and a < a+c and b >= 0 and b < b+c:
                print(a, b, end=' ')
                S += arr[a][b]
                print(S)
                arr[a][b] = 0

                a , b = a+dx[i], b+dy[i]
    # print(S)  