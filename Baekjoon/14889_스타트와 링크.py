# N = int(input())
# board = [list(map(int,input().split())) for _ in range(N)]
# visit = [0 for _ in range(N)]
# ans = 0xfffffff
#
# def back(cnt, idx):
#     global ans
#     if idx == N:
#         return
#     if cnt == N // 2:
#         s1, s2 = 0, 0
#         for i in range(N):
#             for j in range(N):
#                 if visit[i] and visit[j]:
#                     s1 += board[i][j]
#                 if not visit[i] and not visit[j]:
#                     s2 += board[i][j]
#         ans = min(ans, abs(s1-s2))
#         return
#
#     visit[idx] = 1
#     back(cnt+1, idx+1)
#     visit[idx] = 0
#     back(cnt, idx+1)
#
# back(0,0)
# print(ans)

#
# def back(idx):
#     global ans
#     if idx == N:
#         return
#     if idx == N // 2:
#         s1, s2 = 0, 0
#         for i in range(N):
#             for j in range(N):
#                 if visit[i] and visit[j]:
#                     s1 += board[i][j]
#                 if not visit[i] and not visit[j]:
#                     s2 += board[i][j]
#         ans = min(ans, ans(s1-s2))
#         return
# N = int(input())
# board = [list(map(int,input().split())) for _ in range(N)]
# visit = [0]*N
# ans = 0xffffffff
# for i in range(N):
#     for j in range(N):
#         if j > i:
#             board[i][j] += board[j][i]
#         else:
#             board[i][j] = 0
# back(0)
def back(cnt, init):
    global n, answer
    if not answer:
        return
    if cnt == n//2:
        start = link = 0
        for j in range(n):
            for i in range(j+1, n):
                if use[i] and use[j]:
                    start += board[j][i]
                elif not use[i] and not use[j]:
                    link += board[j][i]
        if answer > abs(start-link):
            answer = abs(start-link)
        return
    for i in range(init, n):
        use[i] = True
        back(cnt+1, i+1)
        use[i] = False


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
use = [False] * n
answer = 0xffffff
for j in range(n):
    for i in range(n):
        if i > j:
            board[j][i] += board[i][j]
        else:
            board[j][i] = 0
back(0, 0)
print(answer)