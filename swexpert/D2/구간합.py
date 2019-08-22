T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    arr_sum = 0
    arr_max = 0
    arr_min = 100000000
    for i in range(N-M+1):
        arr_sum = 0
        for j in range(M):
            arr_sum += arr[i+j]
        if arr_sum >= arr_max:
            arr_max = arr_sum
        if arr_sum <= arr_min:
            arr_min = arr_sum
    print(arr_max - arr_min)