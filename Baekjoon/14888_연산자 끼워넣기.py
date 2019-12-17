N = int(input())
A = list(map(int,input().split()))
arr = list(map(int,input().split()))
MAX = -0xfffffffff
MIN = 0xfffffffff
def back(k,tmp):
    global MAX, MIN
    if k == (N-1):
        if tmp > MAX:
            MAX = tmp
        if tmp < MIN:
            MIN = tmp
        return
    for i in range(4):
        if arr[i]:
            arr[i] -= 1
            if i == 0:
                back(k+1,tmp+A[k+1])
            elif i == 1:
                back(k+1,tmp-A[k+1])
            elif i == 2:
                back(k+1,tmp*A[k+1])
            elif i == 3:
                if tmp < 0:
                    back(k+1,-(abs(tmp)//A[k+1]))
                else:
                    back(k+1,tmp//A[k+1])
            arr[i] += 1


back(0,A[0])
print(MAX)
print(MIN)