N = int(input())

arr = list(map(int,input().split()))
dx = -1
dy = 1
P = int(input())
for p in range(P):
    a, b = map(int,input().split())
    if a == 1:
        for x in range(b-1, len(arr), b):
            if arr[x] == 0:
                arr[x] = 1
            elif arr[x] == 1:
                arr[x] = 0
    if a == 2:
        tx = txx = b -1
        while arr[tx] == arr[txx] and tx >= 0 and txx < len(arr):
            if arr[tx] == 1 and arr[txx] == 1:
                arr[tx] = arr[txx] = 0
            elif arr[tx] == 0 and arr[txx] == 0:
                arr[tx] = arr[txx] = 1

            tx += dx
            txx += dy

print(*arr)