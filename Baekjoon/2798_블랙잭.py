N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
a = 0
sum_max = 0


def back(n, k):
    global a, sum_max, result
    if a == 1:
        return
    if k == 3 and result < M and result > sum_max:
        sum_max = result
        return
    if k == 3:
        return
    for i in range(n, N):
        result += arr[i]
        if result == M:
            a = 1
            print(result)
        back(i + 1, k + 1)
        result -= arr[i]

back(0, 0)
if a == 0:
    print(sum_max)
