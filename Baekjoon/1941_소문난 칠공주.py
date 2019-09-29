arr = [list(input()) for _ in range(5)]
visit = [[False]*5 for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
def back(x, y, l, k):
    global count
    if l == 7:
        if k >= 4:
            count += 1
        return
    else:
        for i in range(5):
            for j in range(5):
                for x in range(4):
                    tx = i + dx[x]
                    ty = j + dy[x]
                    if 0 <= tx < 5 and 0 <= ty < 5 and not visit[tx][ty]:
                        if arr[tx][ty] == 'S':
                            back(tx, ty, l+1, k+1)
                        else:
                            back(tx, ty, l+1, k)

back(0, 0)