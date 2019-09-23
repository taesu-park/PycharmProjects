T = int(input())

def back(n):
    print(n)
    global arr_sum, count, visit
    if arr_sum == K:
        count += 1
        return
    for i in range(n, N):
        if not visit[n]:
            arr_sum += arr[i]
            visit[n] = True
            back(i)
            arr_sum -= arr[i]
            visit[i] = False

for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    visit = [False]*N
    count = 0
    arr_sum = 0
    back(0)
    # print(count)

