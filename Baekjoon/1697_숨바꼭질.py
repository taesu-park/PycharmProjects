from collections import deque
Q = deque()
N, K = map(int,input().split())
Q.append(N)
count = 0
a = 0
visit = [False]*100001
while Q:
    if a:
        break
    for i in range(len(Q)):
        v = Q.popleft()
        visit[v] = True
        if v == K:
            a = 1
            print(count)
            break
        else:
            dx = [-1, 1, v]
            for x in range(3):
                tx = v + dx[x]
                if 0 <= tx <= 100000 and not visit[tx]:
                    Q.append(tx)
    count += 1