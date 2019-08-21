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
            zsum = zzsum = 0
            for k in range(N):
                zsum += arr[i][k]
