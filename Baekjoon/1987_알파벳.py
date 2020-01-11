# def dfs(x, y, v, c):
#     global MAX
#     if c > MAX:
#         MAX = c
#     for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         tx, ty = x + dx, y + dy
#         if tx < 0 or tx >= R or ty < 0 or ty >= C:
#             continue
#         if not v[ord(board[tx][ty])-ord('A')]:
#             v[ord(board[tx][ty])-ord('A')] = 1
#             dfs(tx, ty, v, c + 1)
#             v[ord(board[tx][ty])-ord('A')] = 0
# R, C = map(int, input().split())
# board = list(list(input()) for _ in range(R))
# visit = [0 for _ in range(26)]
# cnt = 0
# MAX = 0
# visit[ord(board[0][0]) - ord('A')] = 1
# dfs(0, 0, visit, cnt)
# print(MAX+1)

def bfs(x,y):
    ans = 0
    q = [(x,y,board[x][y])]
    while q:
        v,w,c = q.pop()
        flag = 0
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            tx, ty = v+dx, w+dy
            if tx < 0 or tx >= R or ty < 0 or ty >= C:
                continue
            if board[tx][ty] not in c:
                flag = 1
                if cache[tx][ty] != board[tx][ty] + c:
                    cache[tx][ty] = board[tx][ty] + c
                    q.append((tx,ty,board[tx][ty]+c))
        if not flag:
            ans = max(ans,len(c))
    return ans
R, C = map(int,input().split())
board = [list(input()) for _ in range(R)]
cache = [['' for _ in range(C)] for _ in range(R)]
print(bfs(0,0))
