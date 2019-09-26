import sys
sys.setrecursionlimit(10000)
from collections import deque
N, K = map(int,input().split())
Min = 0xffffffff
visit = [False]*100000
a = 0
Q = deque()
def BFS(x, y):
    Q.append(x)
    while Q:
        for _ in range(len(Q)):
            v = Q.popleft()
            if visit[v]:
                continue
            if v == K:
                return y
            else:
                visit[v] = True
                Q.append(v)
            y += 1


print(BFS(N,0))