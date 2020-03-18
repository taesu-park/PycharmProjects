def swim(n,k,a,b,c):
    global MIN
    if n >= 13:
        if k < MIN:
            MIN = k
        return
    elif k >= MIN:
        return
    else:
        swim(n+1, k+min(plan[n]*price[0],price[1]),a,b,c)
        swim(n+3, k+price[2],a,b,c)


T = int(input())
for tc in range(1, T+1):
    price = list(map(int,input().split()))
    plan = [0] + list(map(int,input().split()))
    MIN = price[3]
    swim(1,0,price[0], price[1], price[2])
    print('#{} {}'.format(tc,MIN))
