def back(x,y,k):
    global MIN
    if y < 0 or k >= MIN:
        return
    if x >= K:
        if k < MIN:
            MIN = k
        return
    else:
        back(x+1,arr[x]-1,k+1)
        back(x+1,y-1,k)
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int,input().split()))
    K = arr[0]
    MIN = 0xffffffff
    back(2,arr[1]-1,0)
    print('#{} {}'.format(tc,MIN))