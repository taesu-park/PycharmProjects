T = int(input())

def back(n):
    global arr_sum, count, visit
    if arr_sum == K:
        count += 1
        return
    for i in range(n, N+1):
        if not visit[i]:
            arr_sum += arr[i-1]
            visit[i] = True
            back(i+1)
            arr_sum -= arr[i-1]
            visit[i] = False

for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    visit = [False]*(N+1)
    count = 0
    arr_sum = 0
    back(1)
    print('#{} {}'.format(tc,count))

