import pprint
N = int(input())
arr = [[0]*101 for _ in range(101)]
num = {}
count = 0
for n in range(N):
    count += 1
    a, b, c, d = map(int,input().split())
    for i in range(101):
        for j in range(101):
            if i >= a and i < a +c and j >= b and j < b+d:
                arr[i][j] = count
    num[n] = count
for k in range(len(num)):
    S = 0
    for i in range(101):
        for j in range(101):
            if arr[i][j] == num[k]:
                # print(num[k])
                S += 1
    print(S)

