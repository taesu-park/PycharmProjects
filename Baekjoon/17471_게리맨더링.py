from collections import deque

N = int(input())
arr = list(map(int,input().split()))
union = [[] for _ in range(N)]
ans = -1
for i in range(N):
    union[i] += (list(map(int,input().split())))
def bfs(G):
    Q = deque()
    Q.append(G[0])
    cnt = arr[G[0]-1]
    n = 1
    visit = [0 for _ in range(N)]
    visit[G[0]-1] = 1
    while Q:
        v = Q.popleft()
        for i in range(1, union[v-1][0]+1):
            if union[v-1][i] in G and not visit[union[v-1][i]-1]:
                visit[union[v-1][i]-1] = 1
                Q.append(union[v-1][i])
                cnt += arr[union[v-1][i]-1]
                n += 1
    return cnt, n


def back(k,s,A,B):
    global ans
    if k == N:
        if len(A) == N or len(B) == N:
            return
        if ans == 0:
            return
        acnt, an = bfs(A)
        bcnt, bn = bfs(B)
        if an + bn == N:
            if ans == -1:
                ans = abs(acnt-bcnt)
            else:
                ans = min(abs(acnt-bcnt),ans)
    else:
        for i in range(s,N+1):
            back(k+1,i+1,A+[i],B)
            back(k+1,i+1,A,B+[i])

back(0,1,[],[])
print(ans)