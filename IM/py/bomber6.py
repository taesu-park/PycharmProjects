import sys
sys.stdin = open('input6.txt', 'r')

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for t in range(1, T+1):
    # print(t, end= ' ')
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    S = 0
    for _ in range(M):
        a, b, c = map(int,input().split())
        # print('>',a,b)
        S += arr[a][b]
        arr[a][b] = 0
        for i in range(4):

            tx , ty = a+dx[i], b+dy[i]

            while tx >= max(0, a-c) and tx < min(a+c+1,N) and ty >= max(0, b-c) and ty < min(b+c+1,N):

                # print(tx, ty)
                S += arr[tx][ty]

                arr[tx][ty] = 0

                tx , ty = tx+dx[i], ty+dy[i]

    print(S)