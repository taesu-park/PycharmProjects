T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAX = 0
    ans = 0
    arr = list(map(int,input().split()))
    for i in range(N-1,-1,-1):
        if arr[i] > MAX:
            MAX = arr[i]
        else:
            ans += MAX - arr[i]
    print('#{} {}'.format(tc,ans))
