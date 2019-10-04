def dfs(x,cnt):
    global arr
    if cnt == int(M):
        if int(''.join(x)) > int(arr):
            arr = ''.join(x)
        return
    if ''.join(x)+str(cnt) in s:
        return
    else:
        s.add(''.join(x)+str(cnt))
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            x[i], x[j] = x[j], x[i]
            dfs(x,cnt+1)
            x[i], x[j] = x[j], x[i]
T = int(input())

for tc in range(1, T+1):
    arr, M = input().split()
    l = list(arr)
    s = set()
    dfs(l,0)
    print('#{} {}'.format(tc,arr))