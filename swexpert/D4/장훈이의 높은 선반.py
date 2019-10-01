def back(x,y):
    global MIN
    if x >= M:
        if x < MIN:
            MIN = x
        else:
            return
        return
    else:
        for i in range(y,len(arr)):
            back(x+arr[i], i+1)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    MIN = 0xfffffff
    back(0,0)
    print('#{} {}'.format(tc,MIN-M))