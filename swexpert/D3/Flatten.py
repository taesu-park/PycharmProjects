for t in range(1, 11):
    a = int(input())
    b = list(map(int,input().split()))
    for i in range(a):
        maxb = b[0]
        minb = b[0]
        idx = 0
        idxx = 0
        for j in range(len(b)):
            if b[j] >= maxb:
                maxb = b[j]
                idx = j
            elif b[j] <= minb:
                minb = b[j]
                idxx = j
        b[idx] -= 1
        b[idxx] += 1
        maxb -= 1
        minb += 1
        for k in b:
            if k >= maxb:
                maxb = k
            elif k <= minb:
                minb = k
    print('#{} {}'.format(t, maxb-minb))
