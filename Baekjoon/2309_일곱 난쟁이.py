arr = []
arr_sum = 0
tmp = 0
result = []
for _ in range(9):
    arr.append(int(input()))

def back(n, k):
    global arr_sum, arr, tmp, result
    if k == 7 and arr_sum == 100:
        tmp = 1
        return
    for i in range(n, len(arr)):
        if arr_sum > 100 or tmp == 1:
            continue
        result.append(arr[i])
        arr_sum += arr[i]
        back(i + 1 , k + 1)
        if tmp == 1:
            break
        arr_sum -= arr[i]
        result.pop()


back(0, 0)
result.sort()
for j in result:
    print(j)