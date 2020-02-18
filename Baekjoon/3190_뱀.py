def solve(x,y,z):
    global ans
    ans += 1
    board[x][y] = 2
    if ans in dir:
        if dir[ans] == 'D':
            z += 1
        elif dir[ans] == 'L':
            z += 3
    tx, ty = x+d[z%4][0], y+d[z%4][1]
    if tx < 0 or tx >= N or ty < 0 or ty >= N or board[tx][ty] == 2:
        return ans
    if board[tx][ty] == 0:
        a, b = snake.popleft()
        board[a][b] = 0
    board[tx][ty] = 2
    snake.append((tx,ty))
    solve(tx,ty,z)
from collections import deque
import sys
sys.setrecursionlimit(10000)
N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
dir = {}
d = [(0,1),(1,0),(0,-1),(-1,0)]
snake = deque()
ans = -1
for _ in range(K):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1
L = int(input())
for _ in range(L):
    a,b = input().split()
    dir[int(a)] = b
snake.append((0,0))
solve(0,0,0)
print(ans+1)