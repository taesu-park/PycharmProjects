T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    S = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    s+= arr[x][y]
                    S.append(s)
    print('#{} {}'.format(tc, max(S)))