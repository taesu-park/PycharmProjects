T = int(input())

for tc in range(1, T+1):
    arr = list(map(int,input().split()))
    S = 0
    avg = 0
    count = 0
    for i in range(1, len(arr)):
        S += arr[i]
    avg = S / arr[0]
    for j in range(1, len(arr)):
        if arr[j] > avg:
            count += 1
    print('{:.3f}%'.format(count/arr[0]*100))