def back(x, l):
    global result
    if len(l) >= 2:
        for i in range(1, len(l)//2):
            for j in range(len(l)):

    if len(l) == N:
        if int(l) < result:
            result = int(l)
        return
    for i in range(x, 4):
        back(i, l+str(i))
N = int(input())
result = 0
back(1, '')