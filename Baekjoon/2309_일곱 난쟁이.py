arr = []
tmp = 0
for _ in range(9):
    arr.append(int(input()))

def back(n, k, p, result):
    global tmp
    if tmp == 1 or p > 100:
        return
    if k == 7 and p == 100:
        tmp = 1
        result.sort()
        for j in result:
            print(j)
        return
    else:
        for i in range(n, len(arr)):
            result.append(arr[i])
            back(i + 1 , k + 1, p + arr[i], result)
            result.pop()

back(0, 0, 0, [])
