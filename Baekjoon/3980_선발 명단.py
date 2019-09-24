C = int(input())

for tc in range(1, C+1):
    arr = [list(map(int,input().split())) for _ in range(11)]
    result = 0
    arr_max = 0
    visit = [False]*11
    vvisit = [False]*11
    def back(n, m):
        global result, arr_max
        if arr_max < result:
            arr_max = result
            return
        for i in range(n, 11):
            for j in range(m, 11):
                if arr[i][j]==0:
                    continue
                if not visit[j] and not vvisit[i]:
                    vvisit[i]=True
                    visit[j]=True
                    result += arr[i][j]
                    back(i, j)
                    result -= arr[i][j]
                    visit[j] = False
                    vvisit[j]=True
    back(0, 0)
    print(arr_max)