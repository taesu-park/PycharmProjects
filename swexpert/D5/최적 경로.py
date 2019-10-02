def back(x,y,k,s):
    global MIN
    if k > MIN:
        return
    if k == N:
        s += abs(x-arr[2])+abs(y-arr[3])
        if s < MIN:
            MIN = s
        return
    else:
        for j in range(k,len(home)):
            back(home[j][0],home[j][1],k+1,s+abs(home[j][0]-x)+abs(home[j][1]-y))




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    home = []
    tmp = []
    MIN = 0xffffffff
    for i in range(4,len(arr)):
        tmp.append(arr[i])
        if len(tmp) == 2:
            home.append(tmp)
            tmp = []
    back(arr[0],arr[1],0,0)
    print(MIN)