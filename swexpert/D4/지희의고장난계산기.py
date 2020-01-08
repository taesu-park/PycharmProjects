def back(l,a,cnt):
    for i in range(len(a)):
        if a[i] in l:
            cnt += 1
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int,input().split()))
    l = set()
    ans = int(input())
    a = list(str(ans))
    print(a)
    for i in range(10):
        if arr[i]:
            l.add(i)
    print(back(l,a,0))