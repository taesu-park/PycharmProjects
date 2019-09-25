arr = [list(map(int,input().split())) for _ in range(5)]
visit = [[False]*5 for _ in range(5)]
ans = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def back(x,y,result):
    if len(result) == 6:
        ans.append(result)
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < 5 and 0 <= ty < 5:
                back(tx, ty, result + str(arr[tx][ty]))
for i in range(5):
    for j in range(5):
        back(i, j, '')
a = set(ans)
print(len(a))