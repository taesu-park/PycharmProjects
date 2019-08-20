T = int(input())

for t in range(1, T+1):
    a = input()
    b = list(map(int,input().split()))
    maxnum = b[0]
    minnum = b[0]
    for num in range(1,len(b)):
        if b[num] >= maxnum:
            maxnum = b[num]
    for num in range(1, len(b)):
        if b[num] <= minnum:
            minnum = b[num]

    print(maxnum - minnum)