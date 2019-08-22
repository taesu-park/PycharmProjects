import sys
sys.stdin = open('input2.txt','r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr2 = [[0]*N for _ in range(N)]
    zsum = zzsum = 0
    zmax = zzmax = 0

    for i in range(N):
        for j in range(N):
            while N - 1 >= i >= 0 and N - 1 >= j >= 0:
                zsum += arr[i][j]
                i -= 1
                j -= 1
            while N - 1 >= i >= 0 and N - 1 >= j >= 0:
                zzsum += arr[i][j]
                i -= 1
                j += 1
            while  N-1 >= i >= 0 and N - 1 >= j >= 0:
                zsum += arr[i][j]
                i += 1
                j += 1
            while N - 1 >= i >= 0 and N - 1 >= j >= 0:
                zzsum += arr[i][j]
                i += 1
                j -= 1


        print(zsum)