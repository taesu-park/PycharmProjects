from collections import deque
import pprint
dx , dy = [0, 0, -1, 1]
M, N, H = map(int,input().split())
tomato = []
for x in range(H):
    tomato.append([list(map(int,input().split())) for _ in range(N)])
Q = deque()
pprint.pprint(tomato)
# for i in range(M):
#     for j in range(N):