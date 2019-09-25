N, K = map(int,input().split())
visit = [False]*100000
Min = 0xffffffff
def back(x, y):
    global Min
    m = [-1, 1, x]
    if y > Min:
        return
    if x == K:
        if x < Min:
            Min = x
        print(y)
        return
    else:
        for i in range(3):
            tx = x + m[i]
            if 0 <= tx < 100000 and not visit[tx]:
                back(tx, y+1)
back(N, 0)