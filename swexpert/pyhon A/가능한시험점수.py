
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    l = [0]
    visit = list([0]*(N*100))
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        for j in range(len(l)):
            t = l[j] + arr[i]
            if not visit[t]:
                l.append(t)
                visit[t] = 1
    print('#{} {}'.format(tc,len(l)))