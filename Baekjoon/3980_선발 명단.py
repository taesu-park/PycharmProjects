C = int(input())

for tc in range(1, C+1):
    arr = [list(map(int,input().split())) for _ in range(11)]
    result = 0
    arr_max = 0
    visit = [False]*11
    vvisit = [False]*11
    def back(k):
        global result, arr_max
        if k == 11:
            if arr_max < result:
                arr_max = result
            return
        for i in range(0, 11):
            if arr[k][i] == 0:
                continue
            if not visit[k] and not vvisit[i]:
                vvisit[i] = True
                visit[k] = True
                result += arr[k][i]
                back(k+1)
                result -= arr[k][i]
                visit[k] = False
                vvisit[i] = False
    back(0)
    print(arr_max)