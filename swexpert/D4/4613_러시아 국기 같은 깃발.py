def back(n):
    global tmp, ans, result
    if len(tmp) == 3:
        if sum(tmp) == N:
            result = 0
            for x in range(0, tmp[0]):
                for y in range(M):
                    if not arr[x][y] == 'W':
                        result += 1
            for x1 in range(tmp[0], tmp[0]+tmp[1]):
                for y1 in range(M):
                    if not arr[x1][y1] == 'B':
                        result += 1
            for x2 in range(tmp[0]+tmp[1], tmp[0]+tmp[1]+tmp[2]):
                for y2 in range(M):
                    if not arr[x2][y2] == 'R':
                        result += 1
            if result < ans:
                ans = result
        return
    for i in range(1, N + 1 - n):
        tmp.append(i)
        back(i + 1)
        tmp.pop()


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    result = 0
    ans = 0xffffffff
    tmp = []
    back(0)
    print('#{} {}'.format(tc,ans))