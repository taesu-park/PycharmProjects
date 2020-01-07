N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in  range(N)]
ans = 0xfffffff
home, chicken = [], []
def back(k,s,pick):
    global ans, MIN
    if k == M:
        res = 0
        for l in range(H):
            tmp = 0xffffff
            for j in pick:
                tmp = min(tmp,dis[j][l])
            res += tmp
            if res >= ans:
                return
        ans = min(ans, res)
        return
    for i in range(s, C):
        back(k+1,i+1, pick+[i])

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append((i, j))

        if board[i][j] == 1:
            home.append((i,j))
H, C = len(home), len(chicken)
dis = [[0]*H for _ in range(C)]

for i_1 in range(C):
    for j_1 in range(H):
        dis[i_1][j_1] = abs(chicken[i_1][0]-home[j_1][0]) + abs(chicken[i_1][1]-home[j_1][1])
back(0,0,[])
print(ans)

