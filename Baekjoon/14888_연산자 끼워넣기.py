N = int(input())
A = [list(map(int,input().split()))]
arr = [list(map(int,input().split()))]
ans = 0


def back(n,k):
    if k == N:
        return
    for i in range(N):
        back(arr[i],k+1)

back(0,0)