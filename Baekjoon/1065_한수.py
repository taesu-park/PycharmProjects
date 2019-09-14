count = 0
N = int(input())
def solution(n):
    global count
    if n <= 99:
        count += 1
        return
    else:
        arr = list(str(n))
        tmp = int(arr[0]) - int(arr[1])
        for j in range(1, len(arr)-1):
            if tmp == int(arr[j]) - int(arr[j+1]):
                count += 1
            else:
                continue
        return



for i in range(1, N+1):
    solution(i)

print(count)